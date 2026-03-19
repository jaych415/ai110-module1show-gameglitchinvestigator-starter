# Reflection

## 1. What was broken when you started?

- Bug 1: Incorrect hints  
Expected: "Too high" when guess > secret  
Actual: Sometimes returned wrong hint  

- Bug 2: Crashes on invalid input  
Expected: Error message  
Actual: Game crashed when input was text  

- Bug 3: Game state reset randomly  
Expected: Score persists during game  
Actual: Secret number reset unexpectedly  

---

## 2. How did you use AI as a teammate?

Correct Suggestion:
AI suggested separating logic into `logic_utils.py`.  
This improved readability and debugging.

Incorrect Suggestion:
AI initially suggested overly complex logic for validation.  
I simplified it manually and tested using pytest.

Verification:
- Ran pytest
- Tested in Streamlit UI

---

## 3. Debugging and testing your fixes

- Added pytest cases
- Tested edge cases (invalid input, bounds)
- Ran app multiple times to confirm stability