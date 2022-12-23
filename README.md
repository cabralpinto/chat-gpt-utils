# chat-gpt-utils

Utility scripts designed to assist with the utilization of ChatGPT.

## Setup

1. Clone the repository with `git clone https://github.com/cabralpinto/chat-gpt-utils.git`.
2. Install the requirements with `pip install -r requirements.txt`.

## Scripts

### `chunker.py`

Splits a set of large text files into smaller chunks to be able to feed it into ChatGPT. Call the script with `python chunker.py <directory>`. It will split each file in the directory into chunks and copy each chunk to the clipboard. Paste the chunk into ChatGPT's input field and click Enter. Repeat until all chunks have been pasted.
