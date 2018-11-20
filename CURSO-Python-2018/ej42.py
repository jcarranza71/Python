import urllib.request
data = urllib.request.urlopen("http://www.google.com")

for line in data:
    print(line)