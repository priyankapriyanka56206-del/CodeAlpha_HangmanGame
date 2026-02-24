{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2fd72db8-7c4a-4c94-829c-4b6877f673c6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to Hangman Game\n",
      "\n",
      "Number of letters in the word is: 5\n",
      "The word belongs to: Animals family\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Guess the word (or type 'hint'):  hint\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hint: The first letter of the word is: t\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Guess the word (or type 'hint'):  taffy\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wrong guess!\n",
      "Remaining chances: 5\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Guess the word (or type 'hint'):  tratar\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wrong guess!\n",
      "Remaining chances: 4\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Guess the word (or type 'hint'):  geytr\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wrong guess!\n",
      "Remaining chances: 3\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Guess the word (or type 'hint'):  jtjt\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wrong guess!\n",
      "Remaining chances: 2\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Guess the word (or type 'hint'):  nht\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wrong guess!\n",
      "Remaining chances: 1\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Guess the word (or type 'hint'):  ntyn\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wrong guess!\n",
      "Remaining chances: 0\n",
      "\n",
      "Game Over!\n",
      "The correct word was: tiger\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Do you want to play again? (yes/no):  yes\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Number of letters in the word is: 6\n",
      "The word belongs to: Programming Languages family\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Guess the word (or type 'hint'):  python\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "🎉 Correct! You guessed the word: python\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "print(\"Welcome to Hangman Game\")\n",
    "\n",
    "words = {\n",
    "    \"apple\": \"Fruits\",\n",
    "    \"tiger\": \"Animals\",\n",
    "    \"rose\": \"Flowers\",\n",
    "    \"python\": \"Programming Languages\",\n",
    "    \"robot\": \"Machines\"\n",
    "}\n",
    "\n",
    "while True:\n",
    "    word = random.choice(list(words.keys()))\n",
    "    family = words[word]\n",
    "    chances = 6\n",
    "    hint_used = False\n",
    "\n",
    "    print(\"\\nNumber of letters in the word is:\", len(word))\n",
    "    print(\"The word belongs to:\", family, \"family\")\n",
    "\n",
    "    while chances > 0:\n",
    "        guess = input(\"\\nGuess the word (or type 'hint'): \").lower()\n",
    "\n",
    "        if guess == \"hint\":\n",
    "            if not hint_used:\n",
    "                print(\"Hint: The first letter of the word is:\", word[0])\n",
    "                hint_used = True\n",
    "            else:\n",
    "                print(\"You already used the hint.\")\n",
    "            continue\n",
    "\n",
    "        if guess == word:\n",
    "            print(\"🎉 Correct! You guessed the word:\", word)\n",
    "            break\n",
    "        else:\n",
    "            chances -= 1\n",
    "            print(\"Wrong guess!\")\n",
    "            print(\"Remaining chances:\", chances)\n",
    "\n",
    "    if chances == 0:\n",
    "        print(\"\\nGame Over!\")\n",
    "        print(\"The correct word was:\", word)\n",
    "\n",
    "    play_again = input(\"\\nDo you want to play again? (yes/no): \").lower()\n",
    "\n",
    "    if play_again != \"yes\":\n",
    "        print(\"Thanks for playing!\")\n",
    "        break\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "188ea431-a944-4e51-b76c-9abc82072608",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
