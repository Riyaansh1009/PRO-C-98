file1 = input("What File do you want to first choose?")
file2 = input("What File do you want to swap the file with?")



def SwapFileData():
    with open(file1,'r') as a :
        data_a = a.read()
    with open(file2,'r') as b :
        data_b = b.read()
    with open(file2,'r') as a :
        data_a.write(data_b)
    
SwapFileData()

