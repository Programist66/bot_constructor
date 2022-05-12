# block codes sites
# 7665856486i5y57 - TITLE
# 7e78f73hf83hfu3 - body
# 7ygf7g3fh3ufg83 - background
# 7h7gffhgfefugif - div_class
import blanks

global text_list
text_list = []

def create_site():
    global text_list
    o = open("Patterns/index_form.html", 'r')
    origion_text = o.read()
    text_list = origion_text[66:].split()
    text_list.insert(0, origion_text[:66])
    o.close()

def choose_title(title):
    global text_list
    text_list[text_list.index("7665856486i5y57")] = title

def choose_background(text, isPhoto):
    if isPhoto == True:
        text_list[text_list.index("7ygf7g3fh3ufg83")] = "url(" + text + ") repeat"
    if isPhoto == False:
        text_list[text_list.index("7ygf7g3fh3ufg83")] = text

def add_div(filling, top, left,  color):
    global text_list
    name_classes = blanks.generate_random_string(8)
    text_list.insert(text_list.index("7e78f73hf83hfu3"), blanks.add_divs(name_classes, filling))
    text_list.insert(text_list.index("7h7gffhgfefugif"), '.'+name_classes+ "{" + f'background:{color}; top: {top}px; left: {left};' + "}")

def complete_creation():
    global text_list
    f = open("index.html", 'w+')
    text = ''
    for i in text_list:
        text += i
    text = text.replace("7e78f73hf83hfu3", "")
    text = text.replace("7h7gffhgfefugif", "")
    f.write(text)
    f.close()


create_site()
add_div("feffefe", 0, 0, "#91b592")
complete_creation()