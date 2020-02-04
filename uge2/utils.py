from os.path import isfile, join
import argparse
import exercise1
import os
import csv

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
    allfiles = os.listdir(path)
    if len(allfiles) == 0:
        return
    else:
        for el in allfiles:
            if os.path.isfile(join(path, el)):
                exercise1.append_string_to_file(output_file, join(path, el))
            else:
                write_all_filenames(join(path, el), output_file)

        return


def print_first_line(filename_list):
    # 3. third takes a list of filenames and print the first line of each
    for file in filename_list:
        filecontent = exercise1.read_csv(file)
        print(filecontent[0])


def print_email_lines(filename_list):
    # 4. fourth takes a list of filenames and print each line that contains an email(just look for @)
    for file in filename_list:
        filecontent = exercise1.read_csv(file)
        print(file)
        for line in filecontent:
            if line.find("@")>-1:
                print(line)


def write_headlines_to_file(filename_list, output_file):
    # 5. fifth takes a list of md files and writes all headlines(lines starting with  # ) to a file
    # Make sure your module can be called both from cli and imported to another module
    # Create a new module that imports utils.py and test each function.
    for file in filename_list:
        filecontent = exercise1.read_csv(file)
        print(file)
        for line in filecontent:
            if line.find("#")>-1:
                print(line)
                exercise1.append_string_to_file(output_file, line)


if __name__ == '__main__':
    """ """
    parser = argparse.ArgumentParser(
        description='A program that will write the content from file to new file_name or otherwise will print it to the console. Example usage: python exercise1.py ./oldfile.csv --file newfile.csv')
    # parser.add_argument('path', help='The path to file')
    # parser.add_argument('--file',
    #                     help='file_name that if given will write the content to file_name')
    # 3 man kan ikke bruge --help da den brokker sig over den allerede er optaget
    # parser.add_argument('--h',
    #                     help='Help text in header')

    args = parser.parse_args()
    file_input = args.path
    filename = basename = os.path.basename(file_input)



