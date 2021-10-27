from flask import Flask, render_template, jsonify, url_for, session, request, redirect
from pymongo import MongoClient
from settings import *

app = Flask(__name__, template_folder='templates')

client = MongoClient(PROJECT_SITE_URL, 27017)
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


@app.route('/user_register', methods=['POST'])
def user_register():
    firstname_receive = request.form['firstname_give']
    sex_receive = request.form['sex_give']
    regi_email_receive = request.form['regi_email_give']
    regi_password_receive = request.form['regi_password_give']
    password_confirm_receive = request.form['password_confirm_give']

    if db.login.find_one({'userid': regi_email_receive}) :
        return jsonify({'msg': '이미 가입되어 있는 ID입니다.! 새로운 ID로 가입하세요!'})
    else :
        if regi_password_receive == password_confirm_receive :
            doc_regi = {
                'firstname': firstname_receive,
                'sex': sex_receive,
                'regi_email': regi_email_receive,
                'regi_password': regi_password_receive,
                'password_comfirm': password_confirm_receive,
            }
            doc_login = {
                'userid': regi_email_receive,
                'password': regi_password_receive,
            }

            db.user_regi.insert_one(doc_regi)
            db.login.insert_one(doc_login)
            return jsonify({'msg': '가입 성공! email ID와 Password를 이용해서 Login하세요!'})
        else :
            return jsonify({'msg': '가입 실패! Password를 다시 확인해 주세요!'})


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


@app.route('/result/list', methods = ['GET'])
def result_course():
    keyword = request.args.get("keyword_give")
    result_cou_id = {}
    find_cou_id = list(db.courses.find({}))

    for index, id in enumerate(find_cou_id):
        result_cou_id[index] = str(id['_id'])

    if keyword == '':
        result_cou = list(db.courses.find({}, {'_id': False}))
    else:
        result_cou = list(db.courses.find({'location': keyword}, {'_id': False}))
    return jsonify({'result_course': result_cou, 'result_cou_id': result_cou_id})

@app.route('/making', methods=['POST'])
def make_course():
    c_name_receive =  request.form['c_name_give']
    location_receive = request.form['location_give']
    theme_receive = request.form['theme_give']
    time_receive = request.form['time_give']
    budgets_receive = request.form['budgets_give']
    main_location_receive = request.form['main_location_give']
    via1_receive = request.form['via1_give']
    via1_comment_receive = request.form['via1_comment_give']
    via2_receive = request.form['via2_give']
    via2_comment_receive = request.form['via2_give']
    via3_receive = request.form['via3_give']
    via3_comment_receive = request.form['via3_give']
    comment_receive = request.form['comment_give']

    doc = {
        'c_name' : c_name_receive,                    
        'location': location_receive,
        'theme': theme_receive,
        'time': time_receive,
        'budgets': budgets_receive,
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
