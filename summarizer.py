import os
import warnings

# Suppress Hugging Face warnings and progress bars for clean output
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"
warnings.filterwarnings("ignore")

import transformers
transformers.logging.set_verbosity_error()

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def summarize_text(text):
    """
    Summarizes text using a SMART system where summary length adapts to input size.
    """
    model_name = "facebook/bart-large-cnn"
    
    print("Loading pre-trained model and tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    
    print("Processing text...")
    # Tokenize the input text
    inputs = tokenizer(text, max_length=1024, return_tensors="pt", truncation=True)
    
    # -----------------------------------------------------------------
    # 🧠 SMART DYNAMIC LENGTH LOGIC
    # -----------------------------------------------------------------
    input_length = inputs["input_ids"].shape[1]  # Count total input tokens
    
    # 1. Target lengths: 30% max, 15% min
    calc_max = int(input_length * 0.30)
    calc_min = int(input_length * 0.15)
    
    # 2. Apply Boundaries: Max must be between 30 and 100
    dynamic_max = max(30, min(100, calc_max))
    
    # 3. Safety Check: Min must always be safely lower than Max
    dynamic_min = min(calc_min, dynamic_max - 5) 
    dynamic_min = max(10, dynamic_min) # make sure minimum isn't effectively 0
    
    print(f"📊 Input Tokens: {input_length} | Summary Range: {dynamic_min} to {dynamic_max} tokens")
    
    # Generate the summary using our dynamic variables
    print("Generating summary...")
    summary_ids = model.generate(
        inputs["input_ids"],
        max_length=dynamic_max,
        min_length=dynamic_min,
        length_penalty=2.5,             # 🔥 Encourages tight, concise phrasing
        num_beams=5,                    # Searches deeper for the best possible wording
        no_repeat_ngram_size=3, 
        repetition_penalty=1.2,       # Prevents repeating 3-word phrases
        early_stopping=True,
        forced_bos_token_id=0           # Keeps terminal clean
    )
    
    # Decode removing special algorithm characters
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary