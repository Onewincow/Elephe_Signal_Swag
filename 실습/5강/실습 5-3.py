def findAllNCount(filename,key):
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    position = text.find(key)
    count = 0
    if position == -1 :
        outfile.write(key+" is not found\n")
    else :
        if text.count(key) == 1:
            outfile.write(key +' is found 1 time.\n')
        else :
            for _ in range(text.count(key)):
                count = count + 1
            outfile.write(key +' is found '+ str(count) + ' times.\n')
    outfile.close()
    infile.close()
    print("Done")

findAllNCount('article.txt','computer') # computer is found 6 times.
