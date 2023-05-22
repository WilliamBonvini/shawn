import os

from halo import Halo
import typer
import openai
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

from shawn import DETAILS
from shawn.utils import get_response, explain_file

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

app = typer.Typer()
console = Console()


@app.command()
def setup():
    if OPENAI_API_KEY is not None:
        print("No setup is needed, since your OPENAI_API_KEY environment variable is non empty.")
        return
    api_key = typer.prompt("OpenAI API Key: ")
    openai.api_key = api_key
    print("Congratulations! Shawn is ready to help you. just write \"shawn\" in your terminal and he will assist you.")


@app.command()
def chat():
    """
    Chat with Shawn.
    """
    console.print(Panel("Hey there, how can I help you?\n", title="Shawn", border_style="blue"))
    content = typer.prompt("") + DETAILS
    while True:
        spinner = Halo(text='Thinking...', spinner='flip')
        spinner.start()
        response = get_response(content)
        spinner.stop()

        md = Markdown(response)
        panel = Panel(md, title="Shawn", border_style="blue")
        console.print(panel)
        content = typer.prompt("")


@app.command()
def dig(p: str):
    """"""
    if os.path.isfile(p):
        explain_file(p)
    elif os.path.isdir(p):
        for root, dirs, files in os.walk(p):
            for name in files:
                file_path = os.path.join(root, name)
                explain_file(file_path)
    else:
        console.print(f'Error: {p} is not a valid path.')


if __name__ == "__main__":
    app()
