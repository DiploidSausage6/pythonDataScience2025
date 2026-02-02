import string

text = "The tortoise and the hare decided to have a race. The hare was very fast and the tortoise was very slow. The hare ran far ahead and then the hare took a nap. While the hare slept, the tortoise kept walking. The tortoise walked and walked until the tortoise passed the sleeping hare. The tortoise won the race because the tortoise never stopped. The hare woke up but the hare was too late. The slow tortoise beat the fast hare."

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

