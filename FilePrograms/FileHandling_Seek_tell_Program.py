#Printing alternate 10-10 characters in file
import os.path
from os import path

if __name__ == '__main__':
    fd = open('..\OneDrive - Nihilent Limited\Desktop\Sample.txt')
    Line = 10
    while True:
        line = fd.read(Line)
        if not line:
            print('End of file')
            break
        else:
            print(line)
            Line = fd.tell()
            Line=Line+10
            fd.seek(Line,0)
print ("File exists:"+str(path.exists('C:\\Users\swapnil.machikar\OneDrive - Nihilent Limited\Desktop\Sample.txt')))
print (path.dirname('C:\\Users\swapnil.machikar\OneDrive - Nihilent Limited\Desktop\Sample.txt'))
print (path.isdir('C:\\Users\swapnil.machikar'))
print (path.isfile('C:\\Users\swapnil.machikar\OneDrive - Nihilent Limited\Desktop\Sample.txt'))
print (path.getsize('C:\\Users\swapnil.machikar\OneDrive - Nihilent Limited\Desktop\Sample.txt'))
print (path.getatime('C:\\Users\swapnil.machikar\OneDrive - Nihilent Limited\Desktop\Sample.txt'))
print (path.normcase('Sample.txt'))
print (path.normpath('C:\\Users\swapnil.machikar\OneDrive - Nihilent Limited\Desktop\Sample.txt'))
print (path.relpath('C:\\Users\swapnil.machikar\OneDrive - Nihilent Limited\Desktop\Sample.txt'))
print (path.samefile('..\OneDrive - Nihilent Limited\Desktop\Sample.txt', '..\OneDrive - Nihilent Limited\Desktop\Sample.txt'))
print (path.splitext('C:\\Users\swapnil.machikar\OneDrive - Nihilent Limited\Desktop\Sample.txt'))
print (path.split('C:\\Users\swapnil.machikar\OneDrive - Nihilent Limited\Desktop\Sample.txt'))