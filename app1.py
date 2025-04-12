from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return {'message': 'No image part'}, 400

    file = request.files['image']
    if file.filename == '':
        return {'message': 'No selected file'}, 400

    print("Image uploaded!")
    return {'message': 'Image received successfully'}, 200

if __name__ == '__main__':
    app.run(debug=True)
