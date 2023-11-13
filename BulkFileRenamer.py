import re
import os
import os.path
import shutil


class BulkFileRenamer:
    def __init__(
        self,
        source_dir,
        replace_str,
        search_str,
        order_by=None,
        number_files=1,
        direction=None,
    ):
        self.source_dir = source_dir
        self.replace_str = replace_str
        self.search_str = search_str
        self.order_by = order_by
        self.direction = direction
        self.number_files = number_files
        self.list_files()

    @property
    def source_dir(self):
        return self._source_dir

    @source_dir.setter
    def source_dir(self, source_dir):
        if not re.search(r"^[A-Z]:\\Users\\(?:\w+(?:\s+\w+)*\\)+$", source_dir + "\\"):
            raise ValueError("The format of the source directory is incorrect")
        elif not os.path.isdir(source_dir):
            raise ValueError("The directory doesn`t exists.")
        for root, _, files in os.walk(source_dir):
            pass
        if len(files) == 0:
            raise ValueError("The directory is empty")
        self._source_dir = source_dir

    @property
    def search_str(self):
        return self._search_str

    @search_str.setter
    def search_str(self, search_str):
        self._search_str = search_str

    @property
    def replace_str(self):
        return self._replace_str

    @replace_str.setter
    def replace_str(self, replace_str):
        if not re.search(r"^[a-zA-Z]+$", replace_str):
            raise ValueError("The pattern must contain only letters.")
        elif len(replace_str) > 20:
            raise ValueError("The pattern must be shorter than 20 characters.")
        self._replace_str = replace_str

    @property
    def number_files(self):
        return self._replace_str

    @number_files.setter
    def number_files(self, number_files):
        for root, _, files in os.walk(self.source_dir):
            pass
        if number_files > len(files):
            raise ValueError("Nº files indicated > Nº files on the directory")
        elif number_files <= 0:
            raise ValueError("Nº files indicated must be greater than 0")
        else:
            self._number_files = number_files

    def list_files(self):
        if self.order_by:
            # FILES TO RENAME HAVE BEEN SORTED
            for root, _, files in os.walk(self._source_dir):
                pass
            if self.order_by == "size":  # SORTED BY SIZE
                k = lambda x: os.stat(os.path.join(root, x)).st_size
            elif self.order_by == "name":  # SORTED BY NAME
                k = lambda x: x
            else:  # SORTED BY TIME
                k = lambda x: os.stat(os.path.join(root, x)).st_mtime
            n = self._number_files
            # NUMBER OF FILES TO BE RENAMED (ONCE THEY'VE BEEN SORTED)
            files = [
                os.path.join(root, f)
                for f in sorted(files, key=k, reverse=self.direction)
            ][:n]
            # LIST OF FILES TO BE RENAMED (ONCE THEY'VE BEEN SORTED AND THE NUMBER-
            # -OF FILES HAS BEEN ESTABLISHED)
        # --------------------------------------------------------------------------------------------------------------------------------------
        else:  # FILES TO RENAME HAVEN´T BEEN SORTED, SO WE'LL RENAME ALL FILES
            files = [
                os.path.join(root, filename)
                for root, _, files in os.walk(self._source_dir)
                for filename in files
            ]

        self.rename_files(files)  # WE'LL RENAME THE LIST OF FILES

    def rename_files(self, files):
        if self._search_str:
            # FROM THE LIST OF FILES, ONLY THE FILES THAT CONTAIN THE SEARCH STRING'LL BE RENAMED
            def func_for_filter(x):
                return re.search(
                    self._search_str, os.path.basename(x).rsplit(".")[0], re.IGNORECASE
                )

            # LAMBDA FUNCTION TO FILTER ONLY THE FILES IN THE LIST THAT CONTAINS THE SEARCH STRING
            files_filtered = filter(func_for_filter, files)
            for old_path in files_filtered:
                new_path = old_path.replace(self._search_str, self._replace_str)
                i = 0
                while os.path.exists(new_path):
                    new_path = old_path.replace(
                        self._search_str, f"{self._replace_str}{i:03}"
                    )
                    i += 1
                shutil.move(old_path, new_path)
                print(f"Renamed: {old_path} to {new_path}")
        else:
            # RENAME ALL FILES FROM LIST (NO SEARCH STRING) AND ADD A COUNTER TO THE NAME
            i = 0
            for old_path in files:
                root = os.path.split(old_path)[0]
                ext = os.path.splitext(old_path)[1]
                new_path = os.path.join(root, f"{self._replace_str}{i:03}.{ext}")
                while os.path.exists(new_path):
                    i += 1
                    new_path = os.path.join(root, f"{self._replace_str}{i:03}.{ext}")
                shutil.move(old_path, new_path)
                print(f"Renamed: {old_path} to {new_path}")
                i += 1
