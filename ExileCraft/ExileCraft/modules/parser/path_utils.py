import os


def get_base_dir(script_path):
    """Return the base directory, which is the project root directory."""
    base_dir = os.path.dirname(script_path)
    while os.path.basename(base_dir) != 'ExileCraft':
        base_dir = os.path.dirname(base_dir)
    return base_dir

def get_rel_path_to_db(base_dir):
    """Return the relative path from the base directory to the 'exilecraft.db' file."""
    return os.path.relpath(r"data/exilecraft.db", base_dir)

def get_abs_path(script_path):
    """Return the absolute path to the 'exilecraft.db' file."""
    base_dir = get_base_dir(script_path)
    rel_path = get_rel_path_to_db(base_dir)
    return os.path.join(base_dir, rel_path)