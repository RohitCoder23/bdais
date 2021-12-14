from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer 
Arr1=["Let me tell u a secret, Peter Parker is Spiderman","Today is one of the best days of my life","Is today the best day of my life"] 
vectorizer1=CountVectorizer() 
vectorizer2=TfidfTransformer() 
a=vectorizer1.fit_transform(Arr1) 
b=vectorizer2.fit(a) 
c=vectorizer2.transform(a,b) 
print(a) 
print(b.idf_) 
print(c)
