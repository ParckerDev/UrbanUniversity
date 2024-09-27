class WordsFinder:
    def __init__(self, *files):
        self.file_names = list(files)

    def get_all_words(self):
        all_words = {}
        for file in self.file_names:
            with open(file, 'r', encoding='utf-8') as file:
                text = file.read().lower()
            words = self.del_punctuation(text).split()
            all_words[file] = words

    @staticmethod
    def del_punctuation(text):
        punct = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for p in punct:
            text = text.replace(p, '')
        return text.replace('  ', ' ')




terra = WordsFinder('text.txt', 'text2.txt', 'text3.txt')
print(terra.__dict__)