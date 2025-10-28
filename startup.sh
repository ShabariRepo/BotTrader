#!/bin/bash

echo "🚀 Setting up Python virtual environment..."

# Create a virtual environment named 'bottrader'
python3 -m venv bottrader

# Activate the virtual environment
source bottrader/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies from requirements.txt
pip install -r requirements.txt

echo "✅ Environment ready. Run the bot with: source bottrader/bin/activate && python main.py"
