from app import app

if __name__ == '__main__':
    app.run(host=app.config['LOCAL_HOST'], port=app.config['LOCAL_PORT'], debug=app.config['DEBUG'])
