# rank.py

This is a no-dependency python script that allows humans to interactively
sort small-to-medium sized lists at maximum theoretical efficiency. 

For example, for an unaided human to properly sort a list of 150 items, in the worst case they will need 
up to 22,500 comparisons. **This utility will allow you to sort the same list with
no greater than 1,085 comparisons, a ~95% savings**!

## examples

1. ranking political candidates for a ranked choice election.
2. organizing a movie collection by how much you enjoyed each entry.
3. creating a dumb, uninspired tier list of something for clout with friends.

...and many more!

## usage

```bash
python rank.py states.txt > sorted-output.txt
```

```yaml
# interactive output example
Which is 'greater'? 
 (1) - 'Alaska'          or 
 (2) - 'Arizona'
Which is 'greater'? 
 (1) - 'Alabama'         or 
 (2) - 'Alaska'
# etc...
```

## approach

Generally, when humans are asked to rank a set of items, they tend to use a 
[hybrid insertion sort](https://en.wikipedia.org/wiki/Insertion_sort) approach.
The problem with this approach is that it scales very poorly.

The sorting algorithm that this utility uses is a custom depth-first [merge sort](https://en.wikipedia.org/wiki/Merge_sort)
with certain properties that are conducive to human sorting, namely that in a vast majority of comparisons, 
**only one of the items being compared will change at a time**, which greatly reduces the cognitive load for human sorting.

