from openai import OpenAI

with open("myapi.txt", "r") as file:
    api_key = file.read().strip()

client = OpenAI(api_key=api_key)

# Define the file ID for the training data and the model name

training_file_id = "file-hwQ9t7FkNpnfu7OcyZd4Glen"
model_name = "davinci-002"

# Create the fine-tuning job
response = client.fine_tuning.jobs.create(
    training_file=training_file_id,
    model=model_name
)

# Get the ID of the fine-tuning job
job_id = response.id
print(f"Fine-tuning job created successfully with ID: {job_id}")