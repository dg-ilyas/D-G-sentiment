import praw
from dotenv import load_dotenv
import os
import jsonlines
from datetime import datetime

load_dotenv()

reddit = praw.Reddit(
    client_id= os.getenv('R_USER'),
    client_secret= os.getenv("R_KEY"),
    user_agent='dg-sentiment by ilyas'
)

subreddit = reddit.subreddit('all')

keyword = "domestic and general"

with jsonlines.open('comments_data.json', mode = 'a') as json_file:
    for submission in subreddit.search(query=keyword, sort="new", time_filter="all"):
        submission.comments.replace_more(limit=None) # Retrieve all comments (including nested ones)
        for comment in submission.comments.list():
            if keyword.lower() in comment.body.lower():
                comment_data = {
                    'comment_id': comment.id,
                    'comment_author': str(comment.author),
                    'comment_body': comment.body,
                }
                print(f"Comment ID: {comment.id}\nAuthor: {comment.author}\nBody: {comment.body}\n")
                json_file.write(comment_data)
