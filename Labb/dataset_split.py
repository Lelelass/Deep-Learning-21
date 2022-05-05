import pandas as pd
import os

def Complete_split(df):
    animals = ('dog', 'cat')
    for animal in animals:
        select_sample_by_type(df, animal, 800)

def get_train_from_path():
    original_train_dir = os.path.abspath("./original_data/train/train")
    train_pictures = os.listdir(original_train_dir)
    return train_pictures

def get_filename_dataframe(folder_files_list : list):
    df = pd.DataFrame(folder_files_list, columns = ['filename'])
    df['label'] = df.filename.str[:3]
    return df

def Read_and_one_hot_dataframe(dataframe):

    pd.get_dummies(df, columns = ['label'])
    pass

def select_sample_by_type(dataframe, animal:str, sample_size:int, random_state=42):
    """Returns a datframe filtered by animal label and sampled to a specified quantity,
        the samples are also cleared from the original dataframe to avoid data leakage"""
    df = dataframe.query(f'label =="{animal}"')
    df = df.sample(n = sample_size,random_state = random_state)
    dataframe.drop(df.index, axis =0, inplace = True)
    return df