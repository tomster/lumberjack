from os import path
from shutil import copytree
from pytest import fixture


@fixture
def examples():
    import lumberjack
    return path.abspath(path.join(path.dirname(lumberjack.__file__), '../examples/'))


@fixture
def simple_jinja(tmpdir, examples):
    location = tmpdir.join('simple_jinja')
    copytree(path.join(examples, 'simple_jinja'), '%s' % location)
    return dict(location=location,
        source=str(location.join('content')),
        templates=str(location.join('templates')),
        destination=str(location.join('build')),)
