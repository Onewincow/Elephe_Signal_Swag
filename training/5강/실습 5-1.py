def findLast(filename,key):
    infile = open('article.txt','r')
    outfile = open('result.txt','w')
    text = infile.read()
    position = text.find(key)
    if position == -1:
        outfile.write(key+" is not found. \n")
    else:
        for _ in range(text.count(key)-1) :
            position = text.find(key, position+1)
        outfile.write(key+" is at "+ str(position) + '. \n')
    outfile.close()
    infile.close()
    print('Done')

def findLast(filename,key) :
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    lastPosition = -1
    position = text.find(key)
    while position != -1 :
        lastPosition = position
        position = text.find(key,position+1)
    if lastPosition == -1:
        outfile.write(key + " is not found.\n")
    else:
        outfile.write(key + " is at " + str(lastPosition) + " the last time.\n")
    outfile.close()
    infile.close()
    print("Done")
