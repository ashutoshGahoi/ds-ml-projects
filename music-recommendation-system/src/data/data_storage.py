from pymongo import MongoClient
from src.config.settings import MONGO_URI

client = MongoClient(MONGO_URI)
db = client.spotify_data


# This function stores track data into the 'tracks' collection
def store_track_data(track_data):
    """
    This function takes a track's data (including metadata and features)
    and stores it in MongoDB in the 'tracks' collection.
    """
    try:
        # Access the 'tracks' collection in the 'spotify_data' database
        tracks_collection = db.tracks

        # Insert data into the collection
        result = tracks_collection.insert_one(track_data)
        print(f"Data inserted with id {result.inserted_id}")
    except Exception as e:
        print(f"Error storing data: {e}")


if __name__ == "__main__":
    # Example data - in a real scenario, this data would come from the API
    example_track_data = {
        "id": "track123",
        "name": "Example Song",
        "artist": "Example Artist",
        "genre": "Pop",
        "danceability": 0.7,
        "energy": 0.8,
        "tempo": 120,
        "valence": 0.6,
    }

    # Store example data
    store_track_data(example_track_data)
