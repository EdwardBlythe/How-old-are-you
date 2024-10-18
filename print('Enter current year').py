print('Enter current year')
cy = int(input())

print('Enter current month')
cm = int(input())

print('Enter current day')
cd = int(input())

##current year * 365 + month * 30 + day = current time? 
ct = 365*cy + 30*cm + cd 

print('Enter birth year')
by = int(input())

print('Enter birth month')
bm = int(input())

print('Enter birth day')
bd = int(input())

bt = 365*by + 30*bm + bd

at = ct -bt

if( at < 10000 ):
    print('You will be 10,000 days old in ', at ,'days' )
else:
    print('You are ', at , 'days old' )