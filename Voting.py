Cand1 = (input("Please Enter 1st Candidate Name: ")) 
Cand2 = (input("Please Enter 2nd Candidate Name: ")) 
Cand1_votes = 0
Cand2_votes = 0
voters_list = [101,102,103,104,105,106,107,108] 
no_of_voters = len(voters_list) 
print("Number of Voters: ", no_of_voters) 

voted = []
while True:
    if voters_list == []:
        print("Voting is Over 🎉🎉🎉🥳🥳🥳")
        if Cand1_votes > Cand2_votes:
            print(f"{Cand1}  Won Election with the votes: {Cand1_votes} 🏆")
        elif Cand1_votes < Cand2_votes:
            print(f"{Cand2}  Won Election with the votes: {Cand2_votes} 🏆")
        elif Cand1_votes == Cand2_votes:
            print("Tied!!!")
        break
    else:
        voter = int(input("Please Enter your Id: "))
        if voter in voted:
            print("Sorry, You are already voted")
        else:
            if voter in voters_list:  # Check eligibility for voting
                print(f"{Cand1}\n{Cand2}")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    Cand1_votes += 1
                    print(f"You voted {Cand1}")
                elif choice == 2:
                    Cand2_votes += 1
                    print(f"You voted {Cand2}")
                voters_list.remove(voter)
                voted.append(voter)
            else:
                print("You're not allowed to vote")

from array import *
a =array("i",[12,123])
a.remove(a[1])
for i in a:
    print(i)