# RPChat-SD

[English](#english) | [中文](#chinese)

<a name="english"></a>

# English

A weekend project that grew into something more - a customizable role-playing chat application powered by Claude 3.5 Sonnet with integrated Stable Diffusion image generation. Born from the frustration with restrictive chat frameworks and the desire for a more immersive experience.

## Features

- **Interactive Chat Interface**

  - Powered by Claude 3.5 Sonnet
  - Complete conversation history control
  - Real-time message editing
  - Custom conversation wrapping

- **Character System**

  - Detailed character customization
  - Dynamic state tracking
  - Personality and behavior simulation
  - Automatic response style adaptation

- **Visual Generation**

  - Scene-appropriate image generation
  - Real-time illustration updates
  - Image regeneration and refinement
  - High-resolution upgrades

- **Environment**
  - Conversation saving/loading
  - Custom configurations
  - Markdown support
  - Storybook export

## Prerequisites

- Python 3.8+
- AWS account with access to Bedrock
- (Optional) Stable Diffusion API endpoint

## Installation

1. Clone the repository:

```bash
git clone https://github.com/CHNSOC/rpchat-sd.git
cd rpchat-sd
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

3. Configure AWS credentials and endpoints:
   Create a `config.ini` file with the following structure:

```ini
[aws]
region = your-region
access_key_id = your-access-key
secret_access_key = your-secret-key
model_id = anthropic.claude-3-5-sonnet-20240620-v1:0

[sd-endpoint]
url = http://your-sd-endpoint/sdapi/v1/txt2img
```

## Project Structure

```
.
├── chara/                  # Character definition files
├── config/                 # Configuration files for LLM
├── conversations/          # Saved conversations
├── descriptions/           # Flavor Texts (For text styles and overloading guardrails)
├── main.py                # Main application
├── create_storybook.py    # Storybook image generator
├── config.ini             # Configuration file
└── README.md
```

[Flavor Text Credits to EraTW Modding Community <3](https://gitgud.io/era-games-zh/touhou/eratw-sub-modding)


## Creating Characters

Characters are defined as JSON files in the `chara` directory. Each character file should follow this structure:
Note: The exact format doesn't need to be strictly followed, and you can freely add fields, but `rp_prompt` and `sd_prompt` must be retained for configuration file reading.

Please refer to the two pre-configured character files for customization examples. Below are just field descriptions.

Minimum Requirements:

```json
{
  "rp_prompt": {
    "basic_info": {
      "name": "", // Character name
      "age": 0,   // Age
      "gender": "" // Gender
    }
  },
  "sd_prompt": {
    "dan_tag": "", // SD tag - enter if character is supported by SD Illustrious Model
  }
}
```

Recommended Structure:

```json
{
  "rp_prompt": {
    "basic_info": {
      "name": "", // Character name
      "age": 0,   // Age
      "gender": "" // Gender
    },
    "appearance": {
      "height": "", // Height
      "weight": "", // Weight
      "hair": {
        "color": "", // Hair color
        "style": "" // Hair style
      },
      "eyes": {
        "color": "" // Eye color
      },
      "distinguishing_features": [] // Distinctive features
    },
    "personality": {
      "core_traits": [] // Character traits
    },
    "speech_patterns": {
      "manner_of_speaking": "", // Speaking style
      "quotes": [] // Common phrases
    },
    "background": {
      "birthplace": "", // Place of birth
      "family": {} // Family details
    },
    "interests": [], // Hobbies and interests

    // Specialized intimate definitions - note specific preferences here if any

    "intimate_details": {
      "body_sensitivities": {
        "breasts": "",
        "neck": "",
        "ears": "",
        "inner_thighs": "",
        "lower_back": ""
      },
      "sexual_preferences": {
        "experience_level": "",
        "fantasies": [],
        "fetishes": []
      },
      "responsiveness": {
        "arousal_signs": [],
        "verbal_responses": []
      }
    }
  },
  "sd_prompt": {
    "dan_tag": "", // SD tag
    "appearance": "" // Appearance description
  }
}
```

## Running the Application

1. Start the application:

```bash
streamlit run main.py
```

2. Select a configuration and character from the sidebar
3. Start chatting!

## Image Generation

To enable image generation:

1. Set up a Stable Diffusion API endpoint
2. Configure the endpoint URL in `config.ini`
3. Enable the "Generate SD Image" checkbox in the interface

## Creating Storybooks

The project includes a utility to create storybook-style images from saved conversations:

```bash
python create_storybook.py path/to/conversation/directory
```

<a name="chinese"></a>

# 中文

这是一个基于 Claude 3.5 Sonnet 的可定制角色扮演聊天应用程序，具有可选的 Stable Diffusion 图像生成功能。

## 功能特点

- 基于 Claude 3.5 Sonnet 的交互式聊天界面
- 角色定制和角色扮演对话
- 可选的 Stable Diffusion 图像生成
- 对话保存和加载
- 支持自定义配置和文本片段
- Markdown 渲染支持
- 消息编辑模式和图像重新生成
- 角色状态跟踪和分析

## 系统要求

- Python 3.8+
- 具有 Bedrock 访问权限的 AWS 账户
- (可选) Stable Diffusion API 端点

## 安装步骤

1. 克隆仓库：

```bash
git clone https://github.com/CHNSOC/rpchat-sd.git
cd rpchat-sd
```

2. 安装所需包：

```bash
pip install -r requirements.txt
```

3. 配置 AWS 凭证和端点：
   创建 `config.ini` 文件，结构如下：

```ini
[aws]
region = your-region
access_key_id = your-access-key
secret_access_key = your-secret-key
model_id = anthropic.claude-3-5-sonnet-20240620-v1:0

[sd-endpoint]
url = http://your-sd-endpoint/sdapi/v1/txt2img
```

## 项目结构

```
.
├── chara/                  # 角色定义文件
├── config/                 # 配置文件
├── conversations/          # 保存的对话
├── descriptions/           # 用于特化 LLM 输出风格和破限的口上
├── main.py                # 主应用程序
├── create_storybook.py    # 故事书图像生成器
├── config.ini             # 配置文件
└── README.md
```

[致谢：口上文件来源于中文 EraTW 社区](https://gitgud.io/era-games-zh/touhou/eratw-sub-modding)

## 创建角色

角色在 `chara` 目录中以 JSON 文件形式定义。每个角色文件应遵循以下结构：
注意：具体格式并不用严格遵循，可以自由增添字段，但需要保留 rp_prompt 和 sd_prompt 用于配置文件读取。

请参考预置的两个角色文件来进行自定义，下方只是字段描述

最低要求：

```json
{
  "rp_prompt": {
    "basic_info": {
      "name": "", // 名字
      "age": 0, // 年龄
      "gender": "" // 性别
    }
  },
  "sd_prompt": {
    "dan_tag": "", // SD标签，如果有 Illustrious 支持的角色可以在这里填入
  }
}
```

推荐：

```json
{
  "rp_prompt": {
    "basic_info": {
      "name": "", // 名字
      "age": 0, // 年龄
      "gender": "" // 性别
    },
    "appearance": {
      "height": "", // 身高
      "weight": "", // 体重
      "hair": {
        "color": "", // 发色
        "style": "" // 发型
      },
      "eyes": {
        "color": "" // 眼睛颜色
      },
      "distinguishing_features": [] // 特征
    },
    "personality": {
      "core_traits": [] // 角色特质
    },
    "speech_patterns": {
      "manner_of_speaking": "", // 说话方式
      "quotes": [] // 常用语
    },
    "background": {
      "birthplace": "", // 出生地
      "family": {} // 家庭
    },
    "interests": [], // 兴趣爱好

    // 下面是色色特化用定义，如有特殊 XP 可以在这里注明

    "intimate_details": {
      "body_sensitivities": {
        "breasts": "",
        "neck": "",
        "ears": "",
        "inner_thighs": "",
        "lower_back": ""
      },
      "sexual_preferences": {
        "experience_level": "",
        "fantasies": [],
        "fetishes": []
      },
      "responsiveness": {
        "arousal_signs": [],
        "verbal_responses": []
      }
    }
  },
  "sd_prompt": {
    "dan_tag": "", // SD标签
    "appearance": "" // 外观描述
  }
}
```

## 运行应用程序

1. 启动应用：

```bash
streamlit run main.py
```

2. 从侧边栏选择配置和角色
3. 开始聊天！

## 图像生成

启用图像生成功能：

1. 设置 Stable Diffusion API 端点
2. 在 `config.ini` 中配置端点 URL
3. 在界面中启用"Generate SD Image"复选框

## 创建故事书

项目包含一个用于从保存的对话创建故事书风格图像的工具：

```bash
python create_storybook.py path/to/conversation/directory
```