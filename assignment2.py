candidate = input("Enter candidates name(comma separated): ").strip()
candidate_list = candidate.split(",")

vote_result = {}
for x in candidate_list:
    vote_result[x] = 0



n = int(input("Enter number of voters: "))

for i in range(n):
    voter_choice = input(f"Voter {i+1}, enter your vote: ").strip()
    if voter_choice in candidate_list:
        vote_result[voter_choice] += 1
    else:
        while voter_choice not in candidate_list:
            voter_choice = input("Candidate not found. Please enter a valid name: ").strip()
        vote_result[voter_choice] += 1

print("---Vote Count---")
for key,value in vote_result.items():
    print(key,":",value)


max_vote = max(vote_result.values())

winners = []

for key, value in vote_result.items():
    if value == max_vote:
        winners.append(key)

if len(winners)==1:
    print("Winner is: ", winners[0], "with",max_vote,"votes!")

else:
    print("Tie! Winners are", ",".join(winners), "with", max_vote,"vote(s) each")

