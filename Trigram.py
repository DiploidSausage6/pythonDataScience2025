import string

text = input("enter the text you wish to analyze: ")

def text_cleaner(text):
  for char in string.punctuation:
    text = text.replace(char, ' ')
  words = text.lower().split()
  return words

words = text_cleaner(text)

counts = {}

for i in range(len(words) -2):
  trigram = (words[i], words[i+1], words[i+2])
  counts[trigram] = counts.get(trigram, 0) +1

freq_list = []
for trigram, count in counts.items():
   freq_list.append((count, trigram))
freq_list.sort(reverse=True)

print("Top 10 Trigrams:")
for count, trigram in freq_list[:10]:
   print(f"{' '.join(trigram)}: {count}")
