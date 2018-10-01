from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True 


@app.route("/signup", methods=["POST"])
def user_error():
    Username= request.form["Username"]
    Password= request.form["Password"]
    Verify_password= request.form["Verify_password"]
    Email= request.form["Email"]

    Password_error = ""
    Username_error = ""
    Verify_error = ""
    Email_error= ""

    

    if len(Username) > 20 or len(Username)<3:      
        Username_error = "Length must be greater than 3 and less than 20"
       
    else:
        for char in Username:
            if char == " ":
                Username_error=" No empty spaces allowed"
                
        
    if len(Password) >20 or len(Password)<3:
        Password_error = "Length must be greater than 3 and less than 20"
        
    else:
        for char in Password:
            if char == " ":
                Password_error=" No empty spaces allowed"
                

    if Verify_password != Password or Verify_password == "":
        Verify_error= "Passwords do not match. Please re-enter"
       

    if Email != "":

        if "@" not in Email or "." not in Email:
             Email_error = "This is not a valid email address"
             
        else:
            if len(Email) >20 or len(Email)<3:
                Email_error = "Length must be greater than 3 and less than 20"
                
            else:
                counter = 0
                for char in Email:
                    if char == " ":
                        Email_error= "No empty spaces allowed"
                       
                    if char == "@" or char == ".":
                        counter+= 1 
                    if counter > 2:
                        Email_error= "Cannot have more than 1 (@) or (.) in a valid email address... Please re-enter"
                       
    if not Password_error and not Username_error and not Verify_error and not Email_error:
        greet_username = Username
        return redirect("/welcome?greet_username={0}".format(greet_username))
    else:
        return render_template("home.html", Email= Email, Username= Username, Password= Password, Verify_password= Verify_password, Email_error= Email_error, Password_error= Password_error, Username_error= Username_error, Verify_error= Verify_error)

@app.route("/welcome")
def welcome():
    Username = request.args.get('greet_username')
    return render_template('Welcome.html', Username= Username)

@app.route("/signup")
def index():
    return render_template("home.html")



app.run()