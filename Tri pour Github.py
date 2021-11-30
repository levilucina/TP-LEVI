def Min(list):
    var=list[0]
    for i in list:
        if var>i:
            var=i
    return var
    
def triSelect (list):
    result=[]
    while len(list)>0:
        var=Min(list)
        
    return result
print(Min([5,3,8,9]))