import os

path = 'C:/Users/sereg/Desktop'
files = [f for f in os.listdir(path=path) if os.path.isfile(os.path.join(path, f))]

print(files)