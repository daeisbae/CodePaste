from argparse import ArgumentParser, Namespace


def generate_argparse() -> Namespace:
    """
    The cli arguments for CodePaste
    :return: Namespace the arguments given by the user
    """
    parser = ArgumentParser(
        prog="CodePaste",
        description="A program that groups your project into one text, so it can be pasted into LLM for analysis",
    )

    parser.add_argument("project_path", help="The path to the project directory")

    parser.add_argument(
        "-c",
        "--clipboard",
        required=False,
        action="store_true",
        help="Copy to the clipboard",
        default=False,
    )

    parser.add_argument(
        "-w",
        "--whitelist",
        required=False,
        action="append",
        default=[],
        help="Comma separated list of whitelisted words (regex)",
    )

    parser.add_argument(
        "-b",
        "--blacklist",
        required=False,
        action="append",
        default=[],
        help="Comma separated list of blacklisted words (regex)",
    )

    parser.add_argument(
        "-f",
        "--blacklist-filename",
        required=False,
        action="append",
        default=[],
        help="Comma separated list of blacklisted word (regex) for filename",
    )

    parser.add_argument(
        "-e",
        "--blacklist-extension",
        required=False,
        action="append",
        default=[],
        help="Comma separated list of blacklisted extension (regex) for file extension",
    )

    arguments = parser.parse_args()

    return arguments
