Hello! I'm a BCA graduate specialized in Data Science, and this repository showcases a series of mini-projects I developed during my internship. These tasks were designed to strengthen my understanding of Python, basic AI concepts, and machine learning techniques through real-world implementations.

Throughout the internship, I worked on diverse projects covering areas like game development, chatbots, and recommendation systems. Each task helped me apply theoretical concepts in practical scenarios and improve my coding, problem-solving, and logical thinking abilities.

This repository contains three core tasks completed during the internship:

A smart Tic Tac Toe game with AI bot.

A simple rule-based chatbot using regular expressions.

A content-based book recommendation system powered by TF-IDF and cosine similarity.

Each project is written in Python and designed to be beginner-friendly, making it a good learning resource for those starting in AI and programming.

Feel free to explore the code, try out the projects, and reach out if you have any questions or suggestions!

Let's see what i have Created ------ 
1. Task 1: Tic Tac Toe with AI Bot
File: Task_1_Tic_tac_toe.py

Summary:
You've created a command-line Tic Tac Toe game where a human player competes against an AI bot. The game runs in a loop until either the player or the bot wins, or it's a draw.

Technologies & Methods Used:
Python core libraries (copy)

Minimax Algorithm: A recursive backtracking algorithm used for decision making in games.

Game Logic Functions: check_win, empty_cells, print_Layout.

AI Bot Logic:

The bot uses Minimax to evaluate possible moves.

Chooses the move with the highest score based on predicted outcomes.

Game Loop: Interactive loop to alternate turns between player and bot.

Highlights:
Good implementation of a classic AI algorithm.

Demonstrates understanding of recursion and game theory.

Could be improved by integrating Alpha-Beta pruning to optimize performance (currently just plain Minimax).

🤖 Task 2: Basic Pattern-Matching Chatbot
File: Task_2_Basic_Chatbot.py

Summary:
This is a simple rule-based chatbot that uses regular expressions to match user input with predefined patterns and respond accordingly.

Technologies & Methods Used:
Python core modules (re for regular expressions).

Text File Handling: Reads patterns and responses from a .txt file (basic_responses.txt).

Pattern Matching: Checks if user input matches any known pattern.

Interactive Loop: Real-time user-bot interaction via terminal.

Highlights:
Functional for basic greetings and FAQs.

A great entry-level implementation of NLP via pattern matching.

You could enhance this with:

Regex generalization (currently depends on exact matches).

Use of NLP libraries like NLTK or spaCy.

Memory or context retention.

📚 Task 3: Book Recommendation System
File: Task_3_Recommendation _system.py

Summary:
You've built a content-based book recommendation system that suggests the top 3 books from a selected category based on ratings and review count.

Technologies & Methods Used:
Pandas: For data manipulation and reading CSV file (Books_review.csv).

TF-IDF Vectorizer (from scikit-learn): Converts book descriptions into vectors.

Cosine Similarity: Measures similarity between books based on description text.

Recommendation Logic:

Filters books by user-selected category.

Ranks books by highest ratings and review count.

Highlights:
Solid implementation of a TF-IDF + cosine similarity model.

Smart use of real-world metrics (ratings, reviews) for recommendation prioritization.

Could be improved by:

Allowing input-based recommendations (like typing book titles).

Using collaborative filtering for personalization.
 
