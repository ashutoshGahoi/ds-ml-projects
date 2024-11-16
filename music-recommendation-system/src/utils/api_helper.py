# Utility functions for API interactions
import requests
import os

AUTH_URL = "https://accounts.spotify.com/api/token"

AUTH_CODE = "AQD-1lzmka23R-IT86-33Mk9e_6rnzcTbyQIEGzusdLfG_cbyIjawIVZ__eue5Jc_hkgqWoLi1kg5mvxvwq70NPteJ5CTqAXZONPpsylfr3BxwUQOM_vCpBfwRd-wxicv6DYIw45dM6F_wMMUxZHUKymJpcy1wgnwzKxzAmmEaebUbyZXLrUVWQ"


def get_token(auth_code, client_id, client_secret, redirect_uri):
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


def get_access_token_from_refresh(refresh_token, client_id, client_secret):
    response = requests.post(
        AUTH_URL,
        data={
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": client_id,
            "client_secret": client_secret,
        },
    )
    response.raise_for_status()
    return response.json()["access_token"]


def api_get_request(url, token, params=None):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()
