def study_schedule(permanence_period: list, target_time: int):
    students = 0

    try:
        for login, logoff in permanence_period:
            if login <= target_time <= logoff:
                students += 1

        return students

    except TypeError:
        return None
