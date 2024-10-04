# ⚠️ This repository is now archived and no longer actively maintained.

# Shawn - Code Assistant 🐕‍🦺

[![PyPI License](https://img.shields.io/pypi/l/shawn.svg)](https://pypi.org/project/shawn)
[![PyPI Version](https://img.shields.io/pypi/v/shawn.svg)](https://pypi.org/project/shawn)
[![PyPI Downloads](https://img.shields.io/pypi/dm/shawn.svg?color=orange)](https://pypistats.org/packages/shawn)
<div style="text-align: center;">
  <img src="docs/imgs/shawn.png" style="width: 20%; height: auto;">
</div>

Shawn is your go-to command-line chatbot for all your coding queries. It's designed to make your coding experience smoother and more efficient.

**Features**:
* **Instant Code Answers**: Shawn taps into the power of OpenAI's Chat Completion API and custom-made functionalities to deliver well-structured and informative responses to your coding questions.

* **Machine Awareness**: It goes the extra mile by understanding and providing information about your machine's state, ensuring tailored assistance.

* **Syntax-Highlighted Code Snippets**: When you seek code suggestions, Shawn doesn't just provide answers; it delivers beautifully syntax-highlighted markdown code snippets.
 

![Alt Text](docs/demo.gif)

### Setup

#### Requirements

* Python 3.8+

#### Installation

Install it with pip

```text
$ pip install shawn
```

or add it to your [Poetry](https://poetry.eustace.io/) project:

```text
$ poetry add shawn
```
### Getting Started
Once Shawn is installed, you can utilize it through the following commands:

#### Start a Chat
To initiate a chat session with Shawn, execute the following command:

```bash
$ shawn chat
```

#### Code Explanation
For a detailed natural language explanation of your source code, use the following commands:

```bash
$ shawn dig path/to/file.c
```

```bash
$ shawn dig path/to/folder
```


