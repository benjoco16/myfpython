def square(x):
    return x * x

def main(): #This def main() will not excute on other python file and will only work inside this file 
    for i in range(10):
        print("{} squared is {}".format(i, square(i)))

if __name__ == "__main__": # Codition to run the loop under main function
    main()
