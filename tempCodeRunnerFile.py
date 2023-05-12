
def new3():
    return render_template('admission.html')

@app.route("/query")
def new4():
    return render_template('query.html')

@app.route('/semster12')
def smeseter(): 
 return redirect("https://drive.google.com/drive/folders/1CTxA4nhRC3Wjbvlw7aEafrNGTeaByBmX")

@app.route('/semster34')
def sem34(): 
 return redirect("https://drive.google.com/drive/folders/1yakEhlolq1RH2f5eVxib0bzPKsQnA0AX")

@app.route('/semster56')
def sem56(): 
 return redirect("https://drive.google.com/drive/folders/1ykrm9R84bDQpJxMPNFt8euj1miSY05Sy")

@app.route('/semster78')
def sem78(): 
 return redirect("https://drive.google.com/drive/folders/1z36HYqXF1361tmU_Q3NnyMh5PlnViCbY")









if __name__ == "__main__":
    app.run(debug=True)
