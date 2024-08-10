from typing import List, Union

from CodePaste.core.directory import Directory
from CodePaste.core.file import File


def draw_directory_tree(root_dir: Directory) -> str:
    """
    Draws a directory tree then return in string
    (But including the root directory at the top branch)
    ast
    ├── CMakeLists.txt
    ├── ast.cpp
    └── ast.hpp
    :param root_dir: The root directory to draw the tree from. (Project directory)
    :return:         The directory tree as a string.
    """
    return root_dir.get_name() + "\n" + draw_directory_tree_(root_dir, "")


def draw_directory_tree_(directory: Directory, prefix: str = "") -> str:
    """
    Draws a directory tree then return in string
    ├── CMakeLists.txt
    ├── ast.cpp
    └── ast.hpp
    :param directory: The directory to draw the tree of.
    :param prefix:    The tree branch to draw and number of spaces
    :return:          The Directory tree in string of the given Directory
    """
    directory_tree_str: str = ""

    directories: List[Directory] = directory.get_subdirectories()
    files: List[File] = directory.get_files()
    contents: List[Union[Directory, File]] = [*directories, *files]

    for i, content in enumerate(contents):
        is_last = i == len(contents) - 1

        directory_tree_str += (
            f"{prefix}{'└── ' if is_last else '├── '}{content.get_name()}\n"
        )

        if isinstance(content, Directory):
            extension = "    " if is_last else "│   "
            directory_tree_str += draw_directory_tree_(content, prefix + extension)

    return directory_tree_str
