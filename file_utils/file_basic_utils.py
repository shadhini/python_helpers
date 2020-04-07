import os
import traceback


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


def read_file(file_name):
    """
    Read content from a file
    :param file_name: file_path/file_name
    :return: return the whole content of the file
    """

    with open(file_name, 'r') as f:
        content = f.read()

    return content


def read_file_line_by_line(file_name):
    """
    Read file content line by line
    :param file_name: file_path/file_name
    :return: return the lines of the file content as a list
    """

    lines = []

    with open(file_name, 'r') as f:
        content = f.readlines()

        for line in content:
            lines.append(line)

    return lines


def read_last_line(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        return lines[-1]


def is_file_exist(file_path):
    if not os.path.exists(file_path):
        print('Unable to find file : ', file_path)
        traceback.print_exc()
        exit(1)