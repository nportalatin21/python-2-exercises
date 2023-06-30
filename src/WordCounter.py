class WordCounter:
    def __init__(self, sentence):
        self.sentence = sentence
        self.word_count = None

    def count_words(self):
        self.word_count = len(self.sentence.split())

    def get_word_count(self):
        return self.word_count

    def get_shortest_word(self):
        words = self.sentence.split()
        if words:
            return min(len(word) for word in words)
        # return 0

    def get_longest_word(self):
        words = self.sentence.split()
        if words:
            return max(len(word) for word in words)
        # return 0
