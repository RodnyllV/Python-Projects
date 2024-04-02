import os, shutil

# Hash map for sorting the files
sortMap = {
    "Pictures": [".png", ".jpg", ".jpeg", ".gif", ".tiff"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".oform", ".html", ".pub", ".xml", ".tiff", ".doc"],
    "Source Code": [".cpp", ".py", ".java", ".c", ".cc", ".cxx", ".h", ".cs", ".pl"],
    "Sounds": [".ogg", ".mp3", ".wav", ".aiff"],
    "Videos": [".mp4", ".mov", ".webm", ".avi", ".html5", ".mpeg"]
}

# Input the directory with the files that need to be sorted
givenDirectory = input("Insert file directory: ")

# Check to see if the directory exists to prevent errors
if not os.path.exists(givenDirectory):
    print("Directory does not exist")

# Create the folders for the files in case they don't already exist
for folder in sortMap.keys():
    sortedFolderDirectory = givenDirectory + "\\" + folder

    if not os.path.exists(sortedFolderDirectory):
        os.mkdir(sortedFolderDirectory)

# Use a nested for loop to sort the files accordingly
for file in os.listdir(givenDirectory):
    for folderType, extension in sortMap.items():
        if extension.count(file[file.find("."):len(file)]) != 0:
            oldDirectory = givenDirectory + "\\" + file
            newDirectory = givenDirectory + "\\" + folderType

            shutil.move(oldDirectory, newDirectory)

