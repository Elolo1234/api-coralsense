from flask import Flask
from routes.usuarios import usuario_bp
from routes.corais import coral_bp
from routes.pesquisas import pesquisa_bp
from routes.pesquisadores import pesquisador_bp

app = Flask(__name__)

app.register_blueprint(usuario_bp)
app.register_blueprint(coral_bp)
app.register_blueprint(pesquisa_bp)
app.register_blueprint(pesquisador_bp)

if __name__ == "__main__":
    app.run(debug=True)
