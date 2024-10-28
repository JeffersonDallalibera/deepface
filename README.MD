## Sistema de Chamada Facial com Flask e DeepFace

Este projeto implementa um backend em Python com Flask para um sistema de chamada facial utilizando a biblioteca DeepFace para reconhecimento facial. 

**Funcionalidades:**

- Cadastro de alunos com foto.
- Registro de presenças com base em reconhecimento facial em imagens enviadas.
- Retorno da lista de presença com status (Presente, Não Reconhecido).

**Tecnologias Utilizadas:**

- **Backend:**
    - Python 3.7+
    - Flask
    - Flask-SQLAlchemy
    - Flask-Migrate
    - DeepFace
    - OpenCV
    - PostgreSQL

**Pré-requisitos:**

- Python 3.7+ instalado.
- PostgreSQL instalado e configurado.
- Um editor de código de sua preferência (VS Code, PyCharm, etc.).

**Como Executar o Projeto:**

1. **Clone o Repositório:**

   ```bash
   git clone https://github.com/seu_usuario/nome_do_repositorio.git
   cd nome_do_repositorio
   ```

2. **Crie e ative o Ambiente Virtual:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate.bat  # Windows
   ```

3. **Instale as Dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o Banco de Dados:**

   - Crie o banco de dados PostgreSQL (se ainda não existir).
   - Atualize as configurações do banco de dados em `config.py`.

5. **Crie as Tabelas do Banco de Dados:**

   ```bash
   flask db init
   flask db migrate -m "migração inicial"
   flask db upgrade
   ```

6. **Inicie o Servidor Flask:**

   ```bash
   flask run
   ```

7. **Acesse a API:**

   - A API estará disponível em `http://127.0.0.1:5000/`.

**Rotas da API:**

- **POST /alunos:** Cadastra um novo aluno.
    - Dados: 
        - `nome` (string)
        - `matricula` (string)
        - `foto` (arquivo de imagem)
- **POST /chamada:** Processa a imagem da turma e retorna a lista de presença.
    - Dados: 
        - `imagem_turma` (arquivo de imagem)

**Observações:**

- Certifique-se de ter as bibliotecas `opencv-python`, `deepface` e `psycopg2-binary` instaladas em seu ambiente virtual.
- A precisão do reconhecimento facial depende da qualidade da imagem, iluminação e outros fatores.
- Ajuste os parâmetros do DeepFace em `routes.py` para otimizar o reconhecimento facial para o seu caso de uso.


**Contribuições:**

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

**Autor:**

[Seu Nome]

**Licença:**

[MIT](https://choosealicense.com/licenses/mit/)
