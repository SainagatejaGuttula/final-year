from flask import Flask,render_template, redirect, request
import numpy as np
import PIL
from tensorflow.keras.models import load_model
import cv2

all_c = load_model(r'C:\Users\Sai Naga Teja\Desktop\Application\Application\model files\all_cancer (1).h5')
brain = load_model(r'C:\Users\Sai Naga Teja\Desktop\Application\Application\model files\brain_tumor.h5')
cervical = load_model(r'C:\Users\Sai Naga Teja\Desktop\Application\Application\model files\cervical_cancer (1).h5')
oral = load_model(r'C:\Users\Sai Naga Teja\Desktop\Application\Application\model files\oral_cancer (1).h5')
lung = load_model(r'C:\Users\Sai Naga Teja\Desktop\Application\Application\model files\lung_and_colon_cancer.h5')
kidney = load_model(r'C:\Users\Sai Naga Teja\Desktop\Application\Application\model files\kidney_tumor.h5')

all_classes = ['benign','early','pre stage','pro stage']
brain_classes = ['Giloma','Meningioma','Pituitary Tumor']
c_c = ['Dyskeratotic', 'Koilocytotic', 'Metaplastic', 'Parabasal', 'Superficial-Intermediat']
o_c = ['Normal','Squamous Cell Carinoma']
k_c = ["Normal", "tumor"]
l_c = ['colon_aca lung cancer', 'colon_bnt lung cancer', 'lung_aca lung cancer', 'lung_bnt lung cancer', 'lung_scc lung cancer']




# def est(test_image,model,labels):
#     img = cv2.imread(test_image)
#     img = img / 255.0
#     img = cv2.resize(img,(64,64))
#     img = img.reshape(1,64,64,3)
#     prediction = model.predict(img)
#     pred_class = np.argmax(prediction, axis = -1)
#     return labels[pred_class[0]]

def est(test_image,model,labels):
    img = cv2.imread(test_image)
    img = img / 255.0
    img = cv2.resize(img,(224,224))
    img = img.reshape(1,224,224,3)
    prediction = model.predict(img)
    pred_class = np.argmax(prediction, axis = -1)
    return labels[pred_class[0]]


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')








@app.route('/ALL')
def all():
    return render_template('Acute Lymphoblastic Leukemia.html')
@app.route("/submit_all", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['all_img']

		img_path = "static/" + img.filename	
		img.save(img_path)

		p = est(img_path, all_c ,all_classes)

	return render_template("Acute Lymphoblastic Leukemia.html", prediction = p, img_path = img_path)




#Grocery Page
@app.route('/cervical_can')
def cervical_cancer():
    return render_template('Cervical Cancer.html')
@app.route("/submit_cer", methods = ['GET', 'POST'])
def get_output2():
	if request.method == 'POST':
		img = request.files['cervical_img']

		img_path = "static/" + img.filename	
		img.save(img_path)

		p = est(img_path,cervical,c_c)

	return render_template("Cervical Cancer.html", prediction = p, img_path = img_path)




@app.route('/oral_can')
def Oral():
    return render_template('Oral Cancer.html')
@app.route("/submit_oral", methods = ['GET', 'POST'])
def get_output3():
	if request.method == 'POST':
		img = request.files['my_image_oral']

		img_path = "static/" + img.filename	
		img.save(img_path)

		p = est(img_path,oral,o_c)

	return render_template("Oral Cancer.html", prediction = p, img_path = img_path)



@app.route('/brain_can')
def brain_cancer():
    return render_template('brain cancer.html')
@app.route("/submit_brain", methods = ['GET', 'POST'])
def get_output4():
	if request.method == 'POST':
		img = request.files['brain_img']

		img_path = "static/" + img.filename	
		img.save(img_path)

		p = est(img_path,brain,brain_classes)

	return render_template("brain cancer.html", prediction = p, img_path = img_path)



@app.route('/lung')
def lung():
    return render_template('brain cancer.html')
@app.route("/submit_lung", methods = ['GET', 'POST'])
def get_output5():
	if request.method == 'POST':
		img = request.files['lung_img']

		img_path = "static/" + img.filename	
		img.save(img_path)

		p = est(img_path,brain,l_c)

	return render_template("Lung and colon cancer.html", prediction = p, img_path = img_path)



@app.route('/kidney')
def kidney():
    return render_template('brain cancer.html')
@app.route("/submit_kidney", methods = ['GET', 'POST'])
def get_output6():
	if request.method == 'POST':
		img = request.files['kidney_img']

		img_path = "static/" + img.filename	
		img.save(img_path)

		p = est(img_path,brain,brain_classes)

	return render_template("Kidney Cancer.html", prediction = p, img_path = img_path)


# @app.route('/nutrition')
# def contact():
#     return render_template('contact.html')







@app.route('/diet')
def faq():
    return render_template('faq.html')

if __name__ == '__main__':
    app.run()