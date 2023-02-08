from flask import Flask, render_template, request
import database as db
app = Flask(__name__)

@app.route("/")
def index():
    quizes = db.getQuiz()
    return render_template("index.html",quizes=quizes)

@app.route("/quiz",methods=['GET','POST'])
def showQuestions():
    if request.method == "POST":
        qid = request.form.get("quiz_id")
        score = 0
        questions = db.getQuestion(qid)
        mapper = {}
        for q in questions:
            mapper[q[0]]=q[4]

        print(mapper)

        for q,ans in request.form.items():
            if "," in q:
                print(q)
                quid = q.split(",")[1]
                expected = mapper[int(quid)]
                if expected == ans:
                    score += 1
        return render_template("quiz.html",questions=questions, quiz_id=qid, score=score)



    quiz_id = request.args.get("id")
    questions = db.getQuestion(quiz_id)
    return render_template("quiz.html",questions=questions, quiz_id=quiz_id)

app.run(debug=True)