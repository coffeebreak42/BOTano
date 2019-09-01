from pprint import pprint
import json
import numpy as np
import statistics
import tensorflow as tf

with open("/data/input", "r") as file:
    data = json.load(file)

features = []
labels = []
for album_uri, album in data.items():
    for track_uri, track in album["tracks"].items():
        if track is not None:
            features.append([track["danceability"], track["instrumentalness"]])
            labels.append([float(album["anthony_score"]) / 10])

features = np.array(features)
labels = np.array(labels)

model = tf.keras.Sequential(
    [
        tf.keras.layers.Dense(units=4, activation="sigmoid", input_shape=(2,)),
        tf.keras.layers.Dense(units=9, activation="sigmoid"),
        tf.keras.layers.Dense(units=1, activation="sigmoid"),
    ]
)

model.compile(loss="mean_squared_error", optimizer=tf.keras.optimizers.Adam(0.05))

model.fit(features[0:18000], labels[0:18000], epochs=100, verbose=1)

for feature, label in zip(features[18000:], labels[18000:]):
    print(model.predict(np.array([feature])))
    print(label)



