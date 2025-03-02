
fruits = ["apple", "banana", "orange","kiwi"]
print(fruits[1:2])  # (start index) → Starts slicing from index 1 ("banana"). (stop index, exclusive) → Stops before index 2 ("orange").
#sequence[start:stop:step]
#start → Inclusive (default is 0 if not specified).
#stop → Exclusive (stops before this index).
#step → Optional (controls how elements are picked).
print(fruits[::2])  # ['apple', 'orange'] #Step = 2, so it skips every alternate item. [0,2,4]
#print(fruits[::-1])  # ['kiwi', 'orange', 'banana', 'apple'] Step = -1, which reverses the list.
print(fruits[-1:1:-1])  # ['kiwi', 'orange'] Starts from -1 ("kiwi") Stops before 1 ("banana") Step = -1 (moves backward) 
        #[kiwi] -> [orange] -> [banana]

        