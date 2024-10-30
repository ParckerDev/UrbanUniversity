class WordsFinder:
    def __init__(self, *files):
        self.file_names = list(files)

    def get_all_words(self):
        all_words = {}
        for file in self.file_names:
            with open(file, 'r', encoding='utf-8') as text_file:
                text = text_file.read().lower()
            words = self.del_punctuation(text).split()
            all_words[file] = words
        return all_words
    
    def find(self, word):
        find_words = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                find_words[key] = value.index(word.lower())
        return find_words

    def count(self, word):
        count_word = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                count_word[key] = value.count(word.lower())
        return count_word

    @staticmethod
    def del_punctuation(text):
        punct = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for p in punct:
            text = text.replace(p, '')
        return text.replace('  ', ' ')




terra = WordsFinder('text.txt', 'text2.txt', 'text3.txt')
print(terra.find('PYThon'))