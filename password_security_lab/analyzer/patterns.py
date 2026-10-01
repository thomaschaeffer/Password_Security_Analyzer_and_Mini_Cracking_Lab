def detection_patterns(password):
    pattern_dict={}
    index_bis=0
    char_reiteration=1

    for index in range (1,len(password)):

        if password[index-1]==password[index]:
            char_reiteration+=1
        
        else:
            if char_reiteration>1:
                char_text = password[index_bis:index]
                while char_text in pattern_dict.keys():
                    char_text= char_text+"_"
                pattern_dict[char_text]= {password[index_bis] :char_reiteration}
            index_bis=index
            char_reiteration=1

    if char_reiteration>1:
        char_text = password[index_bis:index+1]
        while char_text in pattern_dict.keys():
            char_text= char_text+"_"
        pattern_dict[char_text]= {password[index_bis] :char_reiteration}

    return pattern_dict
        


print(detection_patterns("abbbcaaaafbbbffbbb"))
