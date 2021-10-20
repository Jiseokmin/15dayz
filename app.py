from flask import Flask, render_template, jsonify, url_for, session, request, redirect
from pymongo import MongoClient

app = Flask(__name__, template_folder='templates')

client = MongoClient('13.124.239.157', 27017)
db = client.date_service

app.secret_key = "99d7e201187334217ba4f1c51a72e412"
''' DB login 입력
doc = {
    'name': 'Tester',
    'userid': '111@111.com',
    'password': '111',
}

db.login.insert_one(doc)
'''

# 샘플데이터 추가
# doc = {'course_name': '샘플코스22', 'thema': '따듯한 날', 'hashtag': '강서, 등촌역',
#      'start_spot': '우장산역', 'via_spot': '스타벅스', 'end_spot': '우장역', 'contents': '재미있는 코스', 'like': 1}
# db.reviews.insert_one(doc)


@app.route('/')
def home():
    if "userID" in session:
        return render_template("index.html", username=session.get("userID"), login=True)
    else:
        return render_template("index.html", login=False)


@app.route("/login", methods=["get"])
def login():
    _id_ = request.args.get("email")
    _password_ = request.args.get("password")

    if db.login.find_one({'userid': _id_}) and db.login.find_one({'password': _password_}):
        session["userID"] = _id_
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))


@app.route("/logout")
def logout():
    session.pop("userID")
    return redirect("home")


@app.route('/result')
def result():
    return render_template('result.html')


@app.route('/reviews')
def show_map():
    return render_template('reviews.html')

# 모든 리뷰 가져와서 전달


@app.route('/review', methods=['GET'])
def read_reviews():
    all_reviews = list(db.reviews.find({}, {'_id': False}))
    return jsonify({'reviews': all_reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
