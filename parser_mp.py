import re
import sys
import pdb

try:
    if sys.argv[1] == '-f':
        infile = sys.argv[2]

except:
    while True:
        infile = raw_input("What file would you like to parse? ")
        if infile[-4:] == '.txt':
            break
     
regex = []
resp = ''

try:
    if sys.argv[3] == '-i':
        for i in sys.argv[4:]:
            if i[0] == "'" or i[0] == '"':
                i = i[1:-1]
            regex.append(i)

except:
    #print "\nYou are allowed to search for three regular expressions"
    #regex1 = raw_input("Enter regex1: ")
    #regex2 = raw_input("Enter regex2: ")
    #regex3 = raw_input("Enter regex3: ")
    while True:
        s = raw_input("Enter a regex: ")
        if s == '--Done--':
            break
        else:
            regex.append(s)


fin = open(infile, 'r')
#fout = open("parsed.txt", 'wb')

for line in fin:
    #if not regex1 == '&&&':
        #m = re.search(regex1, line)
        #if m is not None:
            #fout.write(m.group() + '\n')
    #if not regex2 == '&&&':
        #n = re.search(regex2, line)
        #if n is not None:
            #fout.write(n.group() + '\n')
    #if not regex3 == '&&&':
        #w = re.search(regex3, line)
        #if w is not None:
            #fout.write(w.group() + '\n')
    for r in regex:
        #pdb.set_trace()
        search = re.search(r, line)
        if search is not None:
            print search.group()
    
    
fin.close()
#fout.close()

