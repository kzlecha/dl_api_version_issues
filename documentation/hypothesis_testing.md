# Hypothesis Testing

## Tests Used
- t test on 95% confidence
    - since the data is extremely heavy tailed, we want to remove outliers
- log t test
    - since the data is extremely heavy tailed
- Man Whitney U
    - see if they come from the same distribution


## Deprecated vs Explicit Mention
### Data Used
This was conducted on all questions referencing the deprecated libraries in question
and any question explictly referencing deprecation.
### T Tests
- question_score : 0.0031867601664352283 %
- view_count : 1.2527707859058279e-199 %
- answer_count : 2.074104706447512e-14 %
- question_comment_count : 36.57435022031312 %
- answer_score : 4.043065516721295e-11 %
- answer_comment_count : 7.526497339802853e-13 %
- quality : 0.0 %
#### Results
We can see that all of our measurements of quality, except for question_comment_count are different for the given data.

### Log T Test
Note that this operates under the assumption that the populations are lognormally
distributed.
- question_score : 59.36884186177698 %
- view_count : 5.31170596611702e-161 %
- answer_count : 2.5506595414013585e-09 %
- question_comment_count : 29.99665731361716 %
- answer_score : 3.2579682960398608e-09 %
- answer_comment_count : 5.102770081261004e-08 %
- quality : 0.0 %

#### Results
This results are interesting in that while there is no statistical evidence to show that the
question_score is statistically different, the answer_score and calculated quality are statistically
different. This provides evidence towards the difference in the quality of the answers.

### Wilcoxon Test
- question_score : 2.3393517678391188e-34 %
- view_count : 5.428202366529635e-106 %
- answer_count : 6.693582287818755e-10 %
- question_comment_count : 59.28960024545569 %
- answer_score : 1.7625759445085696e-08 %
- answer_comment_count : 8.491923368396781e-05 %
- quality : 1.9646976330183393e-42 %

#### Results
This test shows that for all parameters, the populations do not have the same parameter distribution.

### Conclusion

These results provide evidence




## Deprecated vs All Questions
### Data Used
This was conducted on all questions referencing the deprecated libraries in question
and any question about the frameworks studied.

### Quantile T Test
This was done by cutting off the largest values to create a more uniform distribution
- question_score : 0.0 %
- view_count : 0.0 %
- answer_count : 4.216361867753349e-76 %
- question_comment_count : 5.003556815551393e-13 %
- answer_score : 0.0 %
- answer_comment_count : 5.493836211485133e-16 %
- quality : 0.0 %

### Ressults
All of our measures of quality are statistically different. In this way, there is statistically sufficient evidence
to suggest that the quality of a deprecated API is different from the entire population of questions about the
frameworks studied.

### Log T Test
- question_score : 3.0237534050370593e-298 %
- view_count : 0.0 %
- answer_count : 7.018161722466741e-47 %
- question_comment_count : 0.0030682316263962186 %
- answer_score : 0.0 %
- answer_comment_count : 8.972815636357822e-09 %
- quality : 0.0 %

#### Results
There is sufficent evidence to suggest that the mean of the two populations in question_score,
view_count, answer_count, answer_score, and answer_comment_count are statistically
different.

From this, we can see that the questions about an API after it has been deprecated have a 
different score from the entire population of questions about the frameworks these APIs
are from.

Most notably, our analysis of quality is statistically different.

### Wilcoxon Test
- question_score : 7.0418097919485526e-102 %
- view_count : 2.2978510240537494e-303 %
- answer_count : 3.8866925491255385e-41 %
- question_comment_count : 2.594671116751897e-06 %
- answer_score : 2.5719271044295863e-75 %
- answer_comment_count : 4.8714941541920265e-11 %
- quality : 3.7523967071384644e-64 %

#### Results
There is sufficent evidence to suggest that the two populations do not have the same distribution
for question_score, view_count, answer_count, answer_score, or answer_comment_count.

In this, we can see that the questions about an API after it has been deprecated have a
different distribution from the entire population of questions about the frameworks these APIs
are from.

However, our calulated quality does not have evidence to suggest the distribution is different

### Conclusion

In this way, while we can say that the question_comment_count is similar, the other indicators of
quality, notably `question_score` and `answer_score` are statistically different from one another.
Therefore, we can see that the questions about an API after its deprecation is of different
quality from overall questions about the framework.



## Explicit Reference vs All Questions
### Data Used
This was conducted on all questions explicitly referencing deprecation and any
question about the frameworks studied.

### Quantile T Test
This was done by cutting off the largest values to create a more uniform distribution

- question_score : 1.8292607650002853e-122 %
- view_count : 9.918365452438447e-11 %
- answer_count : 0.42227636564401383 %
- question_comment_count : 1.7869767830873808e-07 %
- answer_score : 1.0019481869237383e-294 %
- answer_comment_count : 0.027753415102489475 %
= quality : 0.0 %

#### Results
There is evidence to suggest that for the questions explicitly about deprecation
and questions about the studied frameworks, the mean question_score, view_count,
answer_count, question_comment_count, answer_count, answer_score, and answer_comment_count are
different.

Most notably, the quality we calculated is statistically different.

### Log T Test
- question_score : 5.800577988579067e-63 %
- view_count : 2.0871371071839217e-06 %
- answer_count : 17.975234991355947 %
- question_comment_count : 0.0003494908120125205 %
- answer_score : 0.0 %
- answer_comment_count : 7.199475442678683 %
- quality : 1.580502652815529e-254 %
#### Results
There is sufficent evidence to suggest that for questions explicitly about deprecation
and questions about the studied frameworks, the mean question_score, view_count,
question_comment_count, answer_score, and answer_comment_count are statistically different.

Note that quality is statisticially different.

### Wilcoxon Test
- question_score : 23.002326213568523 %
- view_count : 1.0528071956043465 %
- answer_count : 29.813447212407553 %
- question_comment_count : 0.29412996859482843 %
- answer_score : 0.33096708069004305 %
- answer_comment_count : 4.349245598305937 %
- quality : 0.0032489631072292542 %

#### Results
There is sufficent evidence to suggest that view_count, answer_score and quality have a different distribution
for the two populations

### Conclusion
This provides evidence to suggest that there is a difference in quality for the 

