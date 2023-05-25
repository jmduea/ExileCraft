import json
import os


def get_base_dir(script_path):
    """Return the base directory, which is the project root directory."""
    base_dir = os.path.dirname(script_path)
    while os.path.basename(base_dir) != 'ExileCraft':
        base_dir = os.path.dirname(base_dir)
    return base_dir


def get_rel_path_to_file(base_dir, dir_path, filename):
    """Return the relative path from the base directory to the given file."""
    return os.path.relpath(os.path.join(dir_path, filename), base_dir)


def get_abs_path(script_path, rel_path):
    """Return the absolute path to the given file."""
    base_dir = get_base_dir(script_path)
    return os.path.join(base_dir, rel_path)


def parse_json(abs_path):
    with open(abs_path, 'r') as file:
        data = json.load(file)
    return data
