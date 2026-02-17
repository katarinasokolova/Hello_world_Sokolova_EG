donor = input("Введите группу крови донора (I, II, III, IV): ").strip().upper()
patient = input("Введите группу крови рецепиента (I, II, III, IV): ").strip().upper()
if donor == patient:
    print("Переливание донорской крови возможно")
elif donor == patient == "0":
    print("Переливание донорской крови возможно")
elif patient == 0 and donor != 0:
    print("Переливание крови невозможно")
else:
    print("Переливание крови невозможно")