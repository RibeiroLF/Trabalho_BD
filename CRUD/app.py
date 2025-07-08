from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from db import get_db_connection
from datetime import date

def format_query_results(results):
    formatted_results = []
    for row in results:
        formatted_row = {}
        for key, value in row.items():
            if isinstance(value, date):
                formatted_row[key] = value.strftime('%Y-%m-%d')
            else:
                formatted_row[key] = value
        formatted_results.append(formatted_row)
    return formatted_results

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/funcionarios', methods=['GET'])
def get_funcionarios():
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT cpf, nome, sexo, dt_nasc, cidade, telefone FROM funcionarios")
            results = cursor.fetchall()
            return jsonify(format_query_results(results))
    finally:
        conn.close()

@app.route('/funcionarios', methods=['POST'])
def add_funcionario():
    novo = request.json
    sql = "INSERT INTO funcionarios (cpf, nome, sexo, dt_nasc, uf, cidade, localidade, bairro, telefone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, (novo['cpf'], novo['nome'], novo['sexo'], novo['dt_nasc'], novo['uf'], novo['cidade'], novo['localidade'], novo['bairro'], novo['telefone']))
        conn.commit()
        return jsonify({'message': 'Funcionário adicionado com sucesso!'}), 201
    finally:
        conn.close()

@app.route('/funcionarios/<int:cpf>', methods=['PUT'])
def update_funcionario(cpf):
    dados = request.json
    sql = "UPDATE funcionarios SET nome=%s, cidade=%s, telefone=%s WHERE cpf=%s"
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, (dados['nome'], dados['cidade'], dados['telefone'], cpf))
        conn.commit()
        return jsonify({'message': 'Funcionário atualizado com sucesso!'})
    finally:
        conn.close()

@app.route('/funcionarios/<int:cpf>', methods=['DELETE'])
def delete_funcionario(cpf):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM funcionarios_buffet WHERE cpf = %s", (cpf,))
            cursor.execute("DELETE FROM funcionarios_dependentes WHERE cpf_fun = %s", (cpf,))
            cursor.execute("DELETE FROM funcionarios_funcoes WHERE cpf = %s", (cpf,))
            cursor.execute("DELETE FROM funcionarios_situacoes WHERE cpf = %s", (cpf,))
            cursor.execute("DELETE FROM funcionarios WHERE cpf = %s", (cpf,))
        conn.commit() 
        return jsonify({'message': 'Funcionário e todas as suas associações foram deletados com sucesso!'})
    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

@app.route('/pratos', methods=['GET'])
def get_pratos():
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT cod_prato, nome_prato, acompanhamento FROM pratos")
            return jsonify(cursor.fetchall())
    finally:
        conn.close()

@app.route('/pratos', methods=['POST'])
def add_prato():
    novo = request.json
    sql_get_max = "SELECT MAX(cod_prato) as max_id FROM pratos"
    sql_insert = "INSERT INTO pratos (cod_prato, nome_prato, acompanhamento) VALUES (%s, %s, %s)"
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql_get_max)
            result = cursor.fetchone()
            max_id = result['max_id'] if result and result['max_id'] else 0
            new_id = max_id + 1
            cursor.execute(sql_insert, (new_id, novo['nome_prato'], novo['acompanhamento']))
        conn.commit()
        return jsonify({'message': 'Prato adicionado com sucesso!', 'cod_prato': new_id}), 201
    finally:
        conn.close()

@app.route('/pratos/<int:cod_prato>', methods=['PUT'])
def update_prato(cod_prato):
    dados = request.json
    sql = "UPDATE pratos SET nome_prato=%s, acompanhamento=%s WHERE cod_prato=%s"
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, (dados['nome_prato'], dados['acompanhamento'], cod_prato))
        conn.commit()
        return jsonify({'message': 'Prato atualizado com sucesso!'})
    finally:
        conn.close()

@app.route('/pratos/<int:cod_prato>', methods=['DELETE'])
def delete_prato(cod_prato):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM buffet_pratos WHERE cod_prato = %s", (cod_prato,))
            cursor.execute("DELETE FROM pratos_ingredientes WHERE cod_prato = %s", (cod_prato,))
            cursor.execute("DELETE FROM pratos WHERE cod_prato = %s", (cod_prato,))
        conn.commit()
        return jsonify({'message': 'Prato deletado com sucesso!'})
    finally:
        conn.close()

@app.route('/bebidas', methods=['GET'])
def get_bebidas():
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT cod_bebida, nome_bebida FROM bebidas")
            return jsonify(cursor.fetchall())
    finally:
        conn.close()

@app.route('/bebidas', methods=['POST'])
def add_bebida():
    novo = request.json
    sql_get_max = "SELECT MAX(cod_bebida) as max_id FROM bebidas"
    sql_insert = "INSERT INTO bebidas (cod_bebida, nome_bebida) VALUES (%s, %s)"
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql_get_max)
            result = cursor.fetchone()
            max_id = result['max_id'] if result and result['max_id'] else 0
            new_id = max_id + 1
            cursor.execute(sql_insert, (new_id, novo['nome_bebida']))
        conn.commit()
        return jsonify({'message': 'Bebida adicionada com sucesso!', 'cod_bebida': new_id}), 201
    finally:
        conn.close()

@app.route('/bebidas/<int:cod_bebida>', methods=['PUT'])
def update_bebida(cod_bebida):
    dados = request.json
    sql = "UPDATE bebidas SET nome_bebida=%s WHERE cod_bebida=%s"
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, (dados['nome_bebida'], cod_bebida))
        conn.commit()
        return jsonify({'message': 'Bebida atualizada com sucesso!'})
    finally:
        conn.close()

@app.route('/bebidas/<int:cod_bebida>', methods=['DELETE'])
def delete_bebida(cod_bebida):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM buffet_bebidas WHERE cod_bebida = %s", (cod_bebida,))
            cursor.execute("DELETE FROM bebidas_fornecedores WHERE cod_bebida = %s", (cod_bebida,))
            cursor.execute("DELETE FROM bebidas WHERE cod_bebida = %s", (cod_bebida,))
        conn.commit()
        return jsonify({'message': 'Bebida deletada com sucesso!'})
    finally:
        conn.close()

@app.route('/fornecedores', methods=['GET'])
def get_fornecedores():
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT cod_fornecedor, nome_fornecedor, telefone, dt_ini FROM fornecedores")
            results = cursor.fetchall()
            return jsonify(format_query_results(results))
    finally:
        conn.close()

@app.route('/fornecedores', methods=['POST'])
def add_fornecedor():
    novo = request.json
    sql_get_max = "SELECT MAX(cod_fornecedor) as max_id FROM fornecedores"
    sql_insert = "INSERT INTO fornecedores (cod_fornecedor, nome_fornecedor, telefone, dt_ini) VALUES (%s, %s, %s, %s)"
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql_get_max)
            result = cursor.fetchone()
            max_id = result['max_id'] if result and result['max_id'] else 0
            new_id = max_id + 1
            cursor.execute(sql_insert, (new_id, novo['nome_fornecedor'], novo['telefone'], novo['dt_ini']))
        conn.commit()
        return jsonify({'message': 'Fornecedor adicionado com sucesso!', 'cod_fornecedor': new_id}), 201
    finally:
        conn.close()

@app.route('/fornecedores/<int:cod_fornecedor>', methods=['PUT'])
def update_fornecedor(cod_fornecedor):
    dados = request.json
    sql = "UPDATE fornecedores SET nome_fornecedor=%s, telefone=%s, dt_ini=%s WHERE cod_fornecedor=%s"
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, (dados['nome_fornecedor'], dados['telefone'], dados['dt_ini'], cod_fornecedor))
        conn.commit()
        return jsonify({'message': 'Fornecedor atualizado com sucesso!'})
    finally:
        conn.close()

@app.route('/fornecedores/<int:cod_fornecedor>', methods=['DELETE'])
def delete_fornecedor(cod_fornecedor):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM ingredientes_fornecedores WHERE cod_fornecedor = %s", (cod_fornecedor,))
            cursor.execute("DELETE FROM bebidas_fornecedores WHERE cod_fornecedor = %s", (cod_fornecedor,))
            cursor.execute("DELETE FROM fornecedores WHERE cod_fornecedor = %s", (cod_fornecedor,))
        conn.commit()
        return jsonify({'message': 'Fornecedor deletado com sucesso!'})
    finally:
        conn.close()

@app.route('/ingredientes', methods=['GET'])
def get_ingredientes():
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            sql = """
                SELECT i.cod_ingrediente, i.nome_ingrediente, i.unidade, COALESCE(e.qtd_ingrediente, 0) as quantidade
                FROM ingredientes i
                LEFT JOIN estoque_ingredientes e ON i.cod_ingrediente = e.cod_ingrediente
            """
            cursor.execute(sql)
            return jsonify(cursor.fetchall())
    finally:
        conn.close()

@app.route('/ingredientes', methods=['POST'])
def add_ingrediente():
    novo = request.json
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT MAX(cod_ingrediente) as max_id FROM ingredientes")
            max_id = (cursor.fetchone() or {}).get('max_id') or 0
            new_id = max_id + 1
            
            cursor.execute("INSERT INTO ingredientes (cod_ingrediente, nome_ingrediente, unidade) VALUES (%s, %s, %s)", (new_id, novo['nome_ingrediente'], novo['unidade']))
            cursor.execute("INSERT INTO estoque_ingredientes (cod_ingrediente, qtd_ingrediente) VALUES (%s, %s)", (new_id, novo.get('quantidade', 0)))
        conn.commit()
        return jsonify({'message': 'Ingrediente e estoque inicial criados!', 'cod_ingrediente': new_id}), 201
    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

@app.route('/ingredientes/<int:cod_ingrediente>', methods=['PUT'])
def update_ingrediente(cod_ingrediente):
    dados = request.json
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("UPDATE ingredientes SET nome_ingrediente=%s, unidade=%s WHERE cod_ingrediente=%s", (dados['nome_ingrediente'], dados['unidade'], cod_ingrediente))
            cursor.execute("UPDATE estoque_ingredientes SET qtd_ingrediente=%s WHERE cod_ingrediente=%s", (dados.get('quantidade', 0), cod_ingrediente))
        conn.commit()
        return jsonify({'message': 'Ingrediente e estoque atualizados!'})
    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

@app.route('/ingredientes/<int:cod_ingrediente>', methods=['DELETE'])
def delete_ingrediente(cod_ingrediente):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM estoque_ingredientes WHERE cod_ingrediente = %s", (cod_ingrediente,))
            cursor.execute("DELETE FROM pratos_ingredientes WHERE cod_ingrediente = %s", (cod_ingrediente,))
            cursor.execute("DELETE FROM ingredientes_fornecedores WHERE cod_ingrediente = %s", (cod_ingrediente,))
            cursor.execute("DELETE FROM ingredientes_compra WHERE cod_ingrediente = %s", (cod_ingrediente,))
            cursor.execute("DELETE FROM ingredientes WHERE cod_ingrediente = %s", (cod_ingrediente,))
        conn.commit()
        return jsonify({'message': 'Ingrediente deletado com sucesso!'})
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
