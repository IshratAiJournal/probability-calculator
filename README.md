# Probability Calculator 🎲📊

This is **Project 5** from FreeCodeCamp’s *Scientific Computing with Python* certification.

### 📖 What it does
Simulates drawing colored balls from a hat to estimate probabilities.  
Runs multiple experiments using random draws and compares the results to expected outcomes.

### 🧰 Features

- 🎩 Create a hat with colored balls  
- 🎯 Randomly draw a number of balls  
- 🔁 Run experiments to estimate probability  
- 📈 Compare expected vs. actual outcomes

### 🧠 Skills practiced

- Object-Oriented Programming in Python  
- Simulating randomness with `random`  
- Counting items and tracking outcomes  
- Writing experiments and calculating probability

### 🔁 Example Usage

```python
hat = Hat(red=3, blue=2)
probability = experiment(
    hat=hat,
    expected_balls={"red":2, "blue":1},
    num_balls_drawn=4,
    num_experiments=1000
)

print("Estimated Probability:", probability)

