import random

choose_mad_libs = input("Which mad libs would you like to do?/n[A] ")
strings = ["Maraneri is a village in the sivakasi taluk of Virudhunagar district, Tamil Nadu, India.",
"The HP Slate 500 is a multi-touch capable Windows 7 tablet computer that was announced at CES 2010 and launched on 22 October 2010."]
string = random.choice(strings)
print(string)

