import random, copy
from alapanaSupport import *
from htmlTemplatesQuiz import *
from htmlTemplatesZen import *
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from string import Template

app = Flask(__name__)

alapanasDict = copy.deepcopy(finalAlapanasDict)

def shuffle(alas):
    selections = []
    i = 0
    while i < len(alas):
        selection = random.choice(list(alas.keys()))
        if selection not in selections:
           selections.append(selection)
           i = i+1
    return selections

# GLOBALS ###########################
shuffledAlapanas = shuffle(alapanasDict)
tenAlapanas = shuffledAlapanas[0:5]
times = 0
lnk = ""
numCorrect = 0


@app.route('/')
@app.route('/return', methods=['POST'])
def startPage():
    return render_template("main.html")

# ZEN -------------------------------------
@app.route('/zen', methods=['POST'])
def zenPage():
    return render_template("zen.html")


@app.route('/next', methods=['POST'])
def nextOne():
    global shuffledAlapanas
    a = random.choice(shuffledAlapanas)
    raga = myRagaDict[alapanasDict[a]]
    return(HTML_TEMPLATE_C.substitute(alap=a, rag=raga))


# QUIZ ------------------------------------
@app.route('/quiz', methods=['POST'])
@app.route('/again', methods=['POST'])
def ragaPage():
    global times
    global shuffledAlapanas
    global tenAlapanas
    global lnk
    global numCorrect
    # reset everything
    shuffledAlapanas = shuffle(alapanasDict)
    tenAlapanas = shuffledAlapanas[0:5]
    times = 0
    lnk = ""
    numCorrect = 0
    return render_template('quiz.html')


@app.route('/alapanaQuiz', methods=['POST'])
def alapanaQuiz():
    global times
    global shuffledAlapanas
    global tenAlapanas
    global lnk
    global numCorrect
    if times < 5:
        a = tenAlapanas[times]
        times = times + 1
        lnk = a
        return(HTML_TEMPLATE_Q.substitute(alap=a))
    else:
        return(HTML_TEMPLATE_DONE.substitute(num=numCorrect))


@app.route('/evaluate', methods=['POST'])
def is_correct():
    global lnk
    global numCorrect
    answered = request.form['answerField']
    raga = myRagaDict[alapanasDict[lnk]]
    if raga == answered:
        numCorrect = numCorrect + 1
        return(HTML_TEMPLATE_A.substitute(result="CORRECT!", num=numCorrect, rag=raga))
    else:
        return(HTML_TEMPLATE_A.substitute(result="INCORRECT", num=numCorrect, rag=raga))

if __name__ == '__main__':
    app.run(debug=True)
