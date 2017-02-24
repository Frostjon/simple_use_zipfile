import os
import time
#import demo
import zipfile
from zipfile import ZipFile
from os import listdir
from os.path import isfile, isdir, join



paths = ['/Users/jon/notes']  #The path you need to backup
#paths = '/Users/jon/notes'

while True:
    s = input('Enter the other path you need to backup  \
               \n(the default path is /Users/jon/notes)-->')

    if len(s) != 0:
        paths.append(s)
    else:
        break

target_dir = '/Users/jon/backup'    #The directory of backup file
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    print('Successfully created directory',target_dir)

today = target_dir + os.sep + time.strftime('%y%m%d')

now = time.strftime('%H')   #The default here is an hour

commend = input('Enter a comment -->')

if len(commend ) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
             commend.replace(' ','_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory ',today)


def addFileIntoZipfile(srcDir, fp):
    for subpath in listdir(srcDir):
        subpath = join(srcDir, subpath)
        if isfile(subpath):
            fp.write(subpath)
        elif isdir(subpath):
            fp.write(subpath)
            addFileIntoZipfile(subpath, fp)

def zipCompress(srcDir, desZipfile):
    fp = ZipFile(desZipfile, mode='a')
    addFileIntoZipfile(srcDir, fp)
    fp.close()

for path in paths:
    zipCompress(path, target)

z = zipfile.ZipFile(target,'r')
print(z.namelist())

if len(z.namelist()) != 0:
    print('Successfully backup to',target)
else:
    print('Backup Failed!')
