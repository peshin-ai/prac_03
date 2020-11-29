# TODO: Convert fahrenheit to celsius
def Convert(F_degree):
    return 5 / 9 * (F_degree - 32)

def main():
    Infile = open("temps_input.txt", "r")
    OutFile = open("temps_output.txt", "w")
    for degree in Infile:
        C_degree = Convert(float(degree))
        print(C_degree, file=OutFile)
    Infile.close()
    OutFile.close()


main()
