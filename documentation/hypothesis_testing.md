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
- question_score : 8.782993333732408e-75 %
- view_count : 2.506162246963571e-78 %
- answer_count : 1.5463385346920642e-35 %
- question_comment_count : 0.02599645769234966 %
- answer_score : 1.149396418999879e-22 %
- answer_comment_count : 1.2810513655408481e-11 %
- quality : 0.0 %
#### Results
We can see that all of our measurements of quality are different for the given data.


### Log T Test
Note that this operates under the assumption that the populations are lognormally
distributed.
- question_score : 2.426846541759997e-18 %
- view_count : 6.773743575459597e-278 %
- answer_count : 4.405554308374715e-20 %
- question_comment_count : 0.5650698112414305 %
- answer_score : 1.3139313538256622e-18 %
- answer_comment_count : 6.568406649657489e-07 %
- quality : 7.229204393907865e-173 %

#### Results
This results state that, assuming the populations are lognormally distributed,
the question_comment_count is not statistically different. However, under the proper
assumptions, there is evidence to suggest that the quality 

### Wilcoxon Test
- question_score : 100.0 %
- view_count : 100.0 %
- answer_count : 100.0 %
- question_comment_count : 99.69240413631401 %
- answer_score : 99.99999999999994 %
- answer_comment_count : 6.589012576644252e-06 %
- quality : 2.307096210157907e-50 %

#### Results
This test does not provided sufficent evidence to suggest that question_score, view_count,
answer_count, nor answer_score have a statistically different distribution. In this way,
it acts as evidence to suggest 

### Conclusion

This analysis has incredibly conflicting results. Since the t test relies on the
data to be normally distributed, we can assume that it's results are weaker on this
clearly nonlinear data and put more weight on the Wilcoxon.

Therefore, we don't have evidence to suggest a large difference between the two populations,
outside of answer_comment count. This implies that questions referencing deprecation
have fewer comment on the answers than those that do not. The fewer comments imply less
discussion. This is likely because questions explicitly mentioning deprecation are have
very simple answers, explaining the documentation.




## Deprecated vs All Questions
### Data Used
This was conducted on all questions referencing the deprecated libraries in question
and any question about the frameworks studied.

### Quantile T Test
This was done by cutting off the largest values to create a more uniform distribution
- question_score : 0.0 %
- view_count : 0.0 %
- answer_count : 1.6040673887578851e-83 %
- question_comment_count : 2.893310448452161e-09 %
- answer_score : 0.0 %
- answer_comment_count : 1.9648769316883162e-17 %
- quality : 5.395030744724408e-81 %

### Ressults
All of our measures of quality are statistically different. In this way, there is statistically sufficient evidence
to suggest that the quality of a deprecated API is different from the entire population of questions about the
frameworks studied.

### Log T Test
- question_score : 0.0 %
- view_count : 0.0 %
- answer_count : 4.047721995103728e-64 %
- question_comment_count : 64.72300911672792 %
- answer_score : 0.0 %
- answer_comment_count : 1.8831121429992166e-06 %
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
- question_score : 1.6461135357848295e-147 %
- view_count : 0.0 %
- answer_count : 1.1549296725040123e-73 %
- question_comment_count : 95.15252247396319 %
- answer_score : 2.581592851406949e-99 %
- answer_comment_count : 99.9999949580314 %
- quality : 100.0 %

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

- question_score : 1.6069494037046333e-30 %
- view_count : 9.08781549957505e-05 %
- answer_count : 1.6539338117697442 %
- question_comment_count : 0.0014535089295237844 %
- answer_score : 1.4018198209656138e-123 %
- answer_comment_count : 0.12498548438178374 %
- quality : 1.1461300680787683 %

#### Results
There is evidence to suggest that for the questions explicitly about deprecation
and questions about the studied frameworks, the mean question_score, view_count,
answer_count, question_comment_count, answer_count, answer_score, and answer_comment_count are
different.

Most notably, the quality we calculated is statistically different.

### Log T Test
- question_score : 1.6069494037046333e-30 %
- view_count : 0.004319560563068947 %
- answer_count : 27.221540031873477 %
- question_comment_count : 0.685081517302881 %
- answer_score : 7.165116818138931e-63 %
- answer_comment_count : 0.16585419751905264 %
- quality : 1.3501387392604195e-297 %
#### Results
There is sufficent evidence to suggest that for questions explicitly about deprecation
and questions about the studied frameworks, the mean question_score, view_count,
question_comment_count, answer_score, and answer_comment_count are statistically different.

Note that quality is statisticially different.

### Wilcoxon Test
- question_score : 86.01730967533771 %
- view_count : 99.84313375517281 %
- answer_count : 10.778798303462771 %
- question_comment_count : 99.99150355023461 %
- answer_score : 0.04705475813454254 %
- answer_comment_count : 10.119167255563532 %
- quality : 3.3144694881181275e-05 %

#### Results
There is sufficent evidence to suggest that answer_score and quality have a different distribution
for the two populations

### Conclusion
This provides evidence to suggest that there is a difference in quality for the 

