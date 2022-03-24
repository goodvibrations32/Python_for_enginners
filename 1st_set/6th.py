#%%
import random

ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
suits = ['Spa8i', 'Karo', 'Kardia', 'Mpastouni']
deck = [rank+''+suit for rank in ranks for suit in suits]

ran_cards = random.sample(deck, k= 5)
print('Number of cards before random pick =',len(deck))


for i in range (len(ran_cards)):
    deck.remove(ran_cards[i])
    
print('Randomly selected cards from deck =',ran_cards) 
print('Number of cards in deck after removing selected =',len(deck))

# %%
