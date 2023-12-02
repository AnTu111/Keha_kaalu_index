print("Tere! Olen sinu uus sõber - Python!")
nimi = input(str("Mis on sinu mimi? "))
print(f"{nimi}, oi kui ilus nimi!")
mang = input((nimi + " " +   "! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
if mang == "1":
    try:
        pikkus = int(input("Sinu pikkus "))
        mass = float(input("Sinu mass "))
        index = float(mass/(0.01 * pikkus)**2)
        print(f"Sinu kehaindex on {float(index)}")
    
    except ValueError:
        print("Pidi olema numbriline väärtus")
    if index<16:
        print("Tervisele ohtlik alakaal")
    elif index>=16 and  index<19:
        print("Alakaal")
    elif index>=19 and  index<25:
        print("Normaalkaal")
    elif index>=25 and  index<30: 
        print("Ülekaal")
    elif index>=30 and  index<35:    
        print("Rasvumine")
    elif index>=35 and  index<40:    
        print("Tugev rasvumine")
    elif index>=40:    
        print("Tervisele ohtlik rasvumine")
        
    
else:
    print("Kahju! See on väga kasulik info!")
    
print(f"Kohtumiseni, {nimi} ! Igavesti Sinu, Python!")