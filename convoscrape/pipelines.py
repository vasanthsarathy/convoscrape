# Various processing pipelines
import yaml
from convoscrape.scrape import run_search_scraper, get_conversations
from convoscrape.convoutils import update_corpus
import click

def search(ctx):
    #load config

    with open(ctx['config'], 'r') as file:
        expt_configs = yaml.safe_load(file)

    accounts = expt_configs["twitter"]["accounts"]
    hashtags = expt_configs["twitter"]["hashtags"]
    keywords = expt_configs["twitter"]["keywords"]

    since_to_string = f"since:{expt_configs['twitter']['since']} until:{expt_configs['twitter']['until']}"

    for account in accounts:
        account_string = f"from:{account}"

        search_string = account_string + " " + since_to_string

        click.secho("Twitter Search", bold=True, fg="white")
        click.secho("\t> Running search", fg="yellow")
        df = run_search_scraper(search_string, expt_configs['parameters']['num_terms'])
        click.secho("\t> Expanding to include conversations", fg="yellow")
        df = get_conversations(df)
        click.secho("\t> Updating corpus", fg="yellow")
        success = update_corpus(expt_configs['parameters']['corpus_name'], df)

    return success
