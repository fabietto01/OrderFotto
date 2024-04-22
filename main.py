import sys
#-i "C:\Users\fabio\Desktop\beckap veccio telefeno" -o "C:\Users\fabio\Desktop\Imagini riordinate"

def main():
    """
    Entry point of the program.
    
    This function imports the `execute_from_command_line` function from the `src` module and executes it with the command line arguments passed to the script.
    """
    try:
        from src import execute_from_command_line
    except ImportError as e:
        raise ImportError(
            "Couldn't import ImageSorter"
        )
    execute_from_command_line(sys.argv[1:])

if __name__ == '__main__':
    main()