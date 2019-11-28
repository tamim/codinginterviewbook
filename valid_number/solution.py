def is_valid_number(num):
    num = num.strip()
    
    if len(num) == 0:
        return 0
    
    i, len_num = 0, len(num)
    if num[0] == '+' or num[0] == '-':
        i += 1
    
    gotExp = False
    gotDecimal = False
    gotSignAfterExp = False
        
    while i < len_num:
        if num[i] in "0123456789":
            i += 1
            continue
        if num[i] == '.':
            if gotDecimal or gotExp:
                return 0
            if i + 1 < len_num and num[i+1] in "0987654321":
                i += 1
                gotDecimal = True
            else:
                return 0
        elif num[i] == 'e' or num[i] == 'E':
            if gotExp or i == len_num - 1:
                return 0
            gotExp = True
        elif num[i] in "+-":
            if gotSignAfterExp:
                return 0
            if gotExp:
                gotSignAfterExp = True
                if i == len_num - 1:
                    return 0
            else:
                return 0
        else:
            return 0
            
        i += 1
        
    if i == len_num and num[i-1] in "0987654321":
        return 1
    else:
        return 0

def is_valid_number2(number):
