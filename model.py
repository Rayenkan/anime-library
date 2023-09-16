from flask import Flask, render_template
import os

app = Flask(__name__)

img_folder = r"C:\Users\ac485\OneDrive\Bureau\python sht\anime library\img"
images = [f for f in os.listdir(img_folder)]

@app.route('/')
def rotate_images():
    global images
    if not images:
        images = [f for f in os.listdir(img_folder)]

    image = images.pop(0)
    images.append(image)

    return render_template('index.html', image=image)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
