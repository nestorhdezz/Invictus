import random
# MIT License
# Copyright (c) 2024 Invictus Team
movies_data = {
    "emotions": {
        "Joy": ["Soul (2020)", "La La Land (2016)", "The Grand Budapest Hotel (2014)"],
        "Sadness": ["Blue Valentine (2010)", "The Fault in Our Stars (2014)", "The Pursuit of Happyness (2006)"],
        "Fear": ["Get Out (2017)", "Hereditary (2018)", "The Conjuring (2013)"],
        "Love": ["Pride & Prejudice (2005)", "Crazy Rich Asians (2018)", "Eternal Sunshine of the Spotless Mind (2004)"]
    },
    "topics": {
        "Friendship": ["The Intouchables (2011)", "Stand by Me (1986)", "Toy Story (2005)"],
        "Adventure": ["The Lord of the Rings (2001)", "Indiana Jones: Raiders of the Lost Ark (1981)", "The Secret Life of Walter Mitty (2013)"],
        "Family": ["Coco (2017)", "Little Miss Sunshine (2006)", "The Lion King (1994)"],
        "Self-improvement": ["Good Will Hunting (1997)", "Whiplash (2014)", "Slumdog Millionaire (2008)"]
    },
    "average_score": {
        "7": ["Frozen (2013)", "Wonder Woman (2017)", "Tenet (2020)"],
        "8": ["Joker (2019)", "The Lion King (2019)", "Gladiator (2000)"],
        "9": ["12 Angry Men (1957)", "The Shawshank Redemption (1994)", "The Dark Knight (2008)"],
        "9.5-10": ["Toy Story (1995)", "Parasite (2019)", "Paddington 2 (2017)"]
    }
}

def recommend_movies_by_emotion():
    emotion = input("Choose an emotion (Joy, Sadness, Fear, Love): ")
    recommendations = movies_data["emotions"].get(emotion, [])
    return random.sample(recommendations, min(3, len(recommendations)))

def recommend_movies_by_topic():
    topic = input("Choose a topic (Friendship, Adventure, Family, Self-improvement): ")
    recommendations = movies_data["topics"].get(topic, [])
    return random.sample(recommendations, min(3, len(recommendations)))

def recommend_movies_by_score():
    score = input("Choose an average score (7, 8, 9, 9.5-10): ")
    recommendations = movies_data["average_score"].get(score, [])
    return random.sample(recommendations, min(3, len(recommendations)))

def main():
    print("Welcome to the movie recommendation system. This program is perfect to watch a film bassed in your taste. It is ideal for indecisive people and for improvised plans to watch a movie in a group. ")
    choice = input("Do you want a movie based on emotions, topics, or average score? (Type 'emotions', 'topics', or 'score'): ").strip().lower()

    if choice == "emotions":
        recommendations = recommend_movies_by_emotion()
    elif choice == "topics":
        recommendations = recommend_movies_by_topic()
    elif choice == "score":
        recommendations = recommend_movies_by_score()
    else:
        print("Invalid option. Please try again.")
        return

    if recommendations:
        print("\nHere are your movie recommendations, enjoy it:")
        for movie in recommendations:
            print(f"- {movie}")
    else:
        print("No recommendations found for your selection.")

if __name__ == "__main__":
    main()
