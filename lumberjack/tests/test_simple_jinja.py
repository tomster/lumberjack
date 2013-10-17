from pytest import fixture
from lumberjack.walker import parse_source
from lumberjack.renderer import render_site


@fixture
def site(simple_jinja):
    return parse_source(simple_jinja['source'])


def test_parse(site):
    assert site['root']['index.html'].filename == 'index.html'


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
