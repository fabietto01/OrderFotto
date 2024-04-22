import os
from multiprocessing.pool import ThreadPool
from rich.console import Console

console = Console()

def display_progress(iteration, total):
    bar_max_width = 45  # chars
    bar_current_width = bar_max_width * iteration // total
    bar = "█" * bar_current_width + "-" * (bar_max_width - bar_current_width)
    progress = "%.1f" % (iteration / total * 100)
    console.print(f"|{bar}| {progress} %", end="\r", style="bold green")
    if iteration == total:
        print()

def isdirexist(dir) -> bool:
    """
    Check if the given directory exists.

    Args:
        dir (str): The directory path to check.

    Returns:
        bool: True if the directory exists, False otherwise.
    """
    if os.path.isdir(dir):
        return True
    else:
        return False
    
def threadpool_executer(function, iterable, iterable_length:int=None, max_workers:int=None):
    """
    Execute a function in a thread pool.

    Args:
        function (function): The function to execute.
        iterable (iterable): The iterable to pass to the function.
        iterable_length (int): The length of the iterable.
        max_workers (int, optional): The number of workers to use. Defaults to 4.

    Returns:
        list: The result of the function for each element in the iterable.
    """
    if not max_workers:
        max_workers = os.cpu_count()
    if not iterable_length:
        iterable_length = len(iterable)
    with ThreadPool(max_workers) as pool:
        for loop_index, _ in enumerate(pool.imap(function, iterable), 1):
            display_progress(loop_index, iterable_length)