from os.path import expanduser, realpath, join


def abspath(*args):
    return realpath(
        expanduser(
            join(*args)
        )
    )


def strip_root(path):
    """ strip trailing slash - semantically we need them for the items
    but for rendering purposes we must do away with them"""

    if len(path) > 0 and path[0] == '/':
        return path[1:]
    else:
        return path
