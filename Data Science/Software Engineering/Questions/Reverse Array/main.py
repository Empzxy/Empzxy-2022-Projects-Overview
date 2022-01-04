def reverse(nums):
  
    #Pointing to the first element
    start_index = 0
    #Pointing to the last element
    end_index = len(nums)-1

    while end_index > start_index:
        nums[start_index],nums[end_index] = nums[end_index],nums[start_index]
        start_index = start_index + 1
        end_index = end_index -1

if __name__ == '__main__':
    n = [1,2,3,4,5,7,8]
    reverse(n)
    print(n)