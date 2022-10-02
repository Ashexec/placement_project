# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 21:06:18 2022

@author: dell
"""

from tkinter import *

from tkinter import messagebox as mb

import json 
 
class Quiz:
    
    def __init__(self):
    
        self.question_number=0
        
        self.display_title()
        
        self.display_question()
        
        self.opt_selected=IntVar()
        
        self.opts=self.radio_buttons()
        
        self.display_options()
        
        self.buttons()
        
        self.data_size=len(question)
        
        self.correct=0
        
    def display_result(self):
          
        wrong_count= self.data_size-self.correct
            
        correct=f"Correct: {self.correct}"
        wrong=f"Wrong: {wrong_count}"
            
        score= int(self.correct/self.data_size * 100)
            
        result= f"Score: {score}%"
            
        mb.showinfo("Result", f"{result} \n{correct} \n{wrong}" )
    def check_ans(self, question_number):
        
        if self.opt_selected.get()== answer[question_number]:
            return TRUE
        
    def next_button(self):
        
        if self.check_ans(self.question_number):
            
            self.correct+=1
            
        self.question_number+=1
        
        if self.question_number== self.data_size:
            self.display_result()
            
            gui.destroy()
        else:
            self.display_question()
            self.display_options()
    
    def buttons(self):
        
        next_button= Button(gui, text= "Next", command=self.next_button,
                            width=10, bg='blue', fg='black' ,font= ('ariel',16,'bold'))
        next_button.place(x=350,y=380)
        
        quit_button= Button(gui, text='Quit', command= gui.destroy, 
                            width=5, bg= 'red', fg='blue', font=('ariel',14,'bold' ))
     
        quit_button.place(x=700, y=50)
        
    def display_options(self):
        val=0
        
        self.opt_selected.set(0)
        
        for option in options[self.question_number]:
            self.opts[val]['text']=option
            val+=1
    
    def display_question(self):
        
        q_no= Label(gui, text=question[self.question_number], width=60,
                     font=( 'ariel' ,16, 'bold' ), anchor= 'w')
        
        q_no.place(x=70, y=100)
            
    def display_title(self):
         
        # The title to be shown
        title = Label(gui, text="Indian Economy QUIZ",
        width=50, bg="blue",fg="white", font=("ariel", 20, "bold"))
         
        # place of the title
        title.place(x=0, y=2)
        
    def radio_buttons(self):
         
        # initialize the list with an empty list of options
        q_list = []
         
        # position of the first option
        y_pos = 150
         
        # adding the options to the list
        while len(q_list) < 4:
             
            # setting the radio button properties
            radio_btn = Radiobutton(gui,text=" ",variable=self.opt_selected,
            value = len(q_list)+1,font = ("ariel",14))
             
            # adding the button to the list
            q_list.append(radio_btn)
             
            # placing the button
            radio_btn.place(x = 100, y = y_pos)
             
            # incrementing the y-axis position by 40
            y_pos += 40
         
        # return the radio buttons
        return q_list

gui= Tk()

gui.geometry("800x450")

gui.title('Indian Economy quiz')

with open('quiz.json') as f:
         data=json.load(f)

question=(data['question'])
options=(data['options'])
answer=(data['answer'])

quiz=Quiz()

gui.mainloop()



        
    


