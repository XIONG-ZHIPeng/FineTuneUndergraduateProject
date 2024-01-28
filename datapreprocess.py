import os

folder_path = "Dataset/Supermickiii"

# Initialize JSONL file
jsonl_file = "trial.jsonl"

# Initialize prompt
prompt = "生成一篇小红书旅行博主的文章"

count = 0
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".txt"):
            file_path = os.path.join(root, file)
            with open(file_path, "r") as f:
                content = f.read()
                # Do something with the content
                content_lines = content.split("\n")
                content_lines = content_lines[2:-3]
                content_lines[0] = content_lines[0][6:]
                content = "\n".join(content_lines)

                # Create JSON object for fine tuning
                json_obj = {
                    "prompt": prompt,
                    "completion": content
                }

                # Append JSON object to JSONL file
                with open(jsonl_file, "a") as f:
                    f.write(str(json_obj) + "\n")
                
                print(f"Saved example {count+1} to {jsonl_file}")
                count += 1
                if count == 50:
                    break
    if count == 50:
        break
