sugaymachinelearning =[ ("Supervised", "Decision", "True"),
                        ("Supervised", "Random Forest"),
                        ("Unsupervised", "K-Means"),
                        ("Unsupervised", "Gaussian mixture model"),
                        ]

print("Learning Type: ", sugaymachinelearning[1][0])
for item in sugaymachinelearning:
    if item [0] == "Supervised":
        print("Supervised:",item[1])


print("Learning Type: ", sugaymachinelearning[0][1])
for item in sugaymachinelearning:
    if item [0] == "Unsupervised":
        print("Unsupervised:",item[0])


