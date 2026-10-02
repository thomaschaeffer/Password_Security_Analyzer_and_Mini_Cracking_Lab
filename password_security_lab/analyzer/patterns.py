

def detection_repetition(password):
    '''
    Detects consecutive repetitions of the same character in a password

    Args: 
        password (str): Password to analyze

    Returns:
        dict: Detected repetitions with, as key, all the repeated sequence and its character/count as the value.
              Add " ' " if the we find the same sequence multiple time.
    '''
    dict_repetition={}
    index_bis=0
    char_reiteration=1

    for index in range (1,len(password)):

        #Extend the current repetition while consecutive characters match
        if password[index-1]==password[index]:
            char_reiteration+=1
        
        else:
            #Store the repetition when there is at least two identical characters that have been found
            if char_reiteration>1:
                char_text = password[index_bis:index]
                while char_text in dict_repetition.keys():
                    char_text= char_text+"_"
                dict_repetition[char_text]= {password[index_bis] :char_reiteration}
            index_bis=index
            char_reiteration=1

    #Handle the case when there is a repetition at the end of the password
    if char_reiteration>1:
        char_text = password[index_bis:index+1]
        while char_text in dict_repetition.keys():
            char_text= char_text+"_"
        dict_repetition[char_text]= {password[index_bis] :char_reiteration}

    return dict_repetition
        


def detection_sequence(password):
    '''
    Detects consecutive sequence of the same type in a password

    Args: 
        password (str): Password to analyze

    Returns:
        list: Detected sequences.
    '''
    list_sequence=[]
    char_number=2

    if len(password)<3:
        return list_sequence

    for index in range(2,len(password)):
        x1=password[index-2]
        x2=password[index-1]
        x3=password[index]

        #Check if the three value have the same type and convert them in int
        if x1.isdigit()==x2.isdigit()==x3.isdigit():
            if not x1.isdigit():
                x1 = ord(x1)
                x2 = ord(x2)
                x3 = ord(x3)
            else:
                x1 = int(x1)
                x2 = int(x2)
                x3 = int(x3)

            if x1-x2==x2-x3!=0:
                char_number+=1
                print(char_number)
        else:
            #Store the sequence if the new character doesn't follow the pattern of at least the last 3 characters
            if char_number>2:
                list_sequence.append(password[index-char_number:index])
            char_number=2

    #Handle the case when there is a sequence at the end of the password
    if char_number>2:
        list_sequence.append(password[len(password)-char_number:len(password)])

    return list_sequence



if __name__=="__main__":
    print(detection_repetition("abbbcaaaafbbbffbbb"))
    print(detection_sequence("123456abcdefg1a2b3c4d4444"))