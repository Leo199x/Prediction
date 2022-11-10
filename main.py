import numbers
import os
import string


def menu():
    print("[1] List current positive cases.")
    print("[2] Insert prediction parameters")
    print("[3] List predicted positive cases")
    print("[Q] Quit")


def cal_sum(nums):
    nums = list(map(int, nums))
    return sum(nums)

def predict(s, g, d, compl):
    g = g * (1-(compl/100))
    p_cases = ( s * g ** d)
    return int(p_cases)


def mult_pred(nums, growth, days, compliance):
    nums = [str(predict(int(i), g=growth, d=days, compl=compliance)) for i in nums]
    return nums

p = 1
while True:
    menu()
    option = input("Enter your option: ")
    if option == "1":
        print("The current positive cases are: ")

        with open("Rep.txt",'r') as f:
            data = [i.strip() for i in f.readlines()]
        nums = []
        abbr = []
        for x in data:
            if x.isalpha():
                abbr.append(x) #adds an item to the end of the list
            else:
                nums.append(x)
        day = 1
        print("DAY {} {} {} {} {} {} {} {}".format(*abbr))
        print("{} {} {} {} {} {} {} {} {}".format(day, *nums)) 

                                            
    elif option == "2":
        growth = float(input("Growth Rate? "))
        days = int(input("days to calculate in future? "))
        compliance = float(input("compliance Rate? "))

        fake_nums = [nums.copy()]
        print(f"DAY  {'  '.join(abbr)}")
        print("--------------------------------")
        for i in range(days):
            total = cal_sum(fake_nums[i])
            print(f"{i + 1}  {'  '.join(fake_nums[i])} {total}")
            fake_nums.append(mult_pred(fake_nums[i], growth, days, compliance))

        print ("Option 2 has been called")



    elif option == "3":
        print ("Option 3 has been called")
        print("p is ", p)
        with open(f"result_{p}.txt", "w") as f:
            f.write(f"DAY  {'  '.join(abbr)}  TOTAL")
            f.write("\n")
            f.write("--------------------------------")
            f.write("\n")
            for i, vals in enumerate(fake_nums):
                total = cal_sum(vals)
                f.write(f"{i + 1}  {'  '.join(vals)} {total}")
                f.write("\n")
        p += 1
    elif option.isalpha() and option in "Qq": 
        print("Quitting Time!!")
        break
    else:
        print("Provide valid option!")
        continue




