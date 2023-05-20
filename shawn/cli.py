import typer
import os
import openai
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

from utils import get_response

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
def shawn():
    console.print(Panel("Hey there, how can I help you?\n", title="Shawn", border_style="blue"))
    content = typer.prompt("") + " (if for any reason you are going to provide me a coding snippet make sure to append the language name to the heading three ```)"
    while True:
        response = get_response(content)
        with open("you.txt", "w") as f:
            f.write(response)

        md = Markdown(response)
        panel = Panel(md, title="Shawn", border_style="blue")
        console.print(panel)
        content = typer.prompt("")


if __name__ == "__main__":
    app()
