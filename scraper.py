from bs4 import BeautifulSoup
import re
import sys

html = open(sys.argv[1],'r').read()

soup = BeautifulSoup(html)

lectures = soup.find_all('a', class_="lecture-link")

durations = [re.findall(r"(\d+(?=m))", str(lecture)) + re.findall(r"(\d+(?=s))", str(lecture)) for lecture in lectures]

durations_in_seconds = [int(item[0]) * 60 + int(item[1]) for item in durations]
total_duration = sum(durations_in_seconds)

h = total_duration / 3600
m = (total_duration % 3600) / 60
s = total_duration % 60

formatted_duration = "%d:%d:%d" % (h, m ,s)

print formatted_duration