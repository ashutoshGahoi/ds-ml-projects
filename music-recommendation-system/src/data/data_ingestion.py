# Fetch data from Spotify API
from ..config.settings import CLIENT_ID, CLIENT_SECRET, BASE_URL, REFRESH_TOKEN
from ..utils.api_helper import get_access_token_from_refresh, api_get_request
from .data_storage import store_track_data


def fetch_top_tracks(user_id):
    token = get_access_token_from_refresh(REFRESH_TOKEN, CLIENT_ID, CLIENT_SECRET)
    url = f"{BASE_URL}me/top/tracks"
    return api_get_request(url, token)


def fetch_track_features(track_id):
    token = get_access_token_from_refresh(REFRESH_TOKEN, CLIENT_ID, CLIENT_SECRET)
    url = f"{BASE_URL}audio-features/{track_id}"
    return api_get_request(url, token)


if __name__ == "__main__":
    user_id = "example_user_id"  # Replace with the actual user ID
    top_tracks = fetch_top_tracks(user_id)
    for track in top_tracks["items"]:
        track_id = track["id"]
        features = fetch_track_features(track_id)
        store_track_data({**track, **features})
