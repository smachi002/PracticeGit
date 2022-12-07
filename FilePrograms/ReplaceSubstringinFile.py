try:
    fd = open('.\\Temp1.txt','r')
    line = fd.read()
    print(line)
    if 'Enigma' in line:
        data = line.replace('Enigma','Swapnil')
        fd = open('.\\Temp1.txt','w')
        fd.write(data)
    fd.close()
except FileNotFoundError:
    print('File Not available')