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
def uued_sonad():
    rus_sona=input("Введи слово на русском:")
    est_sona=input("Sisesta sõna eesti keeles:")
    rus_list=salvesta_failisse("rus.txt",rus_sona)
    est_list=salvesta_failisse("est.txt",est_sona)
    return rus_list, est_list
def tolkimine(rus_list,est_list):
    slovo=input("Введите слово для перевода: ")
    if slovo in rus_list:
        ind=rus_list.index(slovo)
        print(f"{slovo} - {est_list[ind]}")
    elif slovo in est_list:
        ind=est_list.index(slovo)
        print(f"{slovo} - {rus_list[ind]}")
    else:
        print(f"{slovo.upper()} отсутствует в словаре")
        v=input("Желаете добавить слово в словарь?")
        if v.lower()=="да": uued_sonad()
rus_list=loe_failist("rus.txt")
est_list=loe_failist("est.txt")
print(rus_list)
print(est_list)
while True:
    v=input("Перевод-1,Новое слово-2,Исправить ошибку-3,Проверка знаний-4: ")
    if v=="1":
        tolkimine(rus_list,est_list)
    elif v=="2":
        rus_list, est_list=uued_sonad()
    elif v=="3":


