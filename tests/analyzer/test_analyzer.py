from password_security_lab.analyzer.analyzer import analyze_password

def test_analyze_password():
    assert(analyze_password("")["length"]==0)
    assert(analyze_password("abcde")["length"]==5)
    assert(analyze_password("a1b2c3d4e5")["length"]==10)

    password_dict=analyze_password("LengE6!4572")
    assert(password_dict["isUpper"]==2)
    assert(password_dict["isLower"]==3)
    assert(password_dict["isDigit"]==5)
    assert(password_dict["isSpecial"]==1)

    password_dict1=analyze_password("OUPSKLqsFE")
    assert(password_dict1["isUpper"]==8)
    assert(password_dict1["isLower"]==2)
    assert(password_dict1["isDigit"]==0)
    assert(password_dict1["isSpecial"]==0)


    password_dict2=analyze_password("§,,/? _5468_??okK")
    assert(password_dict2["isUpper"]==1)
    assert(password_dict2["isLower"]==2)
    assert(password_dict2["isDigit"]==4)
    assert(password_dict2["isSpecial"]==10)

    assert(analyze_password("abcdefg")["distincCharacters"]==7)
    assert(analyze_password("aaabbccc")["distincCharacters"]==3)
    assert(analyze_password("abcdeeeefghij")["distincCharacters"]==10)
