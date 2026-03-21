food=['banana','apple','orange','melon']
cost=[90,52,44,67]
for i,f in enumerate(food):
    print(f'{i}: {f}')
for f,c in zip(food,cost):
    print(f'{f}: {c}')