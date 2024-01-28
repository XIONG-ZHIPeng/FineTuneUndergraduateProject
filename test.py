from openai import OpenAI

with open("myapi.txt", "r") as file:
    api_key = file.read().strip()

client = OpenAI(api_key=api_key)

files = list(client.files.list())

print(files[0].id)