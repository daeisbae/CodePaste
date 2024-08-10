from pathlib import Path

from CodePaste.core.file import File
from typing import Self, List


class Directory:
    """
    Directory responsible for managing subdirectories and files inside the specified directory path.
    """

    name_: str
    absolute_path_: str
    files_: List[File]
    subdirectories_: List[Self]

    def __init__(self, absolute_path: str) -> None:
        """
        The constructor for Directory class.
        :param absolute_path: Absolute path of the directory.
        """
        self.absolute_path_ = absolute_path
        self.name_ = Path(absolute_path).name
        self.files_ = list()
        self.subdirectories_ = list()

    def get_name(self) -> str:
        """
        Returns the name of the directory.
        :return: the name of the directory.
        """
        return self.name_

    def get_absolute_path(self) -> str:
        """
        Returns the absolute path of the directory.
        :return: the absolute path of the directory.
        """
        return self.absolute_path_

    def add_file(self, file: File) -> None:
        """
        Adds a file to the directory.
        :param file: the file to be added to the directory.
        """
        self.files_.append(file)

    def add_files(self, files: list[File]) -> None:
        """
        Adds multiple files to the directory.
        :param files: the files to be added to the directory.
        """
        self.files_.extend(files)

    def add_subdirectory(self, subdirectory: Self) -> None:
        """
        Adds a subdirectory to the directory.
        :param subdirectory: the subdirectory to be added to the directory.
        """
        self.subdirectories_.append(subdirectory)

    def add_subdirectories(self, subdirectories: list[Self]) -> None:
        """
        Adds multiple subdirectories to the directory.
        :param subdirectories: the subdirectories to be added to the directory.
        """
        self.subdirectories_.extend(subdirectories)

    def get_files(self) -> List[File]:
        """
        Returns the child files of the directory.
        :return: the child files inside the directory.
        """
        return self.files_

    def get_subdirectories(self) -> List[Self]:
        """
        Returns the subdirectories of the directory.
        :return: the subdirectories inside the directory.
        """
        return self.subdirectories_

    def __str__(self) -> str:
        return self.name_
