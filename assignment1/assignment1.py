import re
from collections import Counter

regex = re.compile('[^a-zA-Z]')

##############SWAPCHARS################
def swapchars(string):
    #make a copy of the string lowercase and remove punctuation
    better_string = string.lower()
    better_string = regex.sub('', better_string)

    #define counters
    cnt = Counter()
    reversed_cnt = Counter()

    #Count occurances of each letter
    for character in better_string:
        cnt[character] += 1

    #make a reversed counter of char occurances
    for character in cnt:
        reversed_cnt[character] = -1 * cnt[character]

    #most and least common characters
    [(most,_)] = cnt.most_common(1)
    [(least,_)] = reversed_cnt.most_common(1)

    #swap the uppercase characters
    string = string.replace(str.upper(most), '|')
    string = string.replace(str.upper(least), str.upper(most))
    string = string.replace('|', str.upper(least))
    #swap the lowercase characters
    string = string.replace(most, '|')
    string = string.replace(least, most)
    string = string.replace('|', least)

    return string

#############SORTCAT###############
def sortcat(n, *lst):
    #convert the tuple to a sorted list
    lst = sorted(lst, key=len)
    lst.reverse()

    output = ''

    #specify number of elements to return
    if n >= 0:
        lst = lst[0:n]

    #collapse the list into a string
    for i in lst:
        output += str(i)

    return output

############BLUE'S CLUES#############
#make a dict of states and abbreviations
f = open("states.txt", "r")
states = {}
for line in f:
    line = line.rstrip('\n')
    [v,k] = line.split(',')
    states[k] = v

def what_state_is_this(abbr):
    print states[abbr]
    return states[abbr]

############BLUE'S BOOZE#############
def how_do_i_abbrev_this(state):
    for x in states:
        if states[x] == state:
            return x