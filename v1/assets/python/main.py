# command to get server running
# python -m http.server 80
# in root folder
# then localhost/index.html in a browser
texts = {
        'intro' : 'Hello, we are something',
}

def fac(x):
    if x <= 0: return 1
    return x * fac(x-1)

def init():
    """
    Populate the texts dictionary
    with function calls
    """
    global texts
    texts['python'] = fac(5)

def propagate_html():
    """
    Propagate the html page divs with the texts
    """
    for k in texts:
        pyscript.write(k, texts[k])

def main():
    init()
    propagate_html()

main()
