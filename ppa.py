

def solution(n):
    numb = int(input("Digite APENAS número de 2 dígitos(entre 10 e 99): "))
    while 10 <= numb <= 99:
        for n in range(n):
            n = str(numb)
            map_object = map(int, n)
            listofint = list(map_object)
            print(f'{listofint[0] + listofint[1]}')
        return
    else:
        print(ValueError)


if __name__ == '__main__':
    solution(n=1)
    print(solution(n=1))
