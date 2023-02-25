# name: main.py
# desc: This is a main python file that will run our application

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)