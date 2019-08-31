from api.audio_features import get_audio_features
from api.credentials import get_credentials
from api.tracks_of_album import get_tracks_of_album
from colorama import init as colorama_init
from colorama import Back, Fore, Style
from utils.better_pprint import pprint
import csv
import json
import sys

colorama_init()
print()

sys.argv.pop(0)
sys.argv.pop(0)
print(Fore.GREEN + "    Data:" + Style.RESET_ALL)
i = 1
for row in csv.reader(sys.argv[0:10], delimiter=","):
    print(Fore.GREEN + "     [{}]: ".format(i) + Style.RESET_ALL + str(row))
    i += 1

if len(sys.argv) > 10:
    print(Fore.GREEN + "     ..." + Style.RESET_ALL)

print()
print()

print(Fore.GREEN + "    Continue? [y/n]: " + Style.RESET_ALL, end="")
confirm = input()

if confirm.lower() != "y":
    print(Fore.RED + "    Aborting!" + Style.RESET_ALL)
    sys.exit(1)
else:
    print()
    print()

print(
    Fore.YELLOW
    + "    [HINT] Create your Client ID at https://developer.spotify.com/dashboard"
    + Style.RESET_ALL
)
print(Fore.GREEN + "    Client ID: " + Style.RESET_ALL, end="")
client_id = input()

print(Fore.GREEN + "    Client Secret: " + Style.RESET_ALL, end="")
client_secret = input()
print()
print()

credentials = get_credentials(client_id, client_secret)

output = {}

albums_count = 0
tracks_count = 0
for row in csv.reader(sys.argv, delimiter=","):
    albums_count += 1

    output[row[2]] = {}
    output[row[2]]["album_name"] = row[0]
    output[row[2]]["artist"] = row[1]
    output[row[2]]["tracks"] = {}
    output[row[2]]["credit"] = row[3]
    output[row[2]]["anthony_score"] = row[4]

    print()
    print(
        Fore.GREEN
        + "    [{}/{}] Album: {} by {}.".format(
            albums_count, len(sys.argv), row[0], row[1]
        )
        + Style.RESET_ALL
    )
    tracks = get_tracks_of_album(
        row[2].split(":")[2], credentials, abort_on_error=False
    )
    if "error" not in tracks:
        print(
            Fore.GREEN
            + "     → Got tracks! {} tracks present.".format(len(tracks))
            + Style.RESET_ALL
        )
        tracks_count += len(tracks)
        i = 0
        for track in tracks:
            i += 1
            output[row[2]]["tracks"][track["uri"]] = get_audio_features(
                track["uri"].split(":")[2], credentials, abort_on_error=False, index=i
            )

print()
print()
print(
    Fore.GREEN
    + "     ☮ {0} tracks found! {1} albums searched! ☮".format(
        tracks_count, albums_count
    )
    + Style.RESET_ALL
)
print()

with open("output.json", "w") as file:
    json.dump(output, file)
