from pprint import *
import re
class WordsFinder():
    def __init__(self, *file_names):
        self.file_names = file_names
    def get_all_words(self):
        all_words = {}
        lwords = list()
        cwords = list()
        punct = [',', '.', '=', '!', '?', ';', ':', ' - ']


        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:
                content = file.read()
                words_list = content.split()
                lwords = [s.lower() for s in words_list]
                cwords = [re.sub(r'[^\w\s]', '', s) for s in lwords]

                all_words[name] = cwords

                file.close()
        return all_words

    def count(self, word):
        count: int = 0
        dict_all = self.get_all_words()
        word_count = {}

        for file_name, words in dict_all.items():
            count = words.count(word)
            word_count[file_name] = count
        return word_count

    def find(self, word):
        result = {}
        dict_all = self.get_all_words()

        for file_name, words in dict_all.items():
            if word in words:
                result[file_name] = words.index(word)
        return result


w = WordsFinder('text1_7_3.txt', 'text2_7_3.txt')
print(f"=========")
print(f"All words: {w.get_all_words()}")
print(f"Find: {w.find('Study')}")
print(f"Count: {w.count('luck')}")
print()