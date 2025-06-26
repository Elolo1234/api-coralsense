from flask import Flask
from routes.coral_route import coral_bp
from routes.pesquisa_route import pesquisa_bp
from routes.pesquisador_route import pesquisador_bp

app = Flask(__name__)


app.register_blueprint(coral_bp)
app.register_blueprint(pesquisa_bp)
app.register_blueprint(pesquisador_bp)

if __name__ == "__main__":
    app.run(debug=True)
