def get_sum_avg(*marks):
    sum=0
    for n in marks:
        if type(n)== int or float:
            sum += n
    avg = sum/len(marks)
    return f"Summe: {sum}\nDurschnitt: {avg:.2f}"
 
print(get_sum_avg(60,80,95,56,77,84,97))
 
# Sum: ....
# Avg: ...