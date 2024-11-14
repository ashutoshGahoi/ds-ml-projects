# Script for pulling data from Spotify API and others
import json
import requests
import base64
import time

# Spotify API credentials
CLIENT_ID = "117ea4b700524aadb3bf3a3b16f58890"
CLIENT_SECRET = "1d3334606fc149deae94e2ef644b02ac"

# Spotify URLs
AUTH_URL = "https://accounts.spotify.com/api/token"
BASE_URL = "https://api.spotify.com/v1/"

# generates an access token that authorizes API requests
def get_access_token():
    auth_response = requests.post(AUTH_URL, {
        'grant_type' = 'client_credentials',
        'client_id' = 'CLIENT_ID',
        'client_secret' = 'CLIENT_SECRET',
    })
    auth_response_data = auth_response.json()
    return auth_response_data['access_token']
    
