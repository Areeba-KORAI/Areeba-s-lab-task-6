words = ['apple', 'ant', 'banana', 'ball', 'cat']
conclusion = {}
for word in words:
    key = word[0]
    if key in conclusion:
        conclusion[key].append(word)
    else:
        conclusion[key] = [word]
print(conclusion)