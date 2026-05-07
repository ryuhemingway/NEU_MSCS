# CS5001 Homework 4 - Starter Code
## Loops and Functions Practice

## Important Instructions

### AI Code Completion Tools
This folder includes a `.vscode/settings.json` file that **disables all AI code completion tools** including:
- GitHub Copilot
- IntelliCode
- TabNine
- Kite
- All inline suggestions

**To use these settings:**
1. Open this folder in VS Code (File > Open Folder)
2. The AI tools will be automatically disabled for this workspace
3. You must include this comment at the top of each file:
   ```python
   # I confirm that AI code completion tools were disabled while writing this program.
   ```

### Submission Requirements
- Submit your `.py` files via Gradescope
- Write your **name** and **NU ID** at the top of each file as a comment
- **Comment all of your code** - explain what each section does
- Show your work! Don't just give final answers - show the steps you took

## Assignment Focus: Loops AND Functions

This assignment requires you to practice **both loops and function decomposition**. Each problem is broken down into multiple functions to help you learn good programming practices:

### Function Decomposition Benefits
- **Modularity**: Each function does one specific task
- **Reusability**: Functions can be used multiple times
- **Testability**: Easier to test small functions independently
- **Readability**: Code is easier to understand and maintain

## Problems Included

### 1. **problem1_tuition.py** - Tuition Increase Calculator
**Functions you'll implement:**
- `calculate_tuition_for_year()` - Given signature, you implement
- `display_tuition_projection()` - Given signature, you implement
- `main()` - Calls the functions

**Skills practiced:** Loops, function parameters, return values

---

### 2. **problem2_sleep_debt.py** - Sleep Debt Calculator
**Functions you'll implement:**
- `get_sleep_hours()` - Given signature, you implement
- `calculate_sleep_debt()` - YOU design the signature and implement
- `display_sleep_debt_results()` - Given signature, you implement
- `main()` - Calls the functions

**Skills practiced:** Input handling, loops, function design, conditionals

---

### 3. **problem3_factorial.py** - Factorial Calculator
**Functions you'll implement:**
- `get_nonnegative_integer()` - Given signature, you implement
- `calculate_factorial()` - Given signature, you implement
- Display function - YOU design and implement from scratch
- `main()` - Calls the functions

**Skills practiced:** Loops, accumulator pattern, function design

---

### 4. **problem4_population.py** - Population Growth Predictor
**Functions you'll implement:**
- `get_population_inputs()` - Given signature, you implement
- `calculate_next_day_population()` - Given signature, you implement
- Display function - YOU design and implement from scratch
- `main()` - Calls the functions

**Skills practiced:** Multiple inputs, loops, function design, formatting

---

## Structure of Each Problem

Each file follows this pattern:

```python
def helper_function_1(...):
    """Docstring explaining the function"""
    # Your implementation
    pass

def helper_function_2(...):
    """Docstring explaining the function"""
    # Your implementation
    pass

def main():
    """Main function that orchestrates everything"""
    # Call your helper functions here
    pass

# Run the program
main()
```

## Tips for Success

### General Tips
1. **Read all docstrings carefully** - they contain important hints
2. **Implement one function at a time** - test as you go
3. **Use the provided signatures** - don't change parameter names or return types
4. **Design missing functions carefully** - think about what parameters and return values make sense

### Function Design Tips
When you need to create a function from scratch:
1. **What does it do?** (Write this in the docstring)
2. **What information does it need?** (These become parameters)
3. **What does it produce?** (This becomes the return value)
4. **What's a good name?** (Use descriptive verb phrases)

### Testing Strategy
1. Test each function individually before moving to the next
2. Start with simple test cases (e.g., factorial of 0, 1, 5)
3. Use print statements to debug if needed
4. Make sure your output formatting matches the requirements

### Common Mistakes to Avoid
- ❌ Forgetting to return values from functions
- ❌ Not calling functions from main()
- ❌ Changing provided function signatures
- ❌ Putting all code in main() instead of using helper functions
- ❌ Not removing `pass` statements when implementing functions

## Example of Good Function Decomposition

**Bad approach (everything in main):**
```python
def main():
    # 50 lines of code doing everything
    pass
```

**Good approach (decomposed into functions):**
```python
def get_input():
    # Handle user input
    return value

def calculate(value):
    # Do calculations
    return result

def display(result):
    # Show output
    pass

def main():
    value = get_input()
    result = calculate(value)
    display(result)
```

## Getting Started

1. Open the folder in VS Code
2. Start with Problem 1 (it has the most guidance)
3. Read the docstrings and TODO comments
4. Implement one function at a time
5. Test frequently
6. Move to the next problem

Good luck! Remember: good programmers break problems into smaller, manageable pieces! 🎓
