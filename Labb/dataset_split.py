import pandas as pd

def Complete_split(df):
    animals = ('dog', 'cat')
    for animal in animals:
        select_sample_by_type(df, animal, 800)

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