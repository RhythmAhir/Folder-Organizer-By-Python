from os import listdir, mkdir
from os.path import isfile, join, exists

source_folder = '/Users/Administrator/Downloads'
item_list = listdir(source_folder)
extension_to_folder_mapper = {
    'jpeq jpg gif svg': 'images',
    'app dmg pkg exe': 'application',
    'txt xlsx xls doc docx pdf': 'documents',
    'py pyc whl sh': 'programming_files',
    'mp3': 'audio'
}


def get_file_extension(file_name):
    split_name = file_name.split('.')
    return split_name[-1]


def create_folder(name):
    if not exists(join(source_folder, name)):
        mkdir(join(source_folder, name))


def move_file_to_folder(file_name, folder_name):
    print("old path: ", join(source_folder, file_name))
    print("new path: ", join(source_folder, folder_name, file_name))


def map_extension_to_folder(extension, name):
    folder_name = 'others'
    for extension_list, destination_folder in extension_to_folder_mapper.iteritem():
        if extension in extension_list.split(' '):
            folder_name = destination_folder
            break

    create_folder(folder_name)
    move_file_to_folder(name, folder_name)


def main():
    for item_name in item_list:
        if isfile(join(source_folder, item_name)):
            extension = get_file_extension(item_name)
            map_extension_to_folder(extension, item_name)


main()
