import click

import core


@click.command()
@click.argument('mode')
def bashim_clc(mode=''):
    for q in core.get_quotes(core.URLS[mode]):
        click.echo(q)
        click.echo('-------------------------------')
