def linear_interpolation(values):
    """
    Fill missing (None) values using linear interpolation.
    """
    # Write code here

    lin_int = values.copy()
    Trigg_left = False
    left = 0
    right = 0
    vleft = 0
    vright = 0

    for j in range(len(lin_int)):

        if lin_int[j] == None:
            left = j - 1
            vleft = lin_int[j - 1]

            for i in range(j + 1, len(lin_int)):

                if lin_int[i] != None:
                    right = i
                    vright = lin_int[i]
                    break
            
            for i in range(j, right):
                if lin_int[i] == None:
                    lin_int[i] = vleft + (i - left)/(right - left) * (vright - vleft)



    return lin_int