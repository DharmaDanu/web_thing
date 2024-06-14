from flask import Flask, render_template
import random
import os

app = Flask(__name__)

# Home/1st page
@app.route("/")
def pertama():
    # <a> anchor tag with its attribute
    return "<h1>Hello, World!</h1><br><p>Nice to see you</p><p>please check</p><a href='/random_fact'>View a random fact!</a><br><a href='/modern_fact'>View a modern fact!</a><br><a href='/coin'>View a Coin Flip!</a>"
    
# 2nd page
@app.route("/random_fact")

def kedua():
    txt_name = random.choice(os.listdir("fact_list"))
    # formatted string
    with open(f'fact_list/{txt_name}', 'r') as f:
        document = f.read()
    return f'{document}'
# 2nd page
@app.route('/modern_fact')
def index():
    return render_template('dasar.html')#folder templates

# 3rd page
@app.route('/coin')
def flip():
    flipped = random.randint(1, 2)
    if flipped == 1:
        return "<p>It is...</p><h1>Heads!</h1>"
    
    if flipped == 2:
        return "<p>It is...</p><h1>Tails!</h1>"
app.run(debug=True)
