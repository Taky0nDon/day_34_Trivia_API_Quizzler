# import tkinter.messagebox
from tkinter import ttk, messagebox
import tkinter as tk
import quiz_brain
import data

THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, "italic")


# Grid has 2 columns and 3 rows
class QuizInterface:

    def __init__(self, quiz_object: quiz_brain.QuizBrain):
        self.selection = None
        self.quiz_object = quiz_object
        self.window = tk.Tk()
        self.window.title = "Quizzler"
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.cross_image = tk.PhotoImage(file="./images/false.png")
        self.check_image = tk.PhotoImage(file="images/true.png")

        self.category_choices = ttk.Combobox(
            state="readonly",
            values=data.list_of_categories
        )
        self.category_choices.grid(column=0, row=0)

        self.change_cat_but = tk.Button(text="Pick New Category", command=self.change_category)
        self.change_cat_but.grid(column=0, row=1)

        self.score_label = tk.Label(text="Score: 0/0", bg=THEME_COLOR, font=("Arial", 14, "normal"), fg="white")
        self.score_label.grid(column=1, row=0)
# todo: make the canvas reactive? so it gets bigger if the text takes up too much space.
        self.question_canvas = tk.Canvas(height=300, width=300, bg="white")
        self.canvas_question_text = self.question_canvas.create_text((150, 150), text="place holder",
                                                                     font=QUESTION_FONT, width=250, justify="center",
                                                                     fill=THEME_COLOR)
        self.question_canvas.grid(column=0, columnspan=2, row=2, pady=50)

        self.check_button = tk.Button(image=self.check_image, padx=20, borderwidth=0, highlightthickness=0,
                                      command=lambda: self.submit_answer("true"))
        self.check_button.grid(column=0, row=3)

        self.cross_button = tk.Button(image=self.cross_image, padx=20, borderwidth=0, highlightthickness=0,
                                      command=lambda: self.submit_answer("false"))
        self.cross_button.grid(column=1, row=3)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self) -> None:
        self.question_canvas.config(bg="white")
        if self.quiz_object.still_has_questions():
            q_text = self.quiz_object.next_question()  # gets the text returned by the quiz_object next_question() method.
            self.question_canvas.itemconfig(self.canvas_question_text,
                                            text=q_text)  # modifies the canvas text with the text returned above
        else:
            self.end_game()
    def submit_answer(self, answer: str) -> None:
        """changes the canvas background color to green if self.quiz_object.check_answer() returns True, red if it
        return False"""
        user_is_right = self.quiz_object.check_answer(answer)
        self.give_feedback(user_is_right)

    def give_feedback(self, user_is_right):
        if user_is_right:
            self.question_canvas.config(bg="green")
        else:
            self.question_canvas.config(bg="red")
        self.score_label.config(text=f"Score: {self.quiz_object.score}/{self.quiz_object.question_number}")
        self.window.after(200, self.get_next_question)

    def end_game(self):
        self.question_canvas.itemconfig(self.canvas_question_text, text="You have completed the quiz!")
        self.check_button.config(state="disabled")
        self.cross_button.config(state="disabled")

    def get_category_choice(self):
        self.selection = self.category_choices.get()
        print(self.selection)
    def change_category(self):
        cat_str = self.category_choices.get()
        new_category = data.get_category_id(cat_str)
        if new_category == None:
            self.question_canvas.itemconfig(self.canvas_question_text, text="You have not chosen a category")
        else:
            alert = tk.messagebox.showinfo(title="New category selected!",
                                           message=f"Now displaying questions pertaining to {cat_str}.")
            new_questions = data.give_questions_to_user(new_category)
            print(f"{data.parameters=}")
            self.quiz_object = quiz_brain.QuizBrain(new_questions)
            self.get_next_question()
