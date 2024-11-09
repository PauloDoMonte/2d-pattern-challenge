# 2D Pattern Challenge

## Description

This repository contains a solution for a 2D pattern generation and manipulation challenge. The goal is to generate and apply a 2D pattern to determine the termination coordinate, and then reverse the pattern to calculate the initial start coordinate.

## Requirements

- Python 3.x
- No external libraries are required (standard libraries only).

## How to Run

1. Clone the repository or download the files.
2. Install Python 3.x if it's not already installed.
3. Navigate to the project directory and run the main Python script `main.py`:

```bash
python3 main.py data/start-coordinate.txt
```

This will generate the 2D pattern, apply the pattern to calculate the termination coordinate, and reverse the pattern to calculate the initial start coordinate.

### Files

- `start-coordinate.txt` – Input file with the starting coordinates.
- `2d-pattern.json` – Output file with the generated pattern.
- `termination-coord.txt` – Output file with the calculated termination coordinates.
- `start-coordinate-calculated.txt` – Output file with the calculated start coordinates after reversing the pattern.

## Expected Results

1. **Goal 1 (Pattern Generation and Application)**: 
   - The program generates a 2D pattern using powers of 2 (2^N) up to a maximum of 100 points. 
   - The pattern is then applied for a certain number of repetitions to calculate the termination coordinate, which should be between specific green lines defined by powers of 2 (2^575100 to 2^602100).

2. **Goal 2 (Reversing the Pattern)**: 
   - The program reverses the previously generated pattern to compute the start coordinate that, when the pattern is applied, leads to the termination coordinate calculated in Goal 1.

## Usage

Run the main script to generate the pattern, apply it, and reverse it to get the start and termination coordinates.

```bash
python3 main.py data/start-coordinate.txt
```

This will generate:
- `2d-pattern.json` (the generated pattern)
- `termination-coord.txt` (termination coordinates)
- `start-coordinate-calculated.txt` (calculated start coordinates)


```bash
python3 main.py goal2 data/termination-coord.txt data/2d-pattern.json
```

This will generate:
 - `start-coordinate.txt` (initial start coordinates based on the pattern)
 - `test-output.txt` (output with results of the pattern calculations)