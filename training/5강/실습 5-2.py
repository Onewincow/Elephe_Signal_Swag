def findAll(filename,key):
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    position = text.find(key)
    if position == -1:
        outfile.write(key+" is not found.\n")
    else:
        outfile.write(key+" is at "+ str(position) + '.\n')
        for _ in range(text.count(key)-1) :
            position = text.find(key, position+1)
            outfile.write(key+" is at "+ str(position) + '.\n')
    outfile.close()
    infile.close()
    print("Done")

findAll('article.txt','apple')

def findAll(filename,key) :
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    position = text.find(key)
    if position == -1:
        outfile.write(key + " is not found.\n")
    while position != -1 :
        outfile.write(key + " is at " + str(position) + ".\n")
        position = text.find(key,position+1)
    outfile.close()
    infile.close()
    print("Done")
