import datetime
import os
import sys

import typer

from rich import print
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

from shawn import DETAILS, spinner
from shawn.utils import explain_file, get_response


app = typer.Typer()
console = Console()


@app.command()
def doctor():
    """ Check for configuration problems """
    if os.getenv("OPENAI_API_KEY") is not None:
        print(
            "you are good to go, since your OPENAI_API_KEY environment variable is not empty."
        )
        return
    raise EnvironmentError("OPENAI_API_KEY is not set.")


@app.command()
def chat() -> None:
    """
    start a chat with shawn
    """
    console.print(
        Panel("Hey there, how can I help you?\n", title="Shawn", border_style="blue")
    )
    content = typer.prompt("")

    while True:
        if content == "hush":
            return
        spinner.start()
        response = get_response(content + DETAILS)
        spinner.stop()
        md = Markdown(response)
        panel = Panel(md, title="Shawn", border_style="blue")
        console.print(panel)
        content = typer.prompt("")


@app.command()
def dig(p: str) -> None:
    """
    describe in natural language the content of a single source file or an entire directory of files

    :param p: path to file or folder
    """
    if os.path.isfile(p):
        explain_file(p)
    elif os.path.isdir(p):
        for root, dirs, files in os.walk(p):
            for name in files:
                file_path = os.path.join(root, name)
                explain_file(file_path)
    else:
        console.print(f"Error: {p} is not a valid path.")


@app.command()
def invenv() -> None:
    """ return True if you are in a virtual environment, false otherwise """
    print(sys.prefix != sys.base_prefix)


@app.command()
def time() -> None:
    """ return local time """
    print(datetime.datetime.strftime(datetime.datetime.now(), "%H:%m"))


@app.command()
def date() -> None:
    """ return current date """
    print(datetime.datetime.strftime(datetime.datetime.now(), "%d %B %Y"))

