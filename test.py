def find_pair(nums,target):
    pair = []
    found = False
    length = len(nums)
    for i in range(0,length-1):
        for j in range(i+1,length):
            if nums[i]+nums[j] == target:
                pair.append((nums[i],nums[j]))
                found=True
                print(f'Pair found {nums[i],nums[j]}')
    if not found:
        print("Pair not found")
    return pair

test_cases = [[8, 7, 2, 5, 3, 1],[5, 2, 6, 8, 1, 9]]
targets = [10,12]

for nums,target in zip(test_cases,targets):
    print(f'Testing for list of numbers:{nums}, target:{target}')
    result = find_pair(nums,target)
    print(result)
