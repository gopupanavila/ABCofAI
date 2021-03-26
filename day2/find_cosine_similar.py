from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text = ['SECURITY LOCK CAMERA COMPUTER COFFEE MACHINE', 'SECURITY LOCK CAMERA COMPUTER',
        'CAMERA COMPUTER', 'WAITING LOUNGE CAMERA COMPUTER']

cv = CountVectorizer()
count_matrix = cv.fit_transform(text)
print(count_matrix)
print(cv.get_feature_names())
print(count_matrix.toarray())

similarity_scores = cosine_similarity(count_matrix)
print(similarity_scores)
similar_txts = list(enumerate(similarity_scores[1]))
print(sorted(similar_txts, key=lambda x: x[1], reverse=True))

