import os
import pandas as pd
import numpy as np
import json

# Define the folder containing JSON files
path=r"C:\Users\masum\OneDrive\Documents\research_data\dataset_spoti\data_10_files"
data=[]
data_new=[]
count=0
filenames = os.listdir(path)
print("data is loading.....")
for filename in sorted(filenames):
    if filename.startswith("mpd.slice.") and filename.endswith(".json"):
        fullpath = os.sep.join((path, filename))
        f = open(fullpath)
        js = f.read()
        f.close()
        mpd_slice = json.loads(js)
        #mpd_slice = json.loads(js)
        df = pd.json_normalize(mpd_slice, record_path=["playlists", "tracks"])
        data_new = pd.DataFrame(df)
        if len(data) == 0:
            print("The list is empty.")
            #data=pd.DataFrame(data)
            data=data_new.copy()
            count=count+1
            print(f"No.of files: {count}")
        else:
            data = pd.concat([data, data_new], axis=0)
            count=count+1
            print(f"No.of files: {count}")
        
    #print(type(data_new))
    #data.append(data_new)
    #data=pd.concat([np.array(data), np.array(data_new)], axis=0)
print(type(data))
#revised_data=data.copy()
# Save to CSV (optional)
#data_new = pd.DataFrame(data)
#revised_data=pd.DataFrame(data)
data.to_csv(r"C:\Users\masum\OneDrive\Documents\research_data\final_data_new.csv", index=False)
print("Data read and save successfully")


