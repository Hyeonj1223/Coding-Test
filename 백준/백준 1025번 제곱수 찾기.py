if __name__ == '__main__':
    ans = -1
    dnm = [0, 1, -1]
    
    NM = input()
    
    N = int(NM[0])
    M = int(NM[2])
    
    input_list = []
    for n in range(N):
        input_list.append([])
        i = input()
        for m in range(M):
            input_list[n].append(i[m])
            
	    for n in range(N):
        for m in range(M):
             for step_1 in range(1, N+1):
                for step_2 in range(1, M+1):
                    for i in range(3):
                        for j in range(3):   
                            power_number = input_list[n][m]
                            tn = n
                            tm = m

                            power_number = int(power_number)

                            if pow(power_number, (1/2)) == int(pow(power_number, (1/2))):
                                ans = max(ans, power_number)
                            power_number = str(power_number)

                            if dnm[i] == 0 and dnm[j] == 0:
                                continue
                            while True:
                                nn = tn+step_1*dnm[i]
                                nm = tm+step_2*dnm[j]
                                if nn<0 or nm<0 or nn>=N or nm>=M:
                                    break

                                power_number = int(power_number + input_list[nn][nm])

                                if pow(power_number, (1/2)) == int(pow(power_number, (1/2))):
                                    ans = max(ans, power_number)
                                power_number = str(power_number)

                                tn = nn
                                tm = nm
 
    print(ans)