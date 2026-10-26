using System;

int[] nums = {1,2,3,5,6};
int target = 4;

int result = nums.Length;   // domyślnie: na koniec tablicy

for (int i = 0; i < nums.Length; i++)
{
    if (nums[i] >= target)  // pierwszy element >= target
    {
        result = i;
        break;
    }
}

Console.WriteLine(result);
