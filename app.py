from flask import Flask, request, jsonify, render_template
from PIL import Image
import numpy as np
import pickle
import pandas as pd
import requests
from io import BytesIO
import imagehash

app = Flask(__name__)

# --- Load Data at Startup ---
print("Loading image hashes...")
with open('image_features.pkl', 'rb') as f:
    all_features = pickle.load(f)

df = pd.read_csv('products.csv')

# Convert stored hashes to a list for comparison
image_paths = list(all_features.keys())
feature_hashes = [all_features[path] for path in image_paths]
print("Hashes loaded successfully.")


# --- Helper Function ---
def find_similar_images(query_hash, database_hashes, top_n=10):
    """Finds the most similar images based on hash distance."""
    # Calculate the bit difference (Hamming distance) between the query and all database hashes
    distances = [query_hash - db_hash for db_hash in database_hashes]
    
    # Get the indices of the smallest distances (most similar)
    sorted_indices = np.argsort(distances)
    
    results = []
    for i in range(top_n):
        idx = sorted_indices[i]
        distance = distances[idx]
        # Calculate a normalized similarity score.
        # Max distance for a 64-bit hash is 64. 
        # (1 - (distance / max_distance)) gives a score from 0 to 1.
        similarity = 1 - (distance / 64.0)
        results.append({'index': idx, 'similarity': similarity})
        
    return results


# --- Define Application Routes ---
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    try:
        # Handle image URL input
        if request.is_json:
            data = request.get_json()
            url = data.get('url')
            if not url:
                 return jsonify({'error': 'No URL provided'}), 400
            response = requests.get(url, timeout=10)
            response.raise_for_status() # Raise an exception for bad status codes
            img = Image.open(BytesIO(response.content))
        # Handle file upload input
        elif 'file' in request.files:
            file = request.files['file']
            if file.filename == '':
                return jsonify({'error': 'No file selected'}), 400
            img = Image.open(file.stream)
        else:
            return jsonify({'error': 'Invalid request. Please provide a file or a valid URL.'}), 400

        # Generate hash for the query image
        query_hash = imagehash.average_hash(img)
        
        # Find similar images
        similar_items = find_similar_images(query_hash, feature_hashes)
        
        results = []
        for item in similar_items:
            idx = item['index']
            similarity = item['similarity']
            
            img_path = image_paths[idx]
            product_info = df[df['image_path'] == img_path].to_dict('records')[0]
            product_info['similarity'] = round(similarity, 4)
            results.append(product_info)
            
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': f'An error occurred: {e}'}), 500

if __name__ == '__main__':
    # We use waitress to run the app
    from waitress import serve
    serve(app, host='0.0.0.0', port=8080)

