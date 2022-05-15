import os
import re



main_dir = os.path.abspath("")

subsplit = [
    'train',
    'val',
    'test'
]

dirs = ['experiment_small_data', 'experiment_tiny_data', 'original_data']



for dir in dirs:
    data_subpath = f"{main_dir}/{dir}"

    try:
        os.mkdir(data_subpath)
        if 'experiment' in data_subpath:
            for path in subsplit:
                    os.makedirs(f"/{data_subpath}/{path}")
        else :
            for path in subsplit[:2]:
                os.makedirs(f"/{data_subpath}/{path}/{path}")


    except FileExistsError as err:
        print(err)

