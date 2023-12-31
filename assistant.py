import os
import time
import logging
from datetime import datetime
import openai
from openai import OpenAI

# Set up logging
logging.basicConfig(level=logging.INFO)

your_api_key = "REPLACE_WITH_YOUR_API_KEY"

initial_intructions = "You are an assistant chatbot for newcomers in a consultancy company called Abracadabra. You will provide answers to questions based on the content provided by the company, which are present in the files. Always respond with infos from either of the files. Do not make up answers. Do not provide information which is not relevant to the question. Do not answer questions not related to the company context."

client = OpenAI(api_key=your_api_key)

# Get a list of all files in the folder
print(os.getcwd())
folder_path = 'AI-Onboarding-Assistant/content/documents'
files = os.listdir(folder_path)

# Upload all files
file_ids = []
for file_name in files:
    file_path = os.path.join(folder_path, file_name)
    file_object = client.files.create(
        file=open(file_path, 'rb'),
        purpose='assistants'
    )
    # Do something with the file object (e.g. print its ID)
    print(file_object.id)
    file_ids.append(file_object.id)

#Create assistant
assistant = client.beta.assistants.create(
    name="AI Onboarding Assistant",
    instructions=initial_intructions,
    tools=[{"type": "retrieval"}],
    model="gpt-3.5-turbo-1106",
    file_ids=file_ids
)

#Optionally retrieve assistant if it already exists
#assistant = client.beta.assistants.retrieve("asst_REPLACE_WITH_ASSIST_ID")
print(assistant)

#Create thread
thread = client.beta.threads.create()

def post_message_in_thread(message):
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=message
    )
    run = client.beta.threads.runs.create(
        thread_id = thread.id,
        assistant_id = assistant.id
    )
    return run

def wait_for_run_completion(client, thread_id, run_id, sleep_interval=5):
    """
    Waits for a run to complete and prints the elapsed time.:param client: The OpenAI client object.
    :param thread_id: The ID of the thread.
    :param run_id: The ID of the run.
    :param sleep_interval: Time in seconds to wait between checks.
    """
    while True:
        logging.info("Waiting for run to complete...")
        time.sleep(sleep_interval)
        try:
            run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
            if run.completed_at:
                elapsed_time = run.completed_at - run.created_at
                formatted_elapsed_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
                logging.info(f"Run completed in {formatted_elapsed_time}")
                break
        except Exception as e:
            logging.error(f"An error occurred while retrieving the run: {e}")
            break        

def retrieve_assistant_answer():
    messages = client.beta.threads.messages.list(
        thread_id=thread.id
        )

    last_message = messages.data[0]
    response = last_message.content[0].text.value
    print(response)

run = post_message_in_thread(initial_intructions)
wait_for_run_completion(client, thread.id, run.id)
retrieve_assistant_answer()

run = post_message_in_thread("My laptop is broken. Is there any email I can contact?")
wait_for_run_completion(client, thread.id, run.id)
retrieve_assistant_answer()