from pathlib import Path

def get_project_root():
    return Path(__file__).parent.parent

def get_asset_path(file_name):
    return get_project_root() / "assets" / file_name