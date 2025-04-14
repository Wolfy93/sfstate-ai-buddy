from flask import Flask, render_template, jsonify
from temp_data import GREETINGS, CHAT_HISTORY
# import jsonify

app = Flask(__name__)



@app.route("/")
def hello():
    return render_template('sign.html',greetings = GREETINGS, chat_history =CHAT_HISTORY)

@app.route("/api/chatbot")
def sfsu_api():
    return jsonify(CHAT_HISTORY)


if __name__ == "__main__":
    app.run(debug=True)