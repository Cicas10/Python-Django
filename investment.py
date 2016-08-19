def invest(amount, rate, time):
    print("Principal amount: ${}".format(amount))
    print("Annual rate of return: ${}".format(rate))
    for i in range(1, time + 1):
        n = amount + amount*rate
        print("year {}: ${}".format(i, n))
        amount = n


invest(100, 0.05, 8)
invest(2000, .025, 5)


