app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files['file']
    file_name = file.filename
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
    file.save(file_path)

    upload_to_cos(file_path, file_name)
    download_file_from_cos(file_name)
    similar_images = find_similar_images(file_path)

    html = "<h1>Similar products to the uploaded image</h1><p>If you want to customise your own outfit, please go back to the chatbot.</p>"
    for img in similar_images:
        html += f'<img src="{img}" width="224" height="224" style="margin: 10px">'
    return html

@app.route("/generate-image", methods=["POST"])
def generate_image():
    text = request.form['text']
    response = requests.post(
        'https://api.deepai.org/api/text2img',
        headers={'api-key': os.getenv('DEEPAI_API_KEY')},
        data={'text': text}
    )
    image_url = response.json()['output_url']
    return jsonify({'image_url': image_url})

if __name__ == "__main__":
    app.run(debug=True)