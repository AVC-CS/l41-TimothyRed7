def main():

    N = int(input('Enter the number N: '))
    result = []

    """
    ########################################
    Code Your Program here
    ########################################
    """
    v=0
    for v in range(N+1):
        t=2**v
        result.append(t)
        print(result)
    print(result)

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
