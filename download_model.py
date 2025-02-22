from transformers import AutoTokenizer, AutoModelForSequenceClassification
 
# hugging face model id
model_id = "distilbert-base-uncased-finetuned-sst-2-english"
 
AutoModelForSequenceClassification.from_pretrained(model_id).save_pretrained("model")
AutoTokenizer.from_pretrained(model_id).save_pretrained("model")