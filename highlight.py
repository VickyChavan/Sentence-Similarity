from nltk.tokenize import sent_tokenize 
def mark_similar(h1, h2, option):
    final = c = j = ''
    if option == 'Line':
        k = h1.split('\\n')
        for i in k:
            for j in h2:
                if j == i:
                    c = c + f'''<mark>{i}\n</mark>'''
                    break
            if j != i:
                c = c + f'''{i}\n'''
        final = c
    else:
        k = sent_tokenize(h1)
        for i in k:
            for j in h2:
                if j == i:
                    c = c + f'''<mark>fil </mark>'''
                    break
            if j != i:
                c = c + f'''{i}'''
        final = c.replace('\\n', '\n')
    return final

def line(f1, f2):
    k = set(f1.split('\\n'))
    l = set(f2.split('\\n'))
    h = k.intersection(l)
    return h

def sentence(f1, f2):
    a = f1.replace('\\n', '')
    k = set(sent_tokenize(a))
    b = f2.replace('\\n', '')
    l = set(sent_tokenize(b))
    h = k.intersection(l)
    return h