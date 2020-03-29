import pandas as pd
pd.set_option('display.max_colwidth', -1)

#import csv file
jeopardy = pd.read_csv('jeopardy.csv')

#renaming columns to snake_case
jeopardy.rename(columns = {'Show Number': 'show_number', ' Air Date': 'air_date', ' Round': 'round', ' Category': 'category', ' Value': 'value', ' Question': 'question', ' Answer': 'answer'}, inplace=True)
#print(jeopardy.head(5))

#function for filtering questions containing set of words
def list_in_question(data,words):
    all_in_question = lambda x: all(word.lower() in x.lower() for word in words)
    return data.loc[data['question'].apply(all_in_question)]

#test list_in_question function
ex_list = ['King','England']
king_england = list_in_question(jeopardy,ex_list)
#print(king_england)

#new value_float column
jeopardy['value_float'] = jeopardy.value.apply(lambda x: float(x[1:].replace(',','')) if x != 'None' else 0)

#'King' filter mean
king_filter = list_in_question(jeopardy,['King'])
king_mean = king_filter.value_float.mean()

#count of unique answers to 'King' questions
def count_answer(data):
    return data.answer.value_counts()

king_unique = count_answer(king_filter)
#print(king_unique)

#How many questions from the 90s use the word "Computer" compared to questions from the 2000s?
jeopardy['year'] = jeopardy.air_date.apply(lambda x: int(x[:4]))
jeopardy['decade'] = jeopardy.year.apply(lambda x: x - (x % 10))
computer_filter = list_in_question(jeopardy,['Computer'])
computer_by_decade = computer_filter.groupby('decade').show_number.count().reset_index()
computer_90_00 = computer_by_decade[(computer_by_decade.decade == 1990) | (computer_by_decade.decade == 2000)].reset_index(drop=True)
computer_90_00 = computer_90_00.rename(columns = {'show_number': 'counts'})
computer_90_00['diff_from_90s'] = computer_90_00.counts.apply(lambda x: x - computer_90_00.counts.iloc[0])
computer_90_00['percent_rise'] = computer_90_00.diff_from_90s.apply(lambda x: (float(x) / computer_90_00.counts.iloc[0]) * 100)
#print(computer_90_00)

#Is there a connection between the round and the category? Are you more likely to find certain categories, like "Literature" in Single Jeopardy or Double Jeopardy?
def list_in_category(data,words):
    all_in_category = lambda x: all(word.lower() in x.lower() for word in words)
    return data.loc[data['category'].apply(all_in_category)]

literature_filter = list_in_category(jeopardy,['Literature'])
literature_by_round = literature_filter.groupby('round').show_number.count().reset_index()
literature_by_round = literature_by_round.rename(columns = {'show_number': 'counts'})
literature_by_round['round_type'] = literature_by_round['round'].apply(lambda x: 'Double Jeopardy' if x == 'Double Jeopardy!' else 'Single Jeopardy')
literature_double = literature_by_round.groupby('round_type').counts.sum().reset_index()
#print(literature_double)