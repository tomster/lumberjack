import yaml


def parse_config(fs_conf):
    """ Parse the given YAML file and return its contents as dictionary
    """
    with open(fs_conf) as config:
        return yaml.load(config.read())
