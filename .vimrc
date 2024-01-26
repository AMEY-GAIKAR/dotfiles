" ENABLE SYNTAX HIGHLIGHTING
syntax on

" SET <leader> to <Space>
let mapleader = " "

" ENCODING & FILE FORMAT
set encoding=utf-8
set fileformat=unix

" DISABLE MOUSE
set mouse="a"

" SET LINE NUMBER AND RELATIVE LINE NUMBERS
set number 
set relativenumber

" SET SPACES FOR INDENTATION
set expandtab
set tabstop=2
set shiftwidth=2
set autoindent
set smartindent
set smarttab

" WRAP LONG LINES
set wrap 

 set background=dark
 set noshowmode

 " HIGHLIGHT SEARCH, CASE INSENSETIVE, INCREMENTAL SEARCH
set showcmd
set hlsearch
set ignorecase
set smartcase
set incsearch

set ruler
set laststatus=2
set wildmenu
set wildmode=list:longest

set title

set history=100

set timeoutlen=500 

set noswapfile
set noundofile

" PLUGINS
call plug#begin('~/.vim/plugged')

Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

Plug 'preservim/nerdtree' |
        \ Plug 'Xuyuanp/nerdtree-git-plugin' |
        \ Plug 'ryanoasis/vim-devicons'

Plug 'sheerun/vim-polygot'

Plug 'catppuccin/vim', { 'as': 'catppuccin' }

Plug 'junegunn/fzf' |
        \ Plug 'junegunn/fzf.vim'

Plug 'tiagofumo/vim-nerdtree-syntax-highlight'

Plug 'tpope/vim-fugitive'

Plug 'liuchengxu/vim-which-key'

call plug#end()

nnoremap <CR> :noh<CR><CR>:<backspace>

" which-key
nnoremap <leader>wK :WhichKey '<Space>'<CR>
autocmd! FileType which_key
autocmd  FileType which_key set laststatus=0 noshowmode noruler
  \| autocmd BufLeave <buffer> set laststatus=2 showmode ruler
" BUFFER
nnoremap <tab> :bnext<cr>
nnoremap <S-tab> :bprevious<cr>
nnoremap <leader>x :bdelete<cr>
nnoremap <leader>bb :Buffers<CR>

" FZF
nnoremap <leader>fa :Files<CR>
nnoremap <leader>ff :Files <C-r>=expand("%:h")<CR>/<CR>
nnoremap <leader>fb :Rg
nnoremap <leader>fg :GFiles?<CR>
nnoremap <leader>gc :Commits<CR>

" AUTOCLOSE CONFIG
" autoclose and position cursor inside
inoremap ' ''<left>
inoremap ` ``<left>
inoremap " ""<left>
inoremap ( ()<left>
inoremap [ []<left>
inoremap { {}<left>

" autoclose with ; and position cursor inside
inoremap '; '';<left><left>
inoremap `; ``;<left><left>
inoremap "; "";<left><left>
inoremap (; ();<left><left>
inoremap [; [];<left><left>
inoremap {; {};<left><left>

" autoclose with , and position cursor inside
inoremap ', '',<left><left>
inoremap `, ``,<left><left>
inoremap ", "",<left><left>
inoremap (, (),<left><left>
inoremap [, [],<left><left>
inoremap {, {},<left><left>

" autoclose and position cursor after
inoremap '<tab> ''
inoremap `<tab> ``
inoremap "<tab> ""
inoremap (<tab> ()
inoremap [<tab> []
inoremap {<tab> {}

" autoclose two lines below and position cursor inside
inoremap '<CR> '<CR>'<ESC>O
inoremap `<CR> `<CR>`<ESC>O
inoremap "<CR> "<CR>"<ESC>O
inoremap (<CR> (<CR>)<ESC>O
inoremap [<CR> [<CR>]<ESC>O
inoremap {<CR> {<CR>}<ESC>O

let g:lightline = {'colorscheme': 'catppuccin_mocha'}

" NERDTREE
" NERDTree key-bindings
nnoremap <leader>e :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTreeClose<CR>
nnoremap <C-t> :NERDTreeToggle<CR>
nnoremap <C-f> :NERDTreeFind<CR>

" Start NERDTree when Vim is started without file arguments.
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 0 && !exists('s:std_in') | NERDTree | endif

" Start NERDTree when Vim starts with a directory argument.
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 1 && isdirectory(argv()[0]) && !exists('s:std_in') |
     \ execute 'NERDTree' argv()[0] | wincmd p | enew | execute 'cd '.argv()[0] | endif

" Exit Vim if NERDTree is the only window remaining in the only tab.
autocmd BufEnter * if tabpagenr('$') == 1 && winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif

let g:NERDTreeWinSize = 26
let g:NERDTreeDirArrowExpandable = '+'
let g:NERDTreeDirArrowCollapsible = '-'

" Show hidden files
let NERDTreeShowHidden=1

let NERDTreeMinimalUI=1
let NERDTreeMinimalMenu=1

let g:NERDTreeGitStatusIndicatorMapCustom = {
                \ 'Modified'  :'✹',
                \ 'Staged'    :'✚',
                \ 'Untracked' :'✭',
                \ 'Renamed'   :'➜',
                \ 'Unmerged'  :'═',
                \ 'Deleted'   :'✖',
                \ 'Dirty'     :'✗',
                \ 'Ignored'   :'☒',
                \ 'Clean'     :'✔︎',
                \ 'Unknown'   :'?',
                \ }

let g:NERDTreeGitStatusUseNerdFonts = 1

augroup nerdtreehidecwd
    autocmd!
    autocmd FileType nerdtree setlocal conceallevel=3
            \ | syntax match NERDTreeHideCWD #^[</].*$# conceal
            \ | setlocal concealcursor=n
augroup end

" AIRLINE
" Set Airline theme
let g:airline_theme = 'catppuccin_mocha'

if !exists('g:airline_symbols')
    let g:airline_symbols = {}
endif

let g:airline_powerline_fonts = 1
let g:airline_left_sep = ''
let g:airline_right_sep = ''
let g:airline_symbols.linenr = '␊'
let g:airline_symbols.linenr = '␤'
let g:airline_symbols.linenr = '¶'
let g:airline_symbols.branch = '⎇'
let g:airline_symbols.paste = 'ρ'
let g:airline_symbols.paste = 'Þ'
let g:airline_symbols.paste = '∥'
let g:airline_symbols.whitespace = 'Ξ'

" AIRLINE-TABLINE
" Enable tabline
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#left_sep = ''
let g:airline#extensions#tabline#left_alt_sep = ''
let g:airline#extensions#tabline#right_sep = ''
let g:airline#extensions#tabline#right_alt_sep = ''

" name tab as file name
let g:airline#extensions#tabline#formatter = 'unique_tail'

" Source plugins.vim
if filereadable(expand("~/.vim/plugins.vim"))
  source ~/.vim/plugins.vim
endif
