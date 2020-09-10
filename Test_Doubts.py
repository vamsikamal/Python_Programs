ece = {
    "ankush":["197R1A0467","AGE IS 18","CMRTC"],
    "teja":["197R1A0470","AGE IS 19","CMRTC"],
    "tarun":["197R1A0475","AGE IS 19","CMRTC"],
    "nitish":["197R1A0483","AGE IS 20","CMRTC"],
    "nani":["197R1A04B0","AGE IS 20","CMRTC"],
    "govardhan":["197R1A04A6","AGE IS 20","CMRTC"],
    "vamshi":["197R1A04A1","AGE IS 19","CMRTC"]
}
while True :
    name = input("enter your name   : ").strip().lower()
    if name in ece :
        #print(ece[name])
        for i in ece[name]:
            print(i)
        print('*'*20)
