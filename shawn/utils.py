from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

from shawn import spinner, assistant

console = Console()


def explain_file(p: str) -> None:
    content = f"Could you please clarify the function of the following code? Begin the explanation with an h1 markdown header that contaisn the name of the file ({p}). Follow it by your explanation. Show code snippets if you think it's necessary. \n\n"
    content += DETAILS
    with open(p, "r") as f:
        content += f.read()

    spinner.start()
    assistant.add_message("user", "content")
    response = assistant.chat()
    spinner.stop()

    md = Markdown(response)
    panel = Panel(md, title="Shawn", border_style="blue")
    console.print(panel)
