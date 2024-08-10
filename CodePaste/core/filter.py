from typing import List
import re
import os


class PathFilter:
    """
    Filter the file using Regular Expressions.
    It is used to remove the unwanted files or directories
    """

    general_regex_: List[str]
    filename_regex_: List[str]
    extension_regex_: List[str]
    allowed_regex_: List[str]

    def __init__(
        self,
        allowed_regex: List[str] = [],
        general_regex: List[str] = [],
        filename_regex: List[str] = [],
        extension_regex: List[str] = [],
    ) -> None:
        """
        Constructor for File filter
        :param allowed_regex: optional, if the path matches, even it will never be filtered (removed)
        :param general_regex: optional, scan all path if file matches the expression
        :param filename_regex: optional, scan only filenames if file matches the expression
        :param extension_regex: optional, scan only extensions if file matches the expression
        """
        self.allowed_regex_ = allowed_regex
        self.general_regex_ = general_regex
        self.filenames_regex_ = filename_regex
        self.extension_regex_ = extension_regex

    def should_filter(self, fullpath: str) -> bool:
        """
        Does it match the regex patterns?
        If the file matches in allowed regex, it will never be filtered (removed)
        Other than that, any filtering regex will filter the file or directory
        :param fullpath: The full path of the file
        :return: bool result of the match
        """
        for allowed_regex in self.allowed_regex_:
            if re.search(allowed_regex, fullpath):
                return False

        for general_regex in self.general_regex_:
            if re.search(general_regex, fullpath):
                return True

        for filenames_regex in self.filenames_regex_:
            if re.search(filenames_regex, os.path.basename(fullpath)):
                return True

        for extension_regex in self.extension_regex_:
            if re.search(extension_regex, str(os.path.splitext(fullpath)[1])):
                return True

        return False
