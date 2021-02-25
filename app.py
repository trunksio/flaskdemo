from flask import Flask, request, render_template
import base64
import json
import boto3

app = Flask(__name__)
s3 = boto3.resource('s3')
s3_bucket = 'trunkscgt'


##place holder for actual processing work
@app.route('/fancyStuff/<id>',methods=["GET"])
def fancy_stuff(id):
    content_object = s3.Object(s3_bucket, id + '.json')
    file_content = content_object.get()['Body'].read().decode('utf-8')
    json_content = json.loads(file_content)
    return  json_content['textExtraction']

##actually get the pdf from s3
@app.route("/getPdf/<id>", methods=["GET"])
def get_pdf_file(id):

    content_object = s3.Object(s3_bucket, id+ '.json')
    file_content = content_object.get()['Body'].read().decode('utf-8')
    json_content = json.loads(file_content)
    encoded_data = json_content['source']
    return render_template("getPdf.html", encoded_data=encoded_data)


##main route into app
@app.route("/showPdf/<id>", methods=["GET"])
def show_pdf_file(id):
    return render_template("showPdf.html", id=id)