from flask import Flask, render_template, request, redirect, url_for
import pytesseract
from PIL import Image

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['image']

        if uploaded_file:
            extracted_text = ocr_from_image(uploaded_file)

            return render_template('index.html', extracted_text=extracted_text, filename=uploaded_file.filename)

    return render_template('index.html')


def ocr_from_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)

    return text


if __name__ == '__main__':
    app.run(port=3000, debug=True)
