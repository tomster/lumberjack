from collections import OrderedDict
from os import walk

from .utils import abspath


class Item(object):

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


def parse_source(fs_location):
    """ parse the given directory. Returns an instance of (potentially nested) OrderedDict
    with each entry describing its node.
    """
    print "Reading from %s" % fs_location
    site = OrderedDict(root=OrderedDict())
    current = site['root']
    for root, dirs, items in walk(fs_location, followlinks=True):
        for item in items:
            path = root.replace(fs_location, '')
            current[item] = Item(fs_src=abspath(root, item),
                path=path,
                filename=item)

    return site
