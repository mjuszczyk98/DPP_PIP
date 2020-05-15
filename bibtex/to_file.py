def to_new_file(path_to_file, data):
    try:
        file = open(path_to_file, "x")
        file.write(data)
        file.close()
    except Exception as e:
        return e


def append_file(path_to_file, data):
    try:
        file = open(path_to_file, "a")
        file.write(data)
        file.close()
    except Exception as e:
        return e
