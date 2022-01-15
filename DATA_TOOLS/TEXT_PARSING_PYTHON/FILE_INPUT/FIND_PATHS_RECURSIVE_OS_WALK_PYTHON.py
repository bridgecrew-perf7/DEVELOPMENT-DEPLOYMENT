import os

filepath = "."
filetype = ".py"

def list_files(filepath, filetype):
   paths = []
   for root, dirs, files in os.walk(filepath, followlinks=True):
      for file in files:
         if file.lower().endswith(filetype):
            paths.append(os.path.join(root, file))
   return paths

for x in list_files(filepath, filetype):
    print(x)
