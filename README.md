# AI-Onboarding-Assistant

This is an AI onboarding assistant for Abracadabra, the world's leading consultancy company.

Goal: Assist Newcomers Onboarding

“Consultants frequently face challenges integrating into new teams at the onset of a project due to insufficient documentation, instructions, and guidance. This hinders the smooth transition and productivity of the consultant. The goal is to develop a solution using Generative AI to assist consultants during the onboarding process by providing real-time guidance, relevant documentation, and insights into team dynamics.”

### Authors:
Henrique Correia,
Nicolas Ribeiro

## How to test:

1) Install Python 3: 
https://www.python.org/downloads/
2) Install dependencies - open your terminal and run:
    ```bash
    pip3 install --upgrade openai
    pip3 install ipykernel jupyter streamlit requests beautifulsoup4 pdfkit
    ```
3) Download this repo
4. Replace "your_api_key" value in assistant.py code with a valid one from OpenAI, and save the file
5. Run the Streamlit app from your terminal:

    ```bash
    streamlit run assistant.py
    ```

## References
- https://platform.openai.com/docs/api-reference/assistants
- https://platform.openai.com/docs/api-reference/files