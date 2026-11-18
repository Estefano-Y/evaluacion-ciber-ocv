from flask import Flask, request, escape

app = Flask(__name__)

@app.route('/hello')
def hello():
    # Obtenemos el parámetro 'name' y aplicamos escape para prevenir XSS reflejado
    name = request.args.get('name', 'World')
    safe_name = escape(name)
    return f"Hello, {safe_name}!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)