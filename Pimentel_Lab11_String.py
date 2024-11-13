word_Count=0
Words=[]
matched_words=[]
while word_Count<10:
    word=input("Enter a Word: ")
    Words.append(word)
    word_Count+=1
num=int(input("Enter the Numbers of words: "))
for i in Words:
    if len(i)>=num:
        matched_words.append(i)
print(matched_words)