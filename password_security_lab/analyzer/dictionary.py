from patterns import replace_substitutions
import random

def load_dictionary(path):

    words=[]
    with open(path, "r",encoding="utf-8") as file:
        for line in file:
            if line.strip():
                words.append(line.strip())
    return words


def check_dictionary(password, dictionary):
    password_substitution = replace_substitutions(password)
    pos=0
    word_analyze=0
    for word in dictionary:
        word_analyze+=1
        if password == word or password_substitution == word : 
            return True, pos , word_analyze
        pos+=1

    return False, None, None


def mutation_suffix(password):
    special_characters = [
    "!", "@", "#", "$", "%", "&", "*",
    "?", "_", "-", "+", ".", "="
    ]

    return password+random.choice(special_characters)

def mutation_capital(password):
    l_lower_pos=[]
    for i in range(0,len(password)):
        if password[i].islower():
            l_lower_pos.append(i)
    if len(l_lower_pos) == 0:
        return password
    else:
        index = random.choice(l_lower_pos)
        password=password[:index]+password[index].upper()+password[index+1:]
        return password


def mutation_number(password):
    number_list = [
    0,1,2,3,4,5,6,7,8,9
    ]
    return password+random.choice(number_list)

def mutation_substitution(password):
    substitution_pos=[]
    substitutions = {
        "a": ["@", "4"],
        "e": ["3"],
        "i": ["1", "!"],
        "o": ["0"],
        "s": ["$", "5"],
        "t": ["7"]
    }

    for i in range(0,len(password)):
        if password[i].lower() in substitutions.keys():
            substitution_pos.append(i)

    print( substitution_pos)
    if len(substitution_pos) == 0:
        return password
    else:
        index = random.choice(substitution_pos)
        password=password[:index]   +random.choice(substitutions[password[index].lower()])+    password[index+1:]
        return password

print(mutation_substitution("avbkbnsp"))