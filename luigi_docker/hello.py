from flask import Flask

app = Flask(__name__)

def hello_world():
    with open('hello_world_out.txt', 'w') as f:
        f.write("Hello world this is me")

if __name__ == '__main__':
    hello_world()
