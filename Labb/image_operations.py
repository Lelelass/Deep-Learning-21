import matplotlib.pyplot as plt 


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