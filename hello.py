from flask import Flask, redirect, url_for, render_template, request
import numpy as np
import matplotlib.pyplot as plt
from V_Flask import runAll

import folium

app=Flask(__name__)

@app.route('/')
def hello_world():
    #prefix = 'sfbay' #zip = '95010' #dist = str(5) #n = int(240)
    #runAll.run(prefix, zip, dist, n)
    #p1= '/V_Flask/plots/relPlot.png'
    #p2 =
    return render_template('mypage.html', name = 'plot', value = '/static/images/dog.jpg', p1=  '/static/plots/relPlot.png')



@app.route('/', methods=['GET','POST'])
def my_form_post():
    pref = request.form['prefix']
    zip = request.form['zipcode']
    dist = request.form['dist']
    n = request.form['n']
    return redirect("/get?prefix=" + pref + "&zip=" + zip + "&dist=" + dist + "&n=" + n)


@app.route('/get')
def get():

    prefix = request.args.get('prefix', default = 'sfbay', type = str)
    zip = request.args.get('zip', default = '95010', type = str)
    dist = request.args.get('dist', default = '5', type = str)
    n = request.args.get('n', default = 240, type = int)
    runAll.run(prefix, zip, dist, n)
    with open('static/plots/facts.txt', 'r') as f:
        text = f.read()
    #p1= '/V_Flask/plots/relPlot.png'
    #p2 =
    return render_template('mypage2.html', name = text, p1 =  '/static/plots/relPlot.png', p2 =  '/static/plots/distPlots.png')

#Render a basic map using folium
@app.route('/map')
def map():
    start_coords = (46.9540700, 142.7360300)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    '''icon = CustomIcon(
        icon_image,
        icon_size=(38, 95),
        icon_anchor=(22, 94),
        shadow_image=shadow_image,
        shadow_size=(50, 64),
        shadow_anchor=(4, 62),
        popup_anchor=(-3, -76)
    )
    marker = folium.Marker(
    location=[x, y],
    icon=icon,
    popup='Mt. Hood Meadows'
    )'''

    folium_map.save('templates/map.html')
    return render_template('map.html')





# Trying to handle Data
@app.route('/handleData', methods=['GET'])
def handleData():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    return """<html><body><h2>Hello %s %s</h2></body></html>""" % (first_name, last_name)
    '''
    data = request.form['someData']
    return render_template('page2.html')
    '''

@app.route('/query-example')
def query_example():
    loc = request.args.get('loc') #if key doesn't exist, returns None
    zip = request.args.get('zip') #if key doesn't exist, returns None

    return '''<h1>The loc value is: {}</h1>
            <h2>The zip value is: {}</h2>'''.format(loc,zip)



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
