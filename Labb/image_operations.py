def display_images(data, nrows=2, ncols=5, figsize=(12, 4)):

    fig, axes = plt.subplots(nrows, ncols, figsize = figsize)
    

    for i, ax in enumerate(axes.flatten()):
        filename = data.iloc[i,0]
        label = data.iloc[i,1] #Manage one hot encoding
        image = plt.imread(f"{original_train_dir}/{filename}")
        ax.imshow(image)
        ax.axis("off")
        if label == 0:
            ax.set_title('dog')
        else:
            ax.set_title('cat')


    fig.subplots_adjust(wspace=0.3, hspace=.1, bottom=0)