#!/usr/bin/env python3

from os import listdir
from os.path import abspath, dirname


THIS_DIR = dirname(abspath(__file__))
EXT = ('.gitignore')


def create_gitignore(child_dir: 'str') -> 'None':
  """
  Creates a `.gitignore` file from the `.gitignore` files 
  located within a `gitignore` folder, if the files/folder exist
  """  
  
  index = THIS_DIR.rfind(child_dir)
  parent_dir = THIS_DIR[:index]

  # list of files in directory
  gitignore_files = listdir(THIS_DIR)
  
  if not gitignore_files:
    return None
  
  text = ''
  store = []
  
  for file in gitignore_files:
    file_path = f'{THIS_DIR}/{file}'
    if file_path.endswith(EXT) == True:
      with open(file_path, 'r') as f:     
        temp = f.read()
        text = text + temp + '\n'
        store.append({'file': file})
  
  if len(text) == '':
    return None
  
  with open(f'{parent_dir}/.gitignore', 'w') as f:
    # delete file contents
    f.truncate(0)
    # write text to the new file
    f.write(text)
  
  print({
    'directory': parent_dir,
    'consolidated': store})
  return None


if __name__ == '__main__':
  create_gitignore('')
