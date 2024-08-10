import logging
from sys import exit
from pathlib import Path
from typing import List

from CodePaste.core.directory import Directory
from CodePaste.core.finder import directory_refresh


class Project:
    """
    The base directory of all the directories to feed to LLM.
    It is the root directory that connects all the subdirectories and files
    """

    name_: str
    absolute_path: Path
    root_dir_: Directory

    def __init__(
        self,
        path: str,
        allowed_regex: List[str] = [],
        general_regex: List[str] = [],
        filename_regex: List[str] = [],
        extension_regex: List[str] = [],
    ) -> None:
        """
        The constructor for Project class.
        :param path: The root directory of the project.
        """
        self.name_ = Path(path).name
        self.absolute_path = Path(path).absolute()

        if not self.absolute_path.exists():
            logging.critical("Directory does not exist: " + str(self.absolute_path))
            exit(1)
        self.root_dir_ = Directory(str(self.absolute_path))
        directory_refresh(
            self.root_dir_,
            allowed_regex=allowed_regex,
            general_regex=general_regex,
            filename_regex=filename_regex,
            extension_regex=extension_regex,
        )

    def get_name(self) -> str:
        """
        The name of the root directory.
        :return: name of the root directory.
        """
        return self.name_

    def get_root_dir(self) -> Directory:
        """
        The root Directory of the project.
        :return: The root Directory of the project.
        """
        return self.root_dir_
