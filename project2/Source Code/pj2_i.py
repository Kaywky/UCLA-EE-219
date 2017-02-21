import numpy as np
from sklearn import linear_model, metrics
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV

news_train=np.loadtxt('train_out.csv', delimiter=',')
news_test=np.loadtxt('test_out.csv', delimiter=',')

x_train=news_train[:, :-1]
x_test=news_test[:, :-1]
y_train=news_train[:, -1]
y_test=news_test[:, -1]


for Cvalue in [0.01, 0.1, 1, 10, 100, 1000]:
    model=linear_model.LogisticRegression(penalty='l1', C=Cvalue)
    model.fit(x_train, y_train)
    news_true=y_test
    news_predict=model.predict(x_test)
    print('accuracy for penalty as l1 and C as', Cvalue)
    print(metrics.accuracy_score(news_true, news_predict))
    print("precision:")
    print(metrics.precision_score(news_true, news_predict))
    print("recall:")
    print(metrics.recall_score(news_true, news_predict))
    print("confusion matrix:")
    print(metrics.confusion_matrix(news_true, news_predict))

for Cvalue in [0.01, 0.1, 1, 10, 100, 1000]:
    model=linear_model.LogisticRegression(penalty='l2', C=Cvalue)
    model.fit(x_train, y_train)
    news_true=y_test
    news_predict=model.predict(x_test)
    print('accuracy for penalty as l1 and C as', Cvalue)
    print(metrics.accuracy_score(news_true, news_predict))
    print("precision:")
    print(metrics.precision_score(news_true, news_predict))
    print("recall:")
    print(metrics.recall_score(news_true, news_predict))
    print("confusion matrix:")
    print(metrics.confusion_matrix(news_true, news_predict))


model=linear_model.LogisticRegression()

parameters=[{'penalty':['l1'], 'tol':[1e-3, 1e-4], 'C':[1, 10, 100, 1000]},
            {'penalty':['l2'], 'tol':[1e-3, 1e-4], 'C':[1, 10, 100, 1000]}]

clf=GridSearchCV(model, parameters, scoring='accuracy')
clf.fit(x_train, y_train)

news_true=y_test;
news_predict=clf.predict(x_test)
fpr, tpr, thresholds=metrics.roc_curve(y_test, clf.predict_proba(x_test)[:, 1])

print(clf.best_estimator_)

print('accuracy for penalty as l1 and C as', Cvalue)
print(metrics.accuracy_score(news_true, news_predict))
print("precision:")
print(metrics.precision_score(news_true, news_predict))
print("recall:")
print(metrics.recall_score(news_true, news_predict))
print("confusion matrix:")
print(metrics.confusion_matrix(news_true, news_predict))

plt.figure()
plt.plot(fpr, tpr, label="ROC CURVE")
plt.plot([0,1], [0,1], '--')
plt.xlim([0.0, 1.05])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC curve-optimized logistic regression')
plt.legend(loc="lower right")
plt.show()
