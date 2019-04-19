#Euclid Algorithm Python
def returnHCF(a, i):

    while i != 0:
         #Waits For The Remainder To Equal 0
        x = a % i #Finds The Remainder
        a = i #Switches The Variables For Next Run
        i = x

    return a #Returns Our Final Findings



#Code By Sam Poder, sampoder.github.io 




