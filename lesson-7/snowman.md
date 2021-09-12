# Python Snowman

Snowman is a game where you guess a word letter by letter. If you lose the snoman melts!

This is a problem to solve not a tutorial! Think of it like a software product you have been hired to create. You should try your best to solve the problem on your own. There are plenty of solutions on the web. I want you to practice concepts covered in class so far and use your reasoning and logic skills to put the program together from what you know. 

To solve the problem start with pseudo code! Spending more time here will serve you by clarifying the problem and developing your logic skills. It will also help you solve problems at interviews in the future! 

This game is based on Hangman a timeless classic with a questionable title. Read about it here: 

- https://en.wikipedia.org/wiki/Hangman_(game)

## The Assignment

Follow these steps: 

- Play the game until you are clear on the rules and how the game works
- Write pseudo code describing the program you intend to write
- Review your pseudo code with someone else
- Starting writing your code using your pseudo code as a guide

If this problem seems easy try the stretch goals at the end of this page. 

## Game Rules

Snowman is a guessing game. One player, the computer in this version, thinks of a word and keeps it secret.

The computer starts the game by tell us how many letters are in the word. Imagine the word it thought of was "loaf" it would show the player: 

```
Word: ____
```

This would provide the player the clue that the word they were guessing was a four letter word.

The player tries to guess the word by guessing a letter. The computer responds by letting us know if that letter is contained in the word and where that letter appears in the word. For example if you guessed "a". The computer might repsond with: 

```
Word: __a_
```

This would let us know that "a" was in the word and was the third letter. 

If a letter guessed is not contained in the word that counts as a strike against the Snowman. 8 strikes loses the game. For example imagine the player's next guess was the letter "b". The computer might respond with: 

```
Word: __a_
Misses: b
```

The second line shows the number of strikes. Looking at the response we can see the computer is looking for a 4 letter word. The third letter is revealed as "a". So far we have 1 strike. 

The game might show the progress like this: 

```
Turn: 1
word: ____
Guess: 
Misses:
Enter a letter > a

Turn: 2
word: __a_
Guess: a
Misses:
Enter a letter > b

Turn: 3
word: __a_
Guess: a
Misses: b
Enter a letter > 
```

The game would continue from here. Repeating the process above. 

## Pseudo Code

Before you start writing code write a pseudo code description of the program you intend to write. 

**This is an important step. Do not skip this step.** Writing pseudo code is an important process that will make you a stronger programmer. Skipping this step because you "prefer to start by writing code" or similar excuses is saying that you prefer to solve problems by trial and error. This is not a good way to work! 

Writing pseudo code is not easy! There is no auto complete or error messages and warnings. It forces you to think about the problem. This is the hard work don't fool yourself by thinking this step is unimportant and doesn't deserve your best efforts!

Read more about pseudo code here: 

- https://en.wikipedia.org/wiki/Pseudocode
- https://sites.google.com/a/ismanila.org/oliverab_cp/python/pseudocode
- https://www.geeksforgeeks.org/how-to-write-a-pseudo-code/

### Writing the Pseudo code

Write down the steps that you would follow if you were playing the game with someone using paper and pencil. 

Read the steps carefully. Use a word. Use letters that you guess. Follow a real game! Play a real game and write it all down. 

Identify the places where the you need to display something and notate your pseudo code with the word: `DISPLAY`. 

Identify where in your description the program asks for input. Notate your code with: `PROMPT` followed by the message to display at the prompt. 

If the prompt will receive an input mark this with `GET` or `SET`. Give the variable that will hold the value a name.

Look for places where your program makes decisions. Identify the beginning of the decision making and the end and mark them with `IF` and `ENDIF`. If there is a branch use `ELSE` or `ELSEIF`. 

Identify where a value might be changed use `GET` or `SET` here. 

Look for anywhere your code is repeating a process. Mark where this process begins with `WHILE` or `FOR`. Identify where the repeated process ends and mark this with `ENDWHILE` or `ENDFOR`.

Review your pseudo code. Follow a game by stepping through the pseudo code you have written. 

## Code Snippets

### Lists

You need a list of words:

```python
words = ["art", "bear", "cup", "dance", "eleven", "loaf", ...]
```

### Choose a random word

Import the random module.

```python
import random
```

Use `random.choice(some_list)` to return a random element from a list. 

Get a random word like this:

```python
word = random.choice(words)
```

### Split the word into letters

Turn a string into an array of characters with: 

```python
list("some word") # ["s","o","m","e"," ","w","o","r","d"]
```

Imagine the game will need to show the which letters have been guessed and where they are in the word. 

Imagine the word is: "loaf". Your program might show: 

```____```

Four letters and none have been guessed. 

Imagine we guess: `a`. This in the word so we need to display: 

```__a_```

You might keep track of the word and the guessed letters in two arrays: 

```python
word = ['l', 'o', 'a','f']
guess = ['_','_','_','_']
```

Make a list from a string link this: 

```python
word = list("loaf")
```

To make a string of "_" by finding the length of the your word and using *

```python
underscores = "_" * len(word)
```

You could then turn `under_scores` into a list with `list(under_scores)`. Or you could do all of this in one line: 

```python
guess = list("_" * len(word))
```

### Entering a letter

Prompt for a letter with input: 

```python
letter = input("Guess a letter > ")
```

### Find a character in a list

You'll need to find the letter entered in your word list and also know it's index. 

It's also possible that a letter might appear more that once in a word. 

Use a loop to look at each character in your word list. Loop with the index since you'll need that. 

```python
for i in range(len(word)):
	print(i, word[i])
```

### Handling a guess

Handle a guess by looping over the word list and comparing each element to the input letter. If they match you'll need to update the element at that position in your guess list. 

### Game Loop

It will take more that one guess to complete the game. You'll need to set up a game loop. The game loop will repeat part of the program cycling through the same code until the game is won or lost. 

Some of the code would go into the game loop while other code would go outside! In this way some code is run once while other code is run over and over until the game is complete. 

## Stretch Goals

If you've solved the problem try these stretch goals: 

- Use functions. Every block of code should be contained in a function. 
- Start the game with a message. 
- End the game by asking if the player wants to play again.
- Check the input for a single letter.
	- If a string longer than 1 character is input show a message and ask for a single letter.
	- Check input for numbers and prompt that only letters are allowed. 
- Keep all words as lowercase and convert input to lowercase.
- Move the word list to a json file and import it into your main program. 
- Display the Snowman rather than just showing the missed letters. On each miss part of the snoman disappears.
- Keep a list of words of various lengths. Ask the player what length word they would like to guess at the beginning of the game. 

Below are two possible ascii snowmen. The stretch goal is to print the snowman and remove part of the snowman with each miss. You could also make your own snowman art or invent a new way to show progress of the game. 

```
   _==_ _
 _,(",)|_|
  \/. \-|
__( :  )|__
```

```
           ___
         _[___]_  _
          ( " )  [_]
      '--(`~:~`)--|'
        / `-:-' \ |
   __.--\   :   /--.
.'`      '-----'    '-.._
```

```
       *     *
             ___   *
       *   _|___|_      *
  *       '=/a a\='  *
      *     \~_ /        *
    *  _\__/ '-' \__/_
        /  \  o  /  \
  *       / '---' \   *
     jgs |    o    |      *
   ---.---\   o   /-----.---
           '-----'`
```