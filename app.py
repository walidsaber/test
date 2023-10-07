from flask import Flask, render_template, request

app = Flask(__name__)

# Sample math exercises
exercises = [
    {"question": "2 + 3 =", "answer": "5"},
    {"question": "5 - 2 =", "answer": "3"},
    {"question": "4 * 6 =", "answer": "24"}
]

@app.route('/')
def index():
    return render_template('index.html', exercises=exercises)

@app.route('/check', methods=['POST'])
def check_answer():
    user_answer = request.form.get('answer')
    exercise_index = int(request.form.get('exercise_index'))

    correct_answer = exercises[exercise_index]['answer']
    if user_answer == correct_answer:
        result = "Correct!"
    else:
        result = "Incorrect. Try again."

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
