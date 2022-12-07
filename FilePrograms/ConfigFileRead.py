
def ProcessFile(FileName):
    Result = {}
    fd = open(FileName,"r")
    for line in fd:
        if line.startswith('[') or line.endswith(']'):
            Dict = line[1:line.index(']')]
        else:
            Config_Option = line.split('=')
            Result[Config_Option[0]] = Config_Option[1]
        print(Result)
    return Result,Dict
def main():
    FileName = input('Enter File Name')
    Result,Dict = ProcessFile(FileName)
    print(Dict,'=',Result)

if __name__ == '__main__':
    main()