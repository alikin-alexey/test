from app import app
from flask import request

@app.route("/")
def index():
	return("hello world")

@app.route("/load-d", methods=["POST"])
def load_d():
        if request.is_json:
                req = request.get_json()
                dictionary = eval(req.get("dictionary"))

                f = open('dict', 'a')
                for x in dictionary:
                        f.write('{}\n'.format(x))
                f.close()
                return('Dictionary aploaded, go to \"get?word=***\"')
        else:
                return("No json recieved")


@app.route("/get")
def get():
    f = open('dict', 'r')
    word = request.args.get('word')
    anagrams = []
    res = '[\"'
    for line in f:
        sorted_line = sorted(list(line.strip()))
        sorted_word = sorted(list(word))
        if sorted_line == sorted_word:
            anagrams.append(line)
    if anagrams:
        return('[\"'+'\",\"'.join(anagrams[1:])+'\"]')
    else:
        return('null')
