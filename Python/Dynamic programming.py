# QUESTION 1 #

# This class takes two entries (entry no. of student and list of courses taken by student)
class Student:
    def __init__(self,entryNo,listofcourses):
        self.entryNo = entryNo
        self._listofcourses = listofcourses # (Private Attribute)

        # now define three empty lists which will take input as defined
        self.attemptedquiz=[]
        self.quiztitlelist =[]
        self.coursecodelist=[]

    # In the above empty lists, we store course code, quiz title and attempted answers of a particular quiz.
    def attempt(self, courseCode, quizTitle, attemptedAnswers):
        self.coursecodelist.append(courseCode)
        self.quiztitlelist.append(quizTitle)

        # Through this we ignore the new attempt
        if (courseCode,quizTitle,attemptedAnswers) not in self.attemptedquiz:
            self.attemptedquiz.append([courseCode,quizTitle,attemptedAnswers])

    # Gives the unattempted quizzes by a student of every course in the form of a list
    # containing course code and and it's unattempted quizzes
    def getUnattemptedQuizzes(self):
        # initially we define an empty list in which we will append the tuples
        list = []

        # Now we go to every course in list of courses and check
        for i in self._listofcourses:
            for j in i.LISTOFQUIZ():

                # if it's course code is not in my attempted coursecode list
                # if not, it means i have not given any quiz of that course
                # so we append all quiz titles of that course with course code one by one
                # by ranging j in list of quizzes
                if i.COURSECODE() not in self.coursecodelist:
                    list.append((i.COURSECODE(),j.QUIZTITLE()))

                # if course code is in my attempted course code list
                # then we have to check the quiz title not attempted by the student in that course
                # and append that particular quiz title only with it's course code
                else:
                    if j.QUIZTITLE() not in self.quiztitlelist :
                        list.append((i.COURSECODE(),j.QUIZTITLE()))
        # returns list containing course code and and it's unattempted quizzes
        return (list)

    # Gives the student average score as described in the assignment
    def getAverageScore(self,courseCode):
        # initially total correct answers and number of attempted quizzes are 0
        corrans = 0
        Noofattquiz = 0

        # now we range i in our list attemptedquiz and check
        # if quiz title in any particular tuple of attemptedquiz list
        # matches the quiz title of the course code of which we have to calculate average
        # then we increase number of attempted quizzes by one and also
        # increase corrans one by one by checking our answers with the given answers
        for i in self.attemptedquiz:
            for j in courseCode.LISTOFQUIZ():
                if j.QUIZTITLE() == i[1]:
                    Noofattquiz += 1
                    corrans += j.corrinpartquiz(i[2])
        # gives the average score in the desired form
        return (corrans / Noofattquiz)


# This class takes two entries(course code and list of quizzes in that course)
class Course:
    def __init__(self,courseCode,listofQuiz):
        self.courseCode= courseCode
        self.listofQuiz = listofQuiz

    # Gives course code of the course
    def COURSECODE(self):
        return self.courseCode

    # Gives list of quizzes of a particular course
    def LISTOFQUIZ(self):
        return self.listofQuiz


# This class takes two entries(title of the quizzes and list of correct options of the given quizzes)
class Quiz:
    def __init__(self,title,listofcoorectopt):
        self.title = title
        self._listofcoorectopt = listofcoorectopt

    # Gives the title of the quiz of a particular course
    def QUIZTITLE(self):
        return self.title

    # Calculates the total score or correct answers in a particular quiz
    def corrinpartquiz(self,markedopt):
        num = 0
        x = len(self._listofcoorectopt)

        # loop helps to check number of correct answers in a particular quiz
        # to get the number of correct answers
        # we increase num by 1 if correct answer matches attempted answer
        i=0
        while (i < x):
            if self._listofcoorectopt[i] == markedopt[i]:
                num += 1
            i += 1
        return num


col100q1 = Quiz('Quiz1', ['a','b','b'])
col100q2 = Quiz('Quiz2', ['b','d','c'])
col100 = Course('COL100', [col100q1, col100q2])
mtl100q1 = Quiz('Quiz1', ['a','b','d'])
mtl100q2 = Quiz('Quiz2', ['d','c','a'])
mtl100 = Course('MTL100', [mtl100q1, mtl100q2])
s1 = Student('2019Mcc2562', [col100, mtl100])
s2 = Student('2017cc10377', [col100])
s1.attempt('MTL100', 'Quiz1', ['a','b','d'])
s1.attempt('MTL100', 'Quiz2', ['d','c','b'])
print(s1.getUnattemptedQuizzes())
print(s1.getAverageScore(mtl100))







# QUESTION 2 #
# This is defined to do linear mathematical operations on two given matrices.
# This class takes only one input that is the list
class Matrix:
    def __init__(self, lt):
        self.lt = lt

    # Arranges the given matrix in the form described in assignment
    def __str__(self):
        # in every defined function i have taken a and b as defined below.
        a = len(self.lt)
        b = len(self.lt[0])

        # Helps to left align the rows and represent in given/desired format
        for i in range(a):
            for j in range(b):
                print("{0:<4}".format(self.lt[i][j]), end=" ")
            print()

    # Gives addition of two matrices
    def __add__(self, B):
        a = len(self.lt)
        b = len(self.lt[0])
        # initially I taken a temporary matrix in which there are b rows and a columns
        # each element of the matrix is zero at this time
        # now we will overwrite each element of the matrix
        X = [[0 for i in range(a)] for j in range(b)]

        # To overwrite we define
        # X(i,j)th element = (i,j)th element of one matrix + corresponding(i,j)th element of other matrix
        # by ranging i and j in range of a and b respectively.
        for i in range(a):
            for j in range(b):
                X[i][j] = self.lt[i][j] + B.lt[i][j]
        # returns the addition of two matrices in the format given in assignment(catered by .printformat())
        return Matrix(X).__str__()

    # Gives subtraction of two matrices
    def __sub__(self, B):
        a = len(self.lt)
        b = len(self.lt[0])
        # initially I taken a temporary matrix in which there are b rows and a columns
        # each element of the matrix is zero at this time
        # now we will overwrite each element of the matrix
        X = [[0 for i in range(a)] for j in range(b)]

        # To overwrite we define
        # X(i,j)th element = (i,j)th element of one matrix - corresponding(i,j)th element of other matrix
        # by ranging i and j in range of a and b respectively.
        for i in range(a):
            for j in range(b):
                X[i][j] = self.lt[i][j] - B.lt[i][j]
        # returns the subtraction of two matrices in the format given in assignment(catered by .printformat())
        return Matrix(X).__str__()

    # Gives multiplication of two given matrices
    def __mul__(self, D):
        a = len(self.lt)
        b = len(self.lt[0])
        m = len(D.lt[0])

        # initially I taken a temporary matrix in which there are a rows and m columns
        # each element of the matrix is zero at this time
        # now we will overwrite each element of the matrix
        X = [[0 for j in range(m)] for i in range(a)]

        # By ranging i,j and k in range a,m and b respectively
        # we overwrite (i,j)th element by [i,k]th element of first matrix * (k,j)th element of second matrix
        for i in range(a):
            for j in range(m):
                for k in range(b):
                    X[i][j] += self.lt[i][k] * D.lt[k][j]
        # returns the multiplication of two matrices in the format given in assignment(catered by .printformat())
        return (Matrix(X).__str__())

    # Gives multiplication of a scalar with a matrix
    def __scalarmul__(self, D):
        a = len(self.lt)
        b = len(self.lt[0])

        # we multiply each element of matrix by D(scalar)
        # by ranging i and j in a and b respectively
        for i in range (a):
            for j in range(b):
               self.lt[i][j] *= D
        # returns the multiplication of a scalar with a matrix in the format given in assignment(catered by .printformat()
        return (Matrix(self.lt).__str__())

    # Gives the matrix in the form of tuples with its indices as given in assignment problem
    def toSparse(self):
        # initially taken an empty list X in which we will add sublists which will contain tuples.
        X = []
        a = len(self.lt)
        b = len(self.lt[0])

        # As we do not have to add the element with value 0 in matrix
        # we check (i,j)th element
        # if it is not equal to 0 then we append the tuple containing the index of that element and it's value in an empty list A
        # then we append these various tuples in empty list X defined earlier
        for i in range(a):
            A = []
            for j in range(b):
                if self.lt[i][j] != 0:
                    A.append((j, self.lt[i][j]))
            X.append(A)
        return X



# This is defined to do linear mathematical operations on two given sparse matrices.
# This class takes only one input that is the list in sparse matrix form.
class SparseMatrix:
    def __init__(self, lt):
        self.lt = lt

    # Gives addition of two sparse matrices
    def __add__(self, e):
        # in every defined function i have taken a and b as defined below.
        a = len(self.lt)
        b = len(self.lt[0])

        # taken an empty list within a list containing rows as in the two given lists and no columns.
        SMatrix = [[] for i in range(a)]
        i = 0
        while (i < a):
            # we add the tuples from second list to the first list of a particular sublist of list e or self
            self.lt[i].extend(e.lt[i])
            # Then we add this tuple to our sublist of above empty list
            SMatrix[i] = self.lt[i]

            # now we check all these conditions on list SMatrix
            j = 0
            while j < len(SMatrix[i]):
                # this k helps to move over all the tuples of SMatrix with a particular i and equal to j+1
                k = j + 1
                while k < len(SMatrix[i]):
                    # if the index of the matrix self matches with the index of matrix e OR
                    # first element of tuple matches with first element of another tuple in that sublist
                    # then we add second element of both tuples and replace our first tuple
                    # with tuple containing matched index and addition of second element of both tuples with that index.
                    # also we remove the other tuple as it is no longer required.
                    if SMatrix[i][j][0] == SMatrix[i][k][0] :
                        SMatrix[i][j] = (SMatrix[i][j][0], SMatrix[i][j][1] + SMatrix[i][k][1])
                        SMatrix[i].remove(SMatrix[i][k])
                    k += 1
                j += 1
            i += 1
        # returns the SMatrix with all the changes made containing additions of two sparse matrices
        return SMatrix

    # Gives subtraction of two sparse matrices
    def __sub__(self, e):
        a = len(self.lt)
        b = len(self.lt[0])

        # taken an empty list within a list containing rows as in the two given lists and no columns.
        SMatrix = [[] for i in range(a)]

        # now we check all these conditions on list SMatrix
        i = 0
        while (i < a):
            # we add the tuples from second list to the first list of a particular sublist of list e or self
            self.lt[i].extend(e.lt[i])
            # Then we add this tuple to our sublist of above empty list
            SMatrix[i] = self.lt[i]
            j = 0
            while j < len(SMatrix[i]):
                # this k helps to move over all the tuples of SMatrix with a particular i and equal to j+1
                k = j + 1
                while k < len(SMatrix[i]):
                    # if the index of the matrix self matches with the index of matrix e OR
                    # first element of tuple matches with first element of another tuple in that sublist
                    # then we subtract second element of both tuples and replace our first tuple
                    # with tuple containing matched index and subtraction of second element of both tuples with that index.
                    # also we remove the other tuple as it is no longer required.
                    if SMatrix[i][j][0] == SMatrix[i][k][0]:
                        SMatrix[i][j] = (SMatrix[i][j][0], SMatrix[i][j][1] - SMatrix[i][k][1])
                        SMatrix[i].remove(SMatrix[i][k])
                    k += 1
                j += 1
            i += 1
        # returns the SMatrix with all the changes made containing subtraction of two sparse matrices
        return SMatrix

    # Gives multiplication of a scalar with given sparse matrix.
    def __scalarmul__(self,B):
        a = len(self.lt)
        b = len(self.lt[0])

        # As we do not have to represent the tuple having second element 0
        # we return 'a' empty sublists within a list
        if B == 0 :
            return SparseMatrix([[] for i in range(a)])

        # Now if B is not equal to 0
        else:
            # Then we define 'a' empty sublists in which we will append the the required tuples.
            X = [[] for i in range(a)]

            # we will put the tuples with their first element as it is and multiplying their second element with a scalar
            # by ranging i and j as shown and appending the tuples one by one in the desired sublist.
            for i in range(a):
                for j in range(len(self.lt[i])):
                    X[i].append((self.lt[i][j][0], B * self.lt[i][j][1]))
            # Returns the sparse matrix multiplied with given input.
            return X

    # Gives the sparse matrix in form of a matrix i.e. list within a list
    def toDense(self):
        a = len(self.lt)
        b = len(self.lt[0])

        # initially I taken a temporary matrix in which there are b rows and a columns
        # each element of the matrix is zero at this time
        # now we will overwrite each element of the matrix
        X = [[0 for i in range(a)] for i in range(b)]

        # now we range i in 'a' so that we can move across every row
        # But we range j according to the length of the sublists
        # so to cater the case in which some elements are zero in matrix.
        # Then by checking the indices we overwrite elements of matrix X by second value of the tuple.
        for i in range(a):
            for j in range(len(self.lt[i])):
                X[i][self.lt[i][j][0]] = self.lt[i][j][1]
        # returns the sparse matrix in matrix format.
        return X




A = ([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = ([[-2, 0, 5], [0, 0, 0], [0, 10, 0]])
D = 2
print(Matrix(A).__mul__(Matrix(B)))
print(Matrix(A).toSparse())
print(Matrix(A).__scalarmul__(D))
L = [[(0, 1), (1, 2), (2, 3)], [(0, 4), (1, 5), (2, 6)], [(0, 7), (1, 8), (2, 9)]]
e = [[(0, -2), (2, 5)], [], [(1, 10)]]
print(SparseMatrix(L).toDense())
print(SparseMatrix(L).__scalarmul__(D))
