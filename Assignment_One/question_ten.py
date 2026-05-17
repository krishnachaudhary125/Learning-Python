# Smart Exam Proctoring Decision System
# Write a program for an AI-based exam proctoring system:
# Inputs:
#     Face detected (True/False)
#     Multiple persons detected (True/False)
#     Noise level (int)
# Conditions:
#     Face must be detected
#     Multiple persons must be False
#     Noise level < 50
# Output:
#     “Exam Environment Valid”
#     Otherwise specify the exact issue detected.

face_detected = input("Enter face detected (True/False) : ") == "True"
multiple_detected = input("Enter multiple persons detected (True/False) : ") == "True"
noise = int(input("Noise level : "))

if not face_detected:
    print("Face not detected")

elif multiple_detected and noise >= 50:
    print("Multiple face detected and Noise level is loud")

elif multiple_detected and noise < 50:
    print("Multiple face detected")

elif not multiple_detected and noise >= 50:
    print("Noise level is high")

else:
    print("Exam environment valid")