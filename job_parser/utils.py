def sorting(vacancies):
    vacancies = sorted(vacancies, reverse=True)
    return vacancies


def get_top(vacancies, top_count):
    for i in range(top_count):
        print(vacancies[i])
