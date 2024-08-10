# CodePaste
A program that combines your project source code into a single text used for LLM analysis.
Specify directory, file extension to exclude it using Regex, then output comprehensive codebase to feed your codebase to ChatGPT(LLM).
You can copy the output to the clipboard with the cli argument `-c` and paste it directly to any LLM.

## Demo
```sh
>>> codepaste {Path to the project}/dragonfly/src/core -c | more                                                                                                                  ─╯

core
├── testdata
│   └── ids.txt
├── search
│   ├── ast_expr.h
│   ├── ast_expr.cc
│   ├── query_driver.h
│   ├── CMakeLists.txt
│   ├── compressed_sorted_set.h
│   ├── compressed_sorted_set.cc
│   ├── base.cc
│   ├── indices.cc
│   ├── search_test.cc
│   ├── search.cc
│   ├── block_list.h
│   ├── vector_utils.cc
...

./dragonfly/src/core/generate_bin_sizes.py
```python
#!/usr/bin/env python3

import argparse
import random
from array import array

# We print in 64 bit words.
ALIGN = 1 << 10  # 1KB alignment


def print_small_bins():
    prev_val = 0
    for i in range(56, 1, -1):
        len = (4096 - i*8)  # reduce by size of hashes
        len = (len // 8)*8  # make it 8 bytes aligned
        if len != prev_val:
            print(i, len)
            prev_val = len
    print()
    ...
```

## How to Install?
### For Simple Testing
```sh
git clone https://github.com/daeisbae/CodePaste.git
cd CodePaste/CodePaste/cli
python3 __main__.py --help
```

### Manual Installation (Through setup.py)
```sh
git clone https://github.com/daeisbae/CodePaste.git
cd CodePaste
python3 setup.py sdist
pip3 install dist/CodePaste-0.1-py3-none-any.whl
codepaste --help
```

### Docker Installation (Currently Unavailable)
```sh
git clone https://github.com/daeisbae/CodePaste.git
cd CodePaste
docker build -t codepaste .
docker run --rm -it --name codepaste codepaste --help
```

## How to use it?
```sh
codepaste --help
usage: CodePaste [-h] [-c] [-w WHITELIST] [-b BLACKLIST] [-f BLACKLIST_FILENAME] [-e BLACKLIST_EXTENSION] project_path

A program that groups your project into one text, so it can be pasted into LLM for analysis

positional arguments:
  project_path          The path to the project directory

options:
  -h, --help            show this help message and exit
  -c, --clipboard       Copy to the clipboard
  -w WHITELIST, --whitelist WHITELIST
                        Comma separated list of whitelisted words (regex)
  -b BLACKLIST, --blacklist BLACKLIST
                        Comma separated list of blacklisted words (regex)
  -f BLACKLIST_FILENAME, --blacklist-filename BLACKLIST_FILENAME
                        Comma separated list of blacklisted word (regex) for filename
  -e BLACKLIST_EXTENSION, --blacklist-extension BLACKLIST_EXTENSION
                        Comma separated list of blacklisted extension (regex) for file extension
```