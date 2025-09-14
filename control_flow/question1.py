# question1.py
# Author: Jose Serrano
# Purpose: First quiz question with answer checking and score update

# Step 1: Ask for player's name (carried over from Module 1)
player_name = input("Enter your name: ")
score = 0  # starting score

# Step 2: Ask the first question
print("\nQuestion 1:")
print("What is the capital of France?")
answer = input("Your answer: ")

# Step 3: Check the answer (case-insensitive)
if answer.strip().lower() == "paris":
    print("✅ Correct!")
    score += 1  # increase score by 1
else:
    print("❌ Incorrect. The correct answer is Paris.")

# Step 4: Show updated score
print(f"Your score is now: {score}")