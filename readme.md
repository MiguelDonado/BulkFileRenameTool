# Bulk File Renamer

This Python project contains a script `main.py` and a class `BulkFileRenamer` that can be used to rename multiple files in a directory based on certain parameters.

## Features

- **Search and replace**: The class takes a `search_str` and `replace_str` as parameters. It will replace the `search_str` in the file names with the `replace_str`.
- **Order by**: The `order_by` parameter can be used to specify the order in which the files should be renamed.
- **Number of files**: The `number_files` parameter can be used to limit the number of files that will be renamed.
- **Direction**: The `direction` parameter can be used to specify the direction in which the files should be renamed.

## Usage

The `main.py` script uses the `argparse` library to parse command line arguments. You can use the following command line arguments:

- `source`: The directory containing the files to be renamed.
- `replace`: The string to replace in the file names.
- `search`: The string to search for in the file names.
- `order_by`: The order in which the files should be renamed. Can be `name`, `size`, or `time`.
- `number_files`: The number of files to rename.
- `rev`: Whether to reverse the order of the files.
## Example Usage

Run the following command in your terminal:

```bash
python main.py --source path/to/your/directory --replace new --search old --order_by name --number_files 10 --rev
```
