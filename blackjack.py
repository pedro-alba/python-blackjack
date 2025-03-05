import random

# Calculate a cards value
def card_value(card):
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 11
    else:
        return int(card)

# Create a new deck of cards
def new_deck():
    deck = 4*[x for x in range(2,11)] + 4*['J', 'Q', 'K', 'A']
    random.shuffle(deck)
    return deck

# Hand score
def calculate_score(hand):
    score = sum(card_value(card) for card in hand)
    #check and convert ace score (1 or 11)
    aces = hand.count('A')
    while score > 21 and aces:
        score -= 10 
        aces -= 1
        
    return score
    
# Deal x cards of y deck
def deal_card(times:int, deck):
    cards = []
    for _ in range(times):
        card = random.choice(deck)
        deck.remove(card)
        cards.append(card)
    return cards if times > 1 else cards[0]

# Show player stats
def show_player_stats(deck, hand):
    print("Player hand:",hand)
    print("Player score:",calculate_score(hand))

# Show dealer stats 
def show_dealer_stats(deck, hand):
    print("Dealer hand:",hand)
    print("Dealer score:",calculate_score(hand))

# Play!
def play_blackjack():
    print("Starting the game...")
    # shuffles new deck
    deck = new_deck()
    # new player hand with 2 cards, new dealer hand with 2 cards
    player_hand = deal_card(2, deck)
    dealer_hand = deal_card(2, deck)
    
    print("Dealer's second card is:", dealer_hand[1])
    # player turn
    while calculate_score(player_hand) < 21:
        show_player_stats(deck, player_hand)
        action = input("Input 'h' to draw another card. Press any other key to stop: ").lower().strip()
        if action == 'h':
            print("-"*40)
            player_hand.append(deal_card(1, deck))
            
        else:
            break
    
    # handles player hand going over 21
    if calculate_score(player_hand) > 21:
        show_player_stats(deck, player_hand)
        print("-"*40)
        print("YOU LOST!!!")
        print("-"*40)
        return
    
    # dealer turn
    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(deal_card(1, deck))
        show_dealer_stats(deck, dealer_hand)
        
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    
    print("-"*40)
    show_dealer_stats(deck, dealer_hand)
    show_player_stats(deck, player_hand)
    
    if (dealer_score > 21) or (player_score > dealer_score):
        print("YOU WON!!!")
    elif dealer_score > player_score:
        print("YOU LOST!!!")
    else:
        print("IT'S A TIE!!!")
        
    print("-"*40)    

# Start the game
if __name__ == '__main__':
    play_blackjack()
