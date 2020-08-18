


# (Problem 98) Validate Binary Search Tree 
#  Recursion  

class Solution1(object):
    def isValidBST(self, root): 
        return self.traverse(root, -float('inf'), float('inf')) 
        

    def traverse(self, node, mini, maxi): 
        # recursive Breadth First Search on tree 
        if node == None: 
            return True 
        
        if node.val <= mini or node.val >= maxi: 
            return False 
        
        right = self.traverse(node.right, node.val, maxi) 
        left = self.traverse(node.left, mini, node.val) 
        if right == False or left == False: 
            return False 
        return True 


# (Problem 104) Maximum Depth of Binary Tree 
# Recursion 

class Solution2(object):
    def maxDepth(self, root):
        return self.traverse(root)
        
        
    def traverse(self, node): 
        if node == None: 
            return 0 
        left = self.traverse(node.left) 
        right = self.traverse(node.right)
        return max(left + 1, right + 1) 
        


# (Problem 198) House Robber 
#  Dynamic Programming 

class Solution3(object):
    def rob(self, nums):
        nums.insert(0, 0) 
        opt = [0] 
        if len(nums) > 1: 
            opt.append( nums[1]) 
        if len(nums) > 2: 
            opt.append(max (nums[2], nums[1]) )
        if len(nums) <= 3:  
            return opt[len(nums) -1]  
        for i in range (3, len(nums) ):
            if opt[i-1] > opt[i-2] + nums[i]:
                opt.append(opt[i-1]) 
            else:
                opt.append(opt[i-2] + nums[i] ) 
        return opt[len(opt)-1] 


# (Problem 38) Count and Say 
# Dynamic Programming 

class Solution4(object):
    def countAndSay(self, n):
        
        ind = 1 
        prev = '1'  
        while ind < n: 
            prev = self.parse(prev) 
            ind += 1
        return prev
        
    
    def parse(self, string):
            arr = [] 

            while string != '':
                front = 0 
                chunk = ''
                while string[front] == string[0]:
                    chunk = chunk + string[0] 
                    if front + 1 < (len(string)): 
                        front += 1 
                    else: 
                        front +=1 
                        break 
                arr.append(chunk) 
                if front < (len(string)): 
                    string = string[(front):]
                else: 
                    break

            arr = list(map(lambda chunk: [len(chunk), chunk[0]] , arr))
            final = ''
            for arrsmall in arr: 
                final = final + str(arrsmall[0]) + arrsmall[1] 
            return final 


# (Problem 1) Two Sum 
# Just a fast solution I'm proud of 

class Solution5(object):
    def twoSum(self, nums, target):
        length = len(nums) 
        dict = {}
        for i in range(0, length):
            if nums[i] in dict: 
                return [dict[nums[i]], i]
            else: 
                dict[target-nums[i]] = i 
        


