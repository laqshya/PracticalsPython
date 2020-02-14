Cars = ["Mercedes","BMW","Audi"]
Models = ["S-class","I8","R8"]
Dict = {Cars[i] : Models[i] for i in range(len(Cars))}
for i in Dict:
    print(i+":"+Dict[i])