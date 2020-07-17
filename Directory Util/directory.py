import os

def get_current_dir():
    cwd = os.getcwd()  # get current working dir: C:\\Users\\%USERPROFILE%\\Desktop
    return cwd

def file_in_current_dir(fileName):
    currentDir = get_current_dir()
    #search if the file exists in the current directory
    for file in os.listdir(currentDir):
        if file.startswith(fileName):
            return True

def file_in_dir(fileName, dir):
    # search if the file exists in a certian directory
    for file in os.listdir(dir):
        if file.startswith(fileName):
            return True

def to_absolute_path(relPath):
    currentDir = get_current_dir()
    absDir = currentDir + '\\' + relPath
    return absDir

def to_relative_path(absPath):
    currentDir = get_current_dir()
    relDir = absPath.lstrip(currentDir)
    return relDir

if __name__ == '__main__':
    print(to_absolute_path('AI PyPong\Single Player\pypong.py'))
    print(to_relative_path('C:\\Users\\kai\\Desktop\\Programming\\Python\\Python-Projects\\AI PyPong\\Single Player\\pypong.py'))
    with open(to_absolute_path('AI PyPong\Single Player\pypong.py')):
        print('abs')
    with open(to_relative_path('C:\\Users\\kai\\Desktop\\Programming\\Python\\Python-Projects\\AI PyPong\\Single Player\\pypong.py')):
        print('rel')
