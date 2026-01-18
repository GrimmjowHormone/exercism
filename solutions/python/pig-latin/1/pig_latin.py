def translate(text):
    words = text.split()
    translated = []

    for w in words:
        translated.append(piglatin(w))

    return ' '.join(translated)



def piglatin(text):

    consonants=''
    vocals=['a','e','i','o','u']
    if text[0] in vocals:
        return text+'ay'
    if text[:2] in ['xr','yt']:
        return text+'ay'

    if text[0] not in vocals:
        for i,l in enumerate(text):

            if l in vocals:
                break
            if i<len(text)-1 and l+text[i+1]=='qu':
                return(text[i+2:]+text[:i+2]+'ay')

            if l=='y' and i>0:
                return(text[i:]+text[:i]+'ay')

    if text[0] not in vocals:
        consonants=''
        for c in text:
            if c not in vocals:
                consonants+=c
            else:
                break       
        return text[len(consonants):]+consonants+'ay'
        