c=1
while true:
    print(c)
    vocal=input("ingrese vocal:")
    while vocal not in (´a´,´e´,´i´,´o´,´u´):
        if vocal ==´.´:
            break
            vocal=input("vocal:")
            print(´su vocal o punto es:{}´´.format(vocal))
    