from importlib.metadata import PackageNotFoundError, version

from halo import Halo

try:
    __version__ = version("shawn")
except PackageNotFoundError:
    __version__ = "(local)"

del PackageNotFoundError
del version

DETAILS = " (remember that you are a dog named Shawn, but most importantly, you are a coding assistant. Unless I don't ask you to, don't write coding snippets, but if I do make sure to append the language name to the leading three ```)"
spinner = Halo(text="Thinking...", spinner="flip")
