class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.word_count = 0 

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.word_count += 1

    def delete(self, word):
        def _delete_recursive(node, word, index):
            if index == len(word):
                if node.is_end_of_word:
                    node.is_end_of_word = False
                    node.word_count -= 1
                    return len(node.children) == 0
                return False

            char = word[index]
            if char not in node.children:
                return False

            should_delete_child = _delete_recursive(node.children[char], word, index + 1)
            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end_of_word

            return False

        _delete_recursive(self.root, word, 0)

    def count_words_with_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]

        def count_from_node(node):
            count = 0
            if node.is_end_of_word:
                count += node.word_count
            for child in node.children.values():
                count += count_from_node(child)
            return count

        return count_from_node(node)


if __name__ == "__main__":
    trie = Trie()
    words = ["cat", "car", "cart", "care", "dog", "door"]
    for w in words:
        trie.insert(w)

    print("Слов с префиксом 'ca':", trie.count_words_with_prefix("ca"))
    print("Слов с префиксом 'do':", trie.count_words_with_prefix("do"))

    trie.delete("car")
    print("После удаления 'car', слов с префиксом 'ca':", trie.count_words_with_prefix("ca"))