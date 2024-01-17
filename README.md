# Math template

## 1. Probability

### Continuous Distributions:

- in python  (CDF) refers to Continuous Distribution Function,
  and (pdf) refers to Probability Distribution Function.

- (range of possible values)

- Probability distributions where the random variable can take any value within a specified range.
- Examples include the normal (Gaussian), uniform, exponential, beta, gamma, and Weibull distributions.


1. **Uniform Distribution:**
    - **Idea:** Every point in the range is equally likely.
    - **Example:** Picking a random number between 0 and 1.

2. **Normal (Gaussian) Distribution:**
    - **Idea:** Forms a symmetrical bell curve with a defined mean and standard deviation.
    - **Example:** Distribution of human heights or weights.

3. **Exponential Distribution:**
    - **Idea:** Describes the time between events in a Poisson process.
    - **Example:** Time between arrivals of consecutive customers at a store.

4. **Gamma Distribution:**
    - **Idea:** Generalization of the exponential distribution, often used for time until a specified event.
    - **Example:** Time until the next phone call in a call center.

5. **Beta Distribution:**
    - **Idea:** Describes the distribution of probabilities for events with two outcomes.
    - **Example:** Modeling the distribution of success probabilities in a continuous context.

### Discrete Distributions:

- like (coin flips, dice rolls, etc.)
- Probability distributions where the random variable can only take distinct, separate values.
  Examples include the Bernoulli, binomial, Poisson, geometric, hypergeometric, and multinomial distributions.

1. **Bernoulli Distribution:**
    - **Idea:** Models a single trial with two possible outcomes (success or failure).
    - **Example:** Flipping a coin (Heads or Tails).

2. **Binomial Distribution:**
    - **Idea:** Describes the number of successes in a fixed number of independent Bernoulli trials.
    - **Example:** Counting the number of heads in five coin flips.

3. **Poisson Distribution:**
    - **Idea:** Models the number of events occurring in a fixed interval of time or space.
    - **Example:** Counting the number of emails received in an hour.

4. **Geometric Distribution:**
    - **Idea:** Describes the number of trials needed for the first success in a sequence of independent Bernoulli
      trials.
    - **Example:** Finding the number of coin flips needed to get the first Heads.

5. **Hypergeometric Distribution:**
    - **Idea:** Describes the number of successes in a sample drawn without replacement from a finite population.
    - **Example:** Drawing cards from a deck without replacement, counting the number of red cards.

6. **Negative Binomial Distribution:**
    - **Idea:** Generalization of the geometric distribution, describes the number of trials needed for a specified
      number of successes.
    - **Example:** Counting the number of coin flips needed to get three Heads.

7. **Multinomial Distribution:**
    - **Idea:** Generalization of the binomial distribution for more than two categories.
    - **Example:** Rolling a fair six-sided die multiple times, counting the occurrences of each number.

8. **Categorical Distribution:**
    - **Idea:** Describes the probability of observing each category in a set.
    - **Example:** Predicting the category of an image (e.g., cat, dog, or bird).

9. **Discrete Uniform Distribution:**
    - **Idea:** Every outcome in a finite set is equally likely.
    - **Example:** Rolling a fair die.

------------

**Running Jupyter Notebook:**

To launch the Jupyter Notebook server, use the following command:

```bash
jupyter notebook
```

(Note: Use Control-C to stop the server)

---

**Installing Dependencies:**

Ensure that the required dependencies are installed by running the following commands:

```bash
pip install -r requirements.txt
python -m pip install jupyter
```

---

**Memory Profiling:**

To profile the memory usage, decorate your Python script with `@memory_profiler.profile` and run the following command:

```bash
python -m memory_profiler main.py
```

---

**Line Profiling:**

For line-level profiling, use the `line_profiler_pycharm` package. Decorate your Python script with `@profile` and
execute the following command:

```bash
python -m line_profiler main.py.lprof > results.txt
```

Make sure to replace `main.py` with the appropriate filename.