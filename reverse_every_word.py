def reverseWordSentence(Sentence):
    return ' '.join(word[::-1] for word in Sentence.split(" "))
    
Sentence=str(input())
print(reverseWordSentence(Sentence))