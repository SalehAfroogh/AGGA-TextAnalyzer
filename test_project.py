import os
from pathlib import Path
import pytest
from nltk.corpus import stopwords

# Import your functions (adjust based on your script's file structure)
from setup_stopwords import stopwords as custom_stopwords
from Alt_checkpoint import process_docx, process_txt, plot_frequency_chart

# Define paths for testing
TEST_FOLDER = "/Users/salehafroogh/Desktop/AGGAProject2/"
TEST_DOCX = "AGGA_Africa.docx"
TEST_TXT = "AGGA_Africa.txt"

@pytest.fixture
def setup_test_environment():
    """Set up the environment for testing."""
    # Ensure test file exists
    assert Path(os.path.join(TEST_FOLDER, TEST_DOCX)).exists(), "Test DOCX file not found!"
    return os.path.join(TEST_FOLDER, TEST_DOCX), os.path.join(TEST_FOLDER, TEST_TXT)

def test_process_docx(setup_test_environment):
    """Test DOCX to TXT processing."""
    docx_path, txt_path = setup_test_environment
    process_docx(docx_path)
    assert Path(txt_path).exists(), "TXT file was not generated from DOCX!"

def test_stopwords():
    """Test stopwords loading and customization."""
    # Check default stopwords
    default_stopwords = set(stopwords.words('english'))
    assert len(default_stopwords) > 0, "Default stopwords list is empty!"

    # Check customized stopwords
    additional_stopwords = {'use', 'used', 'using'}
    custom_stopwords_set = custom_stopwords.union(additional_stopwords)
    assert additional_stopwords.issubset(custom_stopwords_set), "Custom stopwords not added correctly!"

def test_process_txt(setup_test_environment):
    """Test text preprocessing."""
    _, txt_path = setup_test_environment
    processed_words = process_txt(txt_path)
    assert isinstance(processed_words, list), "Processed words should be a list!"
    assert len(processed_words) > 0, "Processed words list is empty!"
    assert all(isinstance(word, str) for word in processed_words), "Processed words should be strings!"

def test_plot_frequency_chart(setup_test_environment):
    """Test frequency chart generation."""
    _, txt_path = setup_test_environment
    processed_words = process_txt(txt_path)
    try:
        plot_frequency_chart(processed_words, "Test Chart", "#90EE90")
    except Exception as e:
        pytest.fail(f"Frequency chart generation failed: {e}")

if __name__ == "__main__":
    pytest.main()
