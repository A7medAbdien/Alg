# divide and concurs

## linear search

go through all until u find the key else not_found, trivial use of divide and concurs

input: array, key, low, high
output: index or not_found

low and high: identicat/define the range where to search for

## Binary search

sort the array first, the first element is no more than the next one, not less than to allow repeated element, it is called monotonic non-decreasing array

input: array, key, low, high
output: index, or index where it could be added

edge cases: if all elements are grater than the key, return low-1

to solve the translation problem, where we have two arrays each element has the translation of its value in the corresponding index:

we created an augmented array, an array have the indexes of sorted array
