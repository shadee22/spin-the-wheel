## Key Components

### Base Probabilities
`base_probabilities`: Defines the default reward distribution:
- 75% chance for a reward of 5 yen.
- 20% chance for a reward of 100 yen.
- 5% chance for a reward of 500 yen.

### Dynamic Reward Calculation
`calculate_reward_probability(transaction_amount)`: This function dynamically adjusts the reward probabilities based on the transaction amount:
- If the transaction is 1000 yen or more, the reward probabilities are adjusted:
  - Lower rewards (5 yen) are made less likely as the transaction amount increases.
  - Mid-level rewards (100 yen) increase in likelihood in a linear fashion.
  - Highest rewards (500 yen) increase at a faster, quadratic rate as the transaction amount grows.
- Probabilities are then normalized so that they sum to 1, ensuring they are valid probability values.

### Reward Selection
`get_reward(transaction_amount)`: This function:
- Calls `calculate_reward_probability` to get the dynamically adjusted probabilities.
- Uses `np.random.choice` to randomly select one reward based on the calculated probabilities.
- Returns the selected reward and its associated probability.
