import os


def setup():
    os.environ["PATH"] += os.pathsep + "./packages/graphviz/bin"
