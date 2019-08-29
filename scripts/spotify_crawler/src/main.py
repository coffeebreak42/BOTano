from api.audio_features import get_audio_features
from api.credentials import get_credentials
from colorama import init as colorama_init
from colorama import Back, Fore, Style
from utils.better_pprint import pprint
import csv
import json
import sys

colorama_init()
print()

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

features = {}

for row in csv.reader(sys.argv, delimiter=","):
    features[row[0]] = get_audio_features(row[0], credentials, abort_on_error=False)

print()
print()
pprint(features)

print()
print()
print(Fore.GREEN + "    Generated JSON: " + Style.RESET_ALL)
print(json.dumps(features))
print()
