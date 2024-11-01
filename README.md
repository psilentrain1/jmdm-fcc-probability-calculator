### Probability Calculator App

A program to determine the approximate probability of drawing certain balls randomly from a hat.

#### Using the Probability Calculator App

Create a hat and set up the experiment.
Use `hat = Hat(<color>=<count>)` to create a hat filled with colored balls.
Use `experiment(hat=<hat object>, expected_balls=<dict of expected balls>, num_balls_drawn=<number of balls to draw>, num_experiments=<number of times to run experiment>)`. The more experiments run, the higher the probability.

#### Test Cases

```
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
```

Will output similar to:

`0.356`

Since this is based on random draws, the probability will be slightly different each time the code is run.

#### freeCodeCamp Disclaimer

This project was completed as part of [freeCodeCamp.org](https://www.freecodecamp.org)'s _Scientific Computing with Python_ course. This was a Certification Project, meaning [freeCodeCamp](https://www.freecodecamp.org) provided specifications and limited guidance and I was expected to code to meet certain test cases. The code presented here is my own.
