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
