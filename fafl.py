words=input("Enter string ")
words=list(words)
words=['b']+words+['b']
print(words)
count=1

def goright(words,count):
    print("Going right ")
    for i in range(len(words)-2):
        if(words[count]!='b' and words[count]!='Y'):
            print(words[count])
            count+=1
    count-=1
    return count

def goleft(words,count):
    print("Going left ")
    for i in range(len(words)-2):
        if(words[count]!='b' and words[count]!='X'):
            print(words[count])
            count-=1
    count+=1
    return count

def run(words,count):
    for i in range((len(words)-2)):
        if words[count]=='1':
            break
        if (words[count-1]=='b' or words[count-1]=='X') and words[count]=='0' and words[count+1]!='Y':
            words[count]='X'
            count=goright(words,count)
        if (words[count+1]=='b' or words[count+1]=='Y') and words[count]=='1':
            words[count]='Y'
            count=goleft(words,count)
    return words

word=run(words,count)
print(word)
if '1' in words or '0' in words:
    print("Not accepted")
else:
    print("Accepted")
