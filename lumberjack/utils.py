from os.path import expanduser, realpath, join


def abspath(*args):
    return realpath(
        expanduser(
            join(*args)
        )
    )

