from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/SurveyManager', methods=['POST'])
def survey_manager():
    # Recebe os dados enviados na requisição POST
    data = request.json

    # Imprime os dados no terminal
    print("Dados recebidos:", data)

    # Retorna uma resposta para o cliente
    return jsonify({"message": "Dados recebidos com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)
