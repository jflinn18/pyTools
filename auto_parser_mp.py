import os
import multiprocessing as mp
import pdb
from time import *
import subprocess as sp


def run_auto(f):
    try:
        cmd = 'python parser_mp.py -f ' + directory + '/' + f + ' -i ' + regex

        out = sp.check_output(cmd, shell=True)
        s = []
        s.append(f)
        s.append(out)
        return s
        
    except sp.CalledProcessError:
        print '-----CalledProcessError-----'

    except:
        print "-----Error-----"
        print directory + '/' + f

  

    return directory + '/' + f + '   -----Done-----'



try:
    directory = raw_input("Enter the initial directory: ")
    path_directory = raw_input("Enter the target directory: ")
    files = os.listdir(directory)
    test = os.listdir(path_directory)
except:
    print '-----Directory does not Exist-----'

regex = raw_input("Enter the regex: ")


    
start = time()

if directory[-1:] == '/':
    directory = directory[:-1]
        

alg = directory.split('/')
dirs = os.listdir(directory)

results = []
pool = mp.Pool(processes = 4)

for f in dirs:
    results.append(pool.apply_async(run_auto, args=(f,)))


for i in results:
    item = i.get()
    outfile = open(path_directory + '/' + item[0], 'wb')

    outfile.write(item[1])
    outfile.close()



end = time()

print 'Time: ' + str(end - start)
    
