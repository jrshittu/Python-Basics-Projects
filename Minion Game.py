# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

def minion_game(string):
    # your code goes here
    vowels = ['A', 'E', 'I', 'O', 'U']
    stuart = 0
    kevin = 0
		
    for i in range(len(string)):
        if string[i] in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i
            
    if stuart > kevin:
        print(f'Stuart {stuart}')
    elif kevin > stuart:
        print(f'Kevin {kevin}')
    else:
        print('Draw')

s = input()
minion_game(s)