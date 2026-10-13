# Linear Programming Solver in Python

A Python project for solving Linear Programming (LP) problems using the Simplex method and the Big M method.

## Overview

This project was developed to explore and implement classical techniques in Linear Programming and Operations Research.

The program allows users to enter an objective function and a set of linear constraints, then constructs and processes the corresponding Simplex tableau.

## Features

- Define a minimization or maximization problem.
- Enter the coefficients of the objective function.
- Specify linear constraints and their operators (`<=`, `>=`, `=`).
- Display the formulated Linear Programming problem.
- Apply the Simplex method for problems with `<=` constraints.
- Apply the Big M method for problems involving other constraint types.
- Display the intermediate tableaux and iterations.

## Technologies

- Python 3
- Linear Programming
- Simplex algorithm
- Big M method
- Operations Research

## Requirements

- Python 3 installed on your computer.

The project currently uses interactive console input. Additional Python packages may not be required.

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/linear-programming-solver.git
   ```

2. Open the project directory:

   ```bash
   cd linear-programming-solver
   ```

3. Run the program:

   ```bash
   python pl.py
   ```

## Usage

Follow the prompts in the terminal to:

1. Choose minimization or maximization.
2. Enter the number of decision variables.
3. Enter the objective function coefficients.
4. Enter the number of constraints.
5. Enter each constraint's coefficients, operator, and right-hand-side constant.

The program displays the problem formulation and the iterations of the selected method.

## Project Status

Academic project — under development and testing.

## Author

Developed as part of a study of Linear Programming and Operations Research.

## Disclaimer

The implementation is an educational project. Results should be verified against known solutions before using the program for practical optimization problems.
