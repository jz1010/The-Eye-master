from website import create_app
import os

app = create_app()

if __name__ == '__main__':
    app.secret_key=os.urandom(12)
    app.run(host="192.168.86.39", port="5000", debug=True)