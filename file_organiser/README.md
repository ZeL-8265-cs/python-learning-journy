# File Organiser

A simple file organiser tool that categorises files into different folders based on their file type.

---

## How it works 

- The program scans the directory tree and detects files by extension
- Create new folders for different file types
- Copy of files into the corresponding folder

## Feature

- Sort files by types automatically
- Using os.walk() to can the directory tree
- Supports .txt, .pdf, .png, .jpg
- Using Python standard libraries only (os, shutil)

## What I learned

- How to use os.walk to scan the directory tree (or use os.listdir to obtain a list)
- How to manage the file path with os.path
- How to copy and move files by shutil
- How to skip files that should not be processed

## Future improvements:

- Support more file types
- Allow users to choose a target directory
- Compress sorted files into a ZIP archive
