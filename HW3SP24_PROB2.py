import math

def t_distribution(degrees_freedom, z_value):
    if degrees_freedom <= 0:
        raise ValueError("Degrees of freedom must be greater than 0.")

    if abs(z_value) > 100:
        return 1.0  # for large z values, probability is very close to 1

    # Coefficients for the approximation of the t-distribution
    a = [0.3183, 0.1375, 0.0603, 0.0206, 0.0036, 0.0017]
    b = [1.0, 0.455, 0.309, 0.081, 0.054, 0.025]
    c = [0.0, 0.157, 0.429, 1.18, 1.96, 2.56]

    z_abs = abs(z_value)
    t = z_abs / math.sqrt(degrees_freedom)

    probability = 0

    if degrees_freedom == 1:
        probability = 1 - math.atan(t) / (math.pi / 2)
    else:
        for i in range(len(a)):
            probability += a[i] * t ** (2 * i)

        denominator = 1 + sum(b[j] * t ** j for j in range(1, len(b)))
        probability = 1 - probability / denominator

        if degrees_freedom % 2 == 0:
            for i in range(len(c)):
                probability *= (degrees_freedom - 2 * i) / (degrees_freedom + c[i] * t)
        else:
            for i in range(1, len(c)):
                probability *= (degrees_freedom - 2 * i) / (degrees_freedom + c[i] * t)

    return probability

def main():
    degrees_freedom = int(input("Enter degrees of freedom: "))
    z_values = [float(input(f"Enter z value {i+1}: ")) for i in range(3)]

    print("\nDegrees of Freedom:", degrees_freedom)
    for z in z_values:
        probability = t_distribution(degrees_freedom, z)
        print(f"Probability for z = {z}: {probability:.4f}")

if __name__ == "__main__":
    main()






