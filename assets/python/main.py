# command to get server running
# python -m http.server 80 
# in root folder
# then localhost/index.html in a browser
def fac(x):
    if x <= 0: return 1
    return x * fac(x-1)

x = fac(5)
pyscript.write('python', x)
