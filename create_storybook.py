import os
import json
from PIL import Image, ImageDraw, ImageFont
import textwrap
import argparse


def load_font(size):
    """Load a font with specified size. Falls back to default if custom font not found."""
    try:
        # Try to load Arial or a similar font - adjust path as needed
        return ImageFont.truetype('simsun.ttc', size, encoding='unic')
    except IOError:
        print("Font not found, using default font")
        # Fallback to default font
        return ImageFont.load_default()


def wrap_text(text, font, max_width):
    """Wrap text to fit within a given width. Works with both English and Chinese."""
    lines = []
    current_line = ''

    for char in text:
        test_line = current_line + char
        width = font.getlength(test_line)

        if width <= max_width:
            current_line = test_line
        else:
            current_line = current_line.replace(
                '\n', '').replace('*', '')
            lines.append(current_line)
            current_line = char

    if current_line:
        current_line = current_line.replace(
            '\n', '').replace('*', '')
        lines.append(current_line)

    return lines


def create_storybook_image(image_path, text, output_path):
    """Create a storybook-style image with text on the right side."""
    try:
        # Open and process the original image
        with Image.open(image_path) as img:
            # Convert to RGB if necessary
            if img.mode != 'RGB':
                img = img.convert('RGB')

            # Get dimensions
            orig_width, orig_height = img.size
            new_width = orig_width * 2  # Double the width

            # Create new image with white background
            new_image = Image.new('RGB', (new_width, orig_height), 'white')

            # Paste original image on the left
            new_image.paste(img, (0, 0))

            # Setup for text drawing
            draw = ImageDraw.Draw(new_image)

            # Calculate text area dimensions
            text_area_width = orig_width - 120  # Leave 20px padding on each side
            text_area_x = orig_width + 20  # Start after original image + padding

            # Calculate font sizes proportional to image height
            initial_body_font_size = int(
                orig_height * 0.025)  # 2.5% of image height

            def calculate_text_height(text, font_size, max_width):
                test_font = load_font(font_size)
                wrapped = wrap_text(text, test_font, text_area_width)
                # 130% of font size for spacing
                line_height = int(font_size * 1.6)
                return len(wrapped) * line_height, wrapped, test_font, line_height

            # Start with initial size and reduce until content fits
            body_font_size = initial_body_font_size
            max_text_height = orig_height - 100  # Leave room for title and padding
            content_height, wrapped_lines, body_font, line_height = calculate_text_height(
                text, body_font_size, text_area_width)

            # Reduce font size until content fits
            while content_height > max_text_height and body_font_size > 12:  # Don't go smaller than 12px
                body_font_size = int(body_font_size * 0.9)  # Reduce by 10%
                content_height, wrapped_lines, body_font, line_height = calculate_text_height(
                    text, body_font_size, text_area_width)

            # Center the text in remaining space
            start_y = (max_text_height - content_height) // 2

            # Draw each line
            current_y = start_y
            for line in wrapped_lines:
                draw.text((text_area_x, current_y), line,
                          font=body_font, fill='black')
                current_y += line_height

            # Save the new image
            new_image.save(output_path, 'PNG', quality=95)
            return True

    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return False


def process_conversation(conversation_dir):
    """Process all images in a conversation directory."""
    try:
        # Load conversation data
        json_path = os.path.join(conversation_dir, 'conversation.json')
        with open(json_path, 'r', encoding='utf-8') as f:
            conversation = json.load(f)

        # Create output directory
        output_dir = os.path.join(conversation_dir, 'storybook_images')
        os.makedirs(output_dir, exist_ok=True)

        # Process each message in the conversation
        for i, message in enumerate(conversation):
            if message['role'] == 'assistant' and 'images' in message:
                text = message['content']

                # Process each image for this message
                for img_idx, img_path in enumerate(message['images']):
                    full_img_path = os.path.join(conversation_dir, img_path)
                    if os.path.exists(full_img_path):
                        output_path = os.path.join(
                            output_dir,
                            f'storybook_message_{i}_image_{img_idx}.png'
                        )

                        if create_storybook_image(full_img_path, text, output_path):
                            print(f"Created storybook image: {output_path}")
                        else:
                            print(
                                f"Failed to create storybook image for {full_img_path}")

        print(f"Storybook images saved to {output_dir}")

    except Exception as e:
        print(f"Error processing conversation: {e}")


def main():
    parser = argparse.ArgumentParser(
        description='Create storybook images from saved conversations')
    parser.add_argument('conversation_dir',
                        help='Path to the conversation directory')

    args = parser.parse_args()

    if not os.path.exists(args.conversation_dir):
        print(f"Error: Directory {args.conversation_dir} does not exist")
        return

    process_conversation(args.conversation_dir)


if __name__ == "__main__":
    main()
