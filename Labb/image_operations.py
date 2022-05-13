import matplotlib.pyplot as plt 
import seaborn as sns
import cv2
import numpy as np

def display_images(filenames_dataframe, directory:str, nrows=2, ncols=5, figsize=(12, 4)):

    fig, axes = plt.subplots(nrows, ncols, figsize = figsize)
    

    for i, ax in enumerate(axes.flatten()):
        filename = filenames_dataframe.iloc[i,0]
        label = filenames_dataframe.iloc[i,1] #Manage one hot encoding
        image = plt.imread(f"{directory}/{filename}")
        ax.imshow(image)
        ax.axis("off")
        if label == 0:
            ax.set_title('dog')
        else:
            ax.set_title('cat')


    fig.subplots_adjust(wspace=0.3, hspace=.1, bottom=0)

def display_images_array(array, nrows=2, ncols=5, figsize=(12, 4)):

    fig, axes = plt.subplots(nrows, ncols, figsize = figsize)
    
    for i, ax in enumerate(axes.flatten()):
        ax.imshow(array[i])
        ax.axis("off")


def extract_dimesion_distribution(df, directory:str):
    """Reads pictures from filepath column of dataframe,
       extracts width and height pixel values and scatter plots.
       Also returns a list of picture sizes tuples, and of large pictures"""
    all_dims =[]
    big_img = []
    for i, path in df['filename'].items():
        img = plt.imread(f"{directory}/{path}")
        all_dims.append((img.shape[0], img.shape[1]))
        if img.shape[0] > 700 or img.shape[1] > 700:
            big_img.append(df['filename'][i])
    
    #sns.jointplot(data=train_pictures_one_hot_with_dim, x='width', y='height')
    #plt.scatter(*zip(*all_dims))
    #plt.show()
    print(f"oversized pictures : {big_img}")
    return all_dims, big_img

def read_and_resize_images(df, directory:str, target_size:tuple):
    images = []
    for _, path in df['filename'].items():
        img = plt.imread(f"{directory}/{path}")
        img = cv2.resize(img, target_size)
        images.append(img)
    resized_images_array = np.array(images)
    return resized_images_array