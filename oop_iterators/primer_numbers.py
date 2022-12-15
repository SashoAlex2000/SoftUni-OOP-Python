

def get_primes(integer_list):

    def check_if_prime(num):
        if num == 2:
            return True

        if num == 3:
            return True

        if num <= 1:
            return False

        else:
            for n in range(2, num):
                if num % n == 0:
                    return False

            return True

    prime_list = []
    for number in integer_list:
        if check_if_prime(number):
            prime_list.append(number)

    for element in prime_list:
        yield element


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))