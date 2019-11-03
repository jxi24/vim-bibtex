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

    @pynvim.function('Bibtex')
    def vim_bibtex(self, args):
        result = self.inspire.search('f a joshua isaacson')
        text = result.replace('</pre>', ' ').split('\n')
        text = [x for x in text if '<pre>' not in x]
        self.vim.current.buffer.append(text)
