from jinja2 import Environment, FileSystemLoader
from os import path, makedirs
from shutil import copy2


def render_site(site, fs_content, fs_destination, fs_templates, config):
    print "Writing to %s" % fs_destination
    env = Environment(loader=FileSystemLoader([fs_templates, fs_content]))
    for item in site['entities'].query('path'):
        fs_item_dir = path.join(fs_destination, item.path.local)
        if not path.exists(fs_item_dir):
            makedirs(fs_item_dir)
        fs_item_destination = path.join(fs_item_dir, item.path.filename)
        item_type = path.splitext(item.path.filename)[-1].lower()
        if item_type == '.html':
            with open(fs_item_destination, 'w') as destination_file:
                template = env.get_template(item.path.sub)
                destination_file.write(template.render(**config))
        else:
            copy2(item.path.absolute, fs_item_destination)
    return fs_destination
