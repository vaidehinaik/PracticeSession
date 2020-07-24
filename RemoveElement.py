def removeElement(nums, val):
    element_idx = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[element_idx], nums[i] = nums[i], nums[element_idx]
            element_idx += 1
    return element_idx

print(removeElement([3,2,2,3],3))
