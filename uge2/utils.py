from os.path import isfile, join
import argparse
import exercise1
import os

# Create a module called utils.py and put the following functions inside:

#     first function takes a path to a folder and writes all filenames in the folder to a specified output file
#     second takes a path to a folder and write all filenames recursively(files of all sub folders to)
#     third takes a list of filenames and print the first line of each
#     fourth takes a list of filenames and print each line that contains an email(just look for @)
#     fifth takes a list of md files and writes all headlines(lines starting with  # ) to a file Make sure your module can be called both from cli and imported to another module Create a new module that imports utils.py and test each function.


def write_filenames(path, output_file):
    # 1. first function takes a path to a folder and writes all filenames in the folder to a specified output file
    onlyfiles = [f for f in os.listdir(path) if isfile(join(path, f))]
    exercise1.write_list_to_file(output_file, onlyfiles)


def write_all_filenames(path, output_file=""):
    # 2. second takes a path to a folder and write all filenames recursively(files of all sub folders to)
    print("outputfile", output_file)
    allfiles = os.listdir(path)
    if len(allfiles) == 0:
        return
    else:
        for el in allfiles:
            if os.path.isfile(join(path, el)):
                print(list(el))
                exercise1.write_list_to_file(output_file, list(el))
            else:
                write_all_filenames(join(path, el))

        return


# write_filenames("./", "folderfiles.csv")
write_all_filenames("./", "folderfiles.csv")
