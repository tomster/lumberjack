from pytest import fixture
from lumberjack.walker import parse_source
from lumberjack.renderer import render_site


@fixture
def site(simple_jinja):
    return parse_source(str(simple_jinja))


def test_parse(site):
    assert site['root']['index.html'].filename == 'index.html'


def test_render(site, simple_jinja):
    target = simple_jinja.join('build')
    templates = simple_jinja.join('templates')
    render_site(site, fs_source=str(simple_jinja),
        fs_destination=str(target),
        fs_templates=str(templates),
        config=dict(title='foo'))
    assert target.join('index.html').exists()
    assert target.join('recipes', 'green.html').exists()
