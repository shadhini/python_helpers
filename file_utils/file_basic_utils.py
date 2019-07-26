import os


def write_to_file(file_name, data):
    """
    Write to file (w+, if there's no such file, a file would be created)
    :param file_name: file_path/file_name
    :param data:
    :return:
    """
    with open(file_name, 'w+') as f:
        f.write('\n'.join(data))


def append_to_file(file_name, data):

    """
    Append to file (a+, if there's no such file, a file would be created)
    :param file_name: file_path/file_name
    :param data:
    :return:
    """
    with open(file_name, 'a+') as f:
        f.write('\n'.join(data))


def insert(originalfile,string):
    with open(originalfile,'r') as f:
        with open('newfile.txt','w') as f2:
            f2.write(string)
            f2.write(f.read())
    os.rename('newfile.txt',originalfile)


def create_csv_like_txt(file_name, data):
    """
    Create txt file in the format of csv file
    :param file_name: file_path/file_name
    :param data: list of lists
    :return:
    """
    with open(file_name, 'w') as f:
        for _list in data:
            for i in range(len(_list)-1):
                #f.seek(0)
                f.write(str(_list[i]) + ',')
            f.write(str(_list[len(_list)-1]))
            f.write('\n')

        f.close()

