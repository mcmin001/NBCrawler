import os


def mdkir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)


def write_to_file(text, file_path):
    f = open(file_path, "a", encoding='utf-8')
    f.write(text)
    f.close()
