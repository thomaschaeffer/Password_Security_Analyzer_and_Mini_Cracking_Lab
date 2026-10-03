

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
        else:
            #Store the sequence if the new character doesn't follow the pattern of at least the last 3 characters
            if char_number>2:
                list_sequence.append(password[index-char_number:index])
            char_number=2

    #Handle the case when there is a sequence at the end of the password
    if char_number>2:
        list_sequence.append(password[len(password)-char_number:len(password)])

    return list_sequence


def detection_block(password):
    list_temp=[]
    list_block=[]
    for size_block in range(1,len(password)//2+1):
        for offset in range(size_block):
            for index in range(len(password)//size_block):
                if (size_block*(index+1) + offset)>len(password):
                    break
                block = password[size_block*index+offset:size_block*(index+1)+offset]
                if len(list_temp)==0:
                    list_temp.append(block)
                elif list_temp[0]==block:
                    list_temp.append(block)
                else:
                    if len(list_temp)>1 and len(set(list_temp[0]))>1:
                        list_block.append(list_temp[0])
                    list_temp=[block]
    return list_block


def detection_block_bis(password):
    dict_block={}

    for size_block in range(2,len(password)//2+1):
        for i in range(len(password)-size_block):
            block=password[i:size_block+i]
            for j in range(size_block+i,len(password)-size_block + 1 ):
                if password[j:j+size_block]==block:
                    if  block not in dict_block:
                        dict_block[block]=[i]
                    if j not in dict_block[block]:
                        dict_block[block].append(j)               
    return dict_block

def filter_block(dict_block):
    dict_block_filtered=dict_block.copy()
    for k in dict_block.keys():
        for i in dict_block.keys():
            if len(k)!=len(i) and (k in i):
                flag_include = True
                for j in dict_block[k]:
                    flag_AtLeastOnce=False
                    for p in dict_block[i]:
                        if p <= j and j + len(k) <= p + len(i):
                            flag_AtLeastOnce=True
                    if not flag_AtLeastOnce:
                        flag_include=False
                if flag_include:
                    dict_block_filtered.pop(k,None)
    return dict_block_filtered

def detection_date(password):
    dates=[]
    years=[]
    if len(password)>=6:
        for i in range(len(password)-5):
            block=password[i:i+6]
            if block.isdigit():
                day=block[0:2]
                month=block[2:4]
                if int(day)<=31 and int(month)<=12:
                    dates.append(block)
    if len(password)>=4:
        for i in range(len(password)-3):
            block=password[i:i+4]
            if block.isdigit() and 1900<=int(block)<=2026:
                years.append(block)

    print(dates,years)


if __name__=="__main__":
    #print(detection_repetition("abbbcaaaafbbbffbbb"))
    #print(detection_sequence("123456abcdefg1a2b3c4d4444"))
    #print(detection_block("abababab1111"))
    #filter_block(detection_block_bis("abasdfgsfjabababa"))
    detection_date("a123456")
