import streamlit as st
import numpy as np

# Base reward probabilities
base_probabilities = {
    5: 0.75,    # 75% for reward 5
    100: 0.20,  # 20% for reward 100
    500: 0.05   # 5% for reward 500
}

# Function to calculate dynamic reward probabilities
def calculate_reward_probability(transaction_amount):
    dynamic_probabilities = base_probabilities.copy()

    if transaction_amount >= 1000:
        scale_factor = transaction_amount / 1000  # Example scaling factor
        dynamic_probabilities[5] *= (1 / scale_factor)  # Decrease for lower reward
        dynamic_probabilities[100] *= scale_factor       # Increase for mid reward
        dynamic_probabilities[500] *= (scale_factor ** 2) # Increase more for highest reward

    # Normalize probabilities
    total_prob = sum(dynamic_probabilities.values())
    for key in dynamic_probabilities:
        dynamic_probabilities[key] /= total_prob

    return dynamic_probabilities

# Function to get reward for a given transaction amount
def get_reward(transaction_amount):
    probabilities = calculate_reward_probability(transaction_amount)
    rewards = list(probabilities.keys())
    chosen_reward = np.random.choice(rewards, p=list(probabilities.values()))

    return chosen_reward, probabilities[chosen_reward]


st.image("./Data/assets/logo.png", width=200)  
st.title("Spin the Wheel - Transaction-Based Rewards")

# Input for transaction amount
transaction_amount_input = st.number_input("Enter the transaction amount (yen)", min_value=1000.0, step=100.0)

if transaction_amount_input < 1000:
    st.warning("Please enter an amount equal to or greater than 1000 yen to qualify for the reward.")
else:
    # Get reward based on transaction amount
    reward, probability = get_reward(transaction_amount_input)

    # Display the reward and probability
    st.success(f"🎉 For a transaction amount of {transaction_amount_input} yen, you won {reward} yen!")
    st.write(f"Probability of receiving this reward: {probability:.2f}")

    # Display reward probabilities for reference
    st.write("Here are the reward probabilities based on your transaction amount:")
    probabilities = calculate_reward_probability(transaction_amount_input)
    for reward, prob in probabilities.items():
        st.write(f"  Reward {reward} yen: {prob:.2f} probability")

