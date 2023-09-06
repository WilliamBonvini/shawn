import os
from importlib.metadata import PackageNotFoundError, version

from halo import Halo

from gptassistant import GPTAssistant

try:
    __version__ = version("shawn")
except PackageNotFoundError:
    __version__ = "(local)"

del PackageNotFoundError
del version

api_key = os.getenv("OPENAI_API_KEY")

spinner = Halo(text="Thinking...", spinner="flip")
assistant = GPTAssistant(api_key=api_key)
