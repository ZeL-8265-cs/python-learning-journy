# python3_fileOrganiser
import os, shutil

# Create a new folder
os.chdir('/Users/lianzerui/Desktop')
os.makedirs('./sortFile')
os.makedirs('./sortFile/txt')
os.makedirs('./sortFile/pdf')
os.makedirs('./sortFile/png')
os.makedirs('./sortFile/jpg')

# Go through the directory tree
for folderName, subfolders, filenames in os.walk('.'):
    for filename in filenames:
        if folderName.startswith('./sortFile'):
            continue
        # Scan the txt
        if filename.endswith('.txt'):
            try:
                shutil.move(filename, './sortFile/txt')
            except:
                continue
        elif filename.endswith('.pdf'):
            try:
                shutil.move(filename, './sortFile/pdf')
            except:
                continue
        elif filename.endswith('.png'):
            try:
                shutil.move(filename, './sortFile/png')
            except:
                continue
        elif filename.endswith('.jpg'):
            try:
                shutil.move(filename, './sortFile/jpg')
            except:
                continue
