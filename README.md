In decesion making system,I used a system which asks which category then it takes in different values like for carvwe taje milage and kilometres run etc. we only take integer values as input and also take the priority of the values.
The program first collects criteria details (name, type, and priority rank) and then collects options with their values for each criterion.
It converts the priority ranks into numerical weights using the linear rank transformation formula
wᵢ′ = (n − rᵢ + 1), where n is the total number of criteria and rᵢ is the rank. This gives higher importance to lower rank numbers (rank 1 gets the largest weight).
The weights are then normalized using
wᵢ = wᵢ′ / Σwᵢ′, so that all weights sum to 1 and represent proportional influence.
Next, it normalizes each criterion value using min–max normalization: for benefit criteria,
xᵢⱼ(norm) = xᵢⱼ / max(xⱼ), and for cost criteria,
xᵢⱼ(norm) = min(xⱼ) / xᵢⱼ, ensuring all values are comparable on a common scale.
It calculates a final score for each option using the weighted sum model:
Scoreᵢ = Σ (xᵢⱼ(norm) × wⱼ).
Finally, the option with the highest final score is selected as the best choice.
