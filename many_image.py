import matplotlib.pyplot as plt

### Example 1 ###

plt.figure(figsize = (5,5))

for idx in range(25):
  
    plt.subplot(5,5, index + 1)
    plt.imshow(data[idx], cmap = 'gray')
    plt.axis('off')

plt.show()

### Example 2 ###

def make_subplot_layout(signal,res,cluster,row=5,col=5):
    _index = np.where(res == cluster)
    cluster_signal = signal[_index[0][:row*col]]
    plt.figure(figsize=(12,8))
    for i in range(len(cluster_signal)) : 
        plt.subplot(row,col,i+1) 
        plt.plot(cluster_signal[i])
    plt.show()
