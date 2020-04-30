# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    count = 0
    for i in range(len(s)-1):
        if(s[i]==s[i+1]):
            count+=1
    print(count)

if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = alternatingCharacters(s)

