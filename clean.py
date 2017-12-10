i=0
with open("top1000.txt", "r") as top:
    with open("top1000clean.txt", "w") as cleanTop:
        word = ''
        for line in top:
            if i % 3 == 0:
                word = line.rstrip('\n') + '\t'
            if i % 3 == 1:
                word += line
                cleanTop.write(word)
                word = ''
            i = i + 1
    
