def mean_median(array_input):
    panjang_data = len(array_input)
    if array_input==[]:
        return None
        
    for i in range (panjang_data) :
        mean = sum(array_input)/panjang_data
        data_tengah=panjang_data//2
        if panjang_data % 2 == 0  :
            median=((array_input[data_tengah-1])+(array_input[data_tengah]))/2
        else :
            median=array_input[data_tengah]
    return (mean, median)

if __name__ == '__main__':
    print(mean_median([1, 2, 3, 4])) # (2.5, 2.5)
    print(mean_median([1, 2, 3, 4, 5])) # (3.0, 3)
    print(mean_median([7, 8, 9, 13, 15])) # (10.4, 9)
    print(mean_median([10, 20, 30, 40, 50])) # (30.0, 30)
    print(mean_median([15, 20, 30, 60, 120])) # (49.0, 30)