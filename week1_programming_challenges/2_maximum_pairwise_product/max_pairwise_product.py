# python3

#
#def max_pairwise_product(numbers):
#    n = len(numbers)
#    max_product = 0
#    for first in range(n):
#        for second in range(first + 1, n):
#            max_product = max(max_product,numbers[first] * numbers[second])
#    return max_product

def max_pairwise_product_fast(numbers):
    n = len(numbers)
    max_product = 0
    index_1 = 0
    max_1 = 0
	
    for i in range(n):
        if numbers[i] > max_1:
            max_1 = numbers[i]
            index_1 = i
    max_2 = 0
    index_2 = 0
    for i in range(n):
        if (i != index_1) and numbers[i]>max_2:
            max_2 = numbers[i]
            index_2 = i

    return numbers[index_1]*numbers[index_2]		
	
        
if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))
