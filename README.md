# FSFS (Free space from space)

FSFS is a tool designed to help manage and analyze free space within files and directories.

## Why

I was trying to test [Aider](https://aider.chat/) (AI pair programming in your terminal) with [Qwen2.5-coder](https://ollama.com/library/qwen2.5-coder) thru [Ollama](https://ollama.com) in our local machine BestIA with two 24GB VRAM 3090.

So my excuse is to talk about the [holy war about spaces vs tabs](https://softwareengineering.stackexchange.com/questions/57/tabs-versus-spaces-what-is-the-proper-indentation-character-for-everything-in-e
), and to show you that you can free up a lot of space from your source code using [TABs](https://en.wikipedia.org/wiki/Tab_key). **Imagine all github base code using tabs and freeing disk space, and consmuing less resources.**

**Proudly and Obviously coded from a programming language based on indentation with spaces, not tabs, with a style guide that prefer [Spaces over tabs](https://peps.python.org/pep-0008/#tabs-or-spaces).**


## Features

- Count whitespace in files.
- Analyze whitespace distribution in directories.

## Installation

1. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment:**

   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use FSFS, you can run the `fsfs.py` script with the appropriate arguments. For example:

   ```bash
   python fsfs.py ./
   ```

### Ouput
> Running over itself, I can free up 96 bytes

```
File counts for 4 and 8 consecutive spaces:
fsfs.py: 4 spaces: 34, 8 spaces: 22
test_fsfs.py: 4 spaces: 31, 8 spaces: 6
README.md: 4 spaces: 3, 8 spaces: 0

Summary:
Total files with 4 spaces: 3
Total files with 8 spaces: 2
Total occurrences of 4 spaces: 68
Total occurrences of 8 spaces: 28
You can free up space replacing tabs for spaces. You recover 96 bytes.
```
