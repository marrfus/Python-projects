
def kehre_um(text):
    if type(text)!= str:
        text=input("Was möchten Sie kehren? ")
    txet = ""
    b = len(text)
    while b>0:
        txet+=text[b-1]
        b-=1
    return txet

