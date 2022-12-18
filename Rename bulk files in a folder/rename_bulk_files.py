import os


def renamer():
    i = 0
    path = "D:/days of code/projects/blah blah/picture_folder/"
    for file_name in os.listdir(path):
        destn_name = "img" + str(i) + ".jpg"
        source_name = path + file_name
        destn_name = path + destn_name
        os.rename(source_name, destn_name)
        i += 1


renamer()

