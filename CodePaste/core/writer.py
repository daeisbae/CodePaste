import logging
from typing import List

from CodePaste.core.directory import Directory
from CodePaste.core.print.file import file_print_format
from CodePaste.core.project import Project
from CodePaste.core.print.tree import draw_directory_tree


def code_paste(project: Project) -> str:
    """
    The main function which retrieves the path of the Project and
    get all the subfiles and directories
    :param project: the project folder to get all the file
    :return: The tree structure of the project with all the subfiles and directories
    """
    codebase: str = ""
    codebase += draw_directory_tree(project.get_root_dir())
    codebase += "\n"
    codebase += print_child_files_(project.get_root_dir())
    return codebase


def print_child_files_(directory: Directory, newline: int = 0) -> str:
    """
    Returns all the subfiles of the given directory
    :param directory: the directory to search the files
    :param newline: the spacing between each files
    :return: the string of all the subfiles data and path of the given directory
    """
    code_chunks: str = ""
    for file_in_dir in directory.get_files():
        try:
            code_chunks += file_print_format(file_in_dir)
        except UnicodeDecodeError:
            logging.warning(
                f"Failed to read the file: {file_in_dir.get_full_path()} due to unicode error"
            )
        code_chunks += newline * "\n"

    return code_chunks


def get_child_dirs_recursive_(
    directory: Directory, newline: int = 2
) -> List[Directory]:
    """
    Recursively walk the directory tree and return all child directories.
    :param directory: The directory to walk.
    :param newline: The number of newline characters to use.
    :return: list of subdirectories of the directory given.
    """
    all_dirs: List[Directory] = []

    child_dirs: List[Directory] = directory.get_subdirectories()

    all_dirs.extend(child_dirs)
    for child_dir in child_dirs:
        all_dirs.extend(get_child_dirs_recursive_(child_dir, newline=newline))

    return all_dirs
