from typing import List

from pyperclip import copy  # type: ignore

from CodePaste.core.project import Project
from CodePaste.core.writer import code_paste
from CodePaste.cli.arguments import generate_argparse


def main():
    args = generate_argparse()
    clipboard: bool = args.clipboard
    whitelist: List[str] = args.whitelist if args.whitelist is not None else []
    blacklist: List[str] = args.blacklist if args.blacklist is not None else []
    blacklist_filename: List[str] = (
        args.blacklist_filename if args.blacklist_filename is not None else []
    )
    blacklist_extension: List[str] = (
        args.blacklist_extension if args.blacklist_extension is not None else []
    )

    pasted_code = code_paste(
        Project(
            args.project_path,
            allowed_regex=whitelist,
            general_regex=blacklist,
            filename_regex=blacklist_filename,
            extension_regex=blacklist_extension,
        ),
    )

    if clipboard:
        copy(pasted_code)

    print(pasted_code)
