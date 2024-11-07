from flask import Flask, jsonify, request, render_template
import MyClass

app = Flask(__name__)

# Respond with json
@app.route('/data_get', methods=['GET'])
def get_data():

    name = request.args.get('name')
    age = request.args.get('age')

    # create a new person from the inut data
    person = MyClass.Person(name, age)

    # vars will take the members of the class, and turn them into a dictionary
    return jsonify(vars(person))

# Gather the data in a form
@app.route('/data')
def data():

    return render_template('data.html')

# View the data
@app.route('/data_view', methods=['POST'])
def data_view():
    
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        
        return render_template('data_view.html', name=name, age=age)

@app.route('/')
def home():
    return 'Hello from Flask!'
    
if __name__ == '__main__':
    app.run(debug=True, port=8000)
