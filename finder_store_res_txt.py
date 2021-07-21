import os 
def searchfiles(extension='.ttf', folder='H:\\'):
    "Create a txt file with all the file of a type"
    with open(extension[1:] + "file.txt", "w", encoding="utf-8") as filewrite:
        for r, d, f in os.walk(folder):
            for file in f:
                if file.endswith(extension):
                    filewrite.write(f"{r + file}\n")
 
# looking for png file (fonts) in the hard disk H:\
searchfiles('.rtf', 'C:\\')