import sys
import os

class Node:
    word = ""
    left = None
    right = None

    def __init__(self, word: str):
        self.word = word
        self.left = None
        self.right = None


class BST:
    def __init__(self, root=None):
        self.root = root

    def insert(self, word):
        if self.root == None:
            self.root = Node(word)
            return
        self._insert(word, self.root)

    def _insert(self, word, node):
        if word < node.word:
            if node.left:
                self._insert(word, node.left)
            else:
                node.left = Node(word)
                return
        if word > node.word:
            if node.right:
                self._insert(word, node.right)
            else:
                node.right = Node(word)
                return

    def collect(self, node, prefix, results):
        if not node:
            return
        self.collect(node.left, prefix, results)
        if node.word.startswith(prefix):
            results.append(node.word)
        self.collect(node.right, prefix, results)

    def autocomplete(self, prefix):
        results = []
        self.collect(self.root, prefix, results)
        return results

    def build_from_sorted(self, words):
        self.root = self._build_balanced(words, 0, len(words) - 1)

    def _build_balanced(self, words: list[str], lo: int, hi: int) -> Node | None:
        if lo > hi:
            return None
        mid = (lo + hi) // 2
        node = Node(words[mid])
        node.left = self._build_balanced(words, lo, mid - 1)
        node.right = self._build_balanced(words, mid + 1, hi)
        return node


def read_dictionary(filename: str) -> list[str]:
    with open(filename, 'r') as f:
        data = f.read()
        data = data.split('\n')
        return data


def get_char():
    try:
        import termios, tty
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    except ImportError:
        # Windows fallback
        import msvcrt
        return msvcrt.getch().decode("utf-8")


if __name__ == "__main__":
    bst = BST()
    bst.build_from_sorted(read_dictionary("words.txt"))
    print("Start typing (press ESC to quit):")
    prefix = ""

    while True:
        ch = get_char()
        if ord(ch) == 27:
            print("\nExiting...")
            break
        if ch in ("\b", "\x7f"):
            prefix = prefix[:-1]
        elif ch == "\r":
            continue
        else:
            prefix += ch.lower()

        os.system("cls" if os.name == "nt" else "clear")
        print(f"Current input >> {prefix}")
        suggestions = bst.autocomplete(prefix)
        if suggestions:
            for s in suggestions[:5]:
                print(s)
        else:
            print("No matches found.")

    pass