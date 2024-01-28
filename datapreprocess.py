import os
import json

folder_path = "Dataset/Supermickiii"

# Initialize JSONL file
jsonl_file = "trial.jsonl"


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
                    "messages":[
                        {"role":"system","content":"你是一位小红书旅行博主"},
                        {"role":"user","content":"写一篇旅行博客"},
                        {"role":"system","content":content}
                    ]
                }

                # Append JSON object to JSONL file
                with open(jsonl_file, "a") as f:
                    f.write(json.dumps(json_obj, ensure_ascii=False) + "\n")
                
                print(f"Saved example {count+1} to {jsonl_file}")
                count += 1