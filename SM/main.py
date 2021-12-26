from flask import *
from database import WorkspaceData
app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return render_template("home.html")
@app.route('/login',methods=['POST','GET'])
def login():
    return render_template('login.html',retry=False, errorType='none')

@app.route('/validate_login', methods=['POST', 'GET'])
def validate_login():
    if request.method == 'POST':
        if 'login' in request.form:
            user_name = request.form.get('username')
            password = request.form.get('password')
            db = WorkspaceData()
            data = db.get('login', user_name)
            for s in data:
                if user_name == s['username'] and password == s['password']:
                    return redirect('/frontp')
            return render_template('login.html', retry=True, errorType='login')
        elif 'signup' in request.form:
            user_name = request.form.get('name')
            password = request.form.get('password')
            email = request.form.get('email')
            db = WorkspaceData()
            db.add('login', [(user_name, password, email)])
            return render_template('frontpage.html', retry=False, errorType='signup')

@app.route('/validate_stubble', methods=['POST', 'GET'])
def validate_stubble():
    if request.method == 'POST':
            user_name = request.form.get('name')
            address = request.form.get('address')
            sname=request.form.get('stubblename');
            dmy=request.form.get('date');
            quan = request.form.get('quantity');
            mobile = request.form.get('phone');
            iname = request.form.get('industryname');
            iaddress = request.form.get('industryaddress');
            db = WorkspaceData()
            db.add('stubble', [(user_name, address,sname,dmy,quan,mobile,iname,iaddress)])
            return render_template('registartion.html')

@app.route('/signup',methods=['POST','GET'])
def signup():
    return render_template('signup.html')

@app.route('/frontp',methods=['POST','GET'])
def frontp():
    return render_template("frontpage.html")

@app.route('/contactus')
def contactus():
    return render_template('ContactUs.html')

@app.route('/aboutus')
def aboutus():
    return render_template('Aboutus.html')
@app.route('/search',methods=['POST','GET'])
def search():
    return render_template('search.html',info_data=0,length=0)

@app.route('/registartion',methods=['POST','GET'])
def registartion():
    return render_template('registartion.html')

@app.route('/thankyou',methods=['POST','GET'])
def thankyou():
    return render_template('thankyou.html')

@app.route('/validate_search', methods=['POST', 'GET'])
def validate_search():
    if request.method == 'POST':
            name = request.form.get('name')
            place = request.form.get('place')
            db = WorkspaceData()
            data = db.get('industries', name)
            info_data = dict()
            info_data['industryname']=[]
            info_data['industryplace']=[]
            info_data['quantity']=[]
            info_data['price']=[]
            print(place)
            for s in data:
                print(s[1])
                if str(name) == str(s[0]) and str(place) == str(s[1]):
                   print(place)
                   info_data['industryname'].append(s[2])
                   info_data['industryplace'].append(s[3])
                   info_data['quantity'].append(s[4])
                   info_data['price'].append(s[5])
            print(info_data)
            l=len(info_data['industryname'])
            return render_template('search.html', info_data=info_data,length=l)

if __name__ == '__main__':
    app.run(debug=True)