from propdict import propdict
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
    # basic file aspects
    entities.add_aspect('filepath', Column('value', types.Unicode))
    entities.add_aspect('basepath', Column('value', types.Unicode))
    entities.add_aspect('subpath', Column('value', types.Unicode))
    entities.add_aspect('localpath', Column('value', types.Unicode))
    entities.add_aspect('filename', Column('value', types.Unicode))
    # General meta data
    entities.add_aspect('title', Column('value', types.Unicode))
    # ReST aspects TODO: factor into module?
    site['entities'] = entities
    return site


class AspectsForFile(propdict):
    implements(IAspects)

    @property
    def filename(self):
        return path.split(self.subpath)[1]

    @property
    def localpath(self):
        """ returns the path within the source directory,
        without the filename
        """
        return path.split(self.subpath)[0]

    @property
    def filepath(self):
        """ returns the absolute path, including the filename
        """
        return path.join(self.basepath, self.subpath)

    def __init__(self, file=None):
        if file is not None:
            self.update(file.__dict__)
        self.title = u'Welcome'
