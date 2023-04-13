sub1=int(input("Enter the marks subject 1:"))
sub2=int(input("Enter the marks subject 2:"))
sub3=int(input("Enter the marks subject 3:"))
if(sub1<33 or sub2<33 or sub3<33):{
    print("you are fail")
}
elif(sub1+sub2+sub3)/3<40:{
    print("you are fail")
}
else:{
    print("congatulation! you are passsed")
}