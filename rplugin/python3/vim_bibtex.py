"""
Neovim plugin to find all citations in a tex document
and generate either a bibtex or latex file for the bibliography.
"""
import pynvim
import inspire


@pynvim.plugin
class Bibtex(object):
    def __init__(self, vim):
        self.vim = vim
        self.inspire = inspire.Inspire('html')

    @pynvim.command('PublicationList', nargs='*', range='')
    def publication_list(self, args, range):
        if 'vim_bibtex_name' in self.vim.vars:
            name = self.vim.vars.get('vim_bibtex_name')
        else:
            name = args[0] + args[1]
        text = self.inspire.publication_list(name, output='bibtex').split('\n')
        self.vim.current.buffer.append(text)
