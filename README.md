# Assignment 1

NAME: ARKAJYOTI BASAK

ROLL: 101808212

BATCH: 4ME5 (ONLINE)

## Output
```
case 1: Change 1st LSB of each pixel/sample
Decoded message:  hellothapar
MSE: 0.00004353

case 2: Change 4th LSB bit of each pixel/sample and perform no flip to next LSB bits
Decoded message:  hellothapar
MSE: 0.00289330

case 3: Change 4th LSB bit of each pixel/sample and flip the next LSB bits
Decoded message:  hellothapar
MSE: 0.01961016
```

## Usage
`python <file name> <image name> <message>`
```
python main.py original.jpeg hellothapar
```

## Comparison
The best suited algorithm for my input data is the the first one which was **Change 1st LSB of each pixel/sample** since it has the lowest mean squared error. 

