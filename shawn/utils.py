import openai
from halo import Halo
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

from shawn import DETAILS, spinner

console = Console()


def get_response(content: str) -> str:
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": content}]
    )
    response = completion.choices[0].message.content
    return response


def explain_file(p: str) -> None:
    content = f"Could you please clarify the function of the following code? Begin the explanation with an h1 markdown header that contaisn the name of the file ({p}). Follow it by your explanation. Show code snippets if you think it's necessary. \n\n"
    content += DETAILS
    with open(p, "r") as f:
        content += f.read()

    spinner.start()
    response = get_response(content)
    spinner.stop()

    md = Markdown(response)
    panel = Panel(md, title="Shawn", border_style="blue")
    console.print(panel)
