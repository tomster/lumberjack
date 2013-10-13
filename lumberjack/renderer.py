from jinja2 import Environment, FileSystemLoader
from os import path, makedirs
from shutil import copy2


def render_site(site, fs_source, fs_destination, fs_templates, config):
    env = Environment(loader=FileSystemLoader([fs_templates, fs_source]))
    for item in site['root'].values():
        fs_item_dir = path.join(path.abspath(fs_destination), item.path)
        if not path.exists(fs_item_dir):
            makedirs(fs_item_dir)
        fs_item_destination = path.join(path.abspath(fs_destination), item.path, item.filename)
        item_type = path.splitext(item.filename)[-1].lower()
        if item_type == '.html':
            with open(fs_item_destination, 'w') as destination_file:
                template = env.get_template(path.join(item.path, item.filename))
                destination_file.write(template.render(**config))

        else:
            copy2(item.fs_src, fs_item_destination)
