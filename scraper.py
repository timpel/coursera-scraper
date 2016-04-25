from bs4 import BeautifulSoup
import re
import sys

def get_durations(file_name):

	# Create BeautifulSoup parse tree from file entered on command line (if file doesn't exist throw an error)
	try:
		html = open(file_name,'r').read()
		soup = BeautifulSoup(html)
	except IOError:
		print "Couldn't find the specified HTML file."
		return 0

	# Get just the links to lectures, the text of which will contain the durations we want
	lectures = soup.find_all('a', class_="lecture-link")

	# Get a list of completed lectures by taking the previous sibling of each lecture link
	# For completed lectures, the previous sibling will be a span; for incomplete lecture there is no previous sibling
	comp_list = [lecture.previous_sibling for lecture in lectures]

	# Use regex to get just the duration component of each lecture link, separately for minutes and seconds
	durations = [re.findall(r"(\d+(?=m))", str(lecture)) + re.findall(r"(\d+(?=s))", str(lecture)) for lecture in lectures]

	# Get the durations of completed lectures only by only selecting from durations if the corresponding entry in comp_list exists
	comp_durations = [duration[0] for duration in zip(durations, comp_list) if duration[1]]

	# Get the sum of durations for all / completed lectures
	comp_total = total_duration(comp_durations)
	all_total = total_duration(durations)

	# Return tuple of completed lecture duration (formatted), total lecture duration (formatted) and the percentage completed of total
	return (time_format(comp_total), time_format(all_total), comp_total / all_total * 100)

def total_duration(durations):
	# Multiply the minutes by 60 and add to the seconds component for each lecture duration
	durations_in_seconds = [int(item[0]) * 60 + int(item[1]) for item in durations]
	
	# Sum up the seconds and return as a float
	total = sum(durations_in_seconds)
	return float(total)

def time_format(total):

	h = total / 3600
	m = (total % 3600) / 60
	s = total % 60

	formatted_duration = "%d:%d:%d" % (h, m ,s)

	return formatted_duration

def main():
	# Verify that 1 parameter was entered in command line
	if len(sys.argv) != 2:
		print 'Usage: python scraper.py <file_path>'
	
	else:
		result = get_durations(sys.argv[1])

		# If no error was thrown (i.e. the file exists) print out results
		if result:
			print "Completed: ", result[0]
			print "Total: ", result[1]
			print "Percent Complete: ", result[2]

# If scraper.py was run directly by python
if __name__ == '__main__':
	main()