import os
import time
import shutil

def isdirexist(input_dir) -> bool:
    """
    Check if the given directory exists.

    Args:
        input_dir (str): The directory path to check.

    Returns:
        bool: True if the directory exists, False otherwise.
    """
    if os.path.isdir(input_dir):
        return True
    else:
        return False

def get_file_metadata(input_dir) -> list[dict]:
    """
    Retrieves metadata for all files in the specified directory and its subdirectories.

    Args:
        input_dir (str): The directory path to scan for files.

    Returns:
        list[dict]: A list of dictionaries containing the file metadata. Each dictionary
                    contains the following keys:
                    - 'file_path': The absolute path of the file.
                    - 'size': The size of the file in bytes.
                    - 'last_modified': The timestamp of the last modification of the file.
                    - 'last_accessed': The timestamp of the last access to the file.
    """
    metadata = []
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            file_path = os.path.join(root, file)
            info = os.stat(file_path)
            metadata.append({
                'file_path': file_path,
                'size': info.st_size,
                'last_modified': info.st_mtime,
                'last_accessed': info.st_atime
            })
    return metadata


def order_by_created_data(metadata:list[dict]) -> list[dict]:
    """
    Sorts a list of dictionaries containing metadata by the 'last_modified' key in ascending order.

    Args:
        metadata (list[dict]): A list of dictionaries containing metadata.

    Returns:
        list[dict]: The sorted list of dictionaries.

    """
    return sorted(metadata, key=lambda x: x['last_modified'])

def copy_files(metadata:list[dict], output_dir):
    """
    copia i file in output_dir, dividendo i file in cartelle per anno e messe
    """ 
    for file in metadata:
        # Get the year and month of the last modified timestamp
        last_modified = file['last_modified']
        year = time.strftime('%Y', time.gmtime(last_modified))
        month = time.strftime('%m', time.gmtime(last_modified))
        # Create the output directory if it does not exist
        year_dir = os.path.join(output_dir, year)
        month_dir = os.path.join(year_dir, month)
        if not os.path.isdir(month_dir):
            os.makedirs(month_dir)
        # Copy the file to the output directory
        shutil.copy(file['file_path'], month_dir)

def main():
    input_dir = input("Enter the input directory: ")
    if not isdirexist(input_dir):
        raise Exception("The input directory does not exist.")
    output_dir = input("Enter the output directory: ")
    if not isdirexist(output_dir):
        raise Exception("The output directory does not exist.")
    metadata = get_file_metadata(input_dir)
    sorted_metadata = order_by_created_data(metadata)
    copy_files(sorted_metadata, output_dir)

if __name__ == '__main__':
    main()