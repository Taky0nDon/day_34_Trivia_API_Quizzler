D A Y T H I R T Y F O U R
 #### 5/17/23
# Today's Goal:
* Build quizzler app in tkinter
* Check mark for True, cross for False
* Generate questions with API
* Builds on day 17 project
* Get 10 questions from open trivia with an API request instead of
  hardcoding the questions
* API URL:
* `https://opentdb.com/api.php?amount=10&type=boolean`
* everything before the question mark is the endpoint
* after the question mark is the parameters

# Extract json data from an API call with respone_object.json()
ex:
```
response = request.get(API_ENDPOINT)
data = response.json()
```

## how do we format the text from data to get the proper characters?
* We are seeing `HTML entites`, which is a way of replacing a character in
* HTML so it doesn't get mixed up with HTML syntax
* we can use free formatter and googling "unescaping HTML entities in python"
* we can also use the html module
* use html.unescape()

|HTML entity | symbol |
|---|---|
|&lt; | < |
| &quot; | " |

# OOP review:
* classes conventionally named in Pascalcase
* tkinter.mainloop() doesnt like other while loops
* change the `state` of tk buttons with button.config(state="normal" | "disabled")

# Creating the UI

* This time we will create our tkinter UI in a class

# More on data types:
## Type Annotations or Type Hints
* create a variable
`age: int`
* when you define age later, it has to match the initial data type
* Can do the same thing inside a function:
```
def police_check(age: int) -> bool:
  return True if age > 18 else False
```