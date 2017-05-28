import csv
class WordReplacer(object):
    def __init__(self, word_map):
        self.word_map = word_map
    def replace(self, word):
        return self.word_map.get(word, word)
class CsvWordReplacer(WordReplacer):
    def __init__(self, fname):
        word_map = {}
        for line in csv.reader(open(fname)):
            word, syn = line
            word_map[word] = syn
        super(CsvWordReplacer, self).__init__(word_map)

replacer = CsvWordReplacer('synonym_test.csv')
#print(replacer.replace('bday'))
qString = 'I want array algorithm with 10 goods equivalent'
qSplited = qString.split(' ')
qReplaced = ''
for i in qSplited:
    qReplaced += replacer.replace(i)
    qReplaced += ' '
print(qReplaced)