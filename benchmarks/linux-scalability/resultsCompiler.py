#!/usr/bin/env python3
import re

matcher = re.compile("Average execution time = ([0-9]+\.[0-9]+) .*")
f = open("resultTable.txt", 'w')
f.write("threadcount\t1\t2\t4\t8\n")

resultsString = "glib"
with open("glib.log") as resultFile:
	for line in resultFile:
		timeElapsed = matcher.match(line)
		if timeElapsed:
			resultsString = resultsString + "\t" + timeElapsed.group(1)
			#print(float(timeElapsed.group(1)))
f.write(resultsString+'\n')

resultsString = "hoard"
with open("hoard.log") as resultFile:
	for line in resultFile:
		timeElapsed = matcher.match(line)
		if timeElapsed:
			resultsString = resultsString + "\t" + timeElapsed.group(1)
			#print(float(timeElapsed.group(1)))
f.write(resultsString+'\n')

resultsString = "tcmalloc"
with open("tcmalloc.log") as resultFile:
	for line in resultFile:
		timeElapsed = matcher.match(line)
		if timeElapsed:
			resultsString = resultsString + "\t" + timeElapsed.group(1)
			#print(float(timeElapsed.group(1)))
f.write(resultsString+'\n')
f.close()
