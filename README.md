# RAG Chatbot
The Retrieval Augmented Generation Chatbot is a project that includes two chatbots: the Baseline Chatbot and the Multi-lingual Voice Chatbot.

## Baseline Chatbot

The Baseline Chatbot is a text-based chatbot that uses Retrieval Augmented Generation using GPT 3.5 to respond to user queries. 
### Features
1. Custom separators for splitting the knowledge base into chunks (Since the knowledge base is formatted like a markdow, using MarkdownHeaderSplitter to get complete question and description in each embedding chunk)
2. Prevent hallucination by using RAG and a custom prompt template.

To run the Baseline Chatbot, follow these steps:

### Prerequisites

Before running the Baseline Chatbot, ensure you have the following installed:

1. Python (version 3.10.5)
2. Other dependencies specified in the requirements.txt file

### Installation

1. Clone this repository to your local machine.
2. Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

### Usage

To run the Baseline Chatbot, navigate to the "src" directory and execute the following command:

```bash
python gradio app.py
```
