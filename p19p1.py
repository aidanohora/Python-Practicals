def convertbase(x,y):
    """takes a number in base 10 and a base of 2, 8 or 16
    first arguement is the number in base 10 and second is the desired base
    return number converted to base selected
    assumes both argumenets are positive integers"""

    if y == 2 or y == 8:
        res = 0
        i = 0
        while i < len(y):
        res = (int(y[i]) * (x ** i)) + res
        i += 1
return res

    elif y == 8:
        a = ""
        while x > 0: 
            answer = str(x%8)
            x = x//8
            answer += a
            a = answer
        return answer

    elif y == 16:
        a = ""
        while x > 0: 
            answer = x%16
            if answer == 10:
                answer = "A"
            elif answer == 11:
                answer = "B"
            elif answer == 12:
                answer = "C"
            elif answer == 13:
                answer = "D"
            elif answer == 14:
                answer = "E"
            elif answer == 15:
                answer = "F"
            elif answer == 16:
                answer = "G"
            else:
                answer = str(answer)
            x = x//16
            answer += a
            a = answer
        return answer

    else:
        return "Error: Cannot convert to that base."
