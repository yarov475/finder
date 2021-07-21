import os
import shutil
import path
from path import path

destination = "C:/finder/file_copied"


# os.makedirs(destination)


def copyfile(dir, filetype='pptx', counter=0):
    "Searches for pptx (or other - pptx is the default) files and copies them"
    for pack in os.walk(dir):
        for f in pack[2]:
            if f.endswith(filetype):
                fullpath = pack[0] + "\\" + f
                print(fullpath)
                shutil.copy(fullpath, destination)
                counter += 1
    if counter & gt; 0:
        print("------------------------")
        print("\t==&gt; Found in: `" + dir + "` : " + str(counter) + " files\n")


for dir in os.listdir():
    "searches for folders that starts with `_`"
    if dir[0] == '_':
        # copyfile(dir, filetype='pdf')
        copyfile(dir, filetype='txt')