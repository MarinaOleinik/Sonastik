def loe_failist(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas
def salvesta_failisse(f,text):    
    fail=open(f,'a',encoding="utf-8-sig")
    fail.write(text+"\n")
    fail.close()
    mas=[]
    mas=loe_failist(f)
    return mas
def tolkimine():
    pass
rus_list=loe_failist("rus.txt")
est_list=loe_failist("est.txt")
print(rus_list)
print(est_list)
while True:
    v=input("Перевод-1,Новое слово-2,Исправить ошибку-3,Проверка знаний-4: ")
    if v=="1":
        tolkimine()
    elif v=="2":
        rus_sona=input("Введи слово на русском:")
        est_sona=input("Sisesta sõna eesti keeles:")
        rus_list=salvesta_failisse("rus.txt",rus_sona)
        est_list=salvesta_failisse("est.txt",est_sona)
        print(rus_list)
        print(est_list)

