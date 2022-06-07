import random


class Card:
    """Single card class"""
    def __init__(self, rank, value, suit):
        self.rank = rank
        self.value = value
        self.suit = suit

    def display_card(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    """This class gets a list of all cards and deals one"""
    def __init__(self):
        self.card_list = []

    def build_deck(self):
        """Build 52 decks and append it to card_list"""
        suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        ranks = {
            '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11,
        }
        for suit in suits:
            for rank, value in ranks.items():
                card = Card(rank, value, suit)
                self.card_list.append(card)

    def shuffle_deck(self):
        random.shuffle(self.card_list)

    def deal_card(self):
        card = self.card_list.pop()
        return card


class Player:
    """Class that simulates player"""
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.playing_hand = True

    def draw_hand(self, deck):
        """Deal the player's starting hand (2 cards)"""
        for i in range(2):
            card = deck.deal_card()
            self.hand.append(card)

    def display_hand(self):
        """Show the player's hand"""
        print("\nPlayer's Hand:")
        for card in self.hand:
            print(card.display_card())

    def hit(self, deck):
        """Give the player a new card"""
        card = deck.deal_card()
        self.hand.append(card)

    def get_hand_values(self):
        self.hand_value = 0
        ace_in_hand = False

        for card in self.hand:
            self.hand_value += card.value
            # Check for ace
            if card.rank == 'A':
                ace_in_hand = True

        if self.hand_value > 21 and ace_in_hand:
            self.hand_value -= 10
        print(f"Total value: {self.hand_value}")

    def update_hand(self, deck):
        """Update players hand by allowing them to hit"""
        if self.hand_value < 21:
            choice = input("Would you like to hit? (y/n): ").lower()
            if choice == 'y':
                self.hit(deck)
            else:
                self.playing_hand = False
        else:
            self.playing_hand = False


class Dealer(Player):
    """A class simulating the black jack dealer, they must hit up to 17 and they must reveal their 1st card"""
    def __init__(self):
        super().__init__()

    def display_hand(self):
        """Show the dealers hand one card at a time"""
        n = input("\nPress enter to reveal the dealer's hand. ")

        # Show all cards in the dealer's hand
        for card in self.hand:
            print(card.display_card())

    def hit(self, deck):
        """The dealer must hit until they have reached 17, then they stop"""
        self.get_hand_values()

        # As long as the hand_value is less than 17 dealer must hit
        while self.hand_value < 17:
            card = deck.deal_card()
            self.hand.append(card)
            self.get_hand_values()

        print(f"\nDealer is set with a total of {len(self.hand)} cards.")

    def get_hand_values(self):
        self.hand_value = 0
        ace_in_hand = False

        for card in self.hand:
            self.hand_value += card.value
            # Check for ace
            if card.rank == 'A':
                ace_in_hand = True

        if self.hand_value > 21 and ace_in_hand:
            self.hand_value -= 10

    def update_hand(self, deck):
        pass


class Game:
    """A class to hold bets and payouts"""
    def __init__(self, money):
        self.money = int(money)
        self.bet = 20
        self.winner = ""

    def set_bet(self):
        betting = True
        while betting:
            bet = int(input("What would you like to bet (minimum bet of 20): "))

            if bet < 20:
                bet = 20
            if bet > self.money:
                print("Sorry, you can't afford this bet")
            else:
                self.bet = bet
                betting = False

    def scoring(self, p_value, d_value):
        if p_value == 21:
            print("You got BLACK JACK!!! You win!")
            self.winner = 'p'
        elif d_value == 21:
            print("The dealer got BLACK JACK!!! You lose!")
            self.winner = 'd'
        elif p_value > 21:
            print("You went over 21... You lose!")
            self.winner = 'd'
        elif d_value > 21:
            self.winner = 'p'

        else:
            if p_value > d_value:
                print(f"Dealer gets {d_value}. You win")
                self.winner = 'p'
            elif d_value > p_value:
                print(f"Dealer gets {d_value}. You lose")
                self.winner = 'd'
            else:
                print(f"Dealer gets {d_value}. It's a push...")
                self.winner = 'tie'

    def payout(self):
        if self.winner == 'p':
            self.money += self.bet
        elif self.winner == 'd':
            self.money -= self.bet

    def display_money(self):
        print(f"\nCurrent money: ${self.money}")

    def display_money_and_bet(self):
        print(f"\nCurrent money: ${self.money} \t\t Current Bet: ${self.bet}")


print("the minimum bet at this table is $20")
money = int(input("\nhow much money are you willing to play with today: "))
game = Game(money)

# Main game loop
playing = True
while playing:
    # build a deck
    game_deck = Deck()
    game_deck.build_deck()
    game_deck.shuffle_deck()

    # Create player and dealer
    player = Player()
    dealer = Dealer()

    # Show how much money the player has and get players bet
    game.display_money()
    game.set_bet()

    # Draw the player and dealer hands
    player.draw_hand(game_deck)
    dealer.draw_hand(game_deck)

    # Simulate a single round of Black jack for the player
    game.display_money_and_bet()
    print(f"The dealer is showing a {dealer.hand[0].rank} of {dealer.hand[0].suit}.")

    # While player is playing, display values and ask for input
    while player.playing_hand:
        player.display_hand()
        player.get_hand_values()
        player.update_hand(game_deck)

    # Simulate a single round of black jack for the dealer
    dealer.hit(game_deck)
    dealer.display_hand()

    # Determine the winner and the payout
    game.scoring(player.hand_value, dealer.hand_value)
    game.payout()

    # The user ran out of money, kick them out
    if game.money < 20:
        playing = False
        print("Sorry, you ran out of money. Please try again.")

