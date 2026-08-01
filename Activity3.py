def printsecondlargest(a,a_size):
    largest=secondlargest=-9999999999999
    for i in range(a_size):
        if (a[i]>largest):
            secondlargest=largest
            largest=a[i]

        elif (a[i]>secondlargest and a[i]!=largest):
            secondlargest=a[i]

    print(secondlargest)

a=[1,2,3,4,34,23,78,43,-1]
a_size=len(a)
printsecondlargest(a,a_size)