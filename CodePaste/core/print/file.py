from CodePaste.core.file import File


def file_print_format(file: File, new_lines: int = 2) -> str:
    """
    Returns the string of file path and code inside the markdown codeblock for LLMs to understand the codebase
    :param file: The file to print
    :param new_lines: Number of new lines to include after the file info is printed
    :return: The string of file path and code inside the markdown codeblock
    """
    return f"{file.get_full_path()}\n```{file.get_markdown_type()}\n{file.get_data()}\n```{"\n" * new_lines}"
