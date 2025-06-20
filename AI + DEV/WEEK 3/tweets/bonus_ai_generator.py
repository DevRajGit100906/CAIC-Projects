from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
class AITweetGenerator:
    def __init__(self, model_name="gpt2"):
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.model = GPT2LMHeadModel.from_pretrained(model_name)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = self.model.to(self.device)
        self.model.eval()
    def generate_tweet(self, form):
        try:
            prompt = (
                f"Generate a {form.tweet_type.data} tweet for {form.company.data} "
                f"about {form.topic.data}: {form.message.data}"
            )
            inputs = self.tokenizer(
                prompt,
                return_tensors="pt",
                padding=True,
                truncation=True
            ).to(self.device)
            with torch.no_grad():
                outputs = self.model.generate(
                    inputs.input_ids,
                    max_new_tokens=100,
                    temperature=0.7,
                    top_p=0.9,
                    do_sample=True,
                    pad_token_id=self.tokenizer.eos_token_id,
                    eos_token_id=self.tokenizer.eos_token_id,
                    num_return_sequences=1
                )
            generated_tokens = outputs[0][inputs.input_ids.shape[1]:]
            generated_text = self.tokenizer.decode(generated_tokens, skip_special_tokens=True)
            return generated_text.strip()[:280]
        except Exception as e:
            print(f"Error generating tweet: {e}")
            return "Could not generate tweet due to an error."