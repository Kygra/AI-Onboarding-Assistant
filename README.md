# AI-Onboarding-Assistant

The AI Onboarding Assistant is a chatbot designed to assist newcomers in Abracadabra, the world's leading consultancy company. 

It provides answers to questions based on the content provided by the company, which are present in the files. The assistant is trained to respond with relevant information from these files and does not make up answers or provide irrelevant information.

## Presentation
https://docs.google.com/presentation/d/1YBdBMMQLs0aCF9IerHGzjHXf2odUFQC9HJBH04dczeU/

## Features
- Provides answers to questions based on company context
- Accesses content from files to provide accurate information
- Ensures responses are relevant and informative
- Can be integrated into existing systems

## AI Tools used
- OpenAI GPT-3
- OpenAI Assistants API
- Codeium

## How to test:

1) Install Python 3: 
https://www.python.org/downloads/
2) Install dependencies - open your terminal and run:
    ```bash
    pip3 install --upgrade openai
    pip3 install ipykernel jupyter
    ```
3) Download this repo
4) Replace "your_api_key" value in assistant.py code with a valid one from OpenAI, and save the file
5) Run the assistant.py from the terminal or from inside your IDE

## References
- https://platform.openai.com/docs/api-reference/assistants
- https://platform.openai.com/docs/api-reference/files

## Next steps
Implement a visual application with a chat window using streamlit. 
Reference: https://github.com/streamlit/llm-examples

## Authors:
Henrique Correia,
Nicolas Ribeiro
