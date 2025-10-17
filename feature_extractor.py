import pandas as pd
from PIL import Image
from tqdm import tqdm
import pickle
import imagehash

def extract_features(img_path):
    """
    Calculates the perceptual hash (fingerprint) of an image.
    """
    try:
        # Open the image and calculate its average hash
        hash_value = imagehash.average_hash(Image.open(img_path))
        return hash_value
    except Exception as e:
        print(f"Error processing image {img_path}: {e}")
        return None

# --- Process All Images in the Database ---
df = pd.read_csv('products.csv')

all_features = {}
for index, row in tqdm(df.iterrows(), total=df.shape[0], desc="Generating Image Hashes"):
    img_path = row['image_path']
    features = extract_features(img_path)
    if features is not None:
        all_features[img_path] = features

# --- Save the Hashes to a File ---
with open('image_features.pkl', 'wb') as f:
    pickle.dump(all_features, f)

print("\nImage hash generation complete. All features saved to 'image_features.pkl'")

