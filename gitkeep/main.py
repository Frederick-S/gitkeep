import os
import sys


def main():
    folder = '.' if len(sys.argv) == 1 else sys.argv[1]

    create_gitkeep(folder)


def create_gitkeep(folder):
    for root, folders, files in os.walk(folder):
        if len(folders) == 0 and len(files) == 0:
            create_file(os.path.join(root, '.gitkeep'))


def create_file(file_name):
    try:
        with open(file_name, 'x') as f:
            pass
    except FileExistsError as e:
        pass

if __name__ == '__main__':
    main()
