# Functions for data cleaning and feature engineering


def normalize_audio_features(data):
    # Normalize features like tempo, loudness, etc.
    for track in data:
        track["normalized_tempo"] = track["tempo"] / 200  # Example normalization
    return data
