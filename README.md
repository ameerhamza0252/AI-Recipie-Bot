# Recipe Bot

A simple AI-powered Recipe Bot built with Streamlit and OpenAI Agents that suggests easy, tasty recipes based on the ingredients you have. Just type your available ingredients, and the bot will provide step-by-step cooking instructions with fun emojis to make cooking more enjoyable!

## Description

Recipe Bot is a friendly virtual cooking assistant designed to help you whip up delicious meals using the ingredients you already have in your kitchen. Powered by an AI language model (`gemini-2.5-flash`), it generates clear and simple step-by-step recipes, complete with emojis for a fun touch.

This app uses:
- **Streamlit** for the user interface
- **OpenAI Agents** for natural language understanding and recipe generation
- **AsyncOpenAI client** to communicate asynchronously with the AI service
- Environment variables for securely storing API keys

## Features

- Input a list of ingredients and get recipe suggestions tailored to what you have.
- Step-by-step cooking instructions in simple language.
- Use of emojis in instructions to keep the experience light and fun.
- Minimal and easy-to-use interface.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/recipe-bot.git
   cd recipe-bot
