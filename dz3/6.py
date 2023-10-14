def prost(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if not number % i:
            return False
    return True


number = int(input())
print(prost(number))
  
