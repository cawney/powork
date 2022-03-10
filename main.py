import shutil
import os
# from os.path import exists
from sys import argv

# Look in the PO folder
# See if it's empty or if there is stuff in there other than the folders
# When there are .rtf files, grab all of them and zip as one and name source
# Move the .txt files over to the different directory
# Delete the .rtf files once the zip is made.

script, folder_location, output_name = argv

print(f"Current folder is: '{folder_location}'")
print(f"Output is named: {output_name}")


# folder_location = folder_location + "/test1.txt"
# Write a book about how some companies or countries survive a trans generational span whilst others fail and are a shell of themselves.

# print(os.path.getsize(folder_location))

# output_location = 'work/' + output_name

def printout_path():
    print(os.getcwd())
    output_location = os.chdir(r"C:\catalog\printout\po")


def folder_empty():
    if len(os.listdir(folder_location)) == 0:
        print("Folder is empty")
    else:
        print("Folder is NOT empty")





# if len(os.listdir(folder_location)) == 0:
#     print("Folder is empty")
# else:
#     print("Folder is NOT empty")
    # shutil.make_archive(output_location, 'zip', folder_location)
    # shutil.make_archive(output_filename, 'zip', dir_name)
    # print("Done making archive")

cwd = os.getcwd()
print(cwd)
print("*" * 10)
os.chdir('..\\')
cwd = os.getcwd()
print(cwd)

po_path = os.path


def printout_path():
    print(os.getcwd())
    output_location = os.chdir(r"C:\catalog\printout\po")


printout_path()
print(os.getcwd())
folder_empty()
