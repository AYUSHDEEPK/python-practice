from a_class_to_test import anonymous
def test_store_multiple_response():
    """test that three individual responses are stored properly"""
    question="what language did you learn first"
    language_survey=anonymous(question)
    responses=["english","spanish","mandrin","hindi"]
    for response in responses:
        language_survey.store_response(response)
    for reponse in responses:
        assert response in language_survey.responses