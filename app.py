from flask import Flask,render_template, request
import pandas as pd
 
app = Flask(__name__)
@app.route("/")
def index():
   return render_template('index.html')

@app.route("/calc",methods=['GET','POST'])
def calculation():
   if request.method  == "GET":
       return render_template('calculation.html')
   elif request.method  == "POST":
       sunny = request.form['sunny']
       cloudy = request.form['cloudy']
       rainy = request.form['rainy']
       cold = request.form['cold']
       hot = request.form['hot']
 
       df = pd.read_excel('JO1.xlsx', index_col=0)
 
       df['sunny']= (df['valence']**2 + df['liveness'] + df['speechiness'] - df['loudness'])
       df=df.sort_values('sunny', ascending=False)
       df['sunny']=df['sunny']/7.132249

       df['cloudy']= (df['valence']*2 -df['loudness']+(1-df['acousticness'])**2+df['liveness'])
       df=df.sort_values('cloudy', ascending=False)
       df['cloudy']=df['cloudy']/8.482946
 
       df['rainy']= ((1-df['valence'])**2+df['acousticness']+(1-df['energy'])**2+df['tempo']/200)
       df=df.sort_values('rainy', ascending=False)
       df['rainy']=df['rainy']/0.830108

       df['cold']= (df['valence']*2+(1-df['acousticness'])+df['energy']+df['danceability'])
       df=df.sort_values('cold', ascending=False)
       df['cold']=df['cold']/4.474250

       df['hot']= (df['valence']**2 + df['liveness'] + df['energy'] - df['loudness'])
       df=df.sort_values('hot', ascending=False)
       df['hot']=df['hot']/7.671249

 
       df['sunny']=(df['sunny']-float(sunny))**2
 
       df['rainy']=(df['rainy']-float(rainy))**2

       df['cloudy']=(df['cloudy']-float(cloudy))**2

       df['cold']=(df['cold']-float(cold))**2

       df['hot']=(df['hot']-float(hot))**2
 
       df['weather']=(df['sunny'] + df['rainy']+ df['cloudy']+ df['cold']+ df['hot'])/5
       #df['weather']=(df['sunny'] + df['rainy'])/2

       df=df.sort_values('weather')

       #html=df.to_html()
       #text_file=open(r"C:\Users\Kinjo Riko\OneDrive\デスクトップ\GeekSalon\flaskr\templates\df.html","w",encoding="cp932")
       #text_file.write(html)
       #text_file.close()
 
       result=df.index.values[:4]

       return render_template('calculation.html',result=result)
 
if __name__ == "__main__":
   app.run(debug=True)

