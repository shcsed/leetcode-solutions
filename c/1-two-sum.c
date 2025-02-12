/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int* ret = (int*) malloc(sizeof(int) * 2);
    int i = 0;
    for (; i < numsSize; ++i) {
        for (int j = i+1; j < numsSize; ++j) {
            if (nums[i] + nums[j] == target) {
                ret[0] = i;
                ret[1] = j;
                *returnSize = 2;
                return ret;
            }
        }
    }
    *returnSize = 0;
    return malloc(0);
}

