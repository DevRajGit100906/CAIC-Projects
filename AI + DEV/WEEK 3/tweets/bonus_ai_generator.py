from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class AITweetGenerator:
    def __init__(self, model_name="meta-llama/Meta-Llama-3-8B"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.tokenizer.pad_token = self.tokenizer.eos_token

    def generate_ai_tweet(self, prompt, max_length=280):
        inputs = self.tokenizer(prompt, return_tensors='pt')
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_length=max_length,
                temperature=0.8,
                do_sample=True,
                pad_token_id=self.tokenizer.eos_token_id
            )
        generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        tweet = generated_text[len(prompt):].strip()
        return tweet
