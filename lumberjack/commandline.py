from docopt import docopt
from pkg_resources import get_distribution

from .utils import abspath, parse_config
from .renderer import render_site
from .core import factory

from libstasis.walker import Walker


def main():

    """Usage: lumberjack build [-c CONF -s DIR -d DIR -t DIR]

Options:
    -c DIR --config=FILE      The location of the configuration file [default: ./lumberjack.yml]
    -s DIR --content=DIR       The directory containting the content [default: ./content]
    -t DIR --templates=DIR    The directory containting the templates [default: ./templates]
    -d DIR --destination=DIR  The directory that will contain the rendered version [default: ./build]
    --version   Show version
    """

    arguments = docopt(main.__doc__, help=True, version=get_distribution('lumberjack').version)

    # normalize path arguments
    for location in ['--config', '--content', '--destination']:
        arguments[location] = abspath(arguments[location])

    site = factory(config=parse_config(arguments['--config']),
        path=arguments['--content'])

    walker = Walker()
    walker.walk(site)
    render_site(site=site, fs_content=arguments['--content'], fs_destination=arguments['--destination'],
        fs_templates=arguments['--templates'],
        config=site['config'])
    print "Done."
