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
        result = self.inspire.search('f a {}'.format(args[0]))
        text = result.replace('</pre>', ' ').split('\n')
        text = [x for x in text if '<pre>' not in x]
        self.vim.current.buffer.append(text)
