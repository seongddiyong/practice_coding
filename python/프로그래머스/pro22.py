def solution(m, musicinfos):
    answer = None
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    
    for i in musicinfos:
        start, end, title, code = i.split(',')
        
        hour,minute = map(int,start.split(':'))
        start = hour*60 + minute
        hour,minute = map(int,end.split(':'))
        end = hour*60 + minute
        time = end - start
        code = code.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')

        d = (time // len(code)) + 1
        code = code * d
        code = code[:time]
        
        if m not in code:
            continue
    
        if answer == None or answer[0] < time or (answer[0] == time and answer[1] > start):
                    answer = (time, start, title)
                    
    if answer:
        return answer[-1]
        
    return "(None)"

m = "CC#BCC#BCC#BCC#B"	
music = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
print(solution(m,music))