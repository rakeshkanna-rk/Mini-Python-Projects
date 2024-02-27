# Python Tech Quiz Game

Welcome to the Python Tech Quiz Game! This is a simple command-line quiz game built with Python, featuring 10 multiple-choice questions about technology.

## How to Play

1. Answer each question by entering the number corresponding to your choice (1-4).
2. At the end of the quiz, your final score will be displayed.

## Questions
The quiz consists of 10 questions on various technology-related topics such as programming languages, companies, and terms.

## How this works

1. **Questions Data Structure**:
    - The quiz game stores its questions and answers in a list of dictionaries called `questions`.
    - Each dictionary represents a single question and contains three keys: `"question"`, `"options"`, and `"answer"`.
    - `"question"` holds the text of the question, `"options"` contains a list of possible answers, and `"answer"` stores the correct answer.

2. **Main Function (`run_quiz()`)**:
    - The `run_quiz()` function serves as the main entry point for running the quiz.
    - It initializes the variable `score` to keep track of the player's score.

3. **Presenting Questions**:
    - Within the `run_quiz()` function, there is a loop that iterates over each question in the `questions` list.
    - For each question, the function prints the question text and the answer options using a loop.
    - The player is prompted to enter their choice (1-4) corresponding to the options presented.

4. **Input Validation**:
    - After the player enters their choice, the input is validated to ensure it is a digit between 1 and 4.
    - This is done using the `isdigit()` method to check if the input consists only of digits, and then converting it to an integer for further validation.

5. **Scoring**:
    - If the player's input matches the correct answer for the question, their score is incremented by 1.
    - The correct answer is obtained from the `"answer"` key of the question dictionary.

6. **Feedback on Incorrect Answers**:
    - If the player's answer is incorrect, the correct answer is displayed to provide feedback.

7. **End of Quiz**:
    - After all questions have been answered, the function prints the player's final score out of the total number of questions.
    - The player's score is calculated as the number of correct answers out of the total number of questions.

8. **Error Handling**:
    - Basic error handling is implemented to handle cases where the player enters invalid input (e.g., a non-digit or a number outside the range 1-4).
    - In such cases, a message is displayed indicating that the input is invalid, and the player is prompted to try again.

9. **Clean Code Structure**:
    - The code is structured in a clean and readable manner, making use of functions, loops, and conditional statements to organize the logic.
    - Comments are used judiciously to explain complex or important parts of the code, enhancing readability and maintainability.

Overall, the Python Tech Quiz Game is designed to provide an interactive and engaging experience for players while demonstrating key concepts of Python programming such as data structures, loops, conditional statements, and input validation.