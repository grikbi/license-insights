"""Class representing the data store that uses local file system."""

import fnmatch
import json
import os
from src.util.data_store.abstract_data_store import AbstractDataStore


class LocalFileSystem(AbstractDataStore):
    """Class representing the data store that uses local file system."""

    def __init__(self, src_dir):
        """Construct the class and initializes the src_dir attribute."""
        self.src_dir = src_dir
        # ensure path ends with a forward slash
        self.src_dir = self.src_dir if self.src_dir.endswith("/") else self.src_dir + "/"

    def get_name(self):
        """Return printable name of this storage."""
        return "Local filesystem dir: " + self.src_dir

    def list_files(self, prefix=None):
        """List all the files in the source directory."""
        list_filenames = []
        for root, dirs, files in os.walk(self.src_dir):
            for basename in files:
                if fnmatch.fnmatch(basename, "*.json"):
                    filename = os.path.join(root, basename)
                    if prefix is None:
                        filename = filename[len(self.src_dir):]
                        list_filenames.append(filename)
                    elif filename.startswith(os.path.join(self.src_dir, prefix)):
                        filename = filename[len(self.src_dir):]
                        list_filenames.append(filename)
        list_filenames.sort()
        return list_filenames

    def read_json_file(self, filename):
        """Read JSON file from the data_input source."""
        return json.load(open(os.path.join(self.src_dir, filename)))

    def read_all_json_files(self):
        """Read all the files from the data_input source."""
        list_filenames = self.list_files(prefix=None)
        list_contents = []
        for file_name in list_filenames:
            contents = self.read_json_file(filename=file_name)
            list_contents.append((file_name, contents))
        return list_contents

    def write_json_file(self, filename, contents):
        """Write JSON file into data_input source."""
        with open(os.path.join(self.src_dir, filename), 'w') as outfile:
            json.dump(contents, outfile)
        return None

    def upload_file(self, src, target):
        """Upload file into data store."""
        # self.bucket.upload_file(src, target)
        return None

    def download_file(self, src, target):
        """Download file from data store."""
        # self.bucket.download_file(src, target)
        return None

    @classmethod
    def convert_list_of_tuples_to_string(cls, tuple_list):
        """Perform conversion from list of tuples to string."""
        string_value = str(tuple_list)
        return string_value
