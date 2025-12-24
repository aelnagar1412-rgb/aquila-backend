from flask import Flask
from status import status_bp   # عدل الاسم حسب ملفك

def create_app():
    app = Flask(__name__)

    # Register Blueprints
    app.register_blueprint(status_bp)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
