from password_security_lab.analyzer.dictionary import load_dictionary
from password_security_lab.analyzer.dictionary import check_dictionary



def test_load_dictionary(tmp_path):
    dictionary = tmp_path / "dictionary.txt"

    dictionary.write_text(
        "password\n"
        "azerty\n"
        "\n"
        "admin\n",
        encoding="utf-8"
    )

    assert load_dictionary(dictionary) == [
        "password",
        "azerty",
        "admin"
    ]

    assert check_dictionary("admin",load_dictionary(dictionary)) == (True,2,3)

    assert check_dictionary("dfddd",load_dictionary(dictionary)) == (False,None,None)

    assert check_dictionary("p@ssw0rd",load_dictionary(dictionary)) == (True,0,1)





    


def test_load_empty_dictionary(tmp_path):
    dictionary = tmp_path / "dictionary.txt"
    dictionary.write_text("", encoding="utf-8")

    assert load_dictionary(dictionary) == []