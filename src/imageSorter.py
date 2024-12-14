from rich.console import Console
import os
import time
import shutil

from .utils import isdirexist, threadpool_executer, display_progress

console = Console()

class ImageSorter:
    """
    A class for sorting images from an input directory to an output directory.

    Args:
        input_dir (str): The path to the input directory containing the images.
        output_dir (str): The path to the output directory where the images will be sorted.
        multi_thread (bool, optional): Whether to use multi-threading for faster processing. Defaults to False.
    """

    def __init__(self, input_dir:str, output_dir:str, multi_thread:bool=False) -> None:
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.multi_thread = multi_thread

    @classmethod
    def initialize(cls, input_dir:str, output_dir:str, multi_thread:bool=False):
        """
        Initializes an instance of the ImageSorter class.

        Args:
            input_dir (str): The path to the input directory containing the images.
            output_dir (str): The path to the output directory where the images will be sorted.
            multi_thread (bool, optional): Whether to use multi-threading for faster processing. Defaults to False.

        Returns:
            ImageSorter: An instance of the ImageSorter class.
        
        Raises:
            Exception: If the input or output directory does not exist.
        """
        if not isdirexist(input_dir):
            raise Exception("The input directory does not exist.")
        if not isdirexist(output_dir):
            raise Exception("The output directory does not exist.")
        return cls(
            input_dir,
            output_dir,
            multi_thread
        )

    @property
    def metadata_images(self) -> list[dict]:
        """
        Retrieves the metadata of the images in the input directory.

        Returns:
            list[dict]: A list of dictionaries containing the metadata of the images.
                Each dictionary contains the following keys:
                - file_path: The path to the image file.
                - size: The size of the image file in bytes.
                - creation_time: The timestamp of the creation of the image file.
                - last_modified: The timestamp of the last modification of the image file.
                - last_accessed: The timestamp of the last access to the image file.
        """
        metadata = []
        for root, dirs, files in os.walk(self.input_dir):
            for file in files:
                file_path = os.path.join(root, file)
                info = os.stat(file_path)
                metadata.append({
                    'file_path': file_path,
                    'size': info.st_size,
                    'creation_time': info.st_ctime,
                    'last_modified': info.st_mtime,
                    'last_accessed': info.st_atime
                })
        return metadata

    def copy_file(self, file:dict):
        """
        Copies a file to the appropriate directory based on its metadata.

        Args:
            file (dict): A dictionary containing the metadata of the file to be copied.
                The dictionary should have the following keys:
                - file_path: The path to the file.
                - last_modified: The timestamp of the last modification of the file.
                - creation_time: The timestamp of the creation of the file.
                - last_accessed: The timestamp of the last access to the file.
        """
        last_date = min(file['last_modified'], file['creation_time'], file['last_accessed'])
        year = time.strftime('%Y', time.gmtime(last_date))
        month = time.strftime('%m', time.gmtime(last_date))
        year_dir = os.path.join(self.output_dir, year)
        month_dir = os.path.join(year_dir, month)
        try:
            if not os.path.isdir(month_dir):
                os.makedirs(month_dir)
        except FileExistsError:
            pass
        finally:
            shutil.copy2(file['file_path'], month_dir)

    def _run_multi_thread(self):
        """
        Runs the file copying process using multi-threading.
        """
        threadpool_executer(self.copy_file, self.metadata_images)
    
    def _run(self):
        """
        Runs the file copying process sequentially.
        """
        for index, file in enumerate(self.metadata_images, 1):
            self.copy_file(file)
            display_progress(index, len(self.metadata_images))

    def run(self):
        """
        Runs the file copying process based on the specified configuration.

        If multi-threading is enabled, the process will run using multiple threads.
        Otherwise, the process will run sequentially.

        Prints "Done!" when the process is completed.
        """
        if self.multi_thread:
            self._run_multi_thread()
        else:
            self._run()
        console.print("Done!", style="bold green")