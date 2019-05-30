def oneSentencePerLine(filename) :
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    count = 0
    for _ in range(text.count('.') + text.count('?')) :
        if text.find('.') == -1 and text.find('?'):
            break
        elif text.find('.') < text.find('?') or text.find('?')==-1 :
            x = text.partition('.')
            outfile.write(x[0] + x[1] +'\n'+'\n')
            count += 1
            text = x[2].strip()
        elif text.find('.') > text.find('?') or text.find('.')==-1 :
            y = text.partition('?')
            outfile.write(y[0] + y[1] + '\n'+'\n')
            count +=1
            text = y[2].strip()

    outfile.write("There are " + str(count) + " sentences in total.\n")
    outfile.close()
    infile.close()
    print("Done")

oneSentencePerLine('article.txt')


# version 1 (simple version - double quote 미처리)
def textPartition(text) :
    dot = text.find(".")
    que = text.find("?")
    if dot == que == -1 :
        return (text,"","")
    elif que == -1 :
        return text.partition(".")
    elif dot == -1 :
        return text.partition("?")
    elif dot < que :
        return text.partition(".")
    else :
        return text.partition("?")

def oneSentencePerLine(filename) :
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    count = 0
    while text != "":
        (sentence,delimiter,text) = textPartition(text)
        sentence = sentence.strip(' \n')
        outfile.write(sentence + delimiter + "\n\n")
        count += 1
    outfile.write("There are " + str(count) + " sentences in total.\n")
    outfile.close()
    infile.close()
    print("Done")
# oneSentencePerLine("article.txt") # There are 145 sentences in total.
# result.txt 를 보면 :로 끝난 문장이 있습니다. 이건 :로 끝난 문단이 있고, 그 뒤에 \n이
# 2개나 있어서 문장이 끝나진 았았지만, \n이 2개가 그대로 출력이 된 것입니다.
# 따라서 count는 145개 이지만, 줄을 세어보면 147개 입니다.
# 문제 자체의 헛점입니다. 문단이 끝나면 그 문단의 마지막 문장도 끝으로 취급했어야 했었습니다.
# 그럼면 실제 문장의 개수는 147개가 되지요.

# version 2 (double quote 처리 version)
def textPartition2(text) :
    dot = text.find(".")
    question = text.find("?")
    quote = text.find('"')
    if question == -1 and dot == -1:
        return (text,"","")
    if question == -1 :
        return text.partition(".")
    elif dot == -1 :
        return text.partition("?")
    elif dot < question :
        return text.partition(".")
    else :
        return text.partition("?")

def oneSentencePerLine2(filename) :
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    count = 0
    while text != "" :
        (sentence, delimiter, text) = textPartition2(text)
        if text.startswith('"'):
            text = text[1:]
            delimiter += '"'
        sentence = sentence.strip(' \n')
        outfile.write(sentence + delimiter + "\n\n")
        count += 1
    outfile.write("There are " + str(count) + " sentences in total.\n")
    outfile.close()
    infile.close()
    print("Done")
# oneSentencePerLine2("article.txt") # There are 145 sentences in total.
