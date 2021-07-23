def get_baseline_prior(close_contact):
    """Baseline for having covid

    a) https://www.ons.gov.uk/peoplepopulationandcommunity/
    healthandsocialcare/conditionsanddiseases/bulletins/
    coronavirusandselfisolationafterbeingincontactwithapositivecaseinengland/
    28juneto3july2021
    "Percentage who developed COVID-19: 34%

    TODO:
      - Activae case data for granular regions
      - Add factors like close contact
      - https://data.mendeley.com/datasets/nyd3vj48kf/1/files/
        ea325877-a6d9-40d3-a1ba-a86f94a045bf
        TODO - do the symptoms analysis
    """

    if close_contact:
        return 0.34
    else:
        return 0.01


def get_p_false_negative():
    """False negative rate

    a) https://fullfact.org/health/lateral-flow-test/
    "These tests, made by Innova... do return considerably more false
    negatives. Just 76.8% of people who did have the virus received a
    positive result"

    TODO:
        - Add factors like:
            - "who took the test"
            - "How many days since contact"
    """
    return 1. - 0.768


def get_p_true_negative(symptoms):
    """True negative rate

    P(negative test | not covid)

    a) https://www.bmj.com/content/372/bmj.n823
    "In uninfected people the tests correctly ruled out infection in 99.5%
    of people with covid-19-like symptoms and in 98.9% of those without."

    TODO:
        - Add factors like:
            - "who took the test"
            - "How many days since contact"
    """

    if symptoms:
        return 0.995
    else:
        return 0.989


def run_main(symptoms, close_contact):
    """Returns P(covid|negative test)

      = P(neg T | covid) * P(covid baseline) / p(neg T),

      where
        p(neg T) = 
            p(negT|covid) * P(covid)
            + P(negT|!covid) * P(!covid)
        = 
            p_false_positive * P(covid)
            + p_true_negative * P(!covid)
    """

    p_covid_baseline = get_baseline_prior(close_contact)

    p_false_negative = get_p_false_negative()
    p_true_negative = get_p_true_negative(symptoms)

    p_negative_test = (
        p_false_negative * p_covid_baseline
        + p_true_negative * (1. - p_covid_baseline)
    )
    p_covid_given_negative = (
        p_false_negative * p_covid_baseline) / p_negative_test

    return p_covid_given_negative


if __name__ == "__main__":
    prob_covid = run_main(symptoms=True, close_contact=True)
    print("PROBABILITY", prob_covid)
