def read(fd):
    line = fd.readline()
    print(line)
    while True:
        line = fd.readline()
        print(line)
        if not line:
            print('EOF')
            break


if __name__ == '__main__':
    try:
        fd = open('.\\Temp1.txt')
        read(fd)
    except FileNotFoundError:
        print('File Not Available')