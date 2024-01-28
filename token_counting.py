import tiktoken
import jsonlines

encoding = tiktoken.get_encoding("cl100k_base")

def num_tokens_from_messages(messages, tokens_per_message=3, tokens_per_name=1):
    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(str(value)))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3
    return num_tokens

messages = []

with jsonlines.open("trial.jsonl") as reader:
    for obj in reader:
        messages.append(obj)

number = num_tokens_from_messages(messages)

print(number)
print(f"price: {0.008 * number / 1000}")
print()