import collections

text = "kek kek ek ek kek kekekek kekek ek kek"
words = text.split()
most_common, count = collections.Counter(words).most_common()[0]

the_longest = max(words, key=len)

print(most_common, the_longest)
