import pandas as pd
import os
import json

folder_path = r"C:\Users\masum\Downloads\dataset_spoti\data"
file_name="mpd.slice.996000-996999"
data=[]
df=[]
data_new=[]
data_list=[]
data_tracks=pd.DataFrame()
data_file = os.path.join(folder_path, file_name)
print(data_file)
#d=pd.read_json(r"C:\Users\masum\Downloads\dataset_spoti\data\mpd.slice.1000-1999.json")


f = open(r"C:\Users\masum\Downloads\dataset_spoti\data\mpd.slice.1000-1999.json")
js = f.read()
f.close()
mpd_slice = json.loads(js)
#df = pd.json_normalize(mpd_slice["playlists"])

df = pd.json_normalize(mpd_slice, record_path=["playlists", "tracks"])

print(df)
# Save to CSV (optional)
data_new = pd.DataFrame(df)
print(f" tracks data = {data_new}")

#data_tracks["pos"] = data_new["tracks"].apply(lambda x: x["tracks"]["pos"])
print(type(data_new.to_numpy()))
data_new.to_csv(r"C:\Users\masum\OneDrive\Documents\research_data\final_data.csv", index=True, sep=',')

print("data read successfull")