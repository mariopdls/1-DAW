firstside=int(input('First side: '))
secondside=int(input('Second side: '))
thirdside=int(input('Third side: '))

if firstside+secondside>thirdside and secondside+thirdside>firstside and thirdside+firstside>secondside:
    print ('You can form a valid triangle')
    if firstside==secondside==thirdside:
        print ('Equilateral triangle')
    elif firstside==secondside or firstside==thirdside or secondside==thirdside:
        print ('Isosceles triangle')
    elif firstside!=secondside!=thirdside:
        print ('Scalene triangle')

    if (firstside**2+secondside**2==thirdside**2) or (secondside**2+thirdside**2==firstside**2) or (thirdside**2+ firstside**2==secondside**2):
                print ('Right Triangle')
else:
    print ('You can not form a valid triangle')
