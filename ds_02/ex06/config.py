import os

LOG_FILE = "analytics.log"

num_of_steps = 3

report_template = """\
Report
We have made {total} observations from tossing a coin: {tails} of them were tails and {heads} of them were heads.
The probabilities are {tails_pct:.2f}% and {heads_pct:.2f}%, respectively.
Our prediction is that in the next {steps} observations we will have: {pred_tails} tails and {pred_heads} heads.
"""

# Telegram API
TELEGRAM_BOT_TOKEN = "766..."
TELEGRAM_CHAT_ID = "961..."
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
