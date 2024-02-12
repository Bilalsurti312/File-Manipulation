words={}
file = open('TEXT.txt","r')
for line in file:

    line=line.strip()
    line=line.lower()

    word=line.split("")
    word=sorted(word)

    for i in word:
        if i in words:
            words[i]-words[i]+1
        else:
            words[i]=1
for key in list(words.keys()):
    print(key, ":", words[key])