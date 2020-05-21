import eyed3
import os

def scanner(directory):
    ndir = ""
    print(directory)
    if (directory == ""):
        return
    else:
        # Recursively search for folders and files
        # When an MP3 is found, extract tag information
        os.chdir(directory)
        dirlist = os.scandir()
        for i in dirlist:
            if (i.is_dir()):
                print(i.path)
                ndir = os.path.abspath(i.path)
                scanner(ndir)
            elif (i.is_file()):
                if os.path.splitext(i.name)[1] == ".mp3":
                    print(i.name)
            os.chdir(directory)
        dirlist.close()
        ndir = ""
        scanner(ndir)