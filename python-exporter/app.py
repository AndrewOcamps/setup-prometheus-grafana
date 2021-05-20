import requests

def get_response_time(url):
  r = requests.get(url, timeout=30.0)
  return r.elapsed.total_seconds()

def get_urls():
  urls = ['https://www.google.com.py/', 
	  'https://www.github.com/', 
	  'https://www.arahant.life/']
  return urls

# Debug
#for url in get_urls():
#  print((url, get_response_time(url)))


