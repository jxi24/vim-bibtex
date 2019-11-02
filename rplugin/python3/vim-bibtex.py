"""
Neovim plugin to find all citations in a tex document
and generate either a bibtex or latex file for the bibliography.
"""
import neovim


@neovim.plugin
class Bibtex:
    def __init__(self, vim):
        self.vim = vim

    @neovim.function('TestCommand')
    def vim_bibtex(self):
        self.vim.current.line = 'New line'
