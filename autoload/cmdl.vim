" cmdl
" Version: 0.0.1
" Author: kmnk <kmnknmk at gmail.com>
" License: MIT License

if exists('g:loaded_cmdl')
  finish
endif
let g:loaded_cmdl = 1

let s:save_cpo = &cpo
set cpo&vim

let s:data_directory_path = "~/.cache/denite-cmdl"
let s:data_file_name = "cmdl.json"

function! cmdl#set_data_directory_path(path)
  let s:data_directory_path = a:path
endfunction

function! cmdl#get_data_directory_path()
  return fnamemodify(s:data_directory_path, ":p")
endfunction

function! cmdl#get_data_file_path()
  return cmdl#get_data_directory_path() . "/" . s:data_file_name
endfunction


let &cpo = s:save_cpo
unlet s:save_cpo

" vim:set et:
