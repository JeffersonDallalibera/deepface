from app import app, db
from app.models import Aluno, Presenca

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Aluno': Aluno, 'Presenca': Presenca}

if __name__ == '__main__':
    app.run(debug=True)