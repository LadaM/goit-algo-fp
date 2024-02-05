# 2-Dice Sum Probability Calculation
Using monte-carlo method, we try to estimate the probabilities of getting a specific sum when two dice are thrown.
## Actual Probabilities
| Sum | 	Probability   |
|-----|----------------|
| 2   | 	2.78% (1/36)  |
| 3   | 	5.56% (2/36)  |
| 4   | 	8.33% (3/36)  |
| 5   | 	11.11% (4/36) |
| 6   | 	13.89% (5/36) |
| 7   | 	16.67% (6/36) |
| 8   | 	13.89% (5/36) |
| 9   | 	11.11% (4/36) |
| 10  | 	8.33% (3/36)  |
| 11  | 	5.56% (2/36)  |
| 12  | 	2.78% (1/36)  |

## Results
| Rolls  | Exper   | Sum=2 | Sum=3 | Sum=4 | Sum=5 | Sum=6 | Sum=7 | Sum=8 | Sum=9 | Sum=10 | Sum=11 | Sum=12 |
|--------|---------|-------|-------|-------|-------|-------|-------|-------|-------|--------|--------|--------|
| 100    | 100     | 3.0   | 5.43  | 7.0   | 12.0  | 12.86 | 15.43 | 12.14 | 10.57 | 8.86   | 3.29   | 3.14   |
| 100    | 1'000   | 2.29  | 5.0   | 6.71  | 11.29 | 15.14 | 17.57 | 13.71 | 10.0  | 7.86   | 7.0    | 3.0    |
| 100    | 10'000  | 2.57  | 6.57  | 9.29  | 10.0  | 14.29 | 15.86 | 13.14 | 10.57 | 9.29   | 5.29   | 3.14   |
| 100    | 100'000 | 2.71  | 4.14  | 7.57  | 11.57 | 11.57 | 18.29 | 12.57 | 9.43  | 8.86   | 6.29   | 2.43   |
| 1'000  | 100     | 3.03  | 5.66  | 8.29  | 11.31 | 14.09 | 16.91 | 13.71 | 11.7  | 7.94   | 5.71   | 2.7    |
| 1'000  | 1'000   | 2.74  | 4.71  | 8.67  | 10.91 | 13.43 | 16.14 | 14.46 | 10.77 | 8.54   | 5.49   | 2.76   |
| 1'000  | 10'000  | 2.6   | 5.29  | 8.77  | 11.03 | 14.46 | 17.36 | 13.27 | 11.23 | 8.36   | 5.5    | 2.73   |
| 1'000  | 100'000 | 2.59  | 4.74  | 8.83  | 11.37 | 13.83 | 17.2  | 14.09 | 11.37 | 8.47   | 5.67   | 2.73   |
| 10'000 | 100     | 2.73  | 5.57  | 8.5   | 11.19 | 13.9  | 16.74 | 13.92 | 11.26 | 8.39   | 5.54   | 2.72   |
| 10'000 | 1'000   | 2.84  | 5.65  | 8.32  | 11.12 | 13.68 | 16.61 | 13.93 | 11.02 | 8.29   | 5.58   | 2.77   |
| 10'000 | 10'000  | 2.78  | 5.39  | 8.28  | 11.3  | 13.87 | 16.75 | 13.67 | 11.06 | 8.28   | 5.59   | 2.81   |
| 10'000 | 100'000 | 2.79  | 5.4   | 8.35  | 10.94 | 13.9  | 16.53 | 14.18 | 11.07 | 8.22   | 5.54   | 2.79   |

## Conclusions
* Starting from 1'000 experiments and rolls per experiment estimated probabilities start to become closer to reality
* I haven't found a combination of number of experiments and rolls per experiment that could provide a very close result
  * my assumption is that the way dice are thrown and the distribution of the probabilities there has an impact on estimation
  * to achieve better prediction, better way of random selection might need to be considered
* I was surprised that monte-carlo method was in my opinion better in calculating integral than in probability estimation