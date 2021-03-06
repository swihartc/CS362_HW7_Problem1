
def fizzbuzz(i):
    if i % 3 == 0:
        return "fizz"
    else: return i

def main():

    for i in range(1,101):
        val = fizzbuzz(i)
        print(val)


if __name__ == '__main__':
    main()