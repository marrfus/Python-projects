

    #   *
    #  * *
    # * * *
    #* * * *
    #   * 


def baum():
    j=1   #Elementen in Reihen
    i=5   #Reihe
    while i>0:        
        if j<=4:
            print(" "*(4-j)+"* "*j)
            j+=1
        else:
            print(" "*3+"*")  
        i-=1  


baum()