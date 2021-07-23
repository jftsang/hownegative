def get_baseline_prior():
    """Regional baseline for active cases
    
    TODO:
      - Add more granular regions
      - Add factors like close contact
    """
    return 0.01


def get_p_false_negative():
    """False negative rate

    TODO:
        - Add factors like:
            - "who took the test"
            - "How many days since contact"
    """
    return 0.2


def get_p_true_negative():
    """True negative rate

    TODO:
        - Add factors like:
            - "who took the test"
            - "How many days since contact"
    """
    return 0.8


def run_main():
    """Returns P(covid|negative test)

      = P(neg T | covid) * P(covid regional baseline)
        / p(neg T)

    where
        p(neg T) = 
            p(negT|covid) * P(covid)
            + P(negT|!covid) * P(!covid)
        = 
            p_false_positive * P(covid)
            + p_true_negative * P(!covid)
    """

    p_covid = get_baseline_prior()

    # TODO - different based on factors like "you took it"
    p_false_negative = get_p_false_negative()
    p_true_negative = get_p_true_negative()

    p_negative_test = (
        p_false_negative * p_covid
        + p_true_negative * (1. - p_covid)
    )
    p_covid_given_negative = p_false_negative * p_covid / p_negative_test

    return p_covid_given_negative


if __name__ == "__main__":
    prob_covid = run_main()
    print("PROBABILITY", prob_covid)
