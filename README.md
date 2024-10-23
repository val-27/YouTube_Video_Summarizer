###Summarize a Youtube video via llama3 running on my mac

####Details
I ran it using python3.8, haven't tested any other versions. Requires llama3 to be running locally on your machine.

####Installation
```
pip install -r requirements.txt
```
Make sure you have llama running locally on your machine. Instructions:
> https://www.llama.com/docs/llama-everywhere/running-meta-llama-on-mac/

```
ollama pull llama3
```

####Usage
```
usage: yt_summary.py [-h] -v VIDEO [-d DIRECTORY] [-n NAME_OF_FILE]

Takes the transcript of a Youtube video and summarizes it into a markdown file.

optional arguments:
  -h, --help            show this help message and exit
  -v VIDEO, --video VIDEO
                        URL of Youtube video (wrap in '')
  -d DIRECTORY, --directory DIRECTORY
                        /Path/to/root_dir/
  -n NAME_OF_FILE, --name_of_file NAME_OF_FILE
                        Name of the file to be created.

```
