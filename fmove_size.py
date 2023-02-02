import os
import shutil

orig = "C:\\Users\\hp\\Desktop\\H\\Hollywood"
# Creating the folder to store the new files
new = "C:\\Users\\hp\\Desktop\\H\\New folder"

# Creates a new folder
os.mkdir(new)

# To set size
CustomSize = 3.5 # Size in GB

for path, subdirs, files in os.walk(orig):
    for i in files:
        if path != new:
            fil = os.path.join(path, i)
            # To get file size
            stat = os.stat(fil)
            filesize = stat.st_size
            filesize = filesize/1024**3 # Converting bytes to GB

            # Check if file size is greater than the custom size
            if filesize > CustomSize:
                # print(fil,":", str(filesize), "GB")
                # Moving the file to the log directory
                shutil.move(fil, new)
print("DONE, files greater than",CustomSize,"GB are moved to the new folder")
