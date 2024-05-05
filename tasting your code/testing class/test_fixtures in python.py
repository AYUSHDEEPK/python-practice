#a fixture helps to set up a test environment.this mean creating a resorces that used by more than one test. we can use fixture by using a decorator like @pytest.fixture
#example
import pytest
from a_class_to_test import anonymous
@pytest.fixture
def language_survey():
    """a survey that will be available to all test functions."""
    question="which language did you learn first?"
    language_survey=anonymous(question)
    return language_survey
def test_store_single_response(language_survey):
    """Test that a single response is stored properly."""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses
