# WordPress Downloader
Just a python script to download WordPress articles from Public API and insert to MongoDB. The script can be easily modified to put the posts to anything else. I chose MongoDB because it seems a sensible choice as the result is in JSON format.

# How to install MongoDB

```
brew install mongodb
```

# How to install dependencies

```
pip install -r requirements.txt
```

And then run 

```
python download.py
```
