'''
A binary watch has 4 LEDs on the top to represent the hours (0-11), 
and 6 LEDs on the bottom to represent the minutes (0-59). 
Each LED represents a zero or one, with the least significant bit on the right.

Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), 
return all possible times the watch could represent. You may return the answer in any order.

The hour must not contain a leading zero.

For example, "01:00" is not valid. It should be "1:00".
The minute must be consist of two digits and may contain a leading zero.

For example, "10:2" is not valid. It should be "10:02".
 
'''
def readBinaryWatch(self, turnedOn: int) -> List[str]:
    def hoursBasedOnBitsOn(n):
        ans = []
        for i in range(12):
            n_temp = i
            cnt = 0
            while n_temp > 0:
                n_temp = n_temp & (n_temp - 1)
                cnt += 1

            if cnt == n:
                ans.append(str(i))

        return ans

    def minsBasedOnBitsOn(n):
        ans = []
        for i in range(60):
            n_temp = i
            cnt = 0
            while n_temp > 0:
                n_temp = n_temp & (n_temp - 1)
                cnt += 1

            if cnt == n:
                ans.append(str(i) if i >= 10 else "0"+str(i))

        return ans

    ans = []
    for i in range(turnedOn + 1):
        hoursBit = i
        minutesBit = turnedOn - i

        hoursArr = hoursBasedOnBitsOn(hoursBit)
        minsArr = minsBasedOnBitsOn(minutesBit)

        for h in hoursArr:
            for m in minsArr:
                ans.append(h + ":" + m)


    return ans



    

