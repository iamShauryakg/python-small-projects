import pywhatkit as pw

text1 = """
        My name is Shaurya Kumar Gupta and i am a python developer.
        i am also skilled in Sql and html Css.
        
"""
pw.text_to_handwriting(text1, "conva.png", (0, 0, 200))
print(" successfully converted")
