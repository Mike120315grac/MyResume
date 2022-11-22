from flask import flask

#create web application
app = flask(__name__)

#create our roots.
@app.route('/')
def home():
    return render_template("index.html")

#Start the application
if __name__ == "__main__":
  app.run(debug=True)