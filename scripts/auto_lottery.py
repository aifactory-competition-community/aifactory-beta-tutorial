from random import shuffle


if __name__ == "__main__":
    number_set = list(range(1, 46))
    with open("sample_data/answer.csv", 'w') as file:
        for _ in range(6):
            shuffle(number_set)
            file.write(str(number_set.pop())+"\n")

