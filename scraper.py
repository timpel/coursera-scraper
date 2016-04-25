from bs4 import BeautifulSoup
import re
import sys

# TODO: Should verify that 1 parameter was entered in command line and that it points to a real file

# Create BeautifulSoup parse tree from file entered on command line
html = open(sys.argv[1],'r').read()
soup = BeautifulSoup(html)

# Get just the links to lectures, the text of which will contain the durations we want
lectures = soup.find_all('a', class_="lecture-link")

# Use regex to get just the duration component of each lecture link, separately for minutes and seconds
durations = [re.findall(r"(\d+(?=m))", str(lecture)) + re.findall(r"(\d+(?=s))", str(lecture)) for lecture in lectures]

# Multiply the minutes by 60 and add to the seconds component for each lecture duration
durations_in_seconds = [int(item[0]) * 60 + int(item[1]) for item in durations]

total_duration = sum(durations_in_seconds)

h = total_duration / 3600
m = (total_duration % 3600) / 60
s = total_duration % 60

formatted_duration = "%d:%d:%d" % (h, m ,s)

print formatted_duration