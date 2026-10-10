import numpy as np
import matplotlib.pyplot as plt


box = (1/np.sqrt(2)) * np.array([[1, 1],
                                 [1, -1]])

wall = np.array([[1, 0],
                [0, 0]])
def dial(theta):
    return np.array([[1,0],
                      [0, np.exp(1j*theta)]])

if __name__ == "__main__":
    hard = np.array([1, 0])
    soft = np.array([0, 1])
    white = (1/np.sqrt(2)) * np.array([1, 1])

    if np.allclose(box.conj().T @ box, np.eye(2)):
        print ("passed check")
    else:
        print ("failed check")


    print("hard -> colour:", np.abs(box @ hard)**2)
    print("soft -> colour:", np.abs(box @ soft)**2)

    white_in = np.array([1, 0])
    out = box @ dial(0) @ box @ white_in
    print("detector rates [white, black]:", np.abs(out)**2)

    thetas = np.linspace(0, 2*np.pi, 200)
    white_probs = []
    black_probs = []

    for theta in thetas:
        probs = np.abs(box @ dial(theta) @ box @ white_in)**2
        white_probs.append(probs[0])
        black_probs.append(probs[1])
    print("white probs", white_probs[:5])
    print("black probs", black_probs[:5])


    plt.plot(thetas, white_probs, label="white")
    plt.plot(thetas, black_probs, label="black")
    plt.xlabel("dial setting (radians)")
    plt.ylabel("probability")
    plt.legend()
    plt.plot(thetas, np.cos(thetas / 2) ** 2, '--', label="cos²(φ/2)")
    plt.plot(thetas, np.sin(thetas / 2) ** 2, '--', label="sin²(φ/2)")
    plt.show()

    phis = np.linspace(0, 2*np.pi, 200)
    white_wall_probs = []
    black_wall_probs = []

    for phi in phis:
        wall_probs = np.abs(box @ wall @ dial(phi) @ box @ white_in)**2
        white_wall_probs.append(wall_probs[0])
        black_wall_probs.append(wall_probs[1])
    total_wall = np.array(white_wall_probs) + np.array(black_wall_probs)

    print("white probs after wall", white_wall_probs[:5])
    print("black probs after wall", black_wall_probs[:5])
    print ("total reaching detector:", total_wall [:1])
    print("absobred by wall:", 1 - total_wall[:1])

    plt.plot(phis, white_wall_probs, label="white")
    plt.plot(phis, black_wall_probs, label="black")
    plt.plot(phis, total_wall, label="total reaching detector")
    plt.xlabel("dial setting (radians)")
    plt.ylabel("probability")
    plt.legend()
    plt.show()

    dud_out = np.abs(box @ dial(0) @ box @ white_in)**2
    live_out = np.abs(box @ wall @ dial(0) @ box @ white_in)**2
    print("dud [white, black]:", dud_out)
    print("live [white, black]:", live_out)
    print("boom probability:", 1 - live_out.sum())