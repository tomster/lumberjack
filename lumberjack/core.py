from propdict import propdict
from libstasis import Registry
from libstasis.entities import IAspects
from libstasis.entities import Entities
from libstasis.entities import Column, types
from libstasis.rst import RstFile
from libstasis.walker import File
from zope.interface import implements
from os import path


def factory(config, path):
    site = Registry()
    site['config'] = config
    site['path'] = path
    site.registerAdapter(AspectsForFile, (File,), IAspects)
    site.registerAdapter(AspectsForRstFile, (File,), IExtraAspects)
    entities = Entities(registry=site)
    # basic file aspects
    entities.add_aspect('path',
        Column('absolute', types.Unicode),
        Column('base', types.Unicode),
        Column('sub', types.Unicode),
        Column('local', types.Unicode),
        Column('filename', types.Unicode),
        Column('extension', types.Unicode),
    )
    # General meta data
    entities.add_aspect('title', Column('value', types.Unicode))
    entities.add_aspect('metadata',
        Column('author', types.Unicode),
        Column('date', types.DateTime),
        Column('tags', types.Unicode),
    )
    # ReST aspects TODO: factor into module?
    site['entities'] = entities
    return site


from zope.interface import Interface


class IExtraAspects(Interface):
    pass


class AspectsForFile(propdict):
    implements(IAspects)

    def __init__(self, file=None):
        if file is not None and not isinstance(file, propdict):
            # we're called as adapter

            # init the path(s)
            self.path = propdict()
            self.path.absolute = file.filepath
            self.path.base = file.basepath
            # i.e. foo/bar/index.html
            self.path.sub = file.subpath
            # i.e. foo/bar/
            self.path.local = path.split(file.subpath)[0]
            # i.e. index.html
            self.path.filename = path.split(file.subpath)[1]
            # i.e. html
            self.path.extension = path.splitext(file.subpath)[1].lower()

            # hack: inject the path propdict for convenience
            file.path = self.path

            # collect additional aspects from registered adapters
            for name, aspect in file.site.getAdapters((file,), IExtraAspects):
                self.update(aspect)


class AspectsForRstFile(propdict):

    def __init__(self, file=None):
        if file is not None:
            # we're called as adapter
            if file.path.extension in ['.rst', '.rest']:
                # TODO: self.update(rest_aspects) should work. bug in propdict?
                self.update(RstFile(file).__dict__)
