# OrderFotto

This project is responsible for moving and reordering the images in a folder, dividing them into sub-folders divided by year and month.

## Index

- [Installation](#installation)
- [Usage](#usage)

## Installation

Follow these steps to install the project:

1. Clone the repository: `git clone https://github.com/fabietto01/OrderFotto.git`
2. Enter the project directory: `cd OrderFotto`
3. Create a Python virtual environment: `python3 -m venv env`
4. Activate the virtual environment: 
    - On Windows: `.\env\Scripts\activate`
    - On Unix or MacOS: `source env/bin/activate`
5. Install the dependencies from the requirements.txt file: `pip install -r requirements.txt`

## Usage

To use the project, simply start the main.py file and pass the required arguments: `--input`, `--output` and `--multi-thread`. The `--multi-thread` argument is not mandatory and by default is set to false. The other two arguments, `--input` and `--output`, represent respectively the source folder where all the photos are present and the destination folder where the script will insert the images.

For example:

1. Run the command: `python main.py --input path/to/the/photo/folder --output path/to/the/destination/folder`
2. If you want to use multi-threading, add the `--multi-thread` argument: `python main.py --input path/to/the/photo/folder --output path/to/the/destination/folder --multi-thread`
3. Follow the instructions displayed on the console.