#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File name: setup.py
Author: PCLabTools
Created: 2025-02-08
Version: 1.0
Description: Run this script to set up the project as a new rapidPlugin
"""

import os
import tkinter as tk
from tkinter import simpledialog

class MultiInputDialog(simpledialog.Dialog):
  def body(self, master):
    tk.Label(master, text="Please fill in the following details to set up your rapidPlugin project:").grid(row=0, columnspan=2, pady=(10, 20))
    tk.Label(master, text="Plugin Name:").grid(row=1)
    tk.Label(master, text="Author Name:").grid(row=2)
    tk.Label(master, text="Author Email:").grid(row=3)
    tk.Label(master, text="Plugin Description:").grid(row=4)
    
    self.project_name_entry = tk.Entry(master, width=30)
    self.author_name_entry = tk.Entry(master, width=30)
    self.author_email_entry = tk.Entry(master, width=30)
    self.project_description_entry = tk.Text(master, width=28, height=5)

    self.project_name_entry.grid(row=1, column=1)
    self.author_name_entry.grid(row=2, column=1)
    self.author_email_entry.grid(row=3, column=1)
    self.project_description_entry.grid(row=4, column=1)
    return self.project_name_entry  # initial focus

  def apply(self):
    self.project_name = self.project_name_entry.get()
    self.author_name = self.author_name_entry.get()
    self.author_email = self.author_email_entry.get()
    self.project_description = self.project_description_entry.get("1.0", tk.END).strip()

def show_prompt():
  global project_name, author_name, project_description, author_email

  root = tk.Tk()
  root.withdraw()  # Hide the root window

  dialog = MultiInputDialog(root, "Enter Project Details")
  try:
    project_name = dialog.project_name.replace(' ', '_').lower()
    author_name = dialog.author_name
    project_description = dialog.project_description
    author_email = dialog.author_email
  except:
    project_name = ''
    

def write_README():
  FILEPATH_README = 'README.md'
  readme_contents = '''# rapidPlugin_{}

{}

Author: {}

Email: {}

## Installation

### Arduino

To install this library follow the standard method of installing libraries, either using the library manager or a downloaded zip file of this repository.

**Make sure to install the below listed dependencies as this library depends upon them.**

For more information on how to install libraries please visit [Installing Additional Arduino Libraries](https://www.arduino.cc/en/guide/libraries "arduino.cc").

#### Dependencies

| Name | Git Link | ZIP file |
| - | - | - |
|rapidRTOS (PCLabTools) | https://github.com/PCLabTools/rapidRTOS.git | [Download zip file](https://github.com/PCLabTools/rapidRTOS/archive/refs/heads/master.zip) |

### PlatformIO

To include this library and its dependencies simply add the following to the "platformio.ini" file:
```
[env:my_build_env]
framework = arduino
lib_deps = 
  https://github.com/{}/{}.git
```

## Usage

### General Usage

1. Include the {}.h library:

``` cpp
#include <{}.h>
```
'''.format(project_name, project_description, author_name, author_email, author_name, project_name, project_name, project_name)

  with open(FILEPATH_README, 'w') as file:
    file.write(readme_contents)

def update_term_in_file(file_path, search_term, replace_term):
  with open(file_path, 'r') as file:
    content = file.read()
  
  updated_content = content.replace(search_term, replace_term)
  
  with open(file_path, 'w') as file:
    file.write(updated_content)

def recursively_update_files(folder_path, search_term, replace_term):
  for root, dirs, files in os.walk(folder_path):
    dirs[:] = [d for d in dirs if d != '.git']  # Exclude .git directory
    for file in files:
      if file != 'setup.py':
        file_path = os.path.join(root, file)
        update_term_in_file(file_path, search_term, replace_term)

def update_file_name(folder_path):
  os.rename(os.path.join(folder_path, f'src/rapidPlugin_template.h'), os.path.join(folder_path, f'src/rapidPlugin_{project_name}.h'))

if __name__ == "__main__":
  show_prompt()

  if project_name:
    print(f"Project Name: {project_name}")
    print(f"Author Name: {author_name}")
    print(f"Project Description: {project_description}")
    print(f"Author Email: {author_email}")

    write_README()

    folder_path = '.'
    search_term = 'template'
      
    recursively_update_files(folder_path, search_term, project_name)
    update_file_name(folder_path)

    print("Project setup complete!")

  else:
    print("No project name provided. Exiting...")
