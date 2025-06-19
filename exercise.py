import tkinter as tk
back_exercises=["Cat-Cow", "Shoulder Blade Squeeze", "Bird-Dog", "Superman hold", "Bent-over Rows", "Towel Rows", "Australian Pull-ups", "Deadlifts", "Renegade Rows"]
leg_exercises=["Wall Sit", "Step Touch", "Glute Brige", "Lunges", "Sumo Squats", "Single Leg Glute Brige", "Jump Squats", "Bulgarian Split Squats", "Wall Sit March"]
abs_exercises=["Dead Bug", "Seated Knee lifts", "Standing Oblique Crunches", "Leg Raises", "Russian Twists", "Plank", "Plank to Elbow Tap", "Bicycle Crunches", "V-ups"]
root=tk.Tk()
root.title("Exercise Generator")

answers={}

def question1_hide(answer):
    label1.forget()
    button_easy.forget()
    button_medium.forget()
    button_hard.forget()

    answers['question1']=answer
     
    label2=tk.Label(root, text="Pick a body area to train")
    label2.pack(pady=25)

    button_back=tk.Button(root, text="back", command=lambda: question2_hide("back"))
    button_back.pack(pady=25)

    button_legs=tk.Button(root, text="legs", command=lambda: question2_hide("legs"))
    button_legs.pack(pady=25)

    button_abs=tk.Button(root, text="abs", command=lambda: question2_hide("abs"))
    button_abs.pack(pady=25)
    
    def question2_hide(answer):
        label2.forget()
        button_back.forget()
        button_legs.forget()
        button_abs.forget()

        answers['question2']=answer

        results=give_exercise(answers)
        label_exercises=tk.Label(text=results)
        label_exercises.pack(pady=12)



def give_exercise(answers):
    qu1=answers.get('question1')
    qu2=answers.get('question2')

    if qu1=='Easy' and qu2=='back':
        return back_exercises[0:3]
    elif qu1=='Medium' and qu2=='back':
        return back_exercises[3:6]
    elif qu1=='Hard' and qu2=='back':
        return back_exercises[6:9] 
    
    elif qu1=='Easy' and qu2=='legs':
        return leg_exercises[0:3]
    elif qu1=='Medium' and qu2=='legs':
        return leg_exercises[3:6]
    elif qu1=='Hard' and qu2=='legs':
        return leg_exercises[6:9]
    
    elif qu1=='Easy' and qu2=='abs':
        return back_exercises[0:3]
    elif qu1=='Medium' and qu2=='abs':
        return back_exercises[3:6]
    elif qu1=='Hard' and qu2=='abs':
        return back_exercises[6:9]
    

label1=tk.Label(root, text="Chose the intensity level")
label1.pack(pady=20)


button_easy=tk.Button(root, text="Easy", command=lambda: question1_hide("Easy"))
button_easy.pack(pady=25)


button_medium=tk.Button(root, text="Medium", command=lambda: question1_hide("Medium"))
button_medium.pack(pady=25)


button_hard=tk.Button(root, text="Hard", command=lambda: question1_hide("Hard"))
button_hard.pack(pady=25)




root.mainloop()
