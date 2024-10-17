from flask import Flask, render_template, request

app = Flask(__name__)

# Página principal con la calculadora
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para realizar la operación de la calculadora
@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']
    
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        result = num1 / num2
    else:
        result = 'Operación no válida'
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
