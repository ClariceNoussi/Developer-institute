from flask import Flask
app = Flask(__name__)

# default-page
@app.route("/”)
def home():
    string='''<p>Hello this is my paragraph</p>
    <p> This is my second paragraph</p>
    <p>this is my third paragraph'''
   return render_template_tring (string)

if __name__ == "__main__":
   app.run()