#author : Sadique
#desc   : To compile and scan yara rules

import yara
import sys
import os

if (len(sys.argv) != 3) :
	print('yoyo.py rules.yara directory')
	sys.exit(2)

#rule to compile	
rules = yara.compile('sdk.yar')
rules.save('compiled')

fo = open('report.log', 'w')

counter = 0
for root, dirs, files in os.walk(sys.argv[2]):
	for file in files:
		with open(os.path.join(root, file), 'rb') as f:
			matches = rules.match(data=f.read())
		if (matches) : 
			print(os.path.join(root, file), 'Matches')
			fo.write(os.path.join(root, file))
			fo.write('\n')
			counter = counter + 1

print('\nTotal files detected :', counter)
fo.close()