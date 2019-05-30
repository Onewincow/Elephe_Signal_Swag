members = {"doh": ("sid73", 994, 550, 35), "didi": ("edd484", 130, 55, 10), "hy": ("er878re", 35, 18, 2), "dr": ("qwert", 18, 0, -5),"who": ("poiuy", 34, 18, 0)}

def show_top5(members):
    print("-----")
    sorted_members = sorted(members.items(), key= lambda x:x[1][3], reverse = True)
    print("All-time Top 5 based on the number of chips earned")
    if len(sorted_members) < 5:
    	for i in range(len(sorted_members)):
    			if(sorted_list[i][1][3] > 0):
    				print(str(i+1) + '.', sorted_members[i][0] ,":", sorted_members[i][1][3])
    else :
    	for i in range(5):
    		if(sorted_members[i][1][3] > 0):
    			print(str(i+1) + '.', sorted_members[i][0] ,":", sorted_members[i][1][3])
show_top5(members)
