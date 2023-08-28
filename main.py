from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

questions = [
    "What is the capital of France?",
    "Which planet is known as the Red Planet?",
    "What is 2 + 2?"
]
answers = ["Paris", "Mars", "4"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        user_answers = [request.form.get(f'answers[{i}]') for i in range(len(questions))]
        score = 0

        for user_answer, question in zip(user_answers, questions):
            if user_answer == question['correct_option']:
                score += 1

        return render_template('results.html', score=score, total=len(questions))

    return render_template('quiz.html', questiquestions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "Berlin", "Madrid", "Rome"],
        "correct_option": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Jupiter", "Mercury"],
        "correct_option": "Mars"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "correct_option": "4"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"],
        "correct_option": "Leonardo da Vinci"
    },
    {
        "question": "What is the largest mammal?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "correct_option": "Blue Whale"
    },
    {
        "question": "Which gas do plants primarily absorb from the atmosphere?",
        "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Helium"],
        "correct_option": "Carbon Dioxide"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["Au", "Ag", "Go", "Gl"],
        "correct_option": "Au"
    },
    {
        "question": "What is the largest organ in the human body?",
        "options": ["Heart", "Brain", "Liver", "Skin"],
        "correct_option": "Skin"
    },
    {
        "question": "Which famous scientist developed the theory of relativity?",
        "options": ["Isaac Newton", "Galileo Galilei", "Albert Einstein", "Stephen Hawking"],
        "correct_option": "Albert Einstein"
    },
    {
        "question": "In which year did World War II end?",
        "options": ["1939", "1942", "1945", "1947"],
        "correct_option": "1945"
    },
    {
        "question": "What is the tallest mountain in the world?",
        "options": ["Mount Kilimanjaro", "Mount Everest", "Mount Fuji", "Mount McKinley"],
        "correct_option": "Mount Everest"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["1", "2", "3", "5"],
        "correct_option": "2"
    },
    {
        "question": "Which instrument is used to measure atmospheric pressure?",
        "options": ["Thermometer", "Barometer", "Hygrometer", "Anemometer"],
        "correct_option": "Barometer"
    },
    {
        "question": "What is the process by which plants make their own food?",
        "options": ["Photosynthesis", "Respiration", "Fermentation", "Transpiration"],
        "correct_option": "Photosynthesis"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["William Shakespeare", "Charles Dickens", "Mark Twain", "Jane Austen"],
        "correct_option": "William Shakespeare"
    },
    {
        "question": "What gas do humans breathe out during respiration?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "correct_option": "Carbon Dioxide"
    },
    {
        "question": "Which gas is responsible for the ozone layer depletion?",
        "options": ["Oxygen", "Carbon Dioxide", "Chlorofluorocarbons (CFCs)", "Methane"],
        "correct_option": "Chlorofluorocarbons (CFCs)"
    },
    {
        "question": "What is the standard atomic weight of hydrogen?",
        "options": ["1", "2", "3", "4"],
        "correct_option": "1"
    },
    {
        "question": "Which famous scientist formulated the laws of motion and universal gravitation?",
        "options": ["Isaac Newton", "Galileo Galilei", "Albert Einstein", "Stephen Hawking"],
        "correct_option": "Isaac Newton"
    },
    {
        "question": "What is the chemical symbol for the element oxygen?",
        "options": ["Ox", "O", "Oi", "Oy"],
        "correct_option": "O"
    },
    {
        "question": "Which gas is essential for photosynthesis in plants?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "correct_option": "Carbon Dioxide"
    },
    {
        "question": "Who wrote the novel 'Pride and Prejudice'?",
        "options": ["Jane Austen", "Charlotte Brontë", "George Orwell", "Charles Dickens"],
        "correct_option": "Jane Austen"
    },
    {
        "question": "Which continent is known as the 'Dark Continent'?",
        "options": ["Africa", "Asia", "Europe", "Australia"],
        "correct_option": "Africa"
    },
    {
        "question": "Which famous scientist proposed the theory of evolution by natural selection?",
        "options": ["Isaac Newton", "Albert Einstein", "Charles Darwin", "Galileo Galilei"],
        "correct_option": "Charles Darwin"
    },
    {
        "question": "What is the chemical symbol for the element sodium?",
        "options": ["So", "Sd", "Na", "No"],
        "correct_option": "Na"
    },
    {
        "question": "Which gas is responsible for the greenhouse effect?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Methane"],
        "correct_option": "Carbon Dioxide"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Mercury", "Venus", "Earth", "Jupiter"],
        "correct_option": "Jupiter"
    },
    {
        "question": "Which famous artist painted the 'Starry Night'?",
        "options": ["Pablo Picasso", "Vincent van Gogh", "Leonardo da Vinci", "Michelangelo"],
        "correct_option": "Vincent van Gogh"
    },
    {
        "question": "What is the unit of electric current?",
        "options": ["Volt", "Ampere", "Watt", "Ohm"],
        "correct_option": "Ampere"
    },
    {
        "question": "What is the chemical symbol for the element helium?",
        "options": ["He", "H", "Hy", "Ha"],
        "correct_option": "He"
    }])

if __name__ == '__main__':
    app.run(debug=True)