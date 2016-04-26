# coursera-scraper

This is a script that tells you how long it will take to watch all the videos in a Coursera class in which you are enrolled. It also tells you the total duration of videos watched so far, and what percentage of the total duration you've completed.

To use it, run it in the command line, like this:

`python scraper.py <file.html>`

Where `<file.html>` is an HTML file containing the source code of the video list (you have to get this part yourself by going to the 'Video Lectures' page in your course and viewing/saving the HTML source). The script will spit out:

1) The total duration of all the videos, formatted as hh:mm:ss.
2) The total duration of videos marked as 'Completed' on the Video Lectures page of your course.
3) The percentage of the total duration that has already been marked as 'Completed'.
