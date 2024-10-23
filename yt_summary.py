import urllib.request
import urllib.parse
import os
import json
import argparse
import requests
from pytube import extract
from youtube_transcript_api import YouTubeTranscriptApi

parser = argparse.ArgumentParser(description="Takes the transcript of a Youtube video and summarizes it into a markdown file.")

parser.add_argument('-v', '--video', help='URL of Youtube video', required=True)
parser.add_argument('-d', '--directory', help='/Path/to/root_dir/', required=False)
parser.add_argument('-n', '--name_of_file', help='Name of the file to be created.', required=False)

args = parser.parse_args()
print("URL: ", args.video)

filename = ''
if not args.name_of_file:
    #use youtube title to create filename
    params = {"format": "json", "url": args.video}
    url = "https://www.youtube.com/oembed"
    query_string = urllib.parse.urlencode(params)
    url = url + "?" + query_string

    with urllib.request.urlopen(url) as response:
        response_text = response.read()
        data = json.loads(response_text.decode())
        filename = data['title']+".md"
else:
    filename = args.name_of_file + ".md"

id = extract.video_id(args.video)

transcript_li = YouTubeTranscriptApi.get_transcript(id)

full_text = " ".join([i['text'] for i in transcript_li])
full_text = " ".join(full_text.splitlines())

prompt = "Can you summarize the following into key concepts in markdown format?\n" + full_text

url = "http://localhost:11434/api/chat"
data = {
    "model": "llama3",
    "messages": [
        {
            "role": "user",
            "content": prompt 

        }
    ],
    "stream": False,
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, json=data)

filepath = ''
if args.directory is not None:
    filepath = os.path.join(args.directory, filename)
    if not os.path.exists(args.directory):
        os.makedirs(args.directory)
else:
    filepath = filename

print(f"Writing file to {filepath}.\n")
f = open(filepath, "a")
f.write(response.json()["message"]["content"])
print("Complete!")
f.close()

if __name__ == '__main__':
    args = parser.parse_args()

