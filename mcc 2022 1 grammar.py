GRAPH = [
    ['WE', 'DONT'],
    ['THEY', 'DONT'],
    ['DONT', 'KNOW'],
    ['WE', 'KNOW'],
    ['THEY', 'KNOW'],
    ['KNOW', 'WE'],
    ['KNOW', 'THEY'],
    ['KNOW', 'THAT'],
    ['THAT', 'WE'],
    ['THAT', 'THEY']
]
def sentence_splitter(sentence):
    return sentence.split()
def grammarcheck(sentence):
    if len (sentence) > 1:
        check = [sentence[0], sentence[1]]
        if check in GRAPH:
            sentence.pop(0)
            return grammarcheck(sentence)
        return False
    else:
        return True
    
print(grammarcheck(sentence_splitter("WE KNOW WE KNOW WE KNOW THAT WE"))) #True
print(grammarcheck(sentence_splitter("WE THAT DONT WE THEY"))) #False
print(grammarcheck(sentence_splitter("THEY DONT KNOW"))) #True
print(grammarcheck(sentence_splitter("THEY"))) #True