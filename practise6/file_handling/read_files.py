with open('sample.txt','r') as f:
    for line in f:
        print(line.strip())
#reading file line
with open('sample.txt','a') as f:
    f.write('New line!!!!\n')
#added new line
with open('sample.txt','r') as f:
    print(f.read())
#checking added lines