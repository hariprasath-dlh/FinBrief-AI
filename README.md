# FinBrief AI

A beginner-friendly NLP project that takes financial news articles as input and generates short, concise summaries using pre-trained transformer models.

## Features
- **Easy to Use:** Run a simple Python script to summarize text.
- **Flexible Input:** Type your text directly into the console or read from a text file.
- **State-of-the-Art NLP:** Powered by Hugging Face Transformers (`facebook/bart-large-cnn`) for high-quality abstractive summarization.
- **No Training Required:** Leverages powerful pre-trained models.

## Tech Stack
- Python 3.x
- Hugging Face `transformers`
- PyTorch

## Project Structure
```text
FinBrief-AI/
│── main.py            # Main execution script
│── summarizer.py      # Core logic for loading model and summarizing text
│── requirements.txt   # Python dependencies
│── README.md          # Project documentation 
│── sample_input.txt   # Sample article for testing
│── output.txt         # File to store the generated summary
```

## How to Run the Project

1. **Open the Terminal**
   Navigate to the project directory in your terminal or Command Prompt.

2. **Install Required Libraries**
   Run the following command to install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   Execute the `main.py` script:
   ```bash
   python main.py
   ```

4. **Follow the Prompts**
   - You can choose to use the text provided in `sample_input.txt` or type/paste your own text.
   - Wait for the model to generate the summary (the first run will take some time to download the model).
   - Check `output.txt` for the saved summary.

## Sample Input/Output

**Input (`sample_input.txt`):**
> Apple Inc. on Thursday reported fiscal first-quarter net income of $33.92 billion. The Cupertino, California-based company said it had profit of $2.18 per share. The results surpassed Wall Street expectations...

**Output (`output.txt`):**
> Apple Inc. reported fiscal first-quarter net income of $33.92 billion. The Cupertino, California-based company said it had profit of $2.18 per share. The results surpassed Wall Street expectations.
