#문자열처리 문제
def solution(s):
    answer = ""
    idx = 0
    while idx < len(s) :
        if s[idx] == "z" :
            answer += "0"
            idx += 3
        elif s[idx] == "o":
            answer += "1"
            idx += 2
        elif s[idx] == "t":
            if s[idx+1] == "w":
                answer += "2"
                idx+=2
            else :
                answer += "3"
                idx+=4
        elif s[idx] == "f":
            if s[idx+1] == "o":
                answer += "4"
                idx+=3
            else :
                answer += "5"
                idx+=3
        elif s[idx] == "s":
            if s[idx+1] == "i":
                answer += "6"
                idx+=2
            else :
                answer += "7"
                idx+=4
        elif s[idx] == "e":
            answer += "8"
            idx+=4
        elif s[idx] == "n":
            answer += "9"
            idx+=3
        else :
            answer += s[idx]
        idx+=1

    return int(answer)
