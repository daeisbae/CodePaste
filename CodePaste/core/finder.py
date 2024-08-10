import os
from typing import List

from CodePaste.core.directory import Directory
from CodePaste.core.file import File
from CodePaste.core.filter import PathFilter


def directory_refresh(
    directory: Directory,
    allowed_regex: List[str] = [],
    general_regex: List[str] = [],
    filename_regex: List[str] = [],
    extension_regex: List[str] = [],
) -> None:
    """
    It will enumerate subdirectories and subfiles recursively,
    but it will not find files that are blacklisted through regex
    :param directory: The target directory to find subdirectories and subfiles.
    :param allowed_regex: optional, if the path matches, even it will never be filtered (removed)
    :param general_regex: optional, scan all path if file matches the expression
    :param filename_regex: optional, scan only filenames if file matches the expression
    :param extension_regex: optional, scan only extensions if file matches the expression
    :return:
    """
    base_filter: PathFilter = PathFilter(
        allowed_regex=allowed_regex, general_regex=general_regex
    )

    for dir_paths, dir_names, filenames in os.walk(directory.get_absolute_path()):
        if base_filter.should_filter(dir_paths):
            continue

        for dirname in dir_names:
            directory_path = os.path.join(dir_paths, dirname)
            if base_filter.should_filter(directory_path):
                continue

            child_dir = Directory(directory_path)
            directory_refresh(
                child_dir,
                allowed_regex=allowed_regex,
                general_regex=general_regex,
                filename_regex=filename_regex,
                extension_regex=extension_regex,
            )
            directory.add_subdirectory(child_dir)

        file_filter: PathFilter = PathFilter(
            allowed_regex=allowed_regex,
            general_regex=general_regex,
            filename_regex=filename_regex,
            extension_regex=extension_regex,
        )

        for filename in filenames:
            file_path = os.path.join(dir_paths, filename)
            if file_filter.should_filter(file_path):
                continue
            child_file = File(file_path)
            directory.add_file(child_file)
