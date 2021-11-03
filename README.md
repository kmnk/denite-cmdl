# denite-cmdl
execute named commands

## Requirements
- [denite.nvim][denite]

## Usage
1. make first cmdl data json file
    - (default) make template cmdl.json file by make command
        - `make` or `make copy-cmdl-json`
        - then put cmdl.json to `~/.cache/denite-cmdl/cmdl.json`
    - (customized)
        1. copy template/cmdl.json file to where you want to put
        2. set your data directory by prepared command on your .vimrc
            ```
            call cmdl#set_data_directory_path()
            call cmdl#set_data_directory_path('[path to your data directory]')
            ```
2. execute `Denite` command with `cmdl` on Vim
    ```
    Denite cmdl
    ```
3. select and execute listed command

If you want to add other commands, edit your cmdl.json manually )

[denite]:https://github.com/Shougo/denite.nvim
