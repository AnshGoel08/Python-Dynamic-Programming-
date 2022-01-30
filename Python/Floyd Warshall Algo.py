# QUESTION 1 #

# Finds minimum of the three numbers a,b,c
def Min(a,b,c) :

# PRECONDITION: 3 numbers a,b,c are given
              # make a list of these three numbers
              # initial minimum is first element of the list
    list = [a,b,c]
    minimum = list[0]

# We range x from 0 to length of list
# if there is an element whose value is less than initial minimum
# That element is the minimum of three
    for x in range(0,len(list)) :
        if list[x] < minimum :
            minimum = list[x]
    return minimum
# POSTCONDITION: Gives smallest number among 3 numbers



def gridPlay(grid):
    # PRECONDITION:
    # initially we have defined x and y
    # then a matrix is made with (y+1) columns and (x+1) rows whose each entry is 0
    x = len(grid) - 1
    y = len(grid[0]) - 1
    totalcost = [[0 for t in range(len(grid[0]))] for t in range(len(grid))]

    i = 0
    while (i <= x):
        j = 0
        while (j <= y):
            # INVARIANT I1 :
            # For 0 <= i < k1 where k1 is any arbitrary index
            # For 0 <= j < k2 where k2 is any arbitrary index
            # from if and elif conditions we first define all elements of first row and first column.
            # there are three paths to reach the element (i,j) of matrix that is through (left,right and diagonal) elements
            # we take the minimum of the three paths and add it to the cost of element (i,j) to get the lowest cost
            # The previous three paths have got their minimum value just like this. This proves dynamic programming.
            if j == 0:
                totalcost[i][0] = totalcost[i - 1][0] + grid[i][0]
            elif i == 0:
                totalcost[0][j] = totalcost[0][j - 1] + grid[0][j]
            else:
                totalcost[i][j] = Min(totalcost[i - 1][j - 1], totalcost[i - 1][j], totalcost[i][j - 1]) + grid[i][j]

            j += 1
        i += 1
    return totalcost[x][y]
# POSTCONDITION :
# Gives the minimum cost to reach from (0,0) to (x,y) in matrix.

grid  = [[8, 0, 0],
         [3, 5, 0],
         [4, 9, 2]]
print(gridPlay(grid))


# QUESTION 2 #

# Finds minimum of the three numbers a,b,c
def Min3(a,b,c) :
    # PRECONDITION: 3 numbers a,b,c are given
    # make a list of these three numbers
    # initial minimum is first element of the list
    list = [a,b,c]
    minimum = list[0]

    # We range x from 0 to length of list
    # if there is an element whose value is less than initial minimum
    # That element is the minimum of three
    for x in range(0,len(list)) :
        if list[x] < minimum :
            minimum = list[x]
    return minimum

# Similar to above Min3 but calculates minimum for 2 numbers(a,b)
def Min2(a,b) :
    list = [a,b]
    minimum = list[0]

    for x in range(0,len(list)) :
        if list[x] < minimum :
            minimum = list[x]
    return minimum


# I have converted this problem similar to the first problem by making a matrix in which we want minimum value of the element(x,y).
# now through dynamic programming we want minimum value of the three path from which we reach element(x,y).
# This is catered by if else conditions.
# helps to find minimum steps of edits required to convert A to B.
def stringProblem(A,B):

    # PRECONDITION :
    # we have defined a list of vowels and a matrix with (y+1) columns and (x+1) rows.
    lsofvowel = ["a", "e", "i", "o", "u"]
    x = len(A)
    y = len(B)
    initiallt = [[0 for i in range(y+1) ] for j in range(x+1)]

    i = 0
    while (i < x + 1) :
        j = 0
        while (j < y + 1) :
            # INVARIANT :
            # 0 <= i <= K where K is an arbitrary integer
            # 0 <= j <= K1 where K1 is an arbitrary integer


            # if length of string A and string B = 0 then no edits required therefore 0
            initiallt[0][0] = 0

            # if B is empty then we have to delete as many times as the number of elements in string A
            # and therefore we increase element of first column by one successively.
            # first we delete till kth element of string A and then extend the definition of invariance.
            if j == 0:
                initiallt[i][0] = initiallt[i - 1][0] + 1

            # if A is empty then we have to insert as many times as the number of elements in string B
            # And therefore we increase element of the first row by one successively
            # first we insert till k1th element of string B and then extend the definition of invariance.
            elif i == 0:
                initiallt[0][j] = initiallt[0][j-1] + 1

            # if kth element of A = K1th of B then that element(k+1,k1+1) of matrix does not require any edits
            # we move down to the next elements of the strings by reducing the indices by 1.
            elif A[i-1] == B[j-1]:
                initiallt[i][j] = initiallt[i-1][j-1]

            # As vowel cannot be replaced by consonant
            # so we are left with insert and delete only
            # hence we take minimum of two.
            elif A[i-1] != B[j-1] and A[i-1] in lsofvowel and B[j-1] not in lsofvowel :
                initiallt[i][j] = Min2(initiallt[i-1][j],initiallt[i][j-1]) + 1

            # this else condition is
            # A[i-1] != B[j-1] and (A[i-1] not in vowel with B[j-1] anything) or (A[i-1] and B[j-1] both in vowel)
            # we have all three options of delete insert and replace but we take that which gives minimum value
            else :
                initiallt[i][j] = Min3(initiallt[i-1][j],initiallt[i][j-1],initiallt[i-1][j-1]) + 1
                                       # DELETE           # INSERT           # REPLACE
            j += 1
        i += 1
    return(initiallt[x][y])
    # POSTCONDITION :
    # Gives minimum steps of edits required to convert string A to string B





# QUESTION 3 #

# Gives every row of the month in the form of a string.
def individualdate(SOM, x, EOM):
    # initially we define an empty string im which we can overwrite
    string = ""

    for i in range(7):
        if x == 1: # Gives first row of the month.
            if SOM > i: # helps to give 3 spaces consecutively till we get first day of the month.
                string +=  "   "
            else: # Since x=1 that is single digit
                if i == 6: # So if i = 6 then it will get print below sunday and since one space left, we give it through inverted commas
                    string += str(x) + " "
                else: # since single digit therefore we print it and then leave two spaces.
                    string += str(x) + "  "
                x += 1
        elif x > EOM: # Final condition to end the month
            if i == 6:
                string += "  "
            else:
                string += "   "
        else: # Gives rows of dates other than first
            if i == 6: # to put date below Sunday
                if x // 10 == 0: # if date is single digit then we have to add an empty space
                    string += str(x) + " "
                else: # directly prints the date
                    string += str(x)
            else: # to put dates below days other than sundays
                if x // 10 == 0: # if date is single digit then we have to add two spaces before another date comes
                    string += str(x) + "  "
                else: # directly prints the date and add one space before other date comes
                    string += str(x) + " "
            x += 1
    return (string, x)

# Gives all dates in a pack of three months
def alldates(SOM1, SOM2, SOM3, EOM1, EOM2, EOM3):
    x = 1
    y = 1
    z = 1

    # this loop helps to print dates row wise
    # that is firstly all first rows of the three months will be defined
    # and then loop continues till the mentioned conditions giving all the dates of 3 months
    while (x <= EOM1 or y <= EOM2 or z <= EOM3) :
        (string1, x) = individualdate(SOM1, x, EOM1)
        (string2, y) = individualdate(SOM2, y, EOM2)
        (string3, z) = individualdate(SOM3, z, EOM3)

        print(string1 + "          "  + string2 + "           "  + string3)

# Function to check if year is leap year or not
def isleapyear(a):
    if (a % 4 == 0 and a % 100 > 0):
        return True
    else:
        return False

# First set of three months i.e. January,February,March
def printcalendar1(year):
    # Helps to calculate day of 1st January of the mentioned year in the form of indices.
    # That is index[0] = Mo ,index[1] =Tu ,index[2] = We ,index[3] =Th
    # index[4]= Fr ,index[5] = Sa, index[6] = Su
    p = (year - 1) // 100
    q = (year - 1) % 100
    SOM1 = (28 + q + (q // 4) + (p // 4) - (2 * p)) % 7

    # February will have 28 or 29 days depending year is leap or not
    if isleapyear(year):
        k = 29
    else:
        k = 28

    # prints the mentioned year in center aligned way
    print('{:^80}'.format(year))
    print("\n")

    # Helps to print month and day headings with specified spaces
    S1 = "{:^20}"
    S2 = "{:^40}"
    S3 = "{:^20}"

    print(S1.format("-JANUARY-") + S2.format("-FEBRUARY-") + S3.format("-MARCH-"))
    print(S1.format("Mo Tu We Th Fr Sa Su") + S2.format("Mo Tu We Th Fr Sa Su") + S3.format("Mo Tu We Th Fr Sa Su"))

    # Gives the first day of february in form of index
    SOM2 = (SOM1 + 31) % 7
    # Gives the first day of march in form of index
    SOM3 = (SOM2 + k) % 7

    # Gives the calendar of JANUARY,FEBRUARY and MARCH
    alldates(SOM1, SOM2, SOM3, 31, k, 31)

# First set of three months i.e. April,May and June
def printcalendar2(year):
    p = (year - 1) // 100
    q = (year - 1) % 100
    SOM1 = (28 + q + (q // 4) + (p // 4) - (2 * p)) % 7

    if isleapyear(year):
        k = 29
    else:
        k = 28

    SOM2 = (SOM1 + 31) % 7
    SOM3 = (SOM2 + k) % 7

    # Helps to print month and day headings with specified spaces
    S1 = "{:^20}"
    S2 = "{:^40}"
    S3 = "{:^20}"

    print(S1.format("-APRIL-") + S2.format("-MAY-") + S3.format("-JUNE-"))
    print(S1.format("Mo Tu We Th Fr Sa Su") + S2.format("Mo Tu We Th Fr Sa Su") + S3.format("Mo Tu We Th Fr Sa Su"))

    # Gives the first day of april in form of index
    SOM4 = (SOM3 + 31) % 7
    # Gives the first day of may in form of index
    SOM5 = (SOM4 + 30) % 7
    # Gives the first day of june in form of index
    SOM6 = (SOM5 + 31) % 7

    # Gives the calendar of APRIL,MAY and JUNE
    alldates(SOM4, SOM5, SOM6, 30, 31, 30)

# First set of three months i.e. July,August and September
def printcalendar3(year):
    p = (year - 1) // 100
    q = (year - 1) % 100
    SOM1 = (28 + q + (q // 4) + (p // 4) - (2 * p)) % 7

    if isleapyear(year):
        k = 29
    else:
        k = 28

    SOM2 = (SOM1 + 31) % 7
    SOM3 = (SOM2 + k) % 7
    SOM4 = (SOM3 + 31) % 7
    SOM5 = (SOM4 + 30) % 7
    SOM6 = (SOM5 + 31) % 7

    # Helps to print month and day headings with specified space
    S1 = "{:^20}"
    S2 = "{:^40}"
    S3 = "{:^20}"

    print(S1.format("-JULY-") + S2.format("-AUGUST-") + S3.format("-SEPTEMBER-"))
    print(S1.format("Mo Tu We Th Fr Sa Su") + S2.format("Mo Tu We Th Fr Sa Su") + S3.format("Mo Tu We Th Fr Sa Su"))

    # Gives the first day of july in form of index
    SOM7 = (SOM6 + 30) % 7
    # Gives the first day of august in form of index
    SOM8 = (SOM7 + 31) % 7
    # Gives the first day of september in form of index
    SOM9 = (SOM8 + 31) % 7

    # Gives the calendar of JULY,AUGUST and SEPTEMBER
    alldates(SOM7, SOM8, SOM9, 31, 31, 30)

# First set of three months i.e. October,November and December
def printcalendar4(year):
    p = (year - 1) // 100
    q = (year - 1) % 100
    SOM1 = (28 + q + (q // 4) + (p // 4) - (2 * p)) % 7

    if isleapyear(year):
        k = 29
    else:
        k = 28

    SOM2 = (SOM1 + 31) % 7
    SOM3 = (SOM2 + k) % 7
    SOM4 = (SOM3 + 31) % 7
    SOM5 = (SOM4 + 30) % 7
    SOM6 = (SOM5 + 31) % 7
    SOM7 = (SOM6 + 30) % 7
    SOM8 = (SOM7 + 31) % 7
    SOM9 = (SOM8 + 31) % 7

    # Helps to print month and day headings with specified space
    S1 = "{:^20}"
    S2 = "{:^40}"
    S3 = "{:^20}"

    print(S1.format("-OCTOBER-") + S2.format("-NOVEMBER-") + S3.format("-DECEMBER-"))
    print(S1.format("Mo Tu We Th Fr Sa Su") + S2.format("Mo Tu We Th Fr Sa Su") + S3.format("Mo Tu We Th Fr Sa Su"))

    # Gives the first day of October in form of index
    SOM10 = (SOM9 + 30) % 7
    # Gives the first day of November in form of index
    SOM11 = (SOM10 + 31) % 7
    # Gives the first day of December in form of index
    SOM12 = (SOM11 + 30) % 7

    # Gives the calendar of OCTOBER,NOVEMBER and DECEMBER
    alldates(SOM10, SOM11, SOM12, 31, 30, 31)

# Helps to make text file named CALENDAR.txt Which gives calendar of any mentioned year
def printCalendar(year):
    with open("CALENDAR.txt", "w") as f:
        print(printcalendar1(year), file=f)
        print("\n")
        print(printcalendar2(year), file=f)
        print("\n")
        print(printcalendar3(year), file=f)
        print("\n")
        print(printcalendar4(year), file=f)
    f.close()