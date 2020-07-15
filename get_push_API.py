import numpy as np
import dump
from json import JSONEncoder
from flask import Flask, jsonify, Response,Request,request
import flask
import status
from bs4 import BeautifulSoup
import  lxml
import  requests
from pyexcel_ods import get_data,save_data
import json

app =Flask(__name__)

@app.route('/getdetails/<path:website>')
def getdetails(website):
    oauth = request.headers['OAuth']
    if oauth!= 'Secure':
        return Response(None, status= 500)

    if website == 'https://aytm.com/':
        source = requests.get('https://aytm.com/').text
        soup = BeautifulSoup(source, 'lxml')

        # Extract company name
        company_name = (soup.find('a', class_="logo aytm")['title']).split('.')[0]

        # Extract title
        title = soup.title.text

        # Extract image
        image = (soup.find('div', id='main-content-adv').img)['src']

        # Extract Short description

        temp = soup.find('div', class_="section-content-panel centered").p.text
        temp1 = temp.split('\n')
        temp1.pop(0)
        temp1.pop(2)
        x = temp1[1][20:]
        temp1[1] = x
        short_desc = temp1[0] + temp1[1]

        # Extract linkedin profile
        linkedin = (soup.find('a', class_='linkedin'))['href']

        # Extract summary
        sm = (soup.find('div', class_="section-content-block mobile-hidden").p.text)
        temp = sm.split('\n')
        summary = temp[1][16:]

        obj= Extract(company_name, title, image, short_desc,'','',linkedin,summary,'')
        json_obj= ExtractEncoder().encode(obj)
        return Response(json_obj, status=200,mimetype='application/json')

    elif website=='https://www.datawallet.com/':

        source = requests.get('https://www.datawallet.com/').text
        soup = BeautifulSoup(source, 'lxml')

        # Extract company name
        temp = (soup.find('title')).text
        company_name = temp[51:]

        # Extract title
        title = temp[:48]

        # Extract image
        image = (soup.find('img', class_='logotype'))['src']

        # Extract Short description
        short_desc = soup.find('div', class_='grid-box__GridBox-ae5f5l-0 lkaZRv').p.text

        # Extract company icon
        company_icon = (soup.find('img', class_='logomark'))['src']

        # Extract linkedin profile
        st = soup.find_all('div', class_='footer__FooterCol-sc-11ar6no-0 jDLoEy')
        st1 = st[2].find_all('a')
        linkedin = st1[3]['href']

        source1 = requests.get('https://www.datawallet.com/whats-a-datawallet/').text
        soup1 = BeautifulSoup(source1, 'lxml')
        summary = soup1.find('p').text

        obj = Extract(company_name, title, image, short_desc, company_icon, '', linkedin, summary, '')
        json_obj = ExtractEncoder().encode(obj)
        return Response(json_obj, status=200, mimetype='application/json')

    elif website=='https://www.fancyhands.com/':
        source = requests.get('https://www.fancyhands.com/').text
        soup = BeautifulSoup(source, 'lxml')

        # Extract company name
        temp = (soup.find('title')).text
        company_name = temp[26:]
        #print(company_name)

        # Extract title
        title = temp[:23]
        #print(title)

        # Extract image
        im = soup.find('img', class_='center')['src']
        image = 'https://www.fancyhands.com/' + im
        #print(image)

        # Extract Short description
        short_desc = (soup.find_all('h2')[1]).text
        #print(short_desc)

        # Extract company icon
        im = soup.find('img', class_='header--logo')['src']
        company_icon = 'https://www.fancyhands.com/' + im
        #print(company_icon)

        # Extract contact email
        source1 = requests.get('https://www.fancyhands.com/support').text
        soup1 = BeautifulSoup(source1, 'lxml')
        contact_email = soup1.find('p', class_='center-text').text[17:]
        #print(contact_email)

        # Extract summary
        summary = soup.find('h2', class_='landing-panel--heading-explainer').text
        #print(summary)

        obj = Extract(company_name, title, image, short_desc, company_icon,contact_email,'', summary, '')
        json_obj = ExtractEncoder().encode(obj)
        return Response(json_obj, status=200, mimetype='application/json')

    elif website=='https://www.starmind.ai/':

        source = requests.get('https://www.starmind.ai/').text
        soup = BeautifulSoup(source, 'lxml')

        # Extract company name
        temp = (soup.find('title')).text
        company_name = temp[:9]
        #print(company_name)

        # Extract title
        title = temp[14:]
        #print(title)

        # Extract image
        image = soup.find_all('img')[5]['src']

        #print(image)

        # Extract Short description
        short_desc = soup.find('div', class_='inner-wrapper box-container').text[4:120]
        #print(sd)

        # Extract company icon
        company_icon = soup.find('a', id="hs-link-module_1550693277349670_").img['src']
        #print(company_icon)

        # Extract contact email

        # Extract linkedin
        linkedin = soup.find('div', class_='footer-social-icons').a.next_sibling.next_sibling['href']

        #print(temp)
        source1 = requests.get('https://www.starmind.ai/about-us').text
        soup1 = BeautifulSoup(source1, 'lxml')
        summary = soup1.find('div', class_='inner-wrapper box-container').p.text

        obj = Extract(company_name,title,image,short_desc,company_icon,'',linkedin,summary,'')
        json_obj = ExtractEncoder().encode(obj)
        return Response(json_obj, status=200, mimetype='application/json')

    else:

        source= requests.get('https://stackoverflow.com/').text
        soup = BeautifulSoup(source, 'lxml')

        #Extract company name
        temp= (soup.find('title')).text
        company_name= temp[:14]
        #print(company_name)

        #Extract title
        title= temp[17:]
        #print(title)

        #Extract image
        image= soup.find('div', class_= 'grid--cell wmx3 md:ta-center md:pl24 md:pr24 sm:pl0 sm:pr0').img['src']
        #print(image)

        #Extract Short Description
        short_desc= soup.find('div', class_= 'py128 product-hero-background d:fc-white').p.text
        #print(short_desc)

        #Extract company icon
        company_icon= soup.find_all('link')[2]['href']
        #print(company_icon)

        #Extract contact email
        source1= requests.get('https://stackoverflow.com/company/contact').text
        soup1 = BeautifulSoup(source1, 'lxml')
        ce= soup1.find_all('div',class_='_icon')
        contact_email=ce[len(ce)-1].p.text
        #print(contact_email)

        #Extract linkedin
        linkin= soup.find('div',class_='site-footer--copyright fs-fine')
        linkedin= linkin.find_all('li')[3].a['href']
        print(linkedin)

        #Extract summary
        summary= soup.find('p',class_='ta-center fs-body3 w90 wmx5 mx-auto mb48').text
        #print(summary)

        obj = Extract(company_name, title, image, short_desc, company_icon,contact_email, linkedin, summary, '')
        json_obj = ExtractEncoder().encode(obj)
        return Response(json_obj, status=200, mimetype='application/json')


@app.route('/pushdetails', methods= ['PUT'])
def pushdetails():
    r = requests.get('http://127.0.0.1:5000//getdetails/https://aytm.com/', headers={'OAuth': 'Secure'})
    req_data = r.json()

    data = get_data("Junior Data & Automation Engineer.ods")
    data['Sheet1'][1][1]= req_data['company_name']
    data['Sheet1'][1][2]= req_data['title']
    data['Sheet1'][1][3] = req_data['image']
    data['Sheet1'][1][4] = req_data['short_des']
    data['Sheet1'][1][5] = req_data['company_icon']
    data['Sheet1'][1][6] = req_data['contact_email']
    data['Sheet1'][1][7] = req_data['linkedin']
    data['Sheet1'][1][8] = req_data['summary']
    data['Sheet1'][1][9] = req_data['service']
    #save_data("your_file.ods", data)

    r = requests.get('http://127.0.0.1:5000//getdetails/https://www.datawallet.com/', headers={'OAuth': 'Secure'})
    req_data = r.json()

    data['Sheet1'][2][1] = req_data['company_name']
    data['Sheet1'][2][2] = req_data['title']
    data['Sheet1'][2][3] = req_data['image']
    data['Sheet1'][2][4] = req_data['short_des']
    data['Sheet1'][2][5] = req_data['company_icon']
    data['Sheet1'][2][6] = req_data['contact_email']
    data['Sheet1'][2][7] = req_data['linkedin']
    data['Sheet1'][2][8] = req_data['summary']
    data['Sheet1'][2][9] = req_data['service']

    r = requests.get('http://127.0.0.1:5000//getdetails/https://www.fancyhands.com/support', headers={'OAuth': 'Secure'})
    req_data = r.json()

    data['Sheet1'][3][1] = req_data['company_name']
    data['Sheet1'][3][2] = req_data['title']
    data['Sheet1'][3][3] = req_data['image']
    data['Sheet1'][3][4] = req_data['short_des']
    data['Sheet1'][3][5] = req_data['company_icon']
    data['Sheet1'][3][6] = req_data['contact_email']
    data['Sheet1'][3][7] = req_data['linkedin']
    data['Sheet1'][3][8] = req_data['summary']
    data['Sheet1'][3][9] = req_data['service']

    r = requests.get('http://127.0.0.1:5000//getdetails/https://www.starmind.ai/',headers={'OAuth': 'Secure'})
    req_data = r.json()

    data['Sheet1'][4][1] = req_data['company_name']
    data['Sheet1'][4][2] = req_data['title']
    data['Sheet1'][4][3] = req_data['image']
    data['Sheet1'][4][4] = req_data['short_des']
    data['Sheet1'][4][5] = req_data['company_icon']
    data['Sheet1'][4][6] = req_data['contact_email']
    data['Sheet1'][4][7] = req_data['linkedin']
    data['Sheet1'][4][8] = req_data['summary']
    data['Sheet1'][4][9] = req_data['service']

    r = requests.get('http://127.0.0.1:5000//getdetails/https://stackoverflow.com/company/contact', headers={'OAuth': 'Secure'})
    req_data = r.json()

    data['Sheet1'][5][1] = req_data['company_name']
    data['Sheet1'][5][2] = req_data['title']
    data['Sheet1'][5][3] = req_data['image']
    data['Sheet1'][5][4] = req_data['short_des']
    data['Sheet1'][5][5] = req_data['company_icon']
    data['Sheet1'][5][6] = req_data['contact_email']
    data['Sheet1'][5][7] = req_data['linkedin']
    data['Sheet1'][5][8] = req_data['summary']
    data['Sheet1'][5][9] = req_data['service']

    save_data("Junior Data & Automation Engineer.ods", data)



    return jsonify({'result': 'Success'})


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