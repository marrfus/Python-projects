

    #        *
    #       * *
    #      * * *
    #     * * * *
    #    * * * * *
    #   * * * * * *
    #  * * * * * * *
    #      * * *
    #      * * *
    #      * * *
    #      * * *

# def pfeil():
#     j=1
    
#     for i in range(7):
#         print(" "*(12-j)+"* "*j)
#         j+=1
#     for i in range(4):
#         print(" "*9+"* "*3)

def pfeil():
    j=1
    i=11
    while i>0:        
        if j<=7:
            print(" "*(12-j)+"* "*j)
            j+=1
        else:
            print(" "*9+"* "*3)  
        i-=1  



pfeil()