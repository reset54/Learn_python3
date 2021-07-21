<<<<<<< HEAD
import math


try:
    string = input()
    weight_burden_gramms = int(string)

    if (weight_burden_gramms <= 500):
        cost_delivery = math.ceil(weight_burden_gramms // 100 + (weight_burden_gramms % 100)/100) * 80
        print(int(cost_delivery))
    
    elif (1000 >= weight_burden_gramms >= 500):
        cost_delivery = math.ceil((weight_burden_gramms // 100 + weight_burden_gramms%100 / 100)) * 70
        print(int(cost_delivery))
    elif (10000 >= weight_burden_gramms >= 1000):
        cost_delivery = math.ceil((weight_burden_gramms // 100 + weight_burden_gramms%100 / 100)) * 65
        print(int(cost_delivery))   
    elif (weight_burden_gramms > 10000):
        print("не возим")
    else:
        print("Sorry, something goes innapropriatelly, please check correctly your data input")
        exit()

except ValueError:
=======
import math


try:
    string = input()
    weight_burden_gramms = int(string)

    if (weight_burden_gramms <= 500):
        cost_delivery = math.ceil(weight_burden_gramms // 100 + (weight_burden_gramms % 100)/100) * 80
        print(int(cost_delivery))
    
    elif (1000 >= weight_burden_gramms >= 500):
        cost_delivery = math.ceil((weight_burden_gramms // 100 + weight_burden_gramms%100 / 100)) * 70
        print(int(cost_delivery))
    elif (10000 >= weight_burden_gramms >= 1000):
        cost_delivery = math.ceil((weight_burden_gramms // 100 + weight_burden_gramms%100 / 100)) * 65
        print(int(cost_delivery))   
    elif (weight_burden_gramms > 10000):
        print("не возим")
    else:
        print("Sorry, something goes innapropriatelly, please check correctly your data input")
        exit()

except ValueError:
>>>>>>> refs/remotes/origin/readme
    print("некорректный вес")