
# A list of unsorted words
unsorted_words=["dog","bat","cat","mole","vole","ant"]
# An empty list to receive the sorted words
sorted_words=[]

while unsorted_words:
  word = unsorted_words.pop()
  index = 0
  for s_word in sorted_words:
    print(f"comparing {word} with {s_word}")

    if word > s_word:
      index += 1
    else:
      break

  sorted_words.insert(index, word)

print(sorted_words)
