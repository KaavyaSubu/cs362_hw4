 #Code for Question 1

def calcCubeVol(side):


    try:
        side = float(side)
        try:
            if side <= 0: raise ValueError
            else: return pow(side, 3)
        except ValueError:
            print("Not a valid input.")

    except ValueError:
        print("Not a float.")




 # Code for Question 2
def calcListAvg(l):
    try:
        if len(l) == 0: raise ZeroDivisionError

        try:
            check = True
            for x in l:
                if isinstance(x, float) or isinstance(x, int): continue
                else: check = False


            if check == False: raise ValueError

            else:
                avg = float(sum(l))/len(l)
                return avg
        except ValueError:
            print("Not all items in the list are numbers.")


    except ZeroDivisionError:
        print("List is empty.")

 # Code for Question 3

def genFullName(first, last):
    try:
        if not isinstance(first, str) or not isinstance(last, str):
            raise ValueError
        else:
            return str(first) + " " + str(last)
    except ValueError:
        print("String was not entered.")
