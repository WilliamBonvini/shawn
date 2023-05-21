import typer
import os
import openai
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

from shawn import DETAILS
from shawn.utils import get_response

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
    console.print(Panel("Hey there, how can I help you?\n", title="Shawn", border_style="blue"))
    content = typer.prompt("") + DETAILS
    while True:
        response = get_response(content)
        with open("you.txt", "w") as f:
            f.write(response)

        md = Markdown(response)
        panel = Panel(md, title="Shawn", border_style="blue")
        console.print(panel)
        content = typer.prompt("")


@app.command()
def dig(p: str):
    if os.path.isfile(p):
        explain_file(p)
    elif os.path.isdir(p):
        for root, dirs, files in os.walk(p):
            for name in files:
                file_path = os.path.join(root, name)
                explain_file(file_path)
    else:
        console.print(f'Error: {p} is not a valid path.')


def explain_file(p):
    content = f"Can you explain to me what the following code does? write as a markdown h1 header the name of the file ({p}) before starting the explanation\n\n"
    content += DETAILS
    with open(p, "r") as f:
        content += f.read()

    response = get_response(content)

    md = Markdown(response)
    panel = Panel(md, title="Shawn", border_style="blue")
    console.print(panel)


if __name__ == "__main__":
    app()
