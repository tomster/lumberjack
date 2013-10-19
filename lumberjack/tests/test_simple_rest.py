from pytest import xfail
from lumberjack.renderer import render_site
from lumberjack.testing import site_dir


@site_dir('simple_rest')
def test_parse(site):
    assert site['entities'].query('filename')[0].filename.value == 'index.rst'


@site_dir('simple_rest')
def test_render(site, example):
    xfail('not yet implemented')
    render_site(site,
        fs_content=example['source'],
        fs_destination=example['destination'],
        fs_templates=example['templates'],
        config=dict(title='foo'))
    target = example['location'].join('build')
    assert target.join('index.html').exists()
