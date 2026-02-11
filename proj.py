import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

candidates=[]
colors=[]
votes=[]
n=int(input('Enter no of candidates: '))
for i in range(n):
    name=input(f'enter name of candidate: ')
    # name=input(f'enter the {i+1} name of candidate: ')
    vcount=int(input(f'enter votes recieved by {name}: '))
    clr=input(f'color of {name}: ')
    candidates.append(name)
    votes.append(vcount)
    colors.append(clr)
df=pd.DataFrame(
    {
        'Candidates':candidates,
        'Votes':votes
    }
)

votes_ary=np.array(votes)
total_votes=np.sum(votes_ary)
percentage_votes=(votes_ary/total_votes)*100
df['Percentage'] = percentage_votes
print("\nVote Percentage of Each Candidate:\n")
print(df[['Candidates', 'Percentage']])

winner=candidates[np.argmax(votes_ary)]
print("\nWinner of the Election:", winner)

plt.bar(df['Candidates'],df['Votes'], color=colors)
plt.title('Election Vote Count')
plt.xlabel('Candidates')
plt.ylabel('Votes')
plt.show()

plt.pie(df['Votes'],labels=df['Candidates'],colors=colors)
plt.title('Vote Share Distribution')
plt.show()
