import base64
import io
from PIL import Image


def process_image(image_bytes: io.BytesIO, quality: int = 65):
    """
    Process an image by resizing and compressing it.

    Parameters
    ----------
    image_bytes : io.BytesIO
        The image to process.
    quality : int, default 65
        The quality of the compressed image.

    Returns
    -------
    str
        The base64 encoded string of the compressed image.
    """

    img = Image.open(image_bytes)

    width, height = img.size
    threshold_area = 1_250_000
    current_area = width * height
    size_ratio = current_area / threshold_area

    # Determine the resize factor based on the size ratio
    if size_ratio > 1.5:
        resize_factor = 0.5
    elif size_ratio > 1.25:
        resize_factor = 0.75
    else:
        resize_factor = 1

    # Resize the image if necessary
    if resize_factor < 1:
        new_width = int(width * resize_factor)
        new_height = int(height * resize_factor)
        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

    # Compress and convert to JPEG
    buffer = io.BytesIO()
    img = img.convert("RGB")
    img.save(buffer, format="JPEG", quality=quality, optimize=True)

    # Get base64 encoded string
    compressed_image = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return compressed_image

def get_image_hash(image_file):
    """Generate a hash for the image data to track changes"""
    if image_file is None:
        return None
    try:
        # Get the current position in the file
        pos = image_file.tell()
        # Reset to beginning
        image_file.seek(0)
        # Read the data and create hash
        data = image_file.read()
        hash_value = hash(data)
        # Restore position
        image_file.seek(pos)
        return hash_value
    except Exception:
        return None