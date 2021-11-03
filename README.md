# denite-cmdl
execute named commands

## Requirements
- [denite.nvim][denite]

## Usage
1. make first cmdl data json file
    - (default) copy template cmdl.json file by prepared make command
        - `make` or `make copy-cmdl-json`
        - then put first `cmdl.json` to `~/.cache/denite-cmdl/cmdl.json`
    - (customized)
        1. copy template/cmdl.json file to where you want to put
        2. set your data directory by prepared command on your .vimrc
            ```
            call cmdl#set_data_directory_path('[path to your data directory]')
            ```
2. execute `Denite` command with `cmdl` on Vim
    ```
    Denite cmdl
    ```
3. select and execute listed command

If you want to add other commands, edit your cmdl.json manually )

## Example

current my [cmdl.json](https://github.com/kmnk/config/blob/master/json/cmdl.json)

```
{
  "version": "0.1.0",
  "cmdls": [
    {
      "name": "update plugins",
      "to_execute": "call dein#update()"
    },
    {
      "name": "recache runtimepath",
      "to_execute": "call dein#recache_runtimepath()"
    },
    {
      "name": "show messages",
      "to_execute": "messages"
    }
  ]
}
```

[denite]:https://github.com/Shougo/denite.nvim
