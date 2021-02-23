#!/usr/bin/env python3

#test = "CGZNL YJBEN QYDLQ ZQSUQ NZCYD SNQVU"

import sys

if len(sys.argv) < 3:
	print("Usage: \n\t analyse.py filename subseq_length")
	sys.exit(0)
elif len(sys.argv) == 3:
	try:
		subseqNo = int(sys.argv[2])
	except:
		print('second argument must be a number!')
		sys.exit(0)

	try:
		with open(sys.argv[1]) as f:
			task = f.readlines()
	except IOError:
		print("file is missing")
		sys.exit(0)
else:
	print("too many arguments")
	sys.exit(0)

freq= dict()
seq = ''

for test in task:
	for i in range(subseqNo):
		seq += (test[i])

	for j in range(subseqNo , len(test)):
		if test[j] == ' ' or test[j] == '\n':
			continue
		if seq in freq.keys() :
			freq[seq] += 1
		else:
			freq[seq] = 1
		seq += test[j]
		seq = seq[1:]

	tag = [(i , freq[i]) for i in freq.keys() ]
	tag.sort(reverse= True , key=lambda x : x[1])
	for i in tag:
		print(i[0] , ' : ' , i[1])
