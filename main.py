import click
import lexer


@click.command()
@click.argument("filename", type=click.Path(exists=True))
def main(filename: str):
    if filename.endswith(".pypp"):
        lexer.tokens(filename)
    else:
        raise Exception("Not a .pypp file")

if __name__ == "__main__":
    main()
