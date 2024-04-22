from .imageSorter import ImageSorter
import sys
import argparse

def execute_from_command_line(argv=None):
    """
    This function is called when executing the command from the terminal.
    It checks if the following arguments are passed:
    - input_dir, input or -i for the input directory
    - output_dir, output or -o for the output directory

    After that, it initializes the ImageSorter class and calls the run method.
    """
    argv = argv or sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, help='input directory')
    parser.add_argument('-o', '--output', required=True, help='output directory')
    parser.add_argument(
        '-m', '--multi-thread', action='store_true', 
        help='use multi-threading', default=False
    )
    parser.add_help = True
    args = parser.parse_args(argv)
    sorter = ImageSorter.initialize(args.input, args.output, args.multi_thread)
    sorter.run()