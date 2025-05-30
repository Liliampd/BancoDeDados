from flask import Flask, jsonify
import mysql.connector
from dotenv import load_dotenv
import os

# Carregar variáveis do .env
load_dotenv()

app = Flask(__name__)

# Configurações do banco de dados
db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME'),
}

# Rota inicial
@app.route('/')
def home():
    return jsonify({'mensagem': 'API do Zé Delivery funcionando!'})

# Rota para listar todos os parceiros
@app.route('/partners', methods=['GET'])
def listar_parceiros():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM partners")
        resultados = cursor.fetchall()

        cursor.close()
        conn.close()

        return jsonify(resultados)

    except mysql.connector.Error as erro:
        return jsonify({'erro': str(erro)}), 500

# Executar o app
if __name__ == '__main__':
    app.run(debug=True)
