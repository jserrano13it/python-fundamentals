# question2.py
# Author: Jose Serrano
# Purpose: Two-question quiz to practice if/else and score updates

player_name = input("Enter your name:")
score = 0
print("nQuestion 1:")
print("What is the capital of France?")
answer1 = input("Your answer:") 
if answer1.strip().lower() == "paris":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Incorrect. The correct answer is Paris.") 
print(f"Your score is now: {score}")
print("\nQuestion 2:")
print("What is 5 multiplied by 6?")
answer2 = input("Your answer:")
if answer2.strip() == "30":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Incorrect. The correct answer is 30.")    
print(f"Your final score is: {score} out of 2")

