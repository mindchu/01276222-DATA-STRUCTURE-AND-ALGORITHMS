import time
N = int(input("Enter n : ")) 
# set mininum value of n to 100
N= 100 if N<100 else N
print(f"N= {N:_}")
# Measure insert at the end using append()
end_insert_list = []
start_time = time.time()
for i in range(N):
    end_insert_list.append(i)
end_time = time.time()
print(f"Append to end: {end_time - start_time:.4f} seconds")

# Measure insert at the beginning using insert(0, ...)
begin_insert_list = []
start_time = time.time()
for i in reversed(range(N)):
    begin_insert_list.insert(0, i)
end_time = time.time()
print(f"Insert at beginning: {end_time - start_time:.4f} seconds")

head1 = ", ".join(map(str, end_insert_list[:5]))
tail1 = ", ".join(map(str, end_insert_list[-5:]))
print(f"list1 = [ {head1} .. {tail1} ]")

head2 = ", ".join(map(str, begin_insert_list[:5]))
tail2 = ", ".join(map(str, begin_insert_list[-5:]))
print(f"list2 = [ {head2} .. {tail2} ]")
