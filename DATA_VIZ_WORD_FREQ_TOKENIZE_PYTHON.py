import nltk
from nltk import tokenize

tokenSpace = tokenize.WhitespaceTokenizer()
def counter(text, columnText, quantity):
    allWords = ' '.join([text for text in text[columnText].astype('str')])
    tokenPhrase = tokenSpace.tokenize(allWords)
    frequency = nltk.FreqDist(tokenPhrase)
    dfFrequency = pd.DataFrame({"Word": list(frequency.keys()), "Frequency": list(frequency.values())})

    dfFrequency = dfFrequency.nlargest(columns = "Frequency", n = quantity)
    plt.figure(figsize=(12,8))
    ax = sns.barplot(data = dfFrequency, x = "Word", y = "Frequency", palette="deep")
    ax.set(ylabel = "Count")
    plt.xticks(rotation='horizontal')
    plt.show()


my_stop_words = ['the','and','to','i','of','was','with','on','in','for','no','name','is','he','or','at','as','one','she','am','you','his','your','were','by','pt','not','her','be','this','are','there','had','date','from','first','an','that','have','but','has','please','which','namepattern','seen','every','fax', 'home', 'telephone', 'given', 'after','also','will', 'un', 'up', 'well', 'time', 'any']

vect = CountVectorizer(max_features = 3000, tokenizer = note_flatner, stop_words = my_stop_words)

counter(df2[df2['tags'] == 1], 'text', 20)

dfFrequency = dfFrequency [~dfFrequency ['Word'].str.contains('|'.join(my_stop_words))]
