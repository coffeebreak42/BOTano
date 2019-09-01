import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')

from pprint import pprint
from sklearn import linear_model
import json
import pandas as pd
import statistics

with open("/data/input", "r") as file:
    data = json.load(file)

columns = {
    "anthony_score": [],
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
for album_uri, album in data.items():
    for track_uri, track in album["tracks"].items():
        if track is not None:
            columns["anthony_score"].append(float(album["anthony_score"]) / 10)
            columns["acousticness"].append(track["acousticness"])
            columns["danceability"].append(track["danceability"])
            columns["duration_ms"].append(track["duration_ms"])
            columns["energy"].append(track["energy"])
            columns["instrumentalness"].append(track["instrumentalness"])
            columns["key"].append(track["key"])
            columns["liveness"].append(track["liveness"])
            columns["loudness"].append(track["loudness"])
            columns["mode"].append(track["mode"])
            columns["speechiness"].append(track["speechiness"])
            columns["tempo"].append(track["tempo"])
            columns["time_signature"].append(track["time_signature"])
            columns["valence"].append(track["valence"])

df = pd.DataFrame(columns)
pprint(df)

print('"anthony_score" corr {} with "acousticness"'.format(df["anthony_score"].corr(df["acousticness"])))
print('"anthony_score" corr {} with "danceability"'.format(df["anthony_score"].corr(df["danceability"])))
print('"anthony_score" corr {} with "duration_ms"'.format(df["anthony_score"].corr(df["duration_ms"])))
print('"anthony_score" corr {} with "energy"'.format(df["anthony_score"].corr(df["energy"])))
print('"anthony_score" corr {} with "instrumentalness"'.format(df["anthony_score"].corr(df["instrumentalness"])))
print('"anthony_score" corr {} with "key"'.format(df["anthony_score"].corr(df["key"])))
print('"anthony_score" corr {} with "liveness"'.format(df["anthony_score"].corr(df["liveness"])))
print('"anthony_score" corr {} with "loudness"'.format(df["anthony_score"].corr(df["loudness"])))
print('"anthony_score" corr {} with "mode"'.format(df["anthony_score"].corr(df["mode"])))
print('"anthony_score" corr {} with "speechiness"'.format(df["anthony_score"].corr(df["speechiness"])))
print('"anthony_score" corr {} with "tempo"'.format(df["anthony_score"].corr(df["tempo"])))
print('"anthony_score" corr {} with "time_signature"'.format(df["anthony_score"].corr(df["time_signature"])))
print('"anthony_score" corr {} with "valence"'.format(df["anthony_score"].corr(df["valence"])))

Y = df["anthony_score"]

model = linear_model.LinearRegression()
model.fit(df[["acousticness"]], Y)
print('R-squared {} using "acousticness"'.format(model.score(df[["acousticness"]], Y)))
model.fit(df[["danceability"]], Y)
print('R-squared {} using "danceability"'.format(model.score(df[["danceability"]], Y)))
model.fit(df[["duration_ms"]], Y)
print('R-squared {} using "duration_ms"'.format(model.score(df[["duration_ms"]], Y)))
model.fit(df[["energy"]], Y)
print('R-squared {} using "energy"'.format(model.score(df[["energy"]], Y)))
model.fit(df[["instrumentalness"]], Y)
print('R-squared {} using "instrumentalness"'.format(model.score(df[["instrumentalness"]], Y)))
model.fit(df[["key"]], Y)
print('R-squared {} using "key"'.format(model.score(df[["key"]], Y)))
model.fit(df[["liveness"]], Y)
print('R-squared {} using "liveness"'.format(model.score(df[["liveness"]], Y)))
model.fit(df[["loudness"]], Y)
print('R-squared {} using "loudness"'.format(model.score(df[["loudness"]], Y)))
model.fit(df[["mode"]], Y)
print('R-squared {} using "mode"'.format(model.score(df[["mode"]], Y)))
model.fit(df[["speechiness"]], Y)
print('R-squared {} using "speechiness"'.format(model.score(df[["speechiness"]], Y)))
model.fit(df[["tempo"]], Y)
print('R-squared {} using "tempo"'.format(model.score(df[["tempo"]], Y)))
model.fit(df[["time_signature"]], Y)
print('R-squared {} using "time_signature"'.format(model.score(df[["time_signature"]], Y)))
model.fit(df[["valence"]], Y)
print('R-squared {} using "valence"'.format(model.score(df[["valence"]], Y)))

print()
print('"danceability" and "instrumentalness" are the best candidates')
print()

X = df[["danceability", "instrumentalness"]]
model.fit(X, Y)

print('R-squared {} using "danceability" and "instrumentalness"'.format(model.score(X, Y)))

print("Bad linear model, only explains %.2f%% of the data" % (model.score(X, Y) * 100))

ax = df.plot.scatter(x='acousticness', y='anthony_score', c='DarkBlue')
fig = ax.get_figure()
fig.savefig('/app/images/acousticness.png')
ax = df.plot.scatter(x='danceability', y='anthony_score', c='DarkBlue')
fig = ax.get_figure()
fig.savefig('/app/images/danceability.png')
ax = df.plot.scatter(x='duration_ms', y='anthony_score', c='DarkBlue')
fig = ax.get_figure()
fig.savefig('/app/images/duration_ms.png')
ax = df.plot.scatter(x='energy', y='anthony_score', c='DarkBlue')
fig = ax.get_figure()
fig.savefig('/app/images/energy.png')
ax = df.plot.scatter(x='instrumentalness', y='anthony_score', c='DarkBlue')
fig = ax.get_figure()
fig.savefig('/app/images/instrumentalness.png')
ax = df.plot.scatter(x='key', y='anthony_score', c='DarkBlue')
fig = ax.get_figure()
fig.savefig('/app/images/key.png')
ax = df.plot.scatter(x='liveness', y='anthony_score', c='DarkBlue')
fig = ax.get_figure()
fig.savefig('/app/images/liveness.png')
ax = df.plot.scatter(x='loudness', y='anthony_score', c='DarkBlue')
fig = ax.get_figure()
fig.savefig('/app/images/loudness.png')
ax = df.plot.scatter(x='mode', y='anthony_score', c='DarkBlue')
fig = ax.get_figure()
fig.savefig('/app/images/mode.png')
ax = df.plot.scatter(x='speechiness', y='anthony_score', c='DarkBlue')
fig = ax.get_figure()
fig.savefig('/app/images/speechiness.png')
ax = df.plot.scatter(x='tempo', y='anthony_score', c='DarkBlue')
fig = ax.get_figure()
fig.savefig('/app/images/tempo.png')
ax = df.plot.scatter(x='time_signature', y='anthony_score', c='DarkBlue')
fig = ax.get_figure()
fig.savefig('/app/images/time_signature.png')
ax = df.plot.scatter(x='valence', y='anthony_score', c='DarkBlue')
fig = ax.get_figure()
fig.savefig('/app/images/valencee.png')