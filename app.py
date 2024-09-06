from flask import Flask, request, jsonify
import joblib
import json
from interview_prep import answer_question

job_rec_model = joblib.load('model/job_rec_model.pkl')
job_rec_mlb = joblib.load('model/job_rec_mlb_encoder.pkl')
job_rec_list = joblib.load('model/job_rec_list.pkl')

app = Flask(__name__)

@app.route('/job_rec', methods=['POST'])
def job_rec():
    data = request.get_json()
    skills = data['skills']

    skills_vectorized = job_rec_mlb.transform([skills])
    distances, indices = job_rec_model.kneighbors(skills_vectorized, n_neighbors=10)

    unique_candidate_fields = set()

    for index in indices[0]:
        unique_candidate_fields.add(job_rec_list.iloc[index])

    unique_candidate_fields_list = list(unique_candidate_fields)

    if data:
        return jsonify({'job recommendation': unique_candidate_fields_list[:3]}), 200
    else:
        return jsonify({"message": "No data received"}), 400


@app.route('/interview_prep', methods=['POST'])
def interview_prep():
    data = request.get_json()
    cv = json.loads(data['cv_data'])

    answers = answer_question(cv)
    if data:
        return jsonify(answers), 200
    else:
        return jsonify({"message": "No data received"}), 400

if __name__ == '__main__':
    app.run(debug=True)
