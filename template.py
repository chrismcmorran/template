#!/usr/bin/python
import argparse
import os
import shutil

template_directory = os.path.expanduser("~/.template/installed/")


def directory_check(copy, dest):
    dest_path = dest + os.sep + str(copy).split(os.sep)[-1]
    if not os.path.exists(template_directory):
        os.makedirs(template_directory)
        print("Created directory: {}".format(template_directory))
    if os.path.exists(copy):
        print("Generating template from: {}".format(copy))
        shutil.copytree(copy, dest_path)
        if os.path.exists(dest_path):
            print("Template has been generated!")
            print("Location: {}".format(dest_path))
        else:
            print("Failed to generate the template.")
    else:
        print("The template {} is not installed.".format(copy))




def main():
    parser = argparse.ArgumentParser(description="Generate a file-structure template.")
    parser.add_argument("-t", help="The template to generate.", required=True)
    parser.add_argument("-d", help="The destination path to generate into.", default=".")
    parser.add_argument("-i", help="The global template directory. This path stores each template.",
                        default=template_directory)
    parser = parser.parse_args()
    directory_check(parser.i + parser.t, parser.d)



if __name__ == '__main__':
    main()