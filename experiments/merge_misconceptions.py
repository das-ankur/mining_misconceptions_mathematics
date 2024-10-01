# Import libraries
import pandas as pd
from tqdm import tqdm



# Read data and misconceptions
df = pd.read_csv('raw_data/train.csv')
mis_df = pd.read_csv('raw_data/misconception_mapping.csv')

# Map misconceptions
# Merge data
res = []
for row in tqdm(df.to_dict(orient='records'), desc='Merging', total=df.shape[0]):
    row['MisconceptionAText'] = row['MisconceptionBText'] = row['MisconceptionCText'] = row['MisconceptionDText'] = ''
    if not pd.isna(row['MisconceptionAId']):
        row['MisconceptionAText'] = mis_df[mis_df['MisconceptionId']==int(row['MisconceptionAId'])]['MisconceptionName']
    if not pd.isna(row['MisconceptionBId']):
        row['MisconceptionBText'] = mis_df[mis_df['MisconceptionId']==int(row['MisconceptionBId'])]['MisconceptionName']
    if not pd.isna(row['MisconceptionCId']):
        row['MisconceptionCText'] = mis_df[mis_df['MisconceptionId']==int(row['MisconceptionCId'])]['MisconceptionName']
    if not pd.isna(row['MisconceptionDId']):
        row['MisconceptionDText'] = mis_df[mis_df['MisconceptionId']==int(row['MisconceptionDId'])]['MisconceptionName']
    res.append(row)
res = pd.DataFrame(res)

# Save data
res.to_csv('processed_data/data.csv', index=False)