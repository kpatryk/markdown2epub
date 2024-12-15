import click
from importlib.metadata import version

@click.command()
def main():
    """My CLI tool."""
    click.echo(f"Hello, CLI! Version: {version('markdown2epub')}")

if __name__ == "__main__":
    main()
