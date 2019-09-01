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

    def aggregate_mean():
        aggregated = {
            "anthony_score": float(album["anthony_score"]) / 10,
            "acousticness": 0,
            "danceability": 0,
            "duration_ms": 0,
            "energy": 0,
            "instrumentalness": 0,
            "key": 0,
            "liveness": 0,
            "loudness": 0,
            "mode": 0,
            "speechiness": 0,
            "tempo": 0,
            "time_signature": 0,
            "valence": 0,
        }

        for track_uri, track in album["tracks"].items():
            if track is not None:
                aggregated["acousticness"] += track["acousticness"]
                aggregated["danceability"] += track["danceability"]
                aggregated["duration_ms"] += track["duration_ms"]
                aggregated["energy"] += track["energy"]
                aggregated["instrumentalness"] += track["instrumentalness"]
                aggregated["key"] += track["key"]
                aggregated["liveness"] += track["liveness"]
                aggregated["loudness"] += track["loudness"]
                aggregated["mode"] += track["mode"]
                aggregated["speechiness"] += track["speechiness"]
                aggregated["tempo"] += track["tempo"]
                aggregated["time_signature"] += track["time_signature"]
                aggregated["valence"] += track["valence"]

        aggregated["acousticness"] /= len(album["tracks"])
        aggregated["danceability"] /= len(album["tracks"])
        aggregated["duration_ms"] /= len(album["tracks"])
        aggregated["energy"] /= len(album["tracks"])
        aggregated["instrumentalness"] /= len(album["tracks"])
        aggregated["key"] /= len(album["tracks"])
        aggregated["liveness"] /= len(album["tracks"])
        aggregated["loudness"] /= len(album["tracks"])
        aggregated["mode"] /= len(album["tracks"])
        aggregated["speechiness"] /= len(album["tracks"])
        aggregated["tempo"] /= len(album["tracks"])
        aggregated["time_signature"] /= len(album["tracks"])
        aggregated["valence"] /= len(album["tracks"])

        return aggregated

    def aggregate_meadian():
        aggregated = {
            "anthony_score": float(album["anthony_score"]) / 10,
            "acousticness": [],
            "danceability": [],
            "duration_ms": [],
            "energy": [],
            "instrumentalness": [],
            "key": [],
            "liveness": [],
            "loudness": [],
            "mode": [],
            "speechiness": [],
            "tempo": [],
            "time_signature": [],
            "valence": [],
        }

        for track_uri, track in album["tracks"].items():
            if track is not None:
                aggregated["acousticness"].append(track["acousticness"])
                aggregated["danceability"].append(track["danceability"])
                aggregated["duration_ms"].append(track["duration_ms"])
                aggregated["energy"].append(track["energy"])
                aggregated["instrumentalness"].append(track["instrumentalness"])
                aggregated["key"].append(track["key"])
                aggregated["liveness"].append(track["liveness"])
                aggregated["loudness"].append(track["loudness"])
                aggregated["mode"].append(track["mode"])
                aggregated["speechiness"].append(track["speechiness"])
                aggregated["tempo"].append(track["tempo"])
                aggregated["time_signature"].append(track["time_signature"])
                aggregated["valence"].append(track["valence"])

        aggregated["acousticness"] = statistics.median(aggregated["acousticness"])
        aggregated["danceability"] = statistics.median(aggregated["danceability"])
        aggregated["duration_ms"] = statistics.median(aggregated["duration_ms"])
        aggregated["energy"] = statistics.median(aggregated["energy"])
        aggregated["instrumentalness"] = statistics.median(
            aggregated["instrumentalness"]
        )
        aggregated["key"] = statistics.median(aggregated["key"])
        aggregated["liveness"] = statistics.median(aggregated["liveness"])
        aggregated["loudness"] = statistics.median(aggregated["loudness"])
        aggregated["mode"] = statistics.median(aggregated["mode"])
        aggregated["speechiness"] = statistics.median(aggregated["speechiness"])
        aggregated["tempo"] = statistics.median(aggregated["tempo"])
        aggregated["time_signature"] = statistics.median(aggregated["time_signature"])
        aggregated["valence"] = statistics.median(aggregated["valence"])

        return aggregated

    # aggregated = aggregate_mean()
    aggregated = aggregate_meadian()

    features.append([aggregated["danceability"], aggregated["instrumentalness"]])
    labels.append([aggregated["anthony_score"]])

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

model.fit(features[0:1510], labels[0:1510], epochs=100, verbose=2)

for feature, label in zip(features[1510:1528], labels[1510:1528]):
    print(model.predict(np.array([feature])))
    print(label)

