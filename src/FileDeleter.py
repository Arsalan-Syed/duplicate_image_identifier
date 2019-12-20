import os


def delete_files(file_names):
    for file_name in file_names:
        os.remove(file_name)
