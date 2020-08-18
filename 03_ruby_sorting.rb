

# Quicksort 
# Recursion   

def quicksort(array) 
    return array if array.length <= 1 
    pivot = array.shift 
    less, more = [], [] 
    array.each do |i| 
        i < pivot ? less.push(i) : more.push(i) 
    end 
    return quicksort(less) + [pivot] + quicksort(more)
end 

# Mergesort 
# Recursion 

def mergesort(array)
    len = array.length 
    if len <= 1 
        return array 
    else 
        a1 = mergesort(array.shift(array.length/2))
        a2 = mergesort(array)  
        final = [] 
        len.times do 
            if a1[0] && a2[0] 
                a1[0] < a2[0] ? final << a1.shift : final << a2.shift 
            end 
        end 
        return [final, a1, a2].flatten 
    end  
end 

# Insertion Sort 
# Recursion 

def othersort_whole(sorted, left)
    if left.length == 0  
        return sorted 
    else 
        val = left.pop 
        if val <= sorted[0].to_i
            ins = sorted.unshift(val) 
        elsif val >= sorted[-1].to_i 
            ins = sorted.push(val)
        else 
            left = sorted.shift(sorted.length/2)
            if val <= left[-1] 
                ins = [insert(left, val), sorted].flatten 
            else 
                ins = [left, insert(sorted, val)].flatten 
            end 
        end 
        return other_sort(ins, left) 
    end 
end 

# Radix Sort 
# Recursion 

def radix(array, base, max = 0, exp = -1) 
    if exp == -1
        max = Math.log(array.max(), base).ceil 
        exp = 0 
    elsif exp == max
        return array 
    end 
    first = Array.new(base) 
    array.each do |num| 
        digit = (num % (base**(exp+1))) / (base**(exp))
        if first[digit] 
            first [digit] << num 
        else first[digit] = [num]
        end 
    end 
    second = Array.new
    first.each do |num| 
        if num 
            second << num
        end 
    end 
    return radix(second.flatten, base, max, exp+= 1)
end 

