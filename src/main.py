from src import DuplicateImageDeleter

folder_path = "photos_for_project/*"
DuplicateImageDeleter.delete_duplicate_images(folder_path)
