print('Enter your larger number:')
a = input() #Defines Our Largest Number As A Variable

print('Enter your smaller number:')
i = input() #Defines Our Smallest Number As A Variable That We Will Use In Our While Function

while i != 0: #Waits For The Remainder To Equal 0
  x = a % i #Finds The Remainder
  a = i #Switches The Variables For Next Run
  i = x
  

print "The highest common factor is:" #Prints Our Final Findings
print a

#Code By Sam Poder, sampoder.github.io 