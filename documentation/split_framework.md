# Differences Across the Different Frameworks

## Data
This was conducted on questions about a Deprecated API that had been answered and questions
explicitly about deprecation that had been answered.

## Results
### Deprecated API:

#### Means
            question_score   view_count  answer_count  question_comment_count  answer_score  answer_comment_count
framework
caffe             0.918367   548.081633      1.204082                1.163265      0.408163              0.714286
keras             0.590599   357.644414      1.446866                1.421662      0.673025              1.523161
pyspark           0.450000    47.183333      1.400000                1.100000      0.700000              1.550000
pytorch           0.235294    35.352941      1.117647                1.176471      0.705882              1.882353
tensorflow        1.266370   727.433884      1.506357                1.576923      0.926891              1.486332
theano            1.396040  1061.198020      1.539604                0.905941      1.202970              0.628713

#### Number of Questions
framework
caffe           49
keras         1468
pyspark         60
pytorch         17
tensorflow    3146
theano         202

### Explicit Reference:
#### Means
            question_score    view_count  answer_count  question_comment_count  answer_score  answer_comment_count
framework
caffe             1.461538   2044.461538      1.676923                0.846154      1.046154              0.738462
keras             1.853448   1890.163793      1.586207                1.896552      1.560345              1.405172
pyspark           2.241071   6163.607143      1.714286                1.285714      1.526786              0.875000
pytorch           5.953125  16002.046875      2.687500                1.890625      3.546875              1.328125
tensorflow        2.979497   2874.256291      1.794035                1.545200      1.587139              1.064306
theano            2.474359   2025.679487      1.846154                1.192308      1.807692              0.923077

#### Number of Questions
framework
caffe           65
keras          116
pyspark        112
pytorch         64
tensorflow    1073
theano          78

## Analysis

### Deprecated APIs
Theano overall has the highest community scores for both question and answer, followed by tensorflow. This directly
reflects their veiw count, suggesting that the depreacted APIs for theano and tensorflow are more populated than the
deprecated APIs for any other studied framework. PyTorch had the lowest question_score and view_count, but caffe had the lowest
answer_score, while PyTorch had the highest answer_comment_count and an average answer_score. In this way, even if the questions asked about PyTorch are not popular, they likely help the views a lot.

However, interestingly, keras and tensorflow had the highest question_comment_count an theano has the lowest question_comment_count
and answer_comment_count. This implies that the answers are more clear and are not as discussed within the community (likely not needed clarification)

### Explicit Mention
Overall, PyTorch had the highest question and answer score. This is interesting because this was very different from the results of the 

