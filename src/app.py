from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return "我家橘橘要滿一歲了!!!!!!!采妮要給橘橘禮物"
if __name__=='__main__':
    app.run()