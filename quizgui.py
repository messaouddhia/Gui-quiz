import tkinter as tk
from time import sleep

win = tk.Tk()

win.title("Learning game")

class Question:
    def __init__(self,prompt,answer, answer2):
        self.answer = answer
        self.prompt = prompt
        self.answer2 = answer2

def ask():
    global score
    if questions:
        #Check both the possible answers
        if useranwser.get() in (questions[0].answer,questions[0].answer2):
            print("Correct")
            score += 1
        else:
            print("Incorrect")
        questions.pop(0)
        if questions:
            s.set(questions[0].prompt) 
        else:
            print('Done')
            quit() #optional
        useranwser.set('')


question_prompts = [
    "When did Tunisia gain independence? \n 1956 , 1984  , 1965 \n", "What is the captial of tunis ? \n Tunis, Gafsa, Nabuel \n",
    "Who won 2018 football world cup ? \n Italy, France, England \n","how long is the eiffel tower ?\n 324m, 354m, 412m \n",
    "What is the heaviest metal \n Iron, Copper, Uraniam \n "
]

questions = [
    Question(question_prompts[4], "Uraniam","uraniam"),
    Question(question_prompts[0], "1956","1956"),
    Question(question_prompts[1], "Tunis","tunis"),
    Question(question_prompts[2], "France","france"),
    Question(question_prompts[3], "324m","324")
]

s = tk.StringVar()
useranwser = tk.StringVar() 
q = tk.Label(win,textvariable = s)
q.grid(row = 0, column = 0)
u_answer = tk.Entry(win, textvariable = useranwser)
u_answer.grid(row = 1, column = 0)
b = tk.Button(win, text ="Submit", command = ask)
b.grid(row = 2, column =0 ) 

s.set(questions[0].prompt) #Set the initial question 
    
score = 0

win.mainloop()