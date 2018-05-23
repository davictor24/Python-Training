votes = []
inv = 0
for i in range(10):
    num = int(input("Enter 1 for Victor, 2 for Izu and 3 for Tomisin: "))
    if num == 1:
        votes.append("Victor")
    elif num == 2:
        votes.append("Izu")
    elif num == 3:
        votes.append("Tomisin")
    else:
        print("Invalid vote")
        inv += 1
num_votes = {}
for vote in votes:
    num_votes[vote] = num_votes[vote] + 1 if vote in num_votes else 1
    '''
    if vote in num_votes:
        num_votes[vote] += 1
    else:
        num_votes[vote] = 1
    '''
for key in num_votes.keys():
    print("{0} => {1}".format(key, num_votes[key]))
print("{0} => {1}".format("Invalid votes", inv))
    
