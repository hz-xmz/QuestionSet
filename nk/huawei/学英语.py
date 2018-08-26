# def reloop(n):
#     m1 = 'one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen'.split(',')
#     m2 = 'twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety'.split(',')
#     if(n<20):
#         return [m1[n-1]]
#     if(n<100):
#         return [m2[int(n/10)-2]] + reloop(n%10)
#     if(n<1000):
#         return [m1[int(n/100)-1]]+['hundred']+['and']+reloop(n%100)
#     else:
#         for w,p in enumerate(('thousand','million','billion'),1):
#             if(n<1000**(w+1)):
#                 return reloop(int(n/(1000**w)))+[p]+reloop(n%1000**w)
# def question():
#     n = int(input())
#     return ' '.join(reloop(n)) or 0
# while(True):
#     try:
#         print(question())
#     except:
#         break

def reloop(n):
    m1 = 'one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen'.split(',')
    m2 = 'twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety'.split(',')
    m3 = 'thousand,million,billion'.split(',')
    if(n<20):
        return m1[n-1:n]
    if(n<100):
        return [m2[int(n/10)-2]] + reloop(n%10)
    if(n<1000):
        return [m1[int(n/100)-1]]+['hundred']+['and']+reloop(n%100)
    else:
        for x,y in enumerate(m3,1):
            if n<(1000**(x+1)):
                return reloop(int(n/(1000**x))) + [y] + reloop(n%1000**x)
def question():
    n = int(input())
    return ' '.join(reloop(n)) or 0
while(True):
    try:
        print(question())
    except:
        break


