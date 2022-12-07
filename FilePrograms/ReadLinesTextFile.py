def read(fd):
    line = fd.readlines()
    print(line)
if __name__ == '__main__':
    try:
        fd = open('.\\Temp1.txt')
        read(fd)
    except FileNotFoundError:
        print('File Not Available')

