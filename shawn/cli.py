import typer
import os
import openai
from rich import print

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

app = typer.Typer()


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

    content = typer.prompt("Hey there, how can I help you?\n")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": content}
        ]
    )
    response = completion.choices[0].message.content
    with open("you.txt", "w") as f:
        f.write(response)
    print(response)


if __name__ == "__main__":
    app()


"""
Roadmap:

find out how to identify coding language used in ''' brackets.
tell rich to syntax highlight correctly those substrings that I am able to identify. 
print the remaining substrings normally.
find a nice way to wrap the code snippets in. 
find a nice way to show when shawn is speaking, and when it's you that is speaking.
"""