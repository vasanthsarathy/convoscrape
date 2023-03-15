
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


def create_subdirectory(subdirectory_name):
    try:
        os.makedirs(os.path.join("data/corpora", subdirectory_name))
        print(f"Successfully created subdirectory '{subdirectory_name}' inside 'data/corpora'")
    except OSError as e:
        print(f"Error: {e}")


def update_corpus(corpus, data):
    # if add data to various utterance and speaker files
    return True
