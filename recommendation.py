# Week 3 Project
# Simple AI Recommendation System

user_interest = input("Enter your interest (movies, music, sports): ").lower()
if user_interest == "movies":
    print("Recommended: Inception, Interstellar, The Dark Knight")

elif user_interest == "music":
    print("Recommended: Imagine Dragons, Coldplay, Ed Sheeran")

elif user_interest == "sports":
    print("Recommended: Football, Basketball, Tennis")

else:
    print("Sorry, no recommendations found.")