import os, sys, json

BASE_DIR = "C:/Users/erfan/Desktop/WebDev_Master_Learning_Hub"
with open(os.path.join(BASE_DIR, "catalog.json"), "r", encoding="utf-8") as f:
    catalog = json.load(f)

print(f"Total catalog items: {len(catalog)}")
tracks = {}
for item in catalog:
    t = item["track"]
    tracks[t] = tracks.get(t, 0) + 1
print("Track counts:", tracks)
