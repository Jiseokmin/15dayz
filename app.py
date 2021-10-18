from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('13.124.239.157', 27017)
db = client.date_service


# 샘플데이터 추가

# doc = {'course_name': '샘플코스', 'thema': '추적추적 비내리는 날', 'hashtag': '강남, 서울역',
#      'start_spot': '신논현역', 'via_spot': '스타벅스', 'end_spot': '신논혁역', 'contents': '애인에게 칭찬받는 데이트 코스', 'like': 0}
# db.reviews.insert_one(doc)

@app.route('/')
def home():
    return render_template('detail.html')

#모든 리뷰 가져와서 전달
@app.route('/review', methods=['GET'])
def read_reviews():
    all_reviews = list(db.reviews.find({}, {'_id': False}))
    return jsonify({'reviews': all_reviews})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
