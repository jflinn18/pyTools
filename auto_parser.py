import os


try:
    directory = raw_input("Enter the directory: ")
    files = os.listdir(directory)
except:
    print '-----Directory does not Exist-----'

regex = raw_input("Enter the regex: ")

p_dir = directory.split('/')
path_directory = p_dir[0] + '/' + p_dir[1] + '/' + p_dir[2] + '/paths_1'


for f in files:
    os.system('python parser.py -f ' + directory + '/' + f + ' -i ' + regex)
    os.system('mv parsed.txt ' + path_directory + '/' + f)
