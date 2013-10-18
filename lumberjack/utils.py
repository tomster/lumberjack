import yaml
from os.path import expanduser, realpath, join


def abspath(*args):
    return realpath(
        expanduser(
            join(*args)
        )
    )


def parse_config(fs_conf):
    """ Parse the given YAML file and return its contents as dictionary
    """
    with open(fs_conf) as config:
        return yaml.load(config.read())
