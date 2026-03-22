import os
from summarizer import summarize_text

def read_input(file_path="sample_input.txt"):
    """Reads text from the specified input file."""
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read().strip()
    return None

def write_output(summary, file_path="output.txt"):
    """Writes the generated summary to the output file."""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(summary)
    print(f"\n✅ Summary successfully saved to '{file_path}'")

def main():
    print("Welcome to FinBrief AI - Financial News Summarizer\n" + "="*50)
    
    # Keeping it simple: Just read directly from the file to avoid input errors in VS Code
    print("\nReading from 'sample_input.txt'...")
    text_to_summarize = read_input()
    
    if not text_to_summarize:
        print("Error: 'sample_input.txt' is empty or missing.")
        return

    print("\n--- Original Text ---")
    print(text_to_summarize[:200] + ("..." if len(text_to_summarize) > 200 else ""))
    print("-" * 21 + "\n")

    # Get the summary
    try:
        summary = summarize_text(text_to_summarize)
        
        print("\n=== Summary ===")
        print(summary)
        print("===============\n")
        
        # Save to output file
        write_output(summary)
        
    except Exception as e:
        print(f"An error occurred during summarization: {e}")

if __name__ == "__main__":
    main()
