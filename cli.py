#!/usr/bin/env python
import click
from mylib.mathcode import add


@click.command()
@click.option(
    "--valuex",
    help="First number to add",
)
@click.option(
    "--valuey",
    help="second number to add",
)
def add_this(valuex, valuey):
    """Adds two numbers together"""

    result = add(int(valuex), int(valuey))
    click.echo(click.style(f"Total: {result}", fg="red"))

if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    add_this()