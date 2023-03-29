from flask import Flask, render_template, request


# from pdf2image import convert_from_path
import cv2
import numpy as np
# import matplotlib.pyplot as plt
from PIL import ImageDraw, Image
# import json
import os
import io

def pdf2himg(path):

    im = Image.open(path)
    img_arr = np.asarray(im)

    # Convert BGR to HSV
    img_hsv = cv2.cvtColor(img_arr, cv2.COLOR_BGR2HSV)

    # create a mask
    mask = cv2.inRange(img_hsv, np.array([0, 53, 93]), np.array([179, 255, 255]))

    final_img = cv2.bitwise_and(img_arr, img_arr, mask = mask)
    final_img[final_img==0] = 255

    final_img = Image.fromarray(final_img)

    return final_img
    #final_img.save(file_name + ".png")


app = Flask(__name__)

# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")

@app.route("/about")
def about_page():
	return "Hey LOVE!!!"

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		file = request.files['my_image']
		os.makedirs("static", exist_ok=True)

		file_path = "static/" + file.filename	
		file.save(file_path)

		p = pdf2himg(file_path)
		
		a = file.filename.split('.')[0]
		p_path = "static/" + a + "_handwritten.jpg"
		p.save(p_path)

	return render_template("index.html", 
			original = file_path,
			prediction = p_path,
			#img_path = p_path
            )


if __name__ == "__main__":
    app.run(debug=True)