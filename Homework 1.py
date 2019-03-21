def calculateTheResultMoney(money, percentage, years):
    while years > 0:
        money = money * (1 + percentage / 100)
        years = years - 1
    return money


def setupInitMoney():
    money = float(input('Firstly, enter the initial amount of money'))
    return money


def setupPercentage():
    percent = float(input('Now enter the interest percentage'))
    return percent


def setupYears():
    year = int(input("Finally, enter the number of years"))
    return year


def main():
    print(
        'Welcome! My app will allow you to calculate final money if you know the initial money, amount of interest percentage, and the number of years')
    money = setupInitMoney()
    percentage = setupPercentage()
    years = setupYears()
    result = calculateTheResultMoney(money, percentage, years)
    print('After', years,'years your initial money',money,'will become your final money',result, '. Thank You!')


main()
