
import os
import json
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras import optimizers
from tensorflow.keras import layers
from tensorflow.keras.utils import plot_model
import graphviz

# Hyperparametres
n_epochs = 1
batch_size = 32
optimizer = 'adadelta'


def do():
    train_data_dir = "Dataset"
    train_data_dir_gt = "Dataset/gt"
    data = []
    gt_data = []

    os.chdir(train_data_dir)
    for file in os.listdir():
        if file.endswith(".json"):
            with open(file, 'r') as f:
                d = json.load(f)  # returns JSON object as a dictionary
                data = data + d

    os.chdir(train_data_dir_gt)
    for file in os.listdir():
        with open(file, 'r') as f:
            d = json.load(f)
            gt_data = gt_data + d

    # Divide data in train-val-test
    X_train, x_test, Y_train, y_test = train_test_split(data, gt_data, test_size=0.2)
    x_train, x_val, y_train, y_val = train_test_split(X_train, Y_train, test_size=0.25)  # 0.25 x 0.8 = 0.2
    x_length = len(x_train[0])
    y_length = len(y_train[0])

    optimizer = optimizers.SGD(learning_rate=0.0001, momentum=0.5)

    # Creation of the model
    model = Sequential()
    model.add(layers.Dense(256, activation="relu", input_dim=x_length, name="layer1"))
    model.add(layers.Dense(512, activation='relu', name="layer2"))
    model.add(layers.Dense(512, activation='relu', name="layer3"))
    model.add(layers.Dense(y_length, activation='linear', name="layer_out"))

    model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
    model.summary()
    plot_model(model, to_file='model.png', show_shapes=True, show_layer_names=True)

    # Fit data to model
    model.fit(x_train, y_train,
              batch_size=batch_size,
              epochs=n_epochs,
              validation_data=(x_val, y_val)
              )

    # Evaluation
    loss_and_metrics = model.evaluate(x_test, y_test, batch_size=batch_size)
    print('Loss: ' + str(loss_and_metrics[0]) + '    Accuracy: ' + str(loss_and_metrics[1]))

    # Compute and store the result
    # TODO Use the data from the webcam
    result = model.predict(x_test, batch_size=batch_size)

    with open("results.json", 'w') as file:
        json.dump(result.tolist(), file, indent=4)


if __name__ == '__main__':
    do()
