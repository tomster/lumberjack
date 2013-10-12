# convenience makefile to set up development

version = 2.7

bin/pserve bin/py.test: bin/python bin/pip setup.py
	bin/python setup.py dev

tests: bin/py.test
	bin/py.test

bin/python bin/pip:
	virtualenv-$(version) .

clean:
	git clean -fXd

.PHONY: clean tests
