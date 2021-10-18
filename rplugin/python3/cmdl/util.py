"""
cmdl utils
"""

import os
import json
import copy

CMDL_VERSION = "0.1.0"
CMDL_TEMPLATE_OF = {
    CMDL_VERSION: {
        "version": CMDL_VERSION,
        "group": {},
    },
}

def new_cmdl_dict():
    """
    return template cmdl dictionary
    """
    return copy.deepcopy(CMDL_TEMPLATE_OF[CMDL_VERSION])

def write(vim, cmdl_dict):
    """
    write cmdl data to cmdl file
    """
    if not os.path.isdir(__get_data_directory_path(vim)):
        os.makedirs(__get_data_directory_path(vim))

    with open(__get_data_file_path(vim), 'w') as f:
        json.dump(cmdl_dict, f, ensure_ascii=False, indent=2)

def read(vim):
    """
    open and read cmdl data, and return as dictionary
    except FileNotFoundError
    """
    # TODO: switch parse logic by version
    with open(__get_data_file_path(vim)) as f:
        data = f.read()
        return json.loads(data)

def __get_data_directory_path(vim):
    return vim.call('cmdl#get_data_directory_path')

def __get_data_file_path(vim):
    return vim.call('cmdl#get_data_file_path')

def main(): pass

if __name__ == '__main__': main()
