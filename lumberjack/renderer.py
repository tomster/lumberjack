from jinja2 import Environment, FileSystemLoader
from os import path, makedirs
from shutil import copy2


def render_site(site, fs_content, fs_destination, fs_templates, config):
    print "Writing to %s" % fs_destination
    env = Environment(loader=FileSystemLoader([fs_templates, fs_content]))
    for item in site['entities'].query('localpath', 'filename', 'filepath', 'subpath'):
        fs_item_dir = path.join(fs_destination, item.localpath.value)
        if not path.exists(fs_item_dir):
            makedirs(fs_item_dir)
        fs_item_destination = path.join(fs_item_dir, item.filename.value)
        item_type = path.splitext(item.filename.value)[-1].lower()
        if item_type == '.html':
            with open(fs_item_destination, 'w') as destination_file:
                template = env.get_template(item.subpath.value)
                destination_file.write(template.render(**config))
        else:
            copy2(item.filepath.value, fs_item_destination)
    return fs_destination
