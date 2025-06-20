import random

class SimpleTweetGenerator:
    def __init__(self):
        self.templates = {
            'announcement': [
                "🚀 Exciting news from {company}! {message}",
                "Big announcement: {company} is {message} 🎉",
                "Hey everyone! {company} has {message} ✨"
            ],
            'question': [
                "What do you think about {topic}? Let us know! 💬",
                "Quick question: How do you feel about {topic}? 🤔",
                "{company} wants to know: What's your take on {topic}? 🗣️"
            ],
            'general': [
                "Check out what {company} is up to! {message} 🌟",
                "{company} update: {message} 💯",
                "From the {company} team: {message} 🔥"
            ]
        }

    def generate_tweet(self, form):
        company = form.company.data
        tweet_type = form.tweet_type.data.lower()
        message = form.message.data
        topic = form.topic.data

        template_list = self.templates[tweet_type] if tweet_type in self.templates else self.templates['general']
        template = random.choice(template_list)
        tweet = template.format(
            company=company,
            message=message,
            topic=topic
        )
        if len(tweet) > 280:
            tweet = tweet[:277] + "..."
        return tweet
tweet_generator = SimpleTweetGenerator()