import csv
class WordReplacer(object):
    def __init__(self, word_map):
        self.word_map = word_map
    def replace(self, word):
        return self.word_map.get(word)

class CsvWordReplacer(WordReplacer):
    def __init__(self, fname):
        word_map = {}
        for line in csv.reader(open(fname)):
            word, syn = line
            word_map[word] = syn
        super(CsvWordReplacer, self).__init__(word_map)

def refine(qString):
    replacer = CsvWordReplacer('src/keyword_/synonym_test.csv')
    qSplited = qString.split(' ')

    qReplace = []
    for i in qSplited:
        target = replacer.replace(i)

        if target is not None:
            qReplace.append(target)
        

    string = ' '.join(qReplace)

    return string



if __name__ == '__main__':
    replacer = CsvWordReplacer('src/keyword_/synonym_test.csv')
    #print(replacer.replace('bday'))
    qSplited = qString.split(' ')
    qString = 'I want array algorithm with 10 goods equivalent'
    qReplaced = ''
    for i in qSplited:
        qReplaced += replacer.replace(i)
        qReplaced += ' '
    print(qReplaced)