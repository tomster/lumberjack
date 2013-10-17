from pytest import fixture
from libstasis.walker import Walker
from lumberjack.core import factory
from lumberjack.renderer import render_site


@fixture
def site(simple_jinja):
    site = factory(dict(title=u'foo'), simple_jinja['source'])
    walker = Walker()
    walker.walk(site)
    return site


def test_parse(site):
    assert site['entities'].query('filename')[0].filename == 'index.html'


def test_render(site, simple_jinja):
    render_site(site,
        fs_content=simple_jinja['source'],
        fs_destination=simple_jinja['destination'],
        fs_templates=simple_jinja['templates'],
        config=dict(title='foo'))
    target = simple_jinja['location'].join('build')
    assert target.join('index.html').exists()
    assert target.join('recipes', 'green.html').exists()
    assert not target.join('lumberjack.yml').exists()
