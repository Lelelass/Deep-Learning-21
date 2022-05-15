from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.optimizers import Adam, RMSprop


def CNN_model_1(input_shape : tuple, learning_rate=.001, drop_rate=.3, kernels=[32, 64,128,128]):
    adam = Adam(learning_rate=learning_rate)

    model = Sequential(name="CNN_model")

    # the convolutional layers
    for number_kernel in kernels:
        conv_layer = Conv2D(number_kernel, kernel_size=(
            3, 3), activation="relu", kernel_initializer="he_normal",
            input_shape=input_shape[1:])
        
        model.add(conv_layer)
        model.add(MaxPooling2D(pool_size = (2,2), strides = 2))
    
    # MLP layers
    model.add(Flatten())
    model.add(Dropout(drop_rate))
    model.add(Dense(512, activation = "relu", kernel_initializer = "he_normal"))
    model.add(Dense(1, activation = "sigmoid"))

    model.compile(loss = "binary_crossentropy", optimizer = adam, metrics = ["acc"])

    return model


def CNN_model_2(input_shape : tuple, learning_rate=.001, drop_rate=.3, kernels=[32, 64,128,128]):
    rms = RMSprop(learning_rate=learning_rate)

    model = Sequential(name="CNN_model")

    # the convolutional layers
    for number_kernel in kernels:
        conv_layer = Conv2D(number_kernel, kernel_size=(
            3, 3), activation="relu", kernel_initializer="he_normal",
            input_shape=input_shape[1:])
        
        model.add(conv_layer)
        model.add(MaxPooling2D(pool_size = (2,2), strides = 2))

    # MLP layers
    model.add(Flatten())
    model.add(Dropout(drop_rate))
    model.add(Dense(512, activation = "relu", kernel_initializer = "he_normal"))
    model.add(Dense(1, activation = "sigmoid"))

    model.compile(loss = "binary_crossentropy", optimizer = rms, metrics = ["acc"])

    return model


