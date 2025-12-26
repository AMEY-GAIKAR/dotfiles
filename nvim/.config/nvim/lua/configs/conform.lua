local options = {

  formatters_by_ft = {
    c = { "clang-format" },
    cpp = { "clang-format" },
    -- go = { "gofumpt", "goimports-reviser", "golines" },
    lua = { "stylua" },
    python = { "isort", "black" },
    python = { "ruff_format" },
  },

  formatters = {
    -- C & C++
    ["clang-format"] = {
      prepend_args = {
        "-style={ \
                IndentWidth: 2, \
                TabWidth: 2, \
                UseTab: Never, \
                AccessModifierOffset: 0, \
                IndentAccessModifiers: true, \
                PackConstructorInitializers: Never}",
      },
    },

    -- Golang
    -- ["goimports-reviser"] = {
    --   prepend_args = { "-rm-unused" },
    -- },
    --
    -- golines = {
    --   prepend_args = { "--max-len=80" },
    -- },

    -- Python
    ruff_format = {
      command = "ruff",
      args = {
        "format",
        "--stdin-filename",
        "$FILENAME",
        "-",
      },
      stdin = true,
    },

    black = {
      prepend_args = {
        "--fast",
        "--line-length",
        "80",
      },
    },

    isort = {
      prepend_args = {
        "--profile",
        "black",
      },
    },
  },

  format_on_save = {
    -- These options will be passed to conform.format()
    timeout_ms = 900,
    lsp_fallback = true,
  },
}

require("conform").setup(options)
