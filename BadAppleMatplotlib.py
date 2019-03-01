# Code to run matplotlib codes to generate and save the plots

import subprocess

for frameCounter in range (1810, 32855, 5):
    with open(".\\Bad_Apple_matplotlib_code\\" + str(frameCounter) + ".txt", 'r+') as content_file:
        frame = ".\\Bad_Apple_matplotlib_code\\" + str(frameCounter) + ".txt"
        subprocess.check_call(["python", frame], stdout=content_file)


