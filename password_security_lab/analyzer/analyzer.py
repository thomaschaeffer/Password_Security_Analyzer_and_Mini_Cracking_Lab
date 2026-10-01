def distinc_character(password):
    l_character = []
    for character in password:
        if character not in l_character:
            l_character.append(character)

    return len(l_character)



def analyze_password ( password ):
    password_dict={ "password" : password, 
                   "length" : len(password), 
                   "isUpper" : 0, 
                   "isLower": 0, 
                   "isDigit": 0, 
                   "isSpecial": 0, 
                   "distincCharacters": distinc_character(password)}

    for character in password:
        if character.isupper():
            password_dict["isUpper"]+=1
        elif character.islower():
            password_dict["isLower"]+=1
        elif character.isdigit():
            password_dict["isDigit"]+=1
        else:
            password_dict["isSpecial"]+=1

    return password_dict





if __name__ == "__main__":
    print(analyze_password(input()))
