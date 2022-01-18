from flask import Flask, render_template
app = Flask(__name__)
data = [
        {
            'id':1,
            'name':iphone 9',
            'price': 799,
            'remains': True
        },

        {
            'id': 2,
            'name': 'Macbook Pro',
            'price': 4799,
            'remains': False
        },

        {
            'id': 3,
            'name': 'Apple Watch',
            'price': 10799,
            'remains': True
        },

        {
            'id': 4,
            'name': 'Apple stand pro',
            'price': 99999,
            'remains': True
        },
    ]


@app.route('/')
def home():  # put application's code here
    return 'Hello World and welcome to my first flask application!'

@app.route('/product')
def show_product():
    css = open('style.css', 'r').read()
    return render_template('produits.html', products=data, additional_css=css)
@app.route('/product/<id>')
def product_details(id):
    for elements in data:
        if elements['id'] ==int(id):
                dic_to_find=elements
    return render_template('details.html', product=dic_to_find)

if __name__ == '__main__':
    app.run()
