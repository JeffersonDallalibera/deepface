
import os
import cv2
import numpy as np
from datetime import datetime
from flask import jsonify, request, send_from_directory
from deepface import DeepFace

from app import app, db
from app.models import Aluno, Presenca
from app.utils import allowed_file, extract_face
from app.utils import extract_face

# ... (funções auxiliares: allowed_file, extract_face)

@app.route('/alunos', methods=['POST'])
def cadastrar_aluno():
    """Cadastra um novo aluno."""
    print(request.files);
    if 'foto' not in request.files:
        return jsonify({'error': 'Nenhum arquivo de foto encontrado'}), 400
    foto = request.files['foto']
    if foto.filename == '':
        return jsonify({'error': 'Nenhum arquivo de foto selecionado'}), 400
    if not allowed_file(foto.filename):
        return jsonify({'error': 'Extensão de arquivo não permitida'}), 400

    try:
        nome = request.form['nome']
        matricula = request.form['matricula']
        foto_data = foto.read()

        aluno = Aluno(nome=nome, matricula=matricula, foto=foto_data)
        db.session.add(aluno)
        db.session.commit()

        return jsonify({'message': 'Aluno cadastrado com sucesso!', 'id': aluno.id}), 201
    except Exception as e:
        return jsonify({'error': f'Erro ao cadastrar aluno: {str(e)}'}), 500



@app.route('/chamada', methods=['POST'])
def registrar_chamada():
    """Processa a imagem da turma e registra a presença."""
    if 'imagem_turma' not in request.files:
        return jsonify({'error': 'Nenhum arquivo de imagem encontrado'}), 400

    imagem_turma = request.files['imagem_turma']

    if imagem_turma.filename == '':
        return jsonify({'error': 'Nenhum arquivo de imagem selecionado'}), 400

    if not allowed_file(imagem_turma.filename):
        return jsonify({'error': 'Extensão de arquivo não permitida'}), 400

    try:
        # Carrega a imagem e detecta as faces
        nparr = np.fromstring(imagem_turma.read(), np.uint8)
        imagem = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        faces = extract_face(imagem)
        lista_presenca = []

        for face in faces:
            for aluno in Aluno.query.all():
                print('reconheceu');
                foto_aluno = cv2.imdecode(np.frombuffer(aluno.foto, np.uint8), cv2.IMREAD_COLOR)

                # Utiliza o modelo 'Facenet' para reconhecimento facial
                resultado_comparacao = DeepFace.verify(
                    img1_path=face,
                    img2_path=foto_aluno,
                    model_name='Facenet',
                    detector_backend='opencv',
                    distance_metric='cosine',
                    enforce_detection=False
                )

                if resultado_comparacao['verified']:
                    presenca = Presenca(
                        aluno_id=aluno.id,
                        data=datetime.now().date(),
                        hora=datetime.now().time(),
                        status='Presente'
                    )
                    db.session.add(presenca)

                    lista_presenca.append({
                        'aluno_id': aluno.id,
                        'nome': aluno.nome,
                        'status': 'Presente'
                    })
                    break  # Para de buscar quando encontrar o aluno
            else:
                lista_presenca.append({
                    'aluno_id': None,
                    'nome': 'Desconhecido',
                    'status': 'Não reconhecido'
                })

        db.session.commit()
        return jsonify({'lista_presenca': lista_presenca}), 200

    except Exception as e:
        return jsonify({'error': f'Erro ao processar imagem: {str(e)}'}), 500

# ... (outras rotas para: listar alunos, visualizar fotos, etc.)