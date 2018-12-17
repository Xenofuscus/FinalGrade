import re
from flask import Flask, flash, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("main_page.html")

@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    # Get input from form:
    sfirstQuart = request.form.get('firstQuart')
    ssecondQuart = request.form.get('secondQuart')
    stargetFinal = request.form.get('targetSem')
    notNumber = re.compile('[^\d]')
    if notNumber.search(sfirstQuart) or notNumber.search(ssecondQuart):
        flash("Grades must be a number!")
        return render_template("main_page.html", output="")
    # Check if they are valid grades:
    firstQuart = int(sfirstQuart)
    secondQuart = int(ssecondQuart)
    targetFinal = int(stargetFinal)
    if firstQuart > 100 or firstQuart < 0 or secondQuart > 100 or secondQuart < 0:
        flash("Grades must be between 0-100!")
        return render_template("main_page.html", output="")

    # Do the stuff
    finalGrade = calc_target_final_grade(firstQuart, secondQuart, targetFinal)
    if finalGrade < 0:
        outString = "You could skip the final :)"
    elif finalGrade > 100:
        outString = "Oof! Choose a more realistic target grade :("
    else:
        outString = "Aim for a " + str(finalGrade) + " on the final for a final grade of " + str(targetFinal) + " in the class."
    return render_template("main_page.html", output=outString)

def calc_target_final_grade(first, second, final):
    return (10 * final) - (4.5 * (first + second))
