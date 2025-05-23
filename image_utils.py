# Load model once
resnet_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
model = tensorflow.keras.Sequential([resnet_model, GlobalMaxPooling2D()])
model.trainable = False

# Load feature data
feature_list = np.array(pickle.load(open('models/embeddings.pkl', 'rb')))
filenames = pickle.load(open('models/filenames.pkl', 'rb'))

def find_similar_images(input_image_path):
    img = image.load_img(input_image_path, target_size=(224, 224))
    img_data = image.img_to_array(img)
    img_data = np.expand_dims(img_data, axis=0)
    img_data = preprocess_input(img_data)

    features = model.predict(img_data)
    neighbors = NearestNeighbors(n_neighbors=5, algorithm='brute', metric='euclidean')
    neighbors.fit(feature_list)
    _, indices = neighbors.kneighbors(features)

    return [filenames[i] for i in indices.flatten()]
