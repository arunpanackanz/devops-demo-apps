from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    user_ip = request.remote_addr
    return f"""
    <h1>You are hacked ! ! !</h1>
    <p>Your IP address is: <b>{user_ip}</b></p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
