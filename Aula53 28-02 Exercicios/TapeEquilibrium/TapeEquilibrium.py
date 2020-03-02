def solution(A):          
    sum_list = sum(A)
    list_that_ignores_the_last_value = A[:-1]
    sum_with_next_element = 0
    absolute_values_list = []
    for element in list_that_ignores_the_last_value:
        sum_with_next_element += element
        absolute_values_list.append(abs(sum_list - 2*sum_with_next_element))       
        min_value = min(absolute_values_list)
    return min_value

print(solution([3,1,2,4,3]))
