
Approach

This project implements a visual search engine for an e-commerce product database. The product data, consisting of over 2,900 images of apparel and footwear, was sourced from the public "E-commerce Product Images" dataset on Kaggle. A subset of 100 products was used for the database to meet the project's minimum requirements while ensuring a lightweight final application.

The initial technical approach considered using a deep learning model like ResNet50 to generate feature vectors. However, this method proved too memory-intensive for the strict 512MB RAM limit of free-tier hosting services, preventing a successful deployment.

As a result, the project pivoted to a more robust and efficient strategy using Perceptual Hashing. An offline script pre-computes a compact 64-bit hash ("fingerprint") for each product image. When a user provides an image, its hash is generated in real-time. The system then calculates the Hamming distance between the user's hash and all database hashes to find the closest matches.

This lightweight method is extremely fast, uses minimal memory, and demonstrates a practical, problem-solving approach by prioritizing a working, deployable product that meets all functional requirements within the given constraints.


---

Link: https://visual-product-matcher-ikzq.onrender.com/

Name: Sudharson S

Email: sudharson2815@gmail.com

---
