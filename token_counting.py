import tiktoken
import jsonlines

def num_tokens_from_messages(messages, model="gpt-3.5-turbo"):
    """Return the number of tokens used by a list of messages."""
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        print("Warning: model not found. Using cl100k_base encoding.")
        encoding = tiktoken.get_encoding("p50k_base")
    num_tokens = 0

    for message in messages:
        num_tokens += len(encoding.encode(str(message)))
    return num_tokens

messages = []

with jsonlines.open("trial.jsonl") as reader:
    for obj in reader:
        messages.append(obj)

number = num_tokens_from_messages(messages)

print(number)
print(f"price: {0.008 * number / 1000}")
print()