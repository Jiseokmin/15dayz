from flask import Flask, render_template, jsonify, url_for, session, request, redirect
from pymongo import MongoClient
from settings import *

app = Flask(__name__, template_folder='templates')

client = MongoClient('13.124.239.157', 27017)
db = client.date_service
test_db = client.mapcontrol

app.secret_key = SECRET_KEY

doc_login = {
    'name': 'Tester',
    'userid': TEST_USER_ID,
    'password': TEST_USER_PW,
}

# 프로그램 실행할 때마다 DB에 insert가 되어서 이 부분 주석 처리하겠습니다 !  db.login.insert_one(doc_login)
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


@app.route('/index')
def index():
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
        return render_template("detail.html", username=session.get("userID"), login=True)
    else:
        return render_template("detail2.html", login=False)


@app.route("/logout")
def logout():
    session.pop("userID", None)
    return redirect("index")
    # return render_template("index.html", login=False)


@app.route('/tests', methods=['GET'])
def read_test():
    all_reviews = list(test_db.mapcontrol2.find({}, {'_id': False}))
    return jsonify({'reviews': all_reviews})


@app.route('/detail')
def detail():
    return render_template('detail.html')


@app.route('/result')
def result():
    return render_template('result.html')


@app.route('/reviews')
def show_map():
    return render_template('reviews.html')


@app.route('/making')
def making():
    return render_template('making.html')


@app.route('/making', methods=['POST'])
def make_course():
    location_receive = request.form['location_give']
    thema_receive = request.form['thema_give']
    time_receive = request.form['time_give']
    budget_receive = request.form['budget_give']
    main_location_receive = request.form['main_location_give']
    via1_receive = request.form['via1_give']
    via1_comment_receive = request.form['via1_comment_give']
    via2_receive = request.form['via2_give']
    via2_comment_receive = request.form['via2_give']
    via3_receive = request.form['via3_give']
    via3_comment_receive = request.form['via3_give']
    comment_receive = request.form['comment_give']

    doc = {
        'location': location_receive,
        'thema': thema_receive,
        'time': time_receive,
        'budget': budget_receive,
        'main_location': main_location_receive,
        'via1': via1_receive,
        'via1_comment': via1_comment_receive,
        'via2': via2_receive,
        'via2_comment': via2_comment_receive,
        'via3': via3_receive,
        'via3_comment': via3_comment_receive,
        'comment': comment_receive
    }

    db.courses.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})


@app.route('/detail2')
def detail2():
    return render_template('detail2.html')

@app.errorhandler(404) 
def page_not_found(error):
    return render_template('404notfound.html')




# 모든 리뷰 가져와서 전달


@app.route('/review', methods=['GET'])
def read_reviews():
    all_reviews = list(db.reviews.find({}, {'_id': False}))
    return jsonify({'reviews': all_reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
