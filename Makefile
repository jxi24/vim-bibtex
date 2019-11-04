PATH := ./vim-themis/bin:$(PATH)
export THEMIS_VIM := nvim
export THEMIS_ARGS := -e -s --headless
export THEMIS_HOME := ./vim-themis


install: vim-themis
	pip install --upgrade -r test/requirements.txt

test:
	themis --version
	# themis test/autoload/*
	pytest --version
	pytest

vim-themis:
	git clone --depth 1 https://github.com/thinca/vim-themis $@

.PHONY: install test
