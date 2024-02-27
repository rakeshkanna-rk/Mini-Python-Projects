def run_quiz():
    questions = [
        {
            "question": "What does CPU stand for?",
            "options": ["Central Processing Unit", "Computer Personal Unit", "Central Personal Unit", "None of the above"],
            "answer": "Central Processing Unit"
        },
        {
            "question": "Which programming language is known as the 'language of the web'?",
            "options": ["Python", "JavaScript", "Java", "C++"],
            "answer": "JavaScript"
        },
        {
            "question": "What does HTML stand for?",
            "options": ["Hyper Text Markup Language", "Hyperlinks and Text Markup Language", "Home Tool Markup Language", "None of the above"],
            "answer": "Hyper Text Markup Language"
        },
        {
            "question": "Who is the CEO of Tesla?",
            "options": ["Elon Musk", "Jeff Bezos", "Bill Gates", "Mark Zuckerberg"],
            "answer": "Elon Musk"
        },
        {
            "question": "Which company developed Android?",
            "options": ["Google", "Microsoft", "Apple", "Samsung"],
            "answer": "Google"
        },
        {
            "question": "What does URL stand for?",
            "options": ["Universal Resource Locator", "Uniform Resource Locator", "Unified Resource Locator", "None of the above"],
            "answer": "Uniform Resource Locator"
        },
        {
            "question": "Who developed the Python programming language?",
            "options": ["Guido van Rossum", "Larry Page", "Mark Zuckerberg", "Steve Jobs"],
            "answer": "Guido van Rossum"
        },
        {
            "question": "Which of the following is a version control system?",
            "options": ["Git", "HTML", "CSS", "jQuery"],
            "answer": "Git"
        },
        {
            "question": "What does CSS stand for?",
            "options": ["Cascading Style Sheets", "Computer Style Sheets", "Colorful Style Sheets", "Creative Style Sheets"],
            "answer": "Cascading Style Sheets"
        },
        {
            "question": "Which company is the largest online retailer?",
            "options": ["Amazon", "Alibaba", "Walmart", "eBay"],
            "answer": "Amazon"
        }
    ]

    score = 0

    print("Welcome to the Tech Quiz!")
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for j, option in enumerate(q['options'], 1):
            print(f"{j}. {option}")
        user_answer = input("Enter your choice (1-4): ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
            if q['options'][int(user_answer) - 1] == q['answer']:
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")
                print(f"The correct answer is: {q['answer']}")
        else:
            print("Invalid input! Skipping this question.")

    print(f"\nQuiz completed! Your final score is: {score}/{len(questions)}")


if __name__ == "__main__":
    run_quiz()