from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="CodePaste",
    version="0.1",
    description="Paste your codebase to ChatGPT by one simple line of command",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "pyperclip",
    ],
    python_requires=">=3.11",
    url="https://github.com/daeisbae/CodePaste",
    project_urls={
        "Bug Tracker": "https://github.com/daeisbae/CodePaste/issues",
    },
    entry_points={
        "console_scripts": ["codepaste=CodePaste.cli.cli:main"],
    },
)
