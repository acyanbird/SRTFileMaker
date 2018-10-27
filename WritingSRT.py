##created by cyanbird 2018.10.26
##写轴哟哟哟

Nodes = open('TimeLine.txt','r')
nodes = ['00:00:00,000']
FilePath = input('input the text file path including extension:')
for x in Nodes.readlines():
    nodes.append(x.strip('\n'))
Nodes.close()

TextFile = open(FilePath,'r')
Text = []
for line in TextFile.readlines():
    if line != '\n':
        Text.append(line.strip('\n'))
TextFile.close()

print(nodes[-1])
SRTFile = open('SRTFile.txt','w+')
for order in range(len(nodes)-1):
    SRTFile.write('%s\n' % order)
    SRTFile.write('%s --> %s\n' % (nodes[order], nodes[order+1]))
    SRTFile.write('%s\n%s\n\n' % (Text[2*order], Text[2*order+1]))
SRTFile.close()