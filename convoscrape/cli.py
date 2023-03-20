import os
import click
import json
import random


# Shared click options
shared_options = [
    click.option('--verbose/--no-verbose', '-v', default=False, help="If set, console output is verbose"),
]

def add_options(options):
    def _add_options(func):
        for option in reversed(options):
            func = option(func)
        return func
    return _add_options

@click.group()
@click.option('--verbose/--no-verbose', '-v', default=False, help="If set, console output is verbose")
@click.pass_context
def cli(ctx, **kwargs):
    ctx.ensure_object(dict)
    ctx.obj = kwargs
    click.clear()
    click.secho('🏗️  CONVOSCRAPE', bold=True, fg='blue')
    click.secho(f"snscrape → convokit", fg='yellow')
    print(f'-----------------')


@click.command()
@add_options(shared_options)
@click.pass_context
def serve(ctx, **kwargs):
    from convoscrape import websvc
    ctx.obj.update(kwargs)
    websvc.main()


@click.command()
@add_options(shared_options)
@click.option('--config', default="configs/turkey.yaml", help="Provide experiment configuration file")
@click.pass_context
def search(ctx, **kwargs):
    from convoscrape import pipelines
    ctx.obj.update(kwargs)
    success = pipelines.search(ctx.obj)

    if success:
        click.secho("Done", bold=True, fg="green")
    else:
        click.secho("Search and Save failed", bold=True, fg="red")



cli.add_command(serve)
cli.add_command(search)

def main():
    cli(obj={})

if __name__ == "__main__":
    main()

