import os
import urllib.request
import shutil
from zipfile import ZipFile
import tempfile


print('Downloaded. Extracting enwik8 form zipfile')
ZipFile("D:/Sakana/P-4/nanoGPT/data/enwik8/enwik8.zip").extractall("D:/Sakana/P-4/nanoGPT/data/enwik8/")
print('Data extracted. Cleaning up and moving the data files to data directory')