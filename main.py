class Solution:
    def rearrangeArray(self, nums: [int]) -> [int]:
        p_stack = []
        n_stack = []
        n_array = []

        for n in nums:
            if n > 0:
                p_stack.append(n)
            else:
                n_stack.append(n)

        for elem1, elem2 in zip(p_stack, n_stack):
            n_array.append(elem1)
            n_array.append(elem2)

        return n_array

    def rearrangeArray2(self, nums: [int]) -> [int]:
        p_stack = []
        n_stack = []
        n_array = []
        last_is_minus = True

        for n in nums:
            if last_is_minus and n > 0 and len(p_stack) == 0:
                n_array.append(n)
                last_is_minus = False
            elif last_is_minus and n > 0 and len(p_stack) > 0:
                n_array.append(p_stack[0])
                p_stack.remove(p_stack[0])
                p_stack.append(n)
                last_is_minus = False
            elif not last_is_minus and n < 0 and len(n_stack) == 0:
                n_array.append(n)
                last_is_minus = True
            elif not last_is_minus and n < 0 and len(n_stack) > 0:
                n_array.append(n_stack[0])
                n_stack.remove(n_stack[0])
                n_stack.append(n)
                last_is_minus = True
            else:
                if n < 0:
                    n_stack.append(n)
                else:
                    p_stack.append(n)

        if len(p_stack) > 0:
            n_array.append(p_stack[0])

        if len(n_stack) > 0:
            n_array.append(n_stack[0])

        return n_array


if __name__ == '__main__':
    s = Solution()
    test = [3,1,-2,-5,2,-4]
    print(s.rearrangeArray2(test))
