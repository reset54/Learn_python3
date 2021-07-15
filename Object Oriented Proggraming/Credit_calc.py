class Calc_credit():

    def __init__(self, summ_credit: float, your_period: int, loan_rate: float):
        """
        Данный код не закончен! This code is incomlete
        При инициализации для каждого Calc_credit(object) создадутся параметры:
        1. Cумма по кредиту (рублей)
        2. Необходимый период кредитования (лет)
        3. Ставка по кредиту (процентов)
        """
        self.summ_credit = summ_credit
        self.your_period = your_period # in years
        self.loan_rate = loan_rate
    
    
    def differenciated_payment(self) -> float:
        """
        Differenciated formula
        """
        print("Дифференцированная система платежей")
        mp = [] # monthly_payment
        mounths_counter = self.your_period * 12  # years * 12 = months
        rest = self.summ_credit
        mp_real = self.summ_credit / (self.your_period * 12.0)
        
        while mounths_counter != 0:
            mp = mp_real + (rest * self.loan_rate / (12 * 100))
            mp.append(round(mp, 2)) # округление до 0.00 и добавление в массив
            rest = rest - mp_real
            mounths_counter = mounths_counter - 1
        return mp, round(sum(mp), 2)


    def print_result(differenciated_obj: object): 
        for i, v in enumerate(differenciated_obj):
            if i == 0:
                for j, p in enumerate(v):
                    print("Платеж {:5d} : {:.2f} руб.".format(j + 1, p))
            else:
                print("Всего выплачено: {:.2f} руб.".format(v))


differenciated_credit_obj_1 = Calc_credit(summ_credit=100000, your_period=5, loan_rate=10).differenciated_payment() # -> list
Calc_credit.print_result(differenciated_credit_obj_1)
