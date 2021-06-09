def result():
    result = float(int(t1)*40*int(amStr2)/100+int(t2)*40*int(amStr1))
    resultfin = round(result)
    print("T1=", t1, ", T2=", t2, ", Смуг на головній дорозі: ", amStr1, ", Смуг на побічній дорозі: ", amStr2)
    print("Lмашини = 3м, Lпершої дороги = ", int(amStr1)*4, "м, Lдругої дороги = ", int(amStr2)*4, "м")
    print("Машин, що перехрестя пропустить за один цикл: ", resultfin)


amStr1 = input(str("Введіть к-сть смуг на головній дорозі:\n"))
amStr2 = input(str("Введіть к-сть смуг на побічній дорозі:\n"))
t1 = input(str("Введіть T зеленого світла першого світлофора:\n"))
t2 = input(str("Введіть T зеленого світла другого світлофора:\n"))
if amStr2 == "1" and amStr1 == "1":
    print("     │  ↕  │\n─────┘     └─────\n  ↔           ↔\n─────┐     ┌─────\n     │  ↕  │")
    result()
elif amStr1 == "2" and amStr2 == "1":
    print("     │  ↕  │\n─────┘     └─────\n ←            ←\n →            →\n─────┐     ┌─────\n     │  ↕  │")
    result()
elif amStr1 == "2" and amStr2 == "2":
    print("     │ ↓  ↑ │\n─────┘      └─────\n ←             ←\n →             →\n─────┐      ┌─────\n     │ ↓  ↑ │")
    result()
else:
    print("Введені данні завеликі або некорректні.")
