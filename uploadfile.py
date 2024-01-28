from openai import OpenAI

with open("myapi.txt", "r") as file:
    api_key = file.read().strip()

client = OpenAI(api_key=api_key)

# Path to the training data file
training_data_path = "trial.jsonl"

# Upload the training data file using the Files API
with open(training_data_path, "rb") as training_file:
    response = client.files.create(
        file=training_file,
        purpose="fine-tune"
    )

# Get the ID of the uploaded file
file_id = response.id
print("Uploaded training data with ID: " + file_id)