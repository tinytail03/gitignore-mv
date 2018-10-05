import os

########## generator setting ##########

# project folder path
path = '.'

# list of directories that must not be ignored
exclude_dir_list = [
    '.git',
    'data',
    'fonts',
    'icon',
    'img/system',
    'js/plugins'
]

# list of files that must not be ignored
exclude_file_list = [
    '.gitignore',
    'generator.py',
    'Game.rpgproject' # to check tool version
]

########## generator process ##########

# open gitignore file
gitignore = open(os.path.join(path, '.gitignore'), 'w')

# for each root
for root, dir_list, file_list in os.walk(path):

    # skip if root must be excluded
    if any(exclude_dir in root for exclude_dir in exclude_dir_list):
        continue

    # for each file in root
    for file in file_list:

        # skip if file must be excluded
        if file in exclude_file_list:
            continue

        # write file path in gitignore file
        file_path = os.path.join(root, file)
        gitignore.write(file_path[len(path):] + "\n")

# close gitignore file
gitignore.close()
