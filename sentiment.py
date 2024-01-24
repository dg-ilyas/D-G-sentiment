import json
from rich.console import Console

console = Console()

comments = []

with open('comments_data.json', 'r', encoding='utf-8') as json_file:
    for line in json_file:
        comment_info = json.loads(line)
        comments.append(comment_info)

console.print(comments)
