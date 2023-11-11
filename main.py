print("Comienzo del proyecto")
import os
import sys
import shutil


def main():
    if len(sys.argv) != 4:
        print(
            "Usage: python main.py <source_directory> <search_string> <replace_string>"
        )
    else:
        source_dir = sys.argv[1]
        search_str = sys.argv[2]
        replace_str = sys.argv[3]

        renamer = BulkFileRenamer(source_dir, search_str, replace_str)
        renamer.rename_files()


class BulkFileRenamer:
    def __init__(self, source_dir, search_str, replace_str):
        self.source_dir = source_dir
        self.search_str = search_str
        self.replace_str = replace_str

    def rename_files(self):
        try:
            for root, _, files in os.walk(self.source_dir):
                for filename in files:
                    if self.search_str in filename:
                        new_filename = filename.replace(
                            self.search_str, self.replace_str
                        )
                        old_path = os.path.join(root, filename)
                        new_path = os.path.join(root, new_filename)
                        shutil.move(old_path, new_path)
                        print(f"Renamed: {old_path} to {new_path}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
