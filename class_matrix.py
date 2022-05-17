class matrix:

    def __init__(self,list,val_type,rows=None,cols=None):

        """ Initial function for transforming the list into the list of lists. Number of lists and items in each list
            is given by parameters rows and cols, respectively. Firstly, the function checks if all values are the same
            data type, specified by user. If so, the list of lists is assigned to mtx attribute. If not, the warning
            is displayed."""

        self.list = list
        l = len(list)
        logical = map(lambda x: isinstance(x,val_type),list) #check if all values are of the data type specified by user
        t = sum(logical) #sum the logical array
        if l != t:
            print("Values need to be the same type!") #if the sum of array is lower then length of input list, warning is displayed
        elif rows == None:
            rows = len(list) / cols #if number of rows is not specified, it is counted as length of list divided by num. of coumns
            mod = len(list) % cols #calculate modulo in order to check if number of columns is valid
            if mod == 0:
                rows = int(rows)
                self.mtx = [[list[i + j * cols] for i in range(cols)] for j in range(rows)] #if modulo = 0, matrix is created
            else:
                print("Inpropper number of rows and columns!") #if modulo is higher, warning is displayed
        else:
            cols = len(list) / rows #same as above, but in the case if number of rows is specified only, or both values are given
            mod = len(list) % rows
            if mod == 0:
                cols = int(cols)
                self.mtx = [[list[i + j * cols] for i in range(cols)] for j in range(rows)]
            else:
                print("Inpropper number of rows and columns!")

    def plus(self,value):

        """ The function provides element wise sum between two objects of matrix class.
            The value types in both objects need to be compatible for this operation."""

        if isinstance(value,matrix)==True:#check if the input object is of the class matrix
            value = value.mtx
            if len(value) == len(self.mtx) and len(value[0])==len(self.mtx[0]):#check if both objects have the same number of rows and columns
                ll = len(value)
                ln = len(value[0])
                result = [[self.mtx[j][i]+value[j][i] for i in range(ln)] for j in range(ll)]
                self.mtx = result #if the shapes are the same, computation is performed and the result overwrites the mtx attribute
            else:
                print("Matrices need to be the same shape!")#if shapes are different, warning is displayed
        elif type(self.list[0]) != type(value):
            print("Values need to be the same type!")#if the values in both objects are not the same type, warning is displayed
        else:
            result = map(lambda x: list(map(lambda y: y + value,x)),self.mtx)
            self.mtx = list(result)#if the input is scalar and the same data type as are values in self.mtx, computation is performed

    def minus(self,value):

        """ The function provides element wise division between two objects of matrix class.
                    The value types in both objects need to be compatible for this operation."""

        if isinstance(value,matrix)==True:
            if isinstance(value.mtx[0][0],str)==True or isinstance(self.mtx[0][0],str)==True:#check if the values in any of the objects are not strings
                print("Unable to provide difference of strings!")
            else:
                value = value.mtx
                if len(value) == len(self.mtx) and len(value[0])==len(self.mtx[0]):#check if both objects have the same number of rows and columns
                    ll = len(value)
                    ln = len(value[0])
                    result = [[self.mtx[j][i]-value[j][i] for i in range(ln)] for j in range(ll)]
                    self.mtx = result #if the shapes are the same, computation is performed and the result overwrites the mtx attribute
                else:
                    print("Matrices need to be the same shape!")
        elif isinstance(self.mtx[0][0],str)==True or isinstance(value,str)==True:#check if the input value is not string, if the input value is scalar
            print("Unable to provide difference of strings!")
        else:
            result = map(lambda x: list(map(lambda y: y - value,x)),self.mtx)
            self.mtx = list(result)#if the input scalar is not string, computation is provided

    def times(self,value):

        """ The function provides element wise multiplication between two objects of matrix class.
                    The value types in both objects need to be compatible for this operation."""

        if isinstance(value,matrix)==True:#check if the input is of class matrix
            if isinstance(value.mtx[0][0],str)==True and isinstance(self.mtx[0][0],str)==True:#check if the values in any of objects are strings
                print("Can not multiply strings!")
            elif (isinstance(value.mtx[0][0],str)==True and isinstance(self.mtx[0][0],float)==True) or (isinstance(value.mtx[0][0],float)==True and isinstance(self.mtx[0][0],str)==True):#check if one of object is string and one float
                print("Can not multiply strings by float!")
            else:
                value = value.mtx
                if len(value) == len(self.mtx) and len(value[0])==len(self.mtx[0]):#check if both objects have the same number of rows and columns
                    ll = len(value)
                    ln = len(value[0])
                    result = [[self.mtx[j][i]*value[j][i] for i in range(ln)] for j in range(ll)]
                    self.mtx = result#if the shapes are the same, computation is performed and the result overwrites the mtx attribute
                else:
                    print("Matrices need to be the same shape!")
        elif isinstance(value,str)==True and isinstance(self.mtx[0][0],str)==True:#check if the input value and values in mtx are not string, if the input value is scalar
            print("Can not multiply strings!")
        elif (isinstance(value,str)==True and isinstance(self.mtx[0][0],float)==True) or (isinstance(value,float)==True and isinstance(self.mtx[0][0],str)==True):#check if the input value, or values in mtx are not string or float if the input value is scalar
            print("Can not multiply strings by float!")
        else:
            result = map(lambda x: list(map(lambda y: y * value,x)),self.mtx)
            self.mtx = list(result)#if the type of input and types of values in mtx are compatible, computation is performed

    def div(self,value):

        """ The function provides element wise dividing between two objects of matrix class.
                    The value types in both objects need to be compatible for this operation."""

        if isinstance(value, matrix) == True:#check if the input is of class matrix
            if isinstance(value.mtx[0][0], str) == True or isinstance(self.mtx[0][0], str) == True:#check if the values in any of objects are strings
                print("Unable to provide dividing of strings!")
            else:
                value = value.mtx
                if len(value) == len(self.mtx) and len(value[0]) == len(self.mtx[0]):#check if both objects have the same number of rows and columns
                    ll = len(value)
                    ln = len(value[0])
                    result = [[self.mtx[j][i] / value[j][i] for i in range(ln)] for j in range(ll)]
                    self.mtx = result#if the shapes are the same, computation is performed and the result overwrites the mtx attribute
                else:
                    print("Matrices need to be the same shape!")
        elif isinstance(self.mtx[0][0], str) == True or isinstance(value, str) == True:#check if the input value and values in mtx are not string, if the input value is scalar
            print("Unable to provide dividing of strings!")
        else:
            result = map(lambda x: list(map(lambda y: y / value, x)), self.mtx)
            self.mtx = list(result)#if the type of input and types of values in mtx are compatible, computation is performed

    def pow(self,value):

        """ The function provides element wise powering between two objects of matrix class.
                    The value types in both objects need to be compatible for this operation."""

        if isinstance(value, matrix) == True:#check if the input is of class matrix
            if isinstance(value.mtx[0][0], str) == True or isinstance(self.mtx[0][0], str) == True:#check if the values in any of objects are strings
                print("Unable to provide powering of strings!")
            else:
                value = value.mtx
                if len(value) == len(self.mtx) and len(value[0]) == len(self.mtx[0]):#check if both objects have the same number of rows and columns
                    ll = len(value)
                    ln = len(value[0])
                    result = [[self.mtx[j][i] ** value[j][i] for i in range(ln)] for j in range(ll)]
                    self.mtx = result#if the shapes are the same, computation is performed and the result overwrites the mtx attribute
                else:
                    print("Matrices need to be the same shape!")
        elif isinstance(self.mtx[0][0], str) == True or isinstance(value, str) == True:#check if the input value and values in mtx are not string, if the input value is scalar
            print("Unable to provide powering of strings!")
        else:
            result = map(lambda x: list(map(lambda y: y ** value, x)), self.mtx)
            self.mtx = list(result)#if the type of input and types of values in mtx are compatible, computation is performed

    def prod(self,value):

        """ The function provides product between two objects of matrix class.
            The value types in both objects need to be compatible for this operation."""

        if isinstance(value, matrix) == True:#check if the input is of class matrix
            if isinstance(value.mtx[0][0], str) == True or isinstance(self.mtx[0][0], str) == True:#check if the values in any of objects are strings
                print("Unable to provide matrix product with strings!")
            elif len(self.mtx[0]) == len(value.mtx):#check if the number of columns of mtx is equal to number of rows of input
                value = value.mtx
                result = [[sum(self.mtx[k][j] * value[j][i] for j in range(len(value))) for k in range(len(self.mtx))] for i in range(len(self.mtx))]#make products between each row of self.mtx and single column of input and store it in list
                result = [[result[i][j] for i in range(len(result))] for j in range(len(result[0]))]#transpose the list of list such that final matrix has num. of rows of self.mtx and num. of columns of input matrix
                self.mtx = result
            else:
                print("Number of columns of the first matrix needs to be equal to number of rows of the second matrix!")
        else:
            print("The input value needs to be the class of matrix!")

    def transpose(self):
        result = [[self.mtx[i][j] for i in range(len(self.mtx))] for j in range(len(self.mtx[0]))]#switch rows and columns of self.mtx
        self.mtx = result


m_i = matrix([1,2,3,4,5,6,7,8],int,4)
print(m_i.mtx)
