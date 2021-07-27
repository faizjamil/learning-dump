# two arrays, arrival and duration

# each element in arrival and duration represents a different company

# arrival = [1,3,3,5,7]
# duration = [2,2,1,2,1]
# we want to count the nummber of presentations that are possible in total,
# only one compaany can present at a time
# for each company, we check their arrival time with the comapny before it
# if they have the same arrival time as another company we can safely discard that presentations
# actually, we might be able to use a hash map to do this easier than the naive solution
# the naive solution would simply be to iterate through both arrays making note of whenever two companies have the same arrival time
# then simply take the number of comapnies and subtract the number of companies that have overlapping arrival times

# using a hash map we can simply add all the elements of the arrival array as keys
# the value would be the frequency of each key, we simply return the number of keys and we have our count of how many presentations can be held