# 주어진 조건을 만족하기 위한 조건들을 찾고 구현
def SignalProcessing(signal):
    i = 0
    
    while True:

        if signal[i] == '1':
            i += 1
            if i == len(signal):
                return 0

            if signal[i] != '0':
                return 0
            cnt = 0
            while signal[i] == '0':
                cnt+=1
                i+=1
                if i == len(signal):
                    return 0
            if cnt<2:
                return 0
            if signal[i] != '1':
                return 0
            cnt = 0
            while signal[i] == '1':
                i+=1
                cnt += 1
                if i == len(signal):
                    return 1
                if signal[i] == '0' and cnt >= 2:
                    if i+1<len(signal) and signal[i+1] == '0':
                        i -= 1
                        break
                        

        
        elif signal[i] == '0':
            i+=1
            if i==len(signal):

                return 0
            if signal[i] != '1':
                

                return 0
            i+=1
        if i == len(signal):
            return 1
    return 1

        

    
n = int(input())

for i in range(n):
    signal = input()

    if SignalProcessing(signal) == 0:
        print('NO')
    else:
        print('YES')