import click


@click.command()
@click.argument('mode', required=False, default='')
@click.argument('amount', required=False, default=5)
def bashim_clc(mode, amount):
    while True:
        # try:
        #     quotes = core.get_quotes(core.URLS[mode])
        # except:
        #     quotes = core.get_quotes(core.ALIASES[mode])
        #
        # core.pprint(quotes)

        if click.confirm('Another set of quotes?', abort=True):
            pass
