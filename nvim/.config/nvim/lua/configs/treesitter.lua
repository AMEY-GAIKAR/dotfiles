local options = {
  ensure_installed = {
    "bash",
    "c",
    "cmake",
    "cpp",
    "c_sharp",
    "fish",
    "go",
    "gomod",
    "gosum",
    "gotmpl",
    "gowork",
    "lua",
    "luadoc",
    "make",
    "markdown",
    "odin",
    "printf",
    "python",
    "razor",
    "toml",
    "vim",
    "vimdoc",
    "yaml",
  },

  highlight = {
    enable = true,
    use_languagetree = true,
  },

  indent = { enable = true },
}

require("nvim-treesitter.configs").setup(options)
