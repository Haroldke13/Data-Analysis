# Python Program to find sum of array

# Function to find sum of array

def sum_of_array(arr):
    sum = 0; #initialize an empty variable sum
    for num in arr: # have an iterator num check through the array list
        sum += num;#add the total of all the numbers in the list
    return sum;

# Example array
arr = [1, 2, 3, 4, 6,5];

# Display the sum of the array
print("The sum of the array is", sum_of_array(arr));
