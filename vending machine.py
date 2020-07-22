STAMP_PRICE= 44
dollar= float(input("Enter the number of dollars:"))
first_stamp_num= dollar * 100//STAMP_PRICE
#print(first_stamp_num)
change = dollar * 100 % STAMP_PRICE
quarter = change//25
change = change % 25
dime= change //10
change= change % 10
nickel = change// 5
change = change % 5
print( int(quarter), 'quarter(s)\n', int(dime),' dime(s)\n', int(nickel),'nickel(s)\n',  int(change))
