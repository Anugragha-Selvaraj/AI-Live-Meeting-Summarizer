from transformers import pipeline

summarizer = pipeline(
    "text-generation",
    model="gpt2"
)

def generate_summary(text):
    result = summarizer(
        "Summarize this meeting:\n" + text,
        max_length=150,
        do_sample=False
    )
    return result[0]["generated_text"]
