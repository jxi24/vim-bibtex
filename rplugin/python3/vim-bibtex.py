"""
Neovim plugin to find all citations in a tex document
and generate either a bibtex or latex file for the bibliography.
"""
import neovim


@neovim.plugin
class Bibtex:
    def __init__(self, vim):
        self.vim = vim

    @neovim.function('vim_bibtex')
    def vim_bibtex(self, args):
        self.vim.command('echo "Test"')
