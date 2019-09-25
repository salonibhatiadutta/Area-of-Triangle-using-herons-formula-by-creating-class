#   WAP to create  a class for calculating the area an perimeter of triangle with sides a,b,c
class   Triangle:

    def __init__(self,a,b,c): #taking sides as a,b,c
        self.a= a
        self.b= b
        self.c= c
        self.s=0         # s= perimeter
        self.r=0         # r= area

# defining function to calculate perimeter=a+b+c
    def perimeter(self):
        self.s= self.a+self.b+self.c

#defining function to calculate area using heron's formula 

    def area(self):
        self.s= self.s/2      # calculating half perimeter s=(a+b+c)/2
        import math
        #calculating area=sqrt(s*(s-a)*(s-b)*(s-c))
        self.r= math.sqrt(self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c))

side=  Triangle(10,12,14)
print("sides=",side.a,side.b,side.c)
side.perimeter()
print("perimeter is:",side.s)
side.area()
print("area is:", side.r)
print(side.s)   # print half perimeter


