import numpy as np

arr = np.array([10,20,30,40,50,20,30,10,20,40,70,50,80])
print(np.sort(arr))
print(np.unique(arr))
print(np.where(arr >20))
print(np.zeros(20))
print(np.median(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))
print(np.sum(arr))
print(np.var(arr))
print(np.std(arr))
print(np.percentile(arr,50))
print(np.add(arr,20))
print(np.subtract(arr,30))

# save an array to a file 

np.save('numbers.npy',arr)
print("Array saved successfully!")

print(arr)
arr = np.load("numbers.npy")
print(arr)

np.savetxt("data.txt",arr)
print("Text file saved!")
arr = np.loadtxt("data.txt")
print(arr)
