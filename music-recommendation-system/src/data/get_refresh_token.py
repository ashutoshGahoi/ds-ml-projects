from ..config.settings import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
import requests

AUTH_URL = "https://accounts.spotify.com/api/token"

AUTH_CODE = "AQD-1lzmka23R-IT86-33Mk9e_6rnzcTbyQIEGzusdLfG_cbyIjawIVZ__eue5Jc_hkgqWoLi1kg5mvxvwq70NPteJ5CTqAXZONPpsylfr3BxwUQOM_vCpBfwRd-wxicv6DYIw45dM6F_wMMUxZHUKymJpcy1wgnwzKxzAmmEaebUbyZXLrUVWQ"


def get_tokens(auth_code, client_id, client_secret, redirect_uri):
    response = requests.post(
        AUTH_URL,
        data={
            "grant_type": "authorization_code",
            "code": auth_code,
            "redirect_uri": redirect_uri,
            "client_id": client_id,
            "client_secret": client_secret,
        },
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    tokens = get_tokens(AUTH_CODE, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
    print("Access Token:", tokens["access_token"])
    print("Refresh Token:", tokens["refresh_token"])
