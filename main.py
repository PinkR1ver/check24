solution_list = []
global_solution = []

def check24(nums, target, solution):
    
    if len(nums) == 1:
        if nums[0] == target:
            global_solution = solution.copy()
            global_solution.append(nums[0])
            solution_list.append(global_solution)
            return
        else:
            return
            
    
    for i in range(len(nums)):
        nums_copy = nums.copy()
        num = nums_copy.pop(i)
        
        if target % num == 0:
            solution_copy = solution.copy()
            solution_copy.append(num)
            solution_copy.append('x')
            check24(nums_copy, target / num, solution_copy)

        solution_copy = solution.copy()
        solution_copy.append(num)
        solution_copy.append('\\')
        check24(nums_copy, target * num, solution_copy)

        solution_copy = solution.copy()
        solution_copy.append(num)
        solution_copy.append('+')
        check24(nums_copy, target - num, solution_copy)

        
        solution_copy = solution.copy()
        solution_copy.append(num)
        solution_copy.append('-')
        check24(nums_copy, target + num, solution_copy)

if __name__ == '__main__':
    nums = [4,8,3,2]
    check24(nums, 24, [])
    for solution in solution_list:
        for i in range(len(solution) - 1, -1, -1):
            print(solution[i], end=' ')

        print(' ')