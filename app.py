from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/select-entity')
def select_entity():
    return render_template('select-entity.html')

if __name__ == '__main__':
    app.run(debug=True)