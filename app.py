import qrcode
from PIL import Image
from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

def make_poster(id):
    # poster
    im = Image.open('static/poster.png')  # 1242,2208
    w_back = im.size[0]
    h_back = im.size[1]
    w_fore = 100
    h_fore = 100
    base = 'https://shucang.cupsilk.com/#/pages/login/index?code='
    # resize with antialias, otherwise blur
    qr = qrcode.make(base + str(id)).resize((w_fore, h_fore), Image.ANTIALIAS)
    # paste on lower ri
    im.paste(qr, (w_back-w_fore, h_back-h_fore), qr)
    im.save('static/out.png', 'PNG')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':  
        id = request.form.get('id') 
        make_poster(id)
        return redirect(url_for('out'))
    return render_template('index.html')

@app.route('/out')
def out():
    return render_template('out.html')
