import os
import sys


def main():
    folder = '.' if len(sys.argv) == 1 else sys.argv[1]

    create_gitkeep(folder)


def create_gitkeep(folder):
    for root, folders, files in os.walk(folder):
        gitkeep_path = os.path.join(root, '.gitkeep')
        gitkeep_exists = os.path.exists(gitkeep_path)

        if gitkeep_exists and (len(folders) != 0 or len(files) > 1):
            os.remove(gitkeep_path)

        if len(folders) == 0 and len(files) == 0:
            create_file(gitkeep_path)


def create_file(file_path):
    try:
        with open(file_path, 'x') as f:
            pass
    except FileExistsError as e:
        pass


if __name__ == '__main__':
    main()
