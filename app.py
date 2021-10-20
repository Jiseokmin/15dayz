from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('13.124.239.157', 27017)
db = client.date_service


# 샘플데이터 추가
#doc = {'course_name': '샘플코스22', 'thema': '따듯한 날', 'hashtag': '강서, 등촌역',
#      'start_spot': '우장산역', 'via_spot': '스타벅스', 'end_spot': '우장역', 'contents': '재미있는 코스', 'like': 1}
#db.reviews.insert_one(doc)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detail')
def detail():
    return render_template('detail.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/reviews')
def show_map():
    return render_template('reviews.html')

#모든 리뷰 가져와서 전달
@app.route('/review', methods=['GET'])
def read_reviews():
    all_reviews = list(db.reviews.find({}, {'_id': False}))
    return jsonify({'reviews': all_reviews})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
