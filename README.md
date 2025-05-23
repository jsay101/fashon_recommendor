# 👗 Fashion Recommender + Text-to-Image Generator

This Flask app lets users upload a fashion image, find visually similar outfits using deep learning, and even generate new styles using text prompts.

## 🧠 Features
- Upload an outfit image to get visually similar matches
- Generate outfit images based on text (e.g., "red velvet gown")
- Upload and store files in IBM Cloud Object Storage
- Deep learning using ResNet50 + KNN for similarity
- Text-to-image powered by DeepAI API

## ⚙️ Tech Stack
- Python, Flask
- TensorFlow, ResNet50
- IBM Cloud Object Storage (COS)
- DeepAI Text-to-Image API

## 🚀 How to Run
1. Clone this repo  
2. Set up your `.env` with IBM COS and DeepAI API keys  
3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
4. Start the app:
   ```bash
   python app.py
   ```

## 🔐 API Keys
Set the following in your `.env`:
```
IBM_API_KEY=your_key
IBM_SERVICE_INSTANCE_ID=your_crn
DEEPAI_API_KEY=your_key
```

## 👩‍💻 Author
Junaid Ali Sayyed

