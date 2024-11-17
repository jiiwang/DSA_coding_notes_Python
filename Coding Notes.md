## Topic: Backtracking

### Template
```python
result = []
def backtrack(path, choice_list):
    if meets_termination_condition:
        result.add(path)
        return
    
    for choice in choice_list:
        make_choice
        backtrack(path, choice_list)
        undo_choice
```

### Tips
- Draw a small example decision tree to understand how the path changes.

### Questions
1. Permutation (Leetcode 46, Medium):
	- Python list (path variable) is mutable, need to make a shallow copy at the time you append to the result list.