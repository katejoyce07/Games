import random

# Constants
COLORS = ["Red", "Yellow", "Green", "Blue"]
VALUES = ["0", "1", "2", "3", "4", "5", "6",
          "7", "8", "9", "Draw Two", "Skip", "Reverse"]

# Create a deck of UNO cards


def create_deck():
    deck = []
    for color in COLORS:
        for value in VALUES:
            deck.append(f"{color} {value}")
            if value != "0":  # Two of each card except 0
                deck.append(f"{color} {value}")
    random.shuffle(deck)
    return deck

# Deal cards to players


def deal_cards(deck, num_players, hand_size=7):
    hands = []
    for _ in range(num_players):
        hand = [deck.pop() for _ in range(hand_size)]
        hands.append(hand)
    return hands

# Check if a card can be played


def can_play(card, top_card):
    return card.split()[0] == top_card.split()[0] or card.split()[1] == top_card.split()[1]

# Main game loop


def play_game():
    deck = create_deck()
    hands = deal_cards(deck, 2)  # Updated for 2 players
    discard_pile = [deck.pop()]

    player_turn = 0
    while True:
        print(f"\nTop card: {discard_pile[-1]}")
        print(
            f"Player {player_turn + 1}'s turn with hand: {hands[player_turn]}")

        playable_cards = [card for card in hands[player_turn]
                          if can_play(card, discard_pile[-1])]
        if not playable_cards:
            print(f"No playable cards. Drawing a card...")
            drawn_card = deck.pop()
            hands[player_turn].append(drawn_card)
            if can_play(drawn_card, discard_pile[-1]):
                print(f"Drawn card {drawn_card} is playable. Playing it.")
                discard_pile.append(drawn_card)
                hands[player_turn].remove(drawn_card)
        else:
            print(f"Playable cards: {playable_cards}")
            while True:
                card_to_play = input(
                    f"Player {player_turn + 1}, choose a card to play (or type 'draw' to draw a card): ")
                if card_to_play == 'draw':
                    drawn_card = deck.pop()
                    hands[player_turn].append(drawn_card)
                    print(f"You drew {drawn_card}.")
                    if can_play(drawn_card, discard_pile[-1]):
                        print(
                            f"Drawn card {drawn_card} is playable. Playing it.")
                        discard_pile.append(drawn_card)
                        hands[player_turn].remove(drawn_card)
                    break
                elif card_to_play in hands[player_turn] and can_play(card_to_play, discard_pile[-1]):
                    discard_pile.append(card_to_play)
                    hands[player_turn].remove(card_to_play)
                    break
                else:
                    print("Invalid choice. Please choose a valid card to play.")

        # Check if the current player has won
        if not hands[player_turn]:
            print(f"Player {player_turn + 1} wins!")
            break

        # Move to the next player
        player_turn = (player_turn + 1) % 2  # Updated for 2 players


# Start the game
play_game()
