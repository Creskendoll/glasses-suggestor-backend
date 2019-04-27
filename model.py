import pandas as pd
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.models import load_model
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv('housepricedata.csv')
dataset = df.values

X = dataset[:,0:10]
Y = dataset[:,10]

from sklearn import preprocessing

min_max_scaler = preprocessing.MinMaxScaler()
X_scale = min_max_scaler.fit_transform(X)

from sklearn.model_selection import train_test_split

X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(X_scale, Y, test_size=0.3)
X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size=0.5)

model = None
if not os.path.isfile('./model.h5'):
    model = Sequential([
        Dense(32, activation='relu', input_shape=(10,)),
        Dense(32, activation='relu'),
        Dense(1, activation='sigmoid'),
    ])

    model.compile(optimizer='sgd',
                loss='binary_crossentropy',
                metrics=['accuracy'])

    hist = model.fit(X_train, Y_train,
            batch_size=32, epochs=100,
            validation_data=(X_val, Y_val))


    f,vs = plt.subplots(figsize = (8,7))
    sns.heatmap(df.corr(), annot = True, fmt = '.1f', ax = vs)
    plt.show()

    model.save("model.h5")

else:
    new_model = load_model('model.h5')

    prediction=new_model.predict(X_test)
    print(prediction[0])


    #Accuracy
    test_loss, test_acc = new_model.evaluate(X_val_and_test, Y_val_and_test)
    print('Test accuracy:', test_acc)