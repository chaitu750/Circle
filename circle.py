# Circle 
# to draw a circle by printing spaces and characters
R = int(input("Enter Radius of Circle(no of spaces): ")) # max size of R is limited (as per availability of row space)
r = R #(Distance from circle center to present line)
L = 0 #(Length of each row)
l = 0 #(length of row outside circle(Horizontal ))
i=0
n= R*1 #=>controls roundness of circle(eg:R*1.5, R*.5 etc.)
while i<=n:
    L = round((R**2-r**2)**0.5)
    l = R-L
    i+=1
    print(' '*l,'+','*'*(L*2),'+',' '*l,sep='')
    r -= 2*R/n
