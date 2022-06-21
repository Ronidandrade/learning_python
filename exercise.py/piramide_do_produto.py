def piramide_do_produto():
    times = int(input("Número de andares da pirâmide: "));
    andares = "1";
    contador = 0;
    while contador < times:
        result = eval(andares)**2;
        print(f"{andares} x {andares} = {result}".center(180));
        andares += "1";
        contador += 1;
        pass
    pass
if __name__ == "__main__":
    piramide_do_produto();
    pass
