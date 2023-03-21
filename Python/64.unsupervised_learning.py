
from numpy import array

# 有三種菊花，但我們只知道這些花的feature
samples = 18*4 array
from sklearn.cluster import KMeans
model = KMeans(n_clusters = 3)
model.fit(samples)
labels = model.predict(samples) 

# Import pyplot
import matplotlib.pyplot as plt
# Assign the columns of new_points: xs and ys
xs = new_points[:, 0]
ys = new_points[:, 1]
# Make a scatter plot of xs and ys, using labels to define the colors
plt.scatter(xs, ys, c = labels, alpha = 0.5)
# Assign the cluster centers: centroids
centroids = model.cluster_centers_
# Assign the columns of centroids: centroids_x, centroids_y
centroids_x = centroids[:,0]
centroids_y = centroids[:,1]
# Make a scatter plot of centroids_x and centroids_y
plt.scatter(centroids_x, centroids_y, marker = 'D', s= 50)
plt.show()

#檢驗cluster效果
#如果我們已經有3種菊花種類的column，就直接弄成DataFrame就好
import pandas as pd
df = pd.DataFrame({'label':labels, 'species':species})
print(df)

#crosstab #把上面兩個column弄成表的型態
ct = pd.crosstab(df['labels'], df['species'])
print(ct)

#inertia可以得知clusters的分布情況，距離mean/centroid有多遠
from sklearn.cluster import KMeans

model= KMeans(n_cluster=3)
model.fit(samples)
print(model.inertia_)

# Create a KMeans model with 3 clusters: model
model = KMeans(n_clusters = 3)
# Use fit_predict to fit model and obtain cluster labels: labels
labels = model.fit_predict(samples)
# Create a DataFrame with labels and varieties as columns: df
df = pd.DataFrame({'labels': labels, 'varieties': varieties})
# Create crosstab: ct
ct = pd.crosstab(df['labels'], df['varieties']) 
# Display ct
print(ct)

#Standardized
from sklearn.preprocessing import StandardScaler #還有MaxAbsScaler & Normalizer
scaler = StandardScaler()
kmeans = KMeans(n_clusters = 3)

from sklearn.pipeline import make_pipeline
pipeline = make_pipeline(scaler,kmeans)

scaler.fit(samples)
#有用pipeline就
pipeline.fit(samples)
labels = pipeline.predict(samples)

StandardScaler(copy = True, with_mean = True, with_std = True)
samples_scaled = scaler.transform(samples)

#層級圖/樹狀圖 dendrogram，就是羽球淘汰賽的那種圖0
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
mergings = linkage(samples, method = 'complete') #complete是指 以每個clusters 的maximum 來計算距離
labels = fcluster(mergings, 15, criterion = 'distance') #fcluster可以放大樹狀圖只看指定數值的地方
pairs = pd.DataFrame({'labels': labels, 'countries': country_names})
print(pairs.sort_values('labels'))
dendrogram(mergings, labels = country_names, leaf_rotation = 90, leaf_font_size = 6)#圖的y軸是 distance between merging clusters
plt.show()

#t-SNE 一種visualization 可以展現2D/3D的圖
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
model = TSNE(learning_rate = 100) #learning_rate要自己試，值不對的話，點會聚在一團, 一般在50-200之間
transformed = model.fit_transform(samples)
xs = transformed[:,0] #不同feature, 不是target
ys = transformed[:,1] #不同feature, 不是target
plt.scatter(xs, ys, c=species) #出來的圖xy並不具有意義，只是看他是不是能分成預期的cluster而已
plt.show()

# Import TSNE
from sklearn.manifold import TSNE
# Create a TSNE instance: model
model = TSNE(learning_rate = 50)
# Apply fit_transform to normalized_movements: tsne_features
tsne_features = model.fit_transform(normalized_movements)
# Select the 0th feature: xs
xs = tsne_features[:,0]
# Select the 1th feature: ys
ys = tsne_features[:,1]
# Scatter plot
plt.scatter(xs, ys, alpha = 0.5)
# Annotate the points
for x, y, company in zip(xs, ys, companies): #companies是一個list裡面有對應的country name
    plt.annotate(company, (x, y), fontsize=5, alpha=0.75)
plt.show()


#dimension reduction 減少不必要資訊，例如主成分分析 principle component analysis PCA !! 因素分析的其中一種???
from sklearn.decomposition import PCA
model = PCA()
model.fit(samples)
transform = model.transform(samples)
print(model.components_) #回傳因素分析矩陣，每個主成分都有一row

#plot
pca = PCA()
pca.fit(samples)
features = range(pca.n_components) #pca.n_components會顯示出現在剩下幾個component，如果指定他pca.n_components = 2，就是只留最高的兩個
plt.bar(features, pca.explained_variance_)
plt.xticks(features)
plt.ylabel('variance')
plt.xlabel('PCA feature')
plt.show()

#tf-idf- 是用來檢驗一個字詞對一個檔案的重要程度的技術
# Import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
# Create a TfidfVectorizer: tfidf
tfidf = TfidfVectorizer() 
# Apply fit_transform to document: csr_mat
csr_mat = tfidf.fit_transform(documents)
# Print result of toarray() method
print(csr_mat.toarray())
# Get the words: words
words = tfidf.get_feature_names()
# Print words
print(words)

#Sparse arrays
# Perform the necessary imports
from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans
from sklearn.pipeline import make_pipeline

# Create a TruncatedSVD instance: svd
svd = TruncatedSVD(n_components = 50)
# Create a KMeans instance: kmeans
kmeans = KMeans(n_clusters = 6)
# Create a pipeline: pipeline
pipeline = make_pipeline(svd, kmeans)

#另一種可以處理tf-idf的方式是NMF，其他功用跟PCA差不多
from sklearn.decomposition import NMF
model = NMF(n_components = 2)
print(model.components_) #出來結果是2row 表示有兩個components，有4column對應4個單字

#圖也可以用NMF的方式來拆解縮減
import numpy as np
from sklearn.tree import plot_tree
sample = np.array([0, 1, 0.5, 1, 0, 1])
print(sample)
bitmap = sample.reshape((2,3))
print(bitmap)

import matplotlib.pyplot as plt
plt.imshow(bitmap, cmap = 'gray', interpolation = 'nearest') #cmap是colormap的意思，有很多顏色可以選，不一定就是gray，interpolation可以說是色格邊界的模糊度，有很多可以調
plt.colorbar() #會有色條出來給你參考
plt.show()


#檢驗兩個DOCUMENT的相似性
from sklearn.preprocessing import normalize
norm_features = normalize(nmf_features)
#if has index 23
current_article = norm_features[23,:]
similarities = norm_features.dot(current_article) #出來會是其他row/document跟row23的相似性，1為最相似，0為不相似

#相似性pandas
import pandas as pd 
norm_features = normalize(nmf_features)
df = pd.DataFrame(norm_features, index = titles)
current_article = df.loc['Dog bite man']
similarities = df.dot(current_article) #經過normalize 之後的資料再dot，會變為cosine similarity
print(similarities.nlargest())


# Perform the necessary imports
import pandas as pd
from sklearn.preprocessing import normalize
# Normalize the NMF features: norm_features
norm_features = normalize(nmf_features)
# Create a DataFrame: df
df = pd.DataFrame(norm_features, index = titles)
# Select the row corresponding to 'Cristiano Ronaldo': article
article = df.loc['Cristiano Ronaldo']
# Compute the dot products: similarities
similarities = df.dot(article)
# Display those with the largest cosine similarity
print(similarities.nlargest())

# Perform the necessary imports
from sklearn.decomposition import NMF
from sklearn.preprocessing import Normalizer, MaxAbsScaler
from sklearn.pipeline import make_pipeline
# Create a MaxAbsScaler: scaler
scaler = MaxAbsScaler()
# Create an NMF model: nmf
nmf = NMF(n_components = 20)
# Create a Normalizer: normalizer
normalizer = Normalizer()
# Create a pipeline: pipeline
pipeline = make_pipeline(scaler, nmf, normalizer)
# Apply fit_transform to artists: norm_features
norm_features = pipeline.fit_transform(artists)

# Import pandas
import pandas as pd
# Create a DataFrame: df
df = pd.DataFrame(norm_features, index = artist_names)
# Select row of 'Bruce Springsteen': artist
artist = df.loc['Bruce Springsteen']
# Compute cosine similarities: similarities
similarities = df.dot(artist)
# Display those with highest cosine similarity
print(similarities.nlargest())