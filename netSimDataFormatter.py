import sys


try:
    if sys.argv[1] == '-f':
        infile = sys.argv[2]
		
except:
	while True:
		infile = raw_input("What file would you like to parse? ")
		if infile[-4:] == '.txt':
			break
		
		
filein = open(infile, 'r')
fileout = open("formattedData.txt", 'w')

for line in filein:
	if line[0] == '{':
		fileout.write(line)
			
filein.close()
fileout.close()	