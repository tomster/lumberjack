from lumberjack.renderer import render_site
from lumberjack.testing import example_dir


@example_dir('simple_jinja')
def test_parse(site):
    assert site['entities'].query('path')[0].path.filename == 'index.html'


@example_dir('simple_jinja')
def test_render(site, example):
    render_site(site,
        fs_content=example['source'],
        fs_destination=example['destination'],
        fs_templates=example['templates'],
        config=dict(title='foo'))
    target = example['location'].join('build')
    assert target.join('index.html').exists()
    assert target.join('recipes', 'green.html').exists()
    assert not target.join('lumberjack.yml').exists()
