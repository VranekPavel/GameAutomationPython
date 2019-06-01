def read_file(file_name):
    file = open("../resources/" + file_name)
    villages = file.readlines()
    file.close()
    return villages