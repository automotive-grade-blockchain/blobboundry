# blobboundry
Solution to the blobboundry problem written in python

# Problem

A Blob is a shape in two-dimensional integer coordinate space
where all cells have at least one adjoining cell to the right,
left, top, or bottom that is also occupied. Given a 10x10 array
of boolean values that represents a Blob uniformly selected at
random from the set of all possible Blobs that could occupy that
array, write a program that will determine the Blob boundaries.
Optimize first for finding the correct result, second for performing
a minimum number of cell Boolean value reads, and third for the
elegance and clarity of the solution.

# Input

0000000000
0011100000
0011111000
0010001000
0011111000
0000101000
0000101000
0000111000
0000000000
0000000000

# Desired Output

Sample Output:
Cell Reads: 44
Top: 1
Left: 2
Bottom: 7
Right: 6

# Solution

The solution is to read from the beginning of the given input until
a '1' is reached.  Once you see a '1', check around that '1' to see if
there is another '1' nearby.  If there is an adjacent '1' then look and
see if that '1' has any adjacent one, but don't look backwards.  Keep
searching for adjacent '1' until there isn't a connect '1' and you're
done!
