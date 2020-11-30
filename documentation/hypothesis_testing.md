# Hypothesis Testing

## Tests Used
- t test on 95% confidence
    - since the data is extremely heavy tailed, we want to remove outliers
- Man Whitney U
    - see if they come from the same distribution

## Data Used
This was conducted on all questions referencing the deprecated libraries in question
and any question explictly referencing deprecation.

## Results
### T Tests
- question_score : 8.782993333732408e-75 %
- view_count : 2.506162246963571e-78 %
- answer_count : 1.5463385346920642e-35 %
- question_comment_count : 0.02599645769234966 %
- answer_score : 1.149396418999879e-22 %
- answer_comment_count : 1.2810513655408481e-11 %

### Wilcoxon Test
- question_score : 100.0 %
- view_count : 100.0 %
- answer_count : 100.0 %
- question_comment_count : 99.69240413631401 %
- answer_score : 99.99999999999994 %
- answer_comment_count : 6.589012576644252e-06 %

## Conclusion

This analysis has incredibly conflicting results. Since the t test relies on the
data to be normally distributed, we can assume that it's results are weaker on this
clearly nonlinear data and put more weight on the Wilcoxon.

Therefore, we don't have evidence to suggest a large difference between the two populations,
outside of answer_comment count. This implies that questions referencing deprecation
have fewer comment on the answers than those that do not. The fewer comments imply less
discussion. This is likely because questions explicitly mentioning deprecation are very cut and dry

