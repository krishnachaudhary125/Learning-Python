# Fake AI Prediction Confidence Detector
# A prediction system outputs a confidence score.
# Input confidence score (float) and prediction label (string).
# Conditions:
#     Confidence ≥ 0.9 → “Highly Reliable”
#     0.7–0.89 → “Moderately Reliable”
#     Below 0.7 → “Unreliable Prediction”
# Also check:
#     If label is empty → “Invalid Prediction”


confidence = float(input("Enter confidence score (0.0 - 1.0): "))
prediction = input("Enter prediction label : ")

if confidence >= 0.9:
    print("Highly Reliable")

elif confidence >=0.7 and confidence<=0.89:
    print("Moderately Reliable")

else:
    print("Unreliable Prediction")

if prediction == "":print("Invalid Prediction")