
import os


def get_current_corpora():
    """
    Looks through the data/corpora folder and returns
    - list of dir names
    - None for no corpora or if the corpora directory does not exist
    """
    if not os.path.exists("data/corpora"):
        return []

    subfolders = [f.name for f in os.scandir("data/corpora") if f.is_dir()]

    return subfolders



