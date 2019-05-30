def findAllSentences(filename,key) :
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    x = text.find('.')
    y = text.partitiong('.')
    while True:
        if y[0].find(key) == -1 and x == -1 :
            outfile.write (key, ' appears ', text.count(key) , ' times in ', text.count(key),' sentences.')
            break
        elif y[0],find(key)

    outfile.close()
    infile.close()
    print("done")


def findAllSentence(filename,key) :
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    total, sentenceCount = 0, 0
    while text != "" :
        (sentence,delimiter,text) = textPartition(text)
        sentence = sentence.strip(' \n')
        index = sentence.find(key)
        count = 0
        while index != -1 :
            count += 1
            index = sentence.find(key,index+1)
        if count > 0 :
            total += count
            outfile.write("'" + key + "'이(가) " + str(count) + "번 등장\n")
            outfile.write(sentence + delimiter + "\n\n")
            sentence_count += 1
    outfile.write("'" + key + "'이(가) " + str(sentenceCount) + "개 문장에서 " + str(total) + "번 등장\n")
    outfile.close()
    infile.close()
    print("done")
