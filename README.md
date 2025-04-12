# flask-upload-api-nema

## Flask Image Upload API

- This is a simple Flask API that accepts an image file via a POST request and prints "Image uploaded!" to the console.

##  How to Run

1. Install Flask
2. Run the app1.py
3. Use Postman to send a `POST` request to
  -Go to Body → form-data
  -Key: `image` (type: File)
  -Select an image to upload
4. You will see:
  - Response: `{"message": "Image received successfully"}`
  - Console: `Image uploaded!`
    
## Then run

  git add README.md
  git commit -m "Added README"
  git push
