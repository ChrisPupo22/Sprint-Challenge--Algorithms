'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # word = thaththt
    w1 = len(word)
    w2 = len('th')

    if (w1 == 0 or w1 < w2):
        return 0

    if (word[0 : w2] == 'th'):
        return count_th(word[w2 - 1:], 'th') + 1

    return count_th(word[w2 - 1:], 'th')



print(count_th(word='thath'))