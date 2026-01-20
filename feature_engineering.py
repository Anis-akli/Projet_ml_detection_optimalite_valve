import pandas as pd

def extract_features(df):
    features = {}

    sensor_groups = {
        "VS1": ["VS1"],
        "PS1": ["PS1"],
        "PS2": ["PS2"],
        "PS3": ["PS3"],
        "PS5": ["PS5"],
        "PS6": ["PS6"],
        "FS1": ["FS1"],
        "FS2": ["FS2"],
        "TS1": ["TS1"],
        "TS2": ["TS2"],
        "TS3": ["TS3"],
        "TS4": ["TS4"],
        "EPS1": ["EPS1"],
        "CE": ["CE"],
        "CP": ["CP"],
        "SE": ["SE"]
    }

    for sensor, cols in sensor_groups.items():
        for col in cols:
            if col in df.columns:
                features[f"{sensor}_mean"] = df[col].mean()
                features[f"{sensor}_std"] = df[col].std()
                features[f"{sensor}_max"] = df[col].max()
                features[f"{sensor}_median"] = df[col].median()

    return pd.DataFrame([features])
