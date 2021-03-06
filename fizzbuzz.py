
def fizzbuzz(i):
    if i % 3 == 0:
        return "fizz"
    elif i % 5 == 0:
        return "buzz"
    else: return i

def main():

    for i in range(1,101):
        val = fizzbuzz(i)
        print(val)


if __name__ == '__main__':
    main()