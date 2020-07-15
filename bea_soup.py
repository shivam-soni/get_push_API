
from json import JSONEncoder
from flask import Flask, jsonify, Response,Request,request,render_template
from bs4 import BeautifulSoup
import  requests
from pyexcel_ods import get_data,save_data
import json

app =Flask(__name__)

@app.route('/getdetails')
def getdetails():

    website = request.args.get('web')
    if website == 'https://aytm.com/':
        #source = requests.get(/home/soniz/mysite/website).text
        with open("aytm.html", "r") as f:
            source = f.read()
        soup= BeautifulSoup(source, 'lxml')
        company_name = (soup.find('a', class_="logo aytm")['title']).split('.')[0]
        return 'hello {}'.format(company_name)

if __name__=='__main__':

    class Extract:
        def __init__(self,cn,tl,img,sd,ai,ce,li,smr,srv):
            self.company_name= cn
            self.title= tl
            self.image=img
            self.short_des= sd
            self.company_icon=ai
            self.contact_email=ce
            self.linkedin= li
            self.summary=smr
            self.service=srv



    class ExtractEncoder(JSONEncoder):
        def default(self,o):
            return o.__dict__

    app.run(debug=True)