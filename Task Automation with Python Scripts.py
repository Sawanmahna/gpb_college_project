# -*- coding: utf-8 -*-
"""
Created on Mon Jun  10 10:02:13 2024

@author: Sawan Kumar
"""

import os
import shutil
from pathlib import Path


downloads_path = Path.home() / 'Downloads'


file_types = {
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Video': ['.mp4', '.mkv', '.avi', '.mov'],
    'Archives': ['.zip', '.tar', '.gz', '.rar'],
    'Executables': ['.exe', '.msi'],
}


for folder in file_types.keys():
    folder_path = downloads_path / folder
    if not folder_path.exists():
        folder_path.mkdir()


for file in downloads_path.iterdir():
    if file.is_file():
        for folder, extensions in file_types.items():
            if file.suffix.lower() in extensions:
                destination = downloads_path / folder / file.name
                try:
                    shutil.move(str(file), str(destination))
                    print(f'Moved {file.name} to {folder}')
                except PermissionError:
                    print(f'Could not move {file.name} as it is being used by another process.')
                break
