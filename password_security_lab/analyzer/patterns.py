def detection_repetition(password):
    dict_repetition={}
    index_bis=0
    char_reiteration=1

    for index in range (1,len(password)):

        if password[index-1]==password[index]:
            char_reiteration+=1
        
        else:
            if char_reiteration>1:
                char_text = password[index_bis:index]
                while char_text in dict_repetition.keys():
                    char_text= char_text+"_"
                dict_repetition[char_text]= {password[index_bis] :char_reiteration}
            index_bis=index
            char_reiteration=1

    if char_reiteration>1:
        char_text = password[index_bis:index+1]
        while char_text in dict_repetition.keys():
            char_text= char_text+"_"
        dict_repetition[char_text]= {password[index_bis] :char_reiteration}

    return dict_repetition
        


def detection_sequence(password):
    dict_sequence=[]
    char_number=2

    if len(password)<3:
        return dict_sequence

    for index in range(2,len(password)):
        x1=password[index-2]
        x2=password[index-1]
        x3=password[index]
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
            if char_number>2:
                dict_sequence.append(password[index-char_number:index])
            char_number=2

    if char_number>2:
        dict_sequence.append(password[len(password)-char_number:len(password)])

    return dict_sequence



if __name__=="__main__":
    print(detection_repetition("abbbcaaaafbbbffbbb"))
    print(detection_sequence("123456abcdefg1a2b3c4d4444"))