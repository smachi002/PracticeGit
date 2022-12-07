try:
    fd = open('.\\Temp1.txt','r+')
    line = fd.readline()
    print(line)
    while line:
        line = fd.readline()
        print(line)
    fd.write('\nEnigma')
    fd.close()

except FileNotFoundError:
    print('File Not available')