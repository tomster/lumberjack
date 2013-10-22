from libstasis import Registry
from libstasis.entities import IAspects
from libstasis.entities import Entities
from libstasis.entities import Column, types
from libstasis.rst import AspectsForRstFile, RstFile
from libstasis.walker import File
from zope.interface import implements
from os import path


def factory(config, path):
    site = Registry()
    site['config'] = config
    site['path'] = path
    site.registerAdapter(AspectsForFile, (File,), IAspects)
    site.registerAdapter(AspectsForRstFile, (RstFile,), IAspects)
    entities = Entities(registry=site)
    entities.add_aspect('filepath', Column('value', types.Unicode))
    entities.add_aspect('subpath', Column('value', types.Unicode))
    entities.add_aspect('filename', Column('value', types.Unicode))
    site['entities'] = entities
    return site


class AspectsForFile(object):
    implements(IAspects)

    def __init__(self, file):
        self.file = file

    def __getitem__(self, aspect):
        if aspect == 'filepath':
            return self.file.filepath
        elif aspect == 'subpath':
            return path.dirname(self.file.subpath)
        elif aspect == 'filename':
            return path.split(self.file.subpath)[1]
        raise KeyError(aspect)

    def keys(self):
        return iter(['filepath', 'subpath', 'filename'])

    def __iter__(self):
        return iter(self.keys())
