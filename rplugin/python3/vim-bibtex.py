"""
Neovim plugin to find all citations in a tex document
and generate either a bibtex or latex file for the bibliography.
"""
import pynvim
import requests


@pynvim.plugin
class Limit(object):
    def __init__(self, vim):
        self.vim = vim

    @pynvim.function('Bibtex')
    def vim_bibtex(self, args):
        result = requests.get('http://inspirehep.net/search?p='
                              'f+a+joshua+isaacson&em=B&of=hx')
        text = result.text.split('\n')
        self.vim.current.buffer.append(text)
