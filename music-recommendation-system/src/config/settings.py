# Stores API credentials and other configurations

import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")  # Spotify Client ID
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")  # Spotify Client Secret
REFRESH_TOKEN = os.getenv("SPOTIFY_REFRESH_TOKEN")
REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")
BASE_URL = "https://api.spotify.com/v1/"
AUTH_URL = "https://accounts.spotify.com/api/token"
MONGO_URI = os.getenv("MONGO_URI")  # MongoDB URI for data storage


# Print to verify (optional - remove in production)
print(f"CLIENT_ID: {CLIENT_ID}")
print(f"MONGO_URI: {MONGO_URI}")
