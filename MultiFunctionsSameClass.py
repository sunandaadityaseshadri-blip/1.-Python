class MultiFunctions():
    def Subfields(SubFieldList):
        for temp in SubFieldList:
            print(temp)

    def OddEven(num):
        if(num%2==0):
            print(num,"is Even number")
        else:
            print(num,"is Odd number")

    def Elegible(Gender, Age):
        if((Gender=="Male" or Gender=="male") and Age >=21):
            print("Eligible")
        elif((Gender == "female" or Gender=="Female") and Age >=18):
            print("Eligible")
        else:
            print("NOT ELIGIBLE")
    
    def percentage(eng, mat, phy, che, bio):
        total = (eng+mat+phy+che+bio)
        overall= total/5
        return total, overall
        
    def triangle(height, breadth, hght1,hght2, brd1):
        print("Height:", height)
        print("Breadth:", breadth)
        print("Area formula: (Height*Breadth)/2")
        area = (height*breadth)/2
        print("Area of triangle:",area)
        print("Height1:",hght1)
        print("Height2:",hght2)
        print("Breadth:",brd1)
        print("Perimeter formula: Height1+Height2+Breadth")
        perimeter= (hght1+hght2+brd1)
        print("Perimeter of Triangle: ",perimeter)