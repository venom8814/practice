class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.word = word

    def autocomplete(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        results = []
        self._dfs(node, results)
        return results

    def _dfs(self, node, results):
        if node.is_end:
            results.append(node.word)
        for child in node.children.values():
            self._dfs(child, results)

class AutocompleteSystem:
    def __init__(self):
        self.trie = Trie()
        self.freq_map = {}  # word -> frequency

    def add_word(self, word, freq=1):
        self.trie.insert(word)
        self.freq_map[word] = self.freq_map.get(word, 0) + freq

    def suggest(self, prefix):
        words = self.trie.autocomplete(prefix)
        words.sort(key=lambda w: self.freq_map.get(w, 0), reverse=True)
        return words

if __name__ == "__main__":
    system = AutocompleteSystem()

    system.add_word("python", 5)
    system.add_word("pytorch", 3)
    system.add_word("pygame", 2)
    system.add_word("java", 4)
    system.add_word("javascript", 6)
    system.add_word("jupyter", 1)

    prefix = "py"
    suggestions = system.suggest(prefix)
    print(f"\nПодсказки для '{prefix}':")
    for word in suggestions:
        print(f"  {word} (частота: {system.freq_map[word]})")