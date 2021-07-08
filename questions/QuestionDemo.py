##
#  This program shows a simple quiz with two question types.
#

import os
from questions import Question, ChoiceQuestion, NumericQuestion, FillInQuestion, MultiChoiceQuestion

def main() :
    first = Question()
    first.setText("Who was the inventor of Python?")
    first.setAnswer("Guido van Rossum")

    second = ChoiceQuestion()
    second.setText("In which country was the inventor of Python born?")
    second.addChoice("Australia", False)
    second.addChoice("Canada", False)
    second.addChoice("Netherlands", True)
    second.addChoice("United States", False)

    third = NumericQuestion()
    third.setText("This is a test question for Q3, 10 + 0.1 = ?")
    third.setAnswer(10)
    

    fourth = FillInQuestion()
    fourth.setAnswer("Guido van Rossum")
    fourth.setText("The inventor of Python was", fourth._answer)

    fifth = MultiChoiceQuestion()
    fifth.setText("Which of the answers are true: (Please separate your answers with a space)")
    fifth.addChoice("true", True)
    fifth.addChoice("true", True)
    fifth.addChoice("false", False)
    fifth.addChoice("true", True)
    fifth.addChoice("false", False)

   
    presentQuestion(first)
    print()
    presentQuestion(second)
    print()
    presentQuestion(third)
    print()
    presentQuestion(fourth)
    print()
    presentQuestion(fifth)
    print()
    
    os.system("pause")


## Presents a question to the user and checks the response.
#  @param q the question
#
def presentQuestion(q) :
    q.display()   # Uses dynamic method lookup.
    response = input("Your answer: ")
    print(q.checkAnswer(response))   # checkAnswer uses dynamic method lookup.
   
# Start the program.
main()
