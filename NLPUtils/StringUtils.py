def getWord(token):
    index = token.rfind('/')
    word = ''
    if index > -1:
        word = token[0:index]
    return word


def getNature(token):
    index = token.rfind('/')
    nature = ''
    if index > -1:
        nature = token[index + 1:]
    return nature


class StringUtils():
    pass
