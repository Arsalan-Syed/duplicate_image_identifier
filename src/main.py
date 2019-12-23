from src import DuplicateImageDeleter
import os


folder_path = "photos_for_project/*"
os.chdir("..")
DuplicateImageDeleter.delete_duplicate_images(folder_path)
