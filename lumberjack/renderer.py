from jinja2 import Environment, FileSystemLoader
from os import path, makedirs
from shutil import copy2
from .utils import strip_root


def render_site(site, fs_source, fs_destination, fs_templates, config):
    print "Writing to %s" % fs_destination
    env = Environment(loader=FileSystemLoader([fs_templates, fs_source]))
    for item in site['root'].values():
        fs_item_dir = path.join(fs_destination, strip_root(item.path))
        if not path.exists(fs_item_dir):
            makedirs(fs_item_dir)
        fs_item_destination = path.join(fs_item_dir, item.filename)
        item_type = path.splitext(item.filename)[-1].lower()
        if item_type == '.html':
            with open(fs_item_destination, 'w') as destination_file:
                template = env.get_template(path.join(item.path, item.filename))
                destination_file.write(template.render(**config))

        else:
            copy2(item.fs_src, fs_item_destination)
