def solution1(cipher, code):
    answer = ''
    for i in range(1,len(cipher)//code+1):
        answer += cipher[i*code-1]
    return answer

def solution2(cipher, code):
    return cipher[code-1::code]