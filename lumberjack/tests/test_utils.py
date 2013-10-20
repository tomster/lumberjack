from lumberjack.utils import parse_config
from lumberjack.testing import example_dir


@example_dir('simple_jinja')
def test_parse_config(example):
    config = parse_config(str(example['location'].join('lumberjack.yml')))
    assert config['title'] == u'Lemon Curry?!'
