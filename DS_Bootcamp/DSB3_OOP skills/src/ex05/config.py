num_of_steps: int = 3

report = ("We have made {obs} observations from tossing a coin: "
          "{tails} of them were tail{tails_end} and {heads} of them were head{heads_end}.\n"
          "The probabilities are {prob1:.2%} and {prob2:.2%}, respectively.\n"
          f"Our forecast is that in the next {num_of_steps} observations we will have: "
          "{p_tails} tail{p_tails_end} and {p_heads} head{p_heads_end}.")
