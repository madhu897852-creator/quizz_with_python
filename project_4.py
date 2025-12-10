import os
def find_winner(bidder_details):
    highest_bid=0
    winner=''
    for bidder in bidder_details:
        bidder_price=bidder_details
        if bidder_price>highest_bid:
            highest_bid=bidder_price
            winner=bidder
    print(f'here is the list of the bidders:{bidder_details}')
    print(f'the winner is {winner} with the highest price {highest_bid}')
bidder_data={}
end_of_bidding=False
while not end_of_bidding:
    name=input('what is ur name?:')
    price=input('enter ur bid?:')
    bidder_data[name]=price
    more_bidders=input("Are there any bidders do bid?enter 'yes'or 'no'").lower
    if more_bidders=='no':
        end_of_bidding=True
        find_winner(bidder_data)
    elif more_bidders=='yes':
        os.system('cls')