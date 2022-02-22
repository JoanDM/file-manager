import json
import webbrowser
from pathlib import Path


def create_directory(target_directory):
    target_directory = Path(target_directory)
    target_directory.mkdir(parents=True, exist_ok=True)


def find_new_unique_file_path(target_file_path, sep="_"):
    i = 0
    file_id_len = 0
    while target_file_path.exists():
        unique_file_id_len = len(str(target_file_path.stem)) - file_id_len
        i += 1
        target_file_path = Path(
            target_file_path.parent,
            f"{target_file_path.stem[:unique_file_id_len]}"
            f"{sep}{i}{target_file_path.suffix}",
        )
        file_id_len = len(f"{sep}{i}")
    return target_file_path


def list_all_filepaths_in_dir_with_specific_extension(directory, list_of_extensions):
    list_of_files = []
    for extension in list_of_extensions:
        list_of_files += sorted(directory.glob(f"*.{extension}"))
    return list_of_files


def list_all_filenames_in_dir_with_specific_extension(directory, list_of_extensions):
    list_of_filenames = []
    for extension in list_of_extensions:
        list_of_filenames += [f.stem for f in sorted(directory.glob(f"*.{extension}"))]
    return list_of_filenames


def list_all_pngs_in_dir(directory):
    return list_all_filepaths_in_dir_with_specific_extension(directory, ["png"])


def list_all_image_filepaths_in_dir(directory):
    return list_all_filepaths_in_dir_with_specific_extension(
        directory, ["png", "jpg", "jpeg", "bmp", "heic"]
    )


def list_all_image_filenames_in_dir(directory):
    return list_all_filenames_in_dir_with_specific_extension(
        directory, ["png", "jpg", "jpeg", "bmp", "heic"]
    )


def list_all_video_filenams_in_dir(directory):
    return list_all_filenames_in_dir_with_specific_extension(
        directory, ["MP4", "MOV", "mp4", "mov", "avi"]
    )


def list_all_video_filepaths_in_dir(directory):
    return list_all_filepaths_in_dir_with_specific_extension(
        directory, ["MP4", "MOV", "mp4", "mov", "avi"]
    )


def load_json_file_content(path_to_json):
    json_file = open(path_to_json, "r")
    json_content = json_file.read()
    return json.loads(json_content)


def show_file(file_path):
    new = 2  # open in a new tab, if possible
    webbrowser.open(f"file://{file_path}", new=new)
