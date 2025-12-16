import time
import re
from collections import defaultdict

def read_text():
    text = """
    Python is a great language. Python is easy to learn. 
    Many developers love Python because it is simple and powerful.
    Python can be used for web development, data science, automation, and more.
    """
    return text

def clean_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return words

def bad_hash(key):
    return 1

def good_hash(key):
    return hash(key) % 1000000

class FrequencyMap:
    def __init__(self, hash_func=good_hash):
        self.hash_func = hash_func
        self.data = {}

    def add_word(self, word):
        index = self.hash_func(word)
        if index not in self.data:
            self.data[index] = {}
        if word not in self.data[index]:
            self.data[index][word] = 0
        self.data[index][word] += 1

    def get_top_10(self):
        all_words = []
        for bucket in self.data.values():
            for word, count in bucket.items():
                all_words.append((count, word))
        all_words.sort(reverse=True)
        return all_words[:10]

def compare_hashes():
    text = read_text()
    words = clean_words(text)

    start = time.time()
    fm_bad = FrequencyMap(bad_hash)
    for word in words:
        fm_bad.add_word(word)
    top_bad = fm_bad.get_top_10()
    time_bad = time.time() - start

    start = time.time()
    fm_good = FrequencyMap(good_hash)
    for word in words:
        fm_good.add_word(word)
    top_good = fm_good.get_top_10()
    time_good = time.time() - start

    print("Плохая хэш-функция:")
    for count, word in top_bad:
        print(f"  {word}: {count}")

    print("\nХорошая хэш-функция:")
    for count, word in top_good:
        print(f"  {word}: {count}")

    print(f"\n⏱ Время (плохая хэш): {time_bad:.6f} сек")
    print(f"⏱ Время (хорошая хэш): {time_good:.6f} сек")

if __name__ == "__main__":
    compare_hashes()