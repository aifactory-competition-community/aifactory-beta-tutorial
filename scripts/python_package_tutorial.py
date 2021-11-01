from aifactory_easter_eggs import *
from aifactory.AFAPIClient import AFCompetition


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    how_are_you()
    c = AFCompetition(submit_key_path='../sample_data/my_key.afk')
    c.summary()
    c.submit('./sample_data/answer.csv')
