from flask import Flask, render_template, request, send_file
from qrcode import constants
import qrcode
from io import BytesIO

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    # Get user input from the form
    data = request.form['data']

    # Create a QRCode instance
    q = qrcode.QRCode(
        version=1,
        error_correction=constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    q.add_data(data)
    q.make(fit=True)

    # Create a BytesIO object to store the image
    img_stream = BytesIO()
    img = q.make_image(fill_color="orange", back_color="white")
    img.save(img_stream)
    img_stream.seek(0)

    # Return the image as a response
    return send_file(img_stream, mimetype='image/png')
