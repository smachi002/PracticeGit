import configparser


def readConfig(Path):
    parser = configparser.ConfigParser()
    parser.read(Path)
    Url = parser['CommonInfo']['url']
    print(Url)


if __name__ == '__main__':
    Path = '.\\Config.ini'
    readConfig(Path)
