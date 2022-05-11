import pandas as pd
import os

def Complete_set_split_filenames(df, small_split:tuple):
    """Runs all the datasplits given user defined parameters"""
    small_train_sets_by_animal = []
    for animal in range(2):
        for split in small_split:
            small_train_sets_by_animal.append(select_sample_by_type(df, animal, split))
    
    small_train_set = pd.concat([small_train_sets_by_animal[0], small_train_sets_by_animal[3]], axis = 0)
    small_val_set = pd.concat([small_train_sets_by_animal[1], small_train_sets_by_animal[4]], axis = 0)
    small_test_set = pd.concat([small_train_sets_by_animal[2], small_train_sets_by_animal[5]], axis = 0)
    return small_train_set, small_val_set, small_test_set 

def get_filenames_from_path(path:str):
    pictures_filenames = os.listdir(path)
    return pictures_filenames

def gen_filename_dataframe(folder_files_list : list):
    """Reads a list of files in a folder and returns a dataframe with filenames,
     and corresponding animal label; one_hot encoded"""
    df = pd.DataFrame(folder_files_list, columns = ['filename'])
    #Add error hantering ?
    df['label'] = df.filename.str[:3] #Obs : only functions as 'cat' and 'dog' are both 3 char strings.
    df = pd.get_dummies(df, columns = ['label'], prefix=[''])
    return df


def select_sample_by_type(dataframe, animal:bool, sample_size:int, random_state=42):
    """Returns a datframe filtered by animal label and sampled to a specified quantity,
        the samples are also cleared from the original dataframe to avoid data leakage
        animal:  0 returns dog, 1 cat"""
    df = dataframe.query(f'_cat =={animal}')
    df = df.sample(n = sample_size,random_state = random_state)
    dataframe.drop(df.index, axis =0, inplace = True)
    return df