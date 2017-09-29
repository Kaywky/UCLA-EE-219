To solve problem 1
Put u.data, project3_1.m and mywnmfrule.m files in a same folder, then run the program project3_1.m, you can get residual for k=10, 50, and 100. 
Calculate the total LSE using equation: total LSE = (residual)^2.

To solve problem 2
Put u.date, project3_2.m and mywnmfrule.m files in a same folder, then run the program project3_2.m, you can get a 10*3 matrix called avg_error which corresponding to average absolute error. The first column of avg_error matrix refers to case k=10, and the second refers to k=50, the third, k=100. The 10-row means 10-fold. 
Meanwhile, you can change the iteration times in mywnmfrule.m (already changed to 100), if you want to see different results like over-fitting cases.

To solve problem 3
Make sure project3_3.m and wnmfrule.m are in the same directory and run project3_3.m.

To solve problem 4
To calculate the total squared error, run project3_4_1.m and wnmfrule1.m.
also change line 71 in wnmfrule1.m for different lambda.
To draw  the ROC curve, run project3_4_2.m and wnmfrule1.m.
also change line 71 in wnmfrule1.m and line 21 in project3_4_2.m for different lambda and k.

To solve problem 5
To calculate the precision, run project3_5_1.m, matrixNorm.m and wnmfrule1.m.
To calculate the hit rate and false-alarm rate, run project3_5_2.m, matrixNorm.m and wnmfrule1.m.



