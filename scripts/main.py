from aifactory_easter_eggs import *
from aifactory_alpha.API import AFContest


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    how_are_you()
    c = AFContest(user_email='user0@aifactory.page', task_id='3000', debug=True)
    c.summary()
    c.submit('./sample_data/sample_answer.csv')