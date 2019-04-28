import pandas as pd
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.models import load_model
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder
import os
import numpy as np


df = pd.read_csv('faces.csv')
dataset = df.values

X = dataset[:,0:136]
Y = dataset[:,-1]
labels = [0 for x in range(9)]
new_Y = []
for index, cat in enumerate(Y):
    new_labels = labels.copy()
    new_labels[int(cat)] = 1
    new_Y.append(np.array(new_labels)) 

# ohe = OneHotEncoder(categories='auto', categorical_features = 'all')
# Y = ohe.fit_transform(Y).toarray()
new_Y = np.array(new_Y)
print(new_Y)


from sklearn import preprocessing

min_max_scaler = preprocessing.MinMaxScaler()
X_scale = min_max_scaler.fit_transform(X)

from sklearn.model_selection import train_test_split

# X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(X_scale, new_Y, test_size=0.2)
# X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size=0.2)
X_train, X_test, Y_train, Y_test = train_test_split(X_scale, new_Y, test_size=0.2)
# X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size=0.2)

model = None
if not os.path.isfile('./model.h5'):
    model = Sequential([
        Dense(32, activation='relu', input_shape=(136,)),
        Dense(128, activation='relu'),
        Dense(9, activation='softmax'),
    ])

    model.compile(optimizer='adam',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

    hist = model.fit(X_train, Y_train,
            batch_size=4, epochs=1000,
            validation_data=(X_test, Y_test))

    model.save("model.h5")

    # f,vs = plt.subplots(figsize = (8,7))
    # sns.heatmap(df.corr(), annot = True, fmt = '.1f', ax = vs)
    # plt.show()
else:
    new_model = load_model('model.h5')

    prediction=new_model.predict(X_test)
    print(prediction[0])


    #Accuracy
    test_loss, test_acc = new_model.evaluate(X_test, Y_test)
    print('Test accuracy:', test_acc)