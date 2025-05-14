from app import create_app
app = create_app()
app.app_context().push()

if __name__ == '_main_':
    app.run(host="0.0.0.0", debug=True, port=5000)