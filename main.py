from setup import setup
from exact_method.bfs import BFS

def main():
    motif: str = 'MMA'
    BFS.create_graph(motif)

if __name__ == '__main__':
    setup()
    main()
