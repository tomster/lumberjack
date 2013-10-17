from os import path
from shutil import copytree
from pytest import fixture


@fixture
def examples():
    import lumberjack
    return path.abspath(path.join(path.dirname(lumberjack.__file__), '../examples/'))


@fixture
def simple_jinja(tmpdir, examples):
    destination = tmpdir.join('simple_jinja')
    copytree(path.join(examples, 'simple_jinja'), '%s' % destination)
    return destination
