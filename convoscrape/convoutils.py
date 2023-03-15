
from convokit import Corpus
import os
import ndjson
import pathlib

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


def update_corpus(corpus_name, data):
    """
    input: corpus name
    input: data - pandas dataframe

    Each item in data is a tweet/utterance.
    """
    # if add data to various utterance and speaker files
    current_path = pathlib.Path().resolve() / f"data/corpora/{corpus_name}"
    if is_directory_empty(current_path):
        print(f"Directory \"{corpus_name}\" is currently empty")
        corpus = Corpus.from_pandas(data)
        corpus.print_summary_stats()
        corpus.dump(current_path)
        print("Updated.")
        return True

    print("Directory is NOT empty")
    existing_corpus = Corpus(current_path)
    existing_corpus.print_summary_stats()
    new_corpus = Corpus.from_pandas(data)
    corpus = Corpus.merge(existing_corpus, new_corpus)
    corpus.print_summary_stats()
    corpus.dump(current_path)
    print("Updated.")
    return True


def is_in_corpus(corpus, utterance_id):
    path = f"data/corpora/{corpus}/utterances.jsonl"
    with open(path, "r") as f:
        corpus_data = ndjson.load(f)

    if not corpus_data:
        return False

    for item in corpus_data:
        if utterance_id == item['id']:
            return True

    return False


def is_directory_empty(directory_path):
    directory_path = pathlib.Path(directory_path)
    return not any(directory_path.iterdir())
