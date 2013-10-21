# convenience makefile to set up development and run tests

config = buildout.cfg

dir = lib/python2.7/site-packages
venv = $(dir)/virtualenv

# set up a virtual env with a bare OSX python installation (w/o `virtualenv`)
bin/py.test: bin/buildout buildout.cfg
	bin/buildout -c $(config)

tests: bin/py.test
	bin/py.test --cov lumberjack --tb=native

bin/buildout: bin/pip
	bin/pip install zc.buildout

bin/pip: $(venv)
	$(dir)/virtualenv -p `which python` .

$(venv):
	mkdir -p $(dir)
	PYTHONPATH=$(dir) easy_install -d $(dir) virtualenv

clean:
	git clean -fXd

.PHONY: clean tests
