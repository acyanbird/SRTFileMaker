## created by cyanbird, 2018.10.26
##打轴哟哟哟
##gnome-terminal -e "python3 TimeLineWriting.py" | ffplay video

import time

StarPoint = time.time()  ##to record the start time
while 1:
    UserCommand = input()
    if UserCommand != '':
        break
    else:
        node = time.time()-StarPoint
        WholeNode = int(node) ## Get the whole num of node
        print(node)
        with open('TimeLine.txt','a+') as TimeLine:
                ExactTime = ("%02d:%02d:%05.3f" % (WholeNode // 3600, WholeNode // 60, node % 60 )) ##exact time node
                ExactTime = ExactTime.replace('.',',')
                TimeLine.write(ExactTime)
                TimeLine.write('\n')
