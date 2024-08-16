# Fast Exponentiation

The Fast Exponentiation program implements an efficient algorithm for performing modular exponentiation, a fundamental operation in many cryptographic algorithms. This technique leverages the binary representation of the exponent to significantly reduce the number of computations, making it especially useful for cryptographic applications where large numbers are involved.

---

## Table of Contents

- [About](#about)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Files](#files)
- [Usage](#usage)

---

## About

This project was developed as part of the CSC 592 - Introduction to Cryptography course at the University of North Carolina Wilmington (UNCW). The program demonstrates the fast exponentiation algorithm, an efficient method for computing large exponentiations modulo a given number.

---

## Getting Started

### Prerequisites

- Python 3.x

### Installation

Download or clone the repository and run the `fast_exponentiation.py` script.

### Files

- `fast_exponentiation.py`: Contains the implementation of the fast exponentiation algorithm.

---

## Usage

The `expMod` function takes three parameters: the base `x`, the exponent `e`, and the modulus `n`. It returns the result of `(x^e) % n`.

### Example Usage

Here is an example of how to use the `expMod` function:

```python
from fast_exponentiation import expMod

# Example: Calculate (20^30) % 24
result = expMod(20, 30, 24)
print(f"The result of (20^30) % 24 is: {result}")
