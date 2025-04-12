from flask import Flask, request

# Step 1: Create the Flask app
app = Flask(__name__)

# Step 2: Define the route and method
@app.route('/upload', methods=['POST'])
def upload_image():
    # Step 3: Check if the request has an image
    if 'image' not in request.files:
        return {'message': 'No image part'}, 400

    file = request.files['image']

    # Step 4: Check if the image has a filename
    if file.filename == '':
        return {'message': 'No selected file'}, 400

    # Step 5: (Optional) Save the file
    # file.save(f"./uploads/{file.filename}")

    # Step 6: Print confirmation in the terminal
    print("Image uploaded!")  # ← This will show in your VS Code terminal

    # Step 7: Return success response
    return {'message': 'Image received successfully'}, 200

# Step 8: Run the app
if __name__ == '__main__':
    app.run(debug=True)

