from datetime import datetime
from pytest import xfail
from lumberjack.renderer import render_site
from lumberjack.testing import example_dir


@example_dir('simple_rest')
def test_parse(site):
    assert site['entities'].query('path')[0].path.filename == 'index.rst'


@example_dir('simple_rest')
def test_parse_rest_metadata(site):
    result = site['entities'].query('title', 'metadata')[0]
    assert result.title.value == u'Welcome'
    assert result.metadata.author == u'biggles'
    assert result.metadata.date == datetime(2013, 10, 19, 16, 16)


@example_dir('simple_rest')
def test_render(site, example):
    xfail('not yet implemented')
    render_site(site,
        fs_content=example['source'],
        fs_destination=example['destination'],
        fs_templates=example['templates'],
        config=dict(title='foo'))
    target = example['location'].join('build')
    assert target.join('index.html').exists()
