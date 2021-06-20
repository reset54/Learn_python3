# Напиши программу, которая считает стоимость доставки для транспортной компании, имеющей такие тарифы для перевозки:
# Целочисленное деление в Python — оператор //. 
# Остаток от деления — %.  
# Для округления в меньшую сторону — math.floor, в большую — math.ceil:
# Программа принимает вес в граммах на вход. 
# При некорректном весе программа печатает: некорректный вес.
# При весе более 10кг программа печатает: не возим.

# Масса груза-Ставка за каждые полные или неполные 100г, рублей
# <= 500 г	-                               80
# Свыше 500г до 1 000г включительно	 -      70
# Свыше 1 000г до 10 000 г включительно -	65
# Более 10 000 г	-                       не возят
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
    print("некорректный вес")