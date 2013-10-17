from lumberjack.utils import parse_config


def test_parse_config(simple_jinja):
    config = parse_config(str(simple_jinja['location'].join('lumberjack.yml')))
    assert config['title'] == u'Lemon Curry?!'
