import os

for files in os.walk('fioconfig'):
    for file in files:
        filepath = file
        
        if filepath.endswith(".cfg"):
            print (filepath)