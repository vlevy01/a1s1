## CS32 Act I, Scene I -- Programming Assignment

*NOTE: The ["PSet #1" assignment page on the CS 32 Canvas
site](https://canvas.harvard.edu/courses/97999/assignments/532779) on the Canvas
course page indicates when this assignment is due, what materials you should
submit, and how to submit them.*

## ### Big Picture

This assignment has two parts. In the first part, you'll extend and improve the
Python script we wrote in class that converts a story into a theatrical script.
Often you will find yourself starting with a piece of code that does a lot of
what you need, but it needs to be tailored to the specific problem you want
solved. That's why we will often build from an existing script in this class.

However, you may find that there are times when it seems easier to start coding
from scratch. Staring at a completely blank page in your script editor can feel
intimidating at times, and the second part of this assignment has you practice
one technique to overcome this feeling and get you started. The problem to solve
isn't particularly interesting, but the exercise provides you with additional
practice in string processing. It also lays the foundation for later task we'll
ask you to complete. (HINT: As you write this second part, think about the fact
that you'll look at this code again in several weeks.)

## ### Assignment, Part 1

### **Step 1. Covering all cases.**

In our recent class, we realized that our state
machine diagram consumed our input text *one character* at a time, but our first
implementation of our script read the input text *one line* at a time. This
caused a problem for any story line containing more than one double-quote
character. We discussed how we could fix this problem in two different ways.
While the approach taken in class worked for the structure of *The Cat in the
Hat*, it fails to do the right thing for any story with more than two
double-quote characters within a file line. Your first task is to fix this
problem to produce a script that correctly processes a story with *any number*
of double-quote characters on a file line.

**1.1 Read the current code.**

To start, take a look at the script `read32.py`. It is nearly identical to
`seuss6.py` that we developed together. The main difference between the two
scripts is the use of the `sys` library, which allows the script to get the name
of the story file it is to read from the command line. We no longer have to code
the name of the file to read directly into the script. 

`sys.argv` is simply a list of strings values corresponding to the strings you
typed after `python3` on the command line. In this way, we can run this script
over many different input files without ever having to change the script. We
will use this facility quite often in this class.

`read32.py` also does some error checking on how it is invoked. If you don't
invoke it with a file to read (or you put too many arguments on the command
line), it immediately exits with an error message (see line 11 of the script).
To this point in the class, we have only ever exited our scripts by having the
Python interpreter run off the bottom of the script. If you ever need to exit
your script without running off the bottom of it, you should call `sys.exit` at
that place in your script. You might read about other methods to end the
execution of your Python script, but we recommend that you use this approach for
now. It safely cleans up the execution state of your script so you don't
encounter any strangeness. You probably feel everything is strange enough
already!

**1.2 Run the current script and identify the problems to fix.**

Try running `python3 read32.py txts/Hat.txt`. It should successfully translate
the original story into a (one-line) dramatic script. Now try `python3 read32.py
txts/JustDavid-excerpt.txt`. The output doesn't match
`txts/JustDavid-excerpt-soln1.txt` and if you look at the first place where your
output and the solution text differ, you'll see that the missing dialogue begins
with the third double-quote character on that file line.

**1.3 Fix the problem!**

To fix this problem, we ask that you continue to read the file a line at a time,
but don't have the infinite `while` loop necessarily read a new file line on
each of its iterations. Instead, your script should read a new line from the
file only after it is certain no more double-quote characters exist in the
current line.

One possible solution to this problem has your script start keeping track of the
index of the next character to process in `the_line` variable. Solving the
problem then becomes an exercise in searching the appropriate slice of
`the_line` in each state and making sure you consistently (and correctly) update
your index variable. Try writing some pseudocode on a printout of `read32.py`
before you start writing Python code. With this approach, you should be able to
reuse quite a bit of the control-flow structure of `read32.py`. And I always
recommend drawing pictures of what `the_line` looks like in each section of your
code to check your thinking.

### **Step 2. Commas to periods.**

This step and the next clean up a few punctuation
rules that we use for dialogue contained in a story that do not make sense when
these lines of dialogue are placed in a dramatic script. In particular, this
step finds and changes lines of dialogue that end in a comma by replacing the
ending comma with an ending period.

For example, in *The Cat in the Hat*, the eighth page begins, *"I know some good
games we could play," Said the cat.* Dialogue that ends like this, but doesn't
end the sentence in a story, is written as ending in a comma. From this file
line, our script will currently produce `ACTOR: "I know some good games we could
play,"` which isn't what we want. We want `ACTOR: "I know some good games we
could play."`

We ask that you solve this problem by adding a function to your script. Let's
call it `print_dialog`. This function will have a single input parameter, which
is a string of dialogue. Your script should call this function every time it is
ready to print a piece of dialogue that it just sliced out of the story. The
function should assume that the input string includes the double-quote
characters you'd expect in a piece of dialogue. Inside this function we will
perform any cleanup like converting an ending comma into an ending period, and
we will print this line of dialogue with any decoration that we want every
printed line of dialogue to have.

In our example above, this means that we should call `print_dialog` with the
input `"I know some good games we could play,"`, and that it should print
`ACTOR: "I know some good games we could play."`. Please don't forget to prepend
a carriage-return character to the front of the printed line!

### **Step 3. Chatty characters.**

The other grammatical oddity of dialogue in a
story is how we handle long pieces of dialogue that span multiple paragraphs. In
literature, we elide the double-quote character that ends each paragraph of the
long dialogue, but we include a double-quote character at the start of each
paragraph within that long dialogue. Our script is going to put back the elided
ending double-quote characters.

You can do this by adding one `elif` compound statement to the script you've
created so far. HINT: Does your state machine diagram need a new state or a new
transition?

## **### Assignment, Part 2**

It is now time to write your own script from scratch. Most of your life, you
will probably find yourself modifying a script that you or someone else wrote.
Every once in a while, however, you will encounter a task that requires you to
build your own script from scratch. This exercise is meant to squash any fear
you might have that this is hard to do.

I'll tell you what I did to write the solution for the problem assigned in this
step. I took the solution code for step 3, and copied it into a file called
`count32.py`. I opened this new file and modified the document string to make it
appropriate for my new project. I then asked myself if I needed any of the
`import` statements currently listed. If I didn't, I deleted them. I then
started writing a few statements that accomplished Step 4 (below), stealing code
from the old script when helpful. When it became time to try my solution to Step
4, I deleted the rest of the original script or commented it out. Before you
know it, you're back to writing pseudocode and making adjustments to something
that already exists!

**Step 1. Getting user input.** To this point, we have been reading our input
text from a file, but sometimes we want to ask the user running our script for
some information while the script is executing. Python makes this very easy.
Read about the builtin function `input` in the [Python
documentation](https://docs.python.org/3/library/functions.html#inputhttps://docs.python.org/3/library/functions.html%23input),
and implement a script that prompts the user of your script for an input string
and then prints that string back to the terminal. The prompt we will use is
`Text: `, which should end with a space beyond the colon (i.e., there's no typo
in this sentence!).

This script's functionality is similar to how we started working with our file
containing *The Cat in the Hat* story. In particular, your script should behave
as follows:

```
> python3 count32.py
Text: Down, down, down. Would the fall never come to an end!
Down, down, down. Would the fall never come to an end!
```

**Step 2. Counting letters.** Now, instead of immediately printing out what
the user just typed, let's do some analysis of it. Write a function that returns
a count of the number of alphabetic characters in the input text. After calling
that function, print out that count. We define a letter to be any uppercase or
lowercase alphabetic characters. Do not count punctuation, digits, other
non-alphabetic symbols, or whitespace. HINT: What string method in the [Python
documentation](https://docs.python.org/3/library/stdtypes.html#string-methods)
might help here?

Your script should now behave as follows:

```
> python3 count32.py
Text: Down, down, down. Would the fall never come to an end!
40 letter(s)
```

**Step 3. Counting words.** Let's continue our analysis and count the number of
words in the user's input. For the purpose of this problem, we'll consider any
sequence of characters separated by any amount of whitespace to be a word (so a
hyphenated word like `'sister-in-law'` should be considered one word, not
three). Use the string method `split` to create a sequence of words from the
input string and ask for the length of this sequence. Put this analysis code in
its own function.

Your script should now behave as follows:

```
> python3 count32.py
Text: Down, down, down. Would the fall never come to an end!
40 letter(s)
11 word(s)
```

**Step 4. Counting sentences.** Let's grab one more statistic about the user's
input, and that will be the number of sentences it contains. What constitutes a
sentence in English can be quite tricky to define. For this assignment, we will
keep it simple: any sequence of characters and whitespace that ends in a `'.'`,
`'?'`, and `'!'` is a sentence. This means that your script will incorrectly
report that the string `'Mr. and Mrs. Smith left for vacation.'` contains three
sentences. We will avoid this shortcoming by never passing your script any
tricky input.

You may be tempted to dive right in and start writing some Python code for this
part. You might even start by trying to use the `split` method from the last
part. A bit of advice, don't. Take a moment and think about the problem as
stated. Think in pseudocode about what you need to do. HINT: Why does the string
`'Mr. and Mrs. Smith left for vacation.'` contain three sentences? Is there a
[method common to all
sequences](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)
that might help you solve this problem very simply?

Your script should now behave as follows:

```
> python3 count32.py
Text: Down, down, down. Would the fall never come to an end!
40 letter(s)
11 word(s)
2 sentence(s)
```

**Step 5. Choice.** As a last step, we'd like our script to allow the user to
specify whether the input comes from a file or from user input. The user will
indicate this by invoking the script with or without, respectively, a filename
on the command line.

## **### Optional, Fun, Current-Event Reading**

"[Predictive text systems change what we write: Study explores the effects of
autocomplete features on human
writing](https://www.seas.harvard.edu/news/2020/05/predictive-text-systems-change-what-we-write)"
by Leah Burrows. "When a human and an artificial intelligence system work
together, who rubs off on whom? It's long been thought that the more AI
interacts with and learns from humans, the more human-like those systems become.
But what if the reverse is happening? What if some AI systems are making humans
more machine-like? ... The researchers found that when people use these systems,
their writing becomes more succinct, more predictable and less colorful
(literally)." Kenneth Arnold, Krysta Chauncey, and Krzysztof Gajos published
[the paper](https://dl.acm.org/doi/abs/10.1145/3377325.3377523) in 2020 ACM IUI
conference.