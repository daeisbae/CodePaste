from enum import Enum
from pathlib import Path


class FileTypeInMarkdown(Enum):
    """
    Enum class for the conversion of file extension to markdown codeblock language highlighting
    """

    PYTHON = "python"
    C = "c"
    CPP = "cpp"
    CHeader = "h"
    Java = "java"
    SHELL = "sh"
    UNDEFINED = ""


class File:
    """
    A class to represent one file.
    It contains all the file info required to feed the information to LLM
    """

    full_path_: str
    filename_: str
    extension_: str
    markdown_type_: FileTypeInMarkdown
    data_: str

    def __init__(self, full_path: str) -> None:
        """
        :param full_path: The absolute path of the file
        """
        self.full_path_ = full_path
        self.filename_ = Path(self.full_path_).stem
        self.extension_ = Path(self.full_path_).suffix
        self.markdown_type_ = self.match_extension(self.extension_)
        self.data_ = ""

    def get_name(self) -> str:
        return self.filename_ + self.extension_

    def read_file_(self) -> str:
        """
        Reads the file and returns the contents as a string
        :return: the contents of the file
        """
        file_data: str
        with open(self.full_path_, "rb") as f:
            file_data = f.read().decode("utf-8")
        return file_data

    def get_data(self) -> str:
        """
        Returns the contents of the file as a string
        if the data_ is cached, return the cached data
        :return: the contents of the file
        """
        if not self.data_ or len(self.data_) == 0:
            self.data_ = self.read_file_()
        return self.data_

    def get_markdown_type(self) -> str:
        """
        Returns the markdown codeblock language type
        :return: the markdown codeblock language type
        """
        return self.markdown_type_.value

    def get_full_path(self) -> str:
        """
        Returns the absolute path of the file
        :return: the absolute path of the file
        """
        return self.full_path_

    @staticmethod
    def match_extension(extension: str) -> FileTypeInMarkdown:
        """
        Matches the file extension to markdown codeblock language highlighting
        :param extension: The file extension to be matched
        :return: The markdown codeblock language type
        """
        extension_str: FileTypeInMarkdown
        match extension:
            case ".py":
                extension_str = FileTypeInMarkdown.PYTHON
            case ".c":
                extension_str = FileTypeInMarkdown.C
            case ".cpp" | ".cxx" | ".cc":
                extension_str = FileTypeInMarkdown.CPP
            case ".h" | ".hpp" | ".h":
                extension_str = FileTypeInMarkdown.CHeader
            case ".java":
                extension_str = FileTypeInMarkdown.Java
            case ".sh":
                extension_str = FileTypeInMarkdown.SHELL
            case _:
                extension_str = FileTypeInMarkdown.UNDEFINED

        return extension_str

    def __str__(self) -> str:
        return self.filename_ + self.extension_
