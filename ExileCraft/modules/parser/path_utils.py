import os

def get_abs_path(rel_path, script_path):
    """Return the absolute path given a relative path."""
    script_dir = os.path.dirname(os.path.realpath(script_path))
    return os.path.join(script_dir, rel_path)
