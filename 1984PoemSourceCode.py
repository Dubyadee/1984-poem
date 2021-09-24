###THIS CHUNK OF CODE WAS BORROWED FROM RECCOMENDATION OF PROF. ZACH WHALEN###
with open('/content/drive/MyDrive/Defined/1984 txt.txt') as f:
  text = f.read()

text = text.replace("“","\"").replace("”","\"")

from textblob import TextBlob
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('brown')

blob = TextBlob(text)
tagged_words = blob.tags
sentence_list = blob.sentences
phrases_list = blob.noun_phrases
###END###

def cleaner(input):
  import random
  line_1 = TextBlob(input)
  line_1 = line_1.words
  cleaned = []
  for words in line_1:
    if (words not in ["'s", "'ll", "and", "ca", "n't", "'you", "'re", "b-b", "'d", '"']):
      cleaned.append(words)
  cleaned = " ".join(cleaned)
  return(cleaned)

###RUN FROM HERE DOWN IN A DIFFERENT CELL IF YOU DON'T WANT 3 MINUTE WAIT TIMES###
import random
print("Woe, our", cleaner(random.choice(phrases_list)))
print("Look at their", cleaner(random.choice(phrases_list)))
print("See how they deprive us of", cleaner(random.choice(phrases_list)))
print("Literally 1984...")
print(cleaner(random.choice(phrases_list)).capitalize(), "will become our lot...")
print("Don't say I didn't warn you.")
