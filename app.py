class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, points):
        self.score += points

def ask_question(question):
    print(question["question"])
    for i, choice in enumerate(question["choices"], 1):
        print(f"{i}. {choice}")
    answer = input("Your answer (1-4): ")
    return answer.strip() == question["answer"]

def main():
    players = []
    num_players = int(input("Enter number of players: "))
    for _ in range(num_players):
        player_name = input("Enter player's name: ")
        players.append(Player(player_name))

    questions = [
        # Football Questions
        {"question": "Which country has won the most FIFA World Cups?", "choices": ["Germany", "Argentina", "Brazil", "France"], "answer": "3"},
        {"question": "Who has won the most Ballon d'Or awards?", "choices": ["Cristiano Ronaldo", "Lionel Messi", "Pelé", "Zinedine Zidane"], "answer": "2"},
        {"question": "Which club has won the most UEFA Champions League titles?", "choices": ["Real Madrid", "Barcelona", "Manchester United", "Bayern Munich"], "answer": "1"},
        {"question": "Which country hosted the 2018 FIFA World Cup?", "choices": ["Russia", "Brazil", "Qatar", "Germany"], "answer": "1"},
        {"question": "Who is the all-time top scorer in the FIFA World Cup?", "choices": ["Pelé", "Miroslav Klose", "Ronaldo Nazário", "Diego Maradona"], "answer": "2"},
        
        # UFC Questions
        {"question": "Who was the first UFC double champion (simultaneously holding two belts)?", "choices": ["Daniel Cormier", "Conor McGregor", "Georges St-Pierre", "Jon Jones"], "answer": "2"},
        {"question": "Which fighter has the most title defenses in UFC history?", "choices": ["Anderson Silva", "Demetrious Johnson", "Jon Jones", "Georges St-Pierre"], "answer": "2"},
        {"question": "Which UFC fighter is known as 'The Last Stylebender'?", "choices": ["Israel Adesanya", "Kamaru Usman", "Francis Ngannou", "Alexander Volkanovski"], "answer": "1"},
        {"question": "What weight class is 155 lbs in the UFC?", "choices": ["Featherweight", "Welterweight", "Lightweight", "Middleweight"], "answer": "3"},
        {"question": "Who defeated Ronda Rousey to end her undefeated streak?", "choices": ["Amanda Nunes", "Miesha Tate", "Holly Holm", "Cris Cyborg"], "answer": "3"}
    ]

    for question in questions:
        for player in players:
            print(f"{player.name}'s turn:")
            if ask_question(question):
                print("Correct!")
                player.add_score(1)
            else:
                print("Wrong answer.")
            print()

    winner = max(players, key=lambda p: p.score)
    print(f"The winner is {winner.name} with {winner.score} points!")

if __name__ == "__main__":
    main()
