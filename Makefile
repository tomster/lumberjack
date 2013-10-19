# convenience makefile to set up development and run tests

version = 2.7
config = buildout.cfg

bin/py.test: bin/buildout buildout.cfg
	bin/buildout -c $(config)
	touch bin/py.test

tests: bin/py.test
	bin/py.test --cov lumberjack --tb=native

bin/buildout: bin/pip
	bin/pip install zc.buildout

bin/python bin/pip:
	virtualenv-$(version) .

clean:
	git clean -fXd

.PHONY: clean tests
