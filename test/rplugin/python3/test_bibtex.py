from unittest.mock import patch, call

import vim_bibtex
import inspire
from pynvim import attach

TEST_STRING = """
@article{Perry:2019bqg,
      author         = "Perry, Anastasia and Sun, Ranbel and Hughes, Ciaran and
                        Isaacson, Joshua and Turner, Jessica",
      title          = "{Quantum Computing as a High School Module}",
      year           = "2019",
      eprint         = "1905.00282",
      archivePrefix  = "arXiv",
      primaryClass   = "physics.ed-ph",
      reportNumber   = "FERMILAB-FN-1077-T",
      SLACcitation   = "%%CITATION = ARXIV:1905.00282;%%"
}
"""


@patch('inspire.Inspire', autospec=True)
def test_publication_list(mock_inspire):
    mock_inspire.return_value.publication_list.return_value = TEST_STRING

    nvim = attach('child', argv=['nvim', '--embed', '--headless'])
    nvim.command('edit /tmp/foo.bib')

    tex = vim_bibtex.Bibtex(nvim)
    tex.publication_list(['foo', 'bar'], range='')

    mock_inspire.assert_called_once_with('html')
    assert len(nvim.current.buffer) == len(TEST_STRING.split('\n'))+1

    nvim.command('undo')
    nvim.vars['vim_bibtex_name'] = 'foo'

    tex.publication_list('bar', range='')
    assert len(nvim.current.buffer) == len(TEST_STRING.split('\n'))+1

    expected = [call('foobar', output='bibtex'),
                call('foo', output='bibtex')]
    assert mock_inspire.return_value.publication_list.call_args_list == \
        expected
