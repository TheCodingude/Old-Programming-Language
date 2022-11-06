import click
import lexer


@click.command()
@click.argument("filename", type=click.Path(exists=True))
def main(file):

    lexer.tokens(file)



if __name__ == "__main__":
    main()
