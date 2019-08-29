from colorama import Back, Fore, Style
from yaspin import yaspin
from utils.better_pprint import pprint
import sys
import requests
import sys


def get_audio_features(track_id, credentials, abort_on_error=True):
    with yaspin(
        side="right",
        text=Fore.YELLOW
        + "    GET https://api.spotify.com/v1/audio-features/{}".format(track_id)
        + Style.RESET_ALL,
        color="yellow",
    ) as spinner:
        res = requests.get(
            "https://api.spotify.com/v1/audio-features/{}".format(track_id),
            headers={"Authorization": "Bearer {}".format(credentials["access_token"])},
        )
        if res.ok:
            spinner.text = (
                Fore.GREEN
                + "    GET https://api.spotify.com/v1/audio-features/{}".format(
                    track_id
                )
                + Style.RESET_ALL
            )
            spinner.color = "green"
            spinner.ok("✓")
            return res.json()
        else:
            spinner.text = (
                Fore.RED
                + "    GET https://api.spotify.com/v1/audio-features/{}".format(
                    track_id
                )
                + Style.RESET_ALL
            )
            spinner.color = "red"
            spinner.fail("✗")

            print()
            print(
                Fore.RED
                + "     [{0}] {1}".format(res.status_code, res.reason)
                + Style.RESET_ALL
            )
            pprint(res.json(), color=Fore.RED)
            print()
            print()

            if abort_on_error:
                print(Fore.RED + "    Aborting!" + Style.RESET_ALL)
                sys.exit(1)
