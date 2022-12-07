def MaxMin(fd):
        Line = fd.readline()
        Max = Line
        Min = Line
        while True:
            Line = fd.readline()
            print(Line)
            if not Line:
                print('End of file')
                break
            else:
                if len(Line)>len(Max):
                    Max = Line
                if len(Line)<len(Min):                    
                    Min = Line
        return Max,Min           
if __name__ == '__main__':
    fd = open('C:\\Users\swapnil.machikar\OneDrive - Nihilent Limited\Desktop\Sample.txt')
    Max,Min = MaxMin(fd)
    print('Max is:-'+Max,'\nMin is:-'+Min)