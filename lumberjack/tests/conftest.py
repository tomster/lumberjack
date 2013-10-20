from os import path
from shutil import copytree
from pytest import fixture
from libstasis.walker import Walker
from lumberjack.core import factory


@fixture
def example(request, tmpdir):
    import lumberjack
    examples_dir = path.abspath(path.join(path.dirname(lumberjack.__file__), '../examples/'))
    example_dir = request.keywords['example_dir'].args[0]
    location = tmpdir.join(example_dir)
    copytree(path.join(examples_dir, example_dir), '%s' % location)
    return dict(location=location,
        source=str(location.join('content')),
        templates=str(location.join('templates')),
        destination=str(location.join('build')),)


@fixture
def site(example):
    site = factory(dict(title=u'foo'), example['source'])
    walker = Walker()
    walker.walk(site)
    return site
