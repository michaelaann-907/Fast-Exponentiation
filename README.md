# Fast Exponentiation
The Fast Exponentiation program implements an efficient algorithm for performing modular exponentiation, a fundamental operation in many cryptographic algorithms. This technique leverages the binary representation of the exponent to significantly reduce the number of computations, making it especially useful for cryptographic applications where large numbers are involved.

## Features
- **Efficient Computation:** Uses the binary representation of the exponent to reduce the number of operations.
- **Modular Arithmetic:** Computes `(x^e) % n` for large numbers efficiently.
- **Cryptographic Applications:** Useful for cryptographic algorithms requiring modular exponentiation.


## Requirements
- **Python 3.x**: Ensure you have Python 3.x installed.


## Installation & Usage
1. Clone the repository or download the source code.

2. Run the program using Python:
   ```bash
   python fast_exponentiation.py
   ```
3. Output Information:
    - The program calculates the result of `(x^e) % n`.
    - Displays the result based on the input parameters.


### Example Usage
Here is an example of how to use the `expMod` function:

```python
from fast_exponentiation import expMod

# Example: Calculate (20^30) % 24
result = expMod(20, 30, 24)
print(f"The result of (20^30) % 24 is: {result}")
```

## Example Output
Below are examples of the output with different inputs.

### Example 1
```plaintext
The result of (20^30) % 24 is: 16
```
![fast_exp1](https://github.com/user-attachments/assets/b4577f97-3e41-407f-b3cd-f5aa00752979)


### Example 2
```plaintext
The result of (5^13) % 9 is: 5
```
![fast_exp2](https://github.com/user-attachments/assets/be87d3c3-2165-4cbc-b211-41a5962c5664)

