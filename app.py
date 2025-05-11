from app import create_app
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
app = create_app()
app.app_context().push()

if __name__ == '_main_':
    app.run(host="0.0.0.0", debug=False, port=5000)