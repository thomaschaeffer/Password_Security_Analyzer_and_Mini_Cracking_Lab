from password_security_lab.analyzer.patterns import replace_substitutions

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