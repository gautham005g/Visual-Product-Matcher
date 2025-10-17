This project is a visual search engine designed for an e-commerce product database. To build the database, product images of apparel and footwear were sourced from the public "E-commerce Product Images" Kaggle dataset. To ensure the final application was lightweight and met the project's minimum requirements, a curated subset of 100 products was selected.

Initially, the plan was to use a deep learning model, specifically ResNet50, to generate feature vectors for each image. This approach, while powerful, was found to be too memory-intensive for the 512MB RAM constraint typical of free-tier hosting platforms, making a successful deployment impossible.

Consequently, the project pivoted to a more efficient strategy: Perceptual Hashing. Using this method, a compact 64-bit hash, or "fingerprint," is pre-computed for every product image in the database. When a user submits an image, its hash is calculated on the fly. The system then finds the closest visual matches by comparing the user's hash against all database hashes using the Hamming distance metric.

This hash-based method is extremely fast and has a very low memory footprint. It showcases a practical, problem-solving mindset by prioritizing the delivery of a fully functional and deployable application that operates successfully within the specified technical constraints.

Link: https://visual-product-matcher-ikzq.onrender.com/

Name: Gowtham

Email: gautham7394@gmail.com
