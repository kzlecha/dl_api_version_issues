'''
IMPORTANT NOTE

I have not been able to test this program because i cannot install tensorflow

'''

from pandas import read_csv, to_datetime
from sklearn.model_selection import train_test_split

import tensorflow as tf


def clean_data(df):
    '''
    @param dataframe
    '''
    df["question_date"] = to_datetime(df["question_date"])
    df["answer_date"] = to_datetime(df["answer_date"])

    # find our metric of quality
    df["quality"] = (df["question_score"] + df["answer_score"])/2

    df["time_until_answer"] = df["answer_date"] - df["question_date"]

    # df_train = df[["answer_count", "question_comment_count", "answer_comment_count", "time_until_answer"]]
    df_train = df[['question_score', "view_count", "answer_count", "answer_score", "question_comment_count", "answer_comment_count", "time_until_answer"]]
    # df_train = df[['question_score', "view_count", "answer_count", "answer_score", "question_comment_count", "answer_comment_count"]]

    # scale the data
    df_train = (df - df.min())/(df.max() - df.min())
    return df, df_train


# files = ["deprecated_libraries", "explicit_mention"]
files = ["explicit_mention"]

for filename in files:
    # read the data
    filepath = "data/filtered/"+filename+".csv" 
    df = read_csv(filepath)
    
    df, df_train = clean_data(df)

    # split into training and test
    x_train, x_test, y_train, y_test =  train_test_split(df_train.values, df["quality"].values, test_size=0.33)
    
    # create model
    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10)
    ])

    predictions = model(x_train).numpy()
    tf.nn.softmax(predictions).numpy()

    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    loss_fn(y_train[:1], predictions).numpy()

    model.compile(optimizer='adam', loss=loss_fn, metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=5)

    # save the model
    model.save('models/ann')

    print(model.evaluate(x_test,  y_test, verbose=2))
    probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
    probability_model(x_test)
    




    
