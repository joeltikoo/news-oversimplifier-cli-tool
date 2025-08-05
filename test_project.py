from project import summarize_text, word_count, capitalize_title


def test_word_count():
    assert word_count("This is a test") == 4
    assert word_count("") == 0
    assert word_count("    spaced out   words ") == 3


def test_summarize_text():
    input_text = ("""CS50P
                  An introduction to programming using a language called Python.
                  Learn how to read and write code as well as how to test and "debug" it.
                  Designed for students with and without prior programming experience who'd like to learn Python specifically.
                  Learn about functions, arguments, and return values (oh my!); variables and types; conditions and Boolean expressions; loops; and objects and methods.
                  Plus exceptions, file I/O, and libraries. Hands-on opportunities for lots of practice.
                  Exercises inspired by real-world programming problems.
                  """)

    assert summarize_text(input_text, ratio=0.5) != ""
    assert summarize_text(input_text, ratio=0.5) != input_text
    assert len(summarize_text(input_text, ratio=0.5)) < len(input_text)


def test_capitalize_title():
    assert capitalize_title("hello world") == "HELLO WORLD"
    assert capitalize_title("  mixed Case Text  ") == "MIXED CASE TEXT"
    assert capitalize_title("") == ""
