correct_answers = ['A','C','B','D','B']

your_answer = []
for i in range(5):
    answer = input(f"Q{i+1}: ").upper()
    your_answer.append(answer)


x = 0
matched_answers = 0
for ans in your_answer:
    if ans == correct_answers[x]:
        matched_answers += 1
    x += 1

print("--- Quiz Result ---")
print("YOUR SCORE", matched_answers,"/5")
print("Percentage: ", (matched_answers/5)*100,"%")
