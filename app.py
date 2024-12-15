from flask import Flask, render_template, request, flash
import pytesseract
from PIL import Image

app = Flask(__name__)

app.secret_key = 'secret'

template_index = 'index.html'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['image']

        if uploaded_file:
            if not allowed_file(uploaded_file.filename):
                flash('Invalid file type. Allowed types: png, jpg, jpeg, gif, bmp, webp.')
                return render_template(template_index)

            extracted_text = ocr_from_image(uploaded_file)

            return render_template(template_index, extracted_text=extracted_text, filename=uploaded_file.filename)

    return render_template(template_index)


def ocr_from_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)

    return text

def allowed_file(filename):
    allowed_extension = {'png', 'jpg', 'jpeg', 'gif', 'webp', 'bmp'}

    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extension

if __name__ == '__main__':
    app.run(port=3000, debug=True)
