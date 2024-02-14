import os
from importlib.metadata import PackageNotFoundError, version

from halo import Halo


try:
    __version__ = version("shawn")
except PackageNotFoundError:
    __version__ = "(local)"

del PackageNotFoundError
del version

api_key = os.getenv("OPENAI_API_KEY")

spinner = Halo(text="Thinking...", spinner="flip")
