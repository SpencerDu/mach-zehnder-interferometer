# mach-zehnder-interferometer

Simulates the Mach-Zehnder interferometer the way Prof. Adams sets it up in MIT OCW 8.04 (Spring 2013), with electrons and colour/hardness boxes instead of photons and beam splitters:

white electrons -> a hardness box splits them into a hard path and a soft path -> a dial shifts the phase of one path -> the paths are rejoined -> a colour box sorts them into white or black -> measure the outcome

I learnt this from those lectures, so the code uses the same language. That is why everything is called colours, hardness and boxes. In optics terms, a box is a 50:50 beam splitter, the dial is a phase shifter on one arm, and the wall blocks one arm.

## Why

To build up intuition for the foundations of QM.

## The physics

In the lectures each box has magic monkeys inside that sort the electrons: a colour box into white or black, a hardness box into hard or soft. The detectors just sort particles by that property.

A white electron is an equal mix of hard and soft, so it goes down both paths. The dial delays one path, which shifts its phase. When the paths are rejoined they superpose, and the phase difference decides the odds of white or black at the colour box.

With the dial at 0, the black parts from the two paths cancel and the white parts add, so every electron comes out white.

In the code each piece is a 2x2 matrix acting on the state:

    box  = (1/sqrt(2)) * [[1, 1], [1, -1]]
    dial = [[1, 0], [0, e^(i*theta)]]
    wall = [[1, 0], [0, 0]]

    output = box * dial * box * input

## Results

- Dial at 0: 100% white, 0% black.
- Turning the dial: white = cos^2(theta/2) and black = sin^2(theta/2), the interference fringes.
- One arm blocked: blocking a path measures which path the electron took. 50% of the time it took the blocked path and hits the wall. The other 50% it took the open path, so its hardness is now known, and a known hardness is 50/50 in colour. That gives 25% white and 25% black, whatever the dial is set to. The fringes are gone.

## The bomb tester (Elitzur-Vaidman)

A bomb sits on one arm, like the wall. A live bomb explodes if the electron goes through that arm. A dud lets it through as if the arm were empty.

- Dud: the arm is open, so 100% white.
- Live: 50% explodes, 25% white, 25% black.

So with one electron:

- explodes -> live
- black -> live, and it did not explode. A dud can never give black.
- white -> inconclusive

25% of the time a live bomb is found without setting it off. The electron that came out black never went through the bomb's arm, or the bomb would have gone off.

## Known limitations

- Everything is ideal: perfect 50:50 boxes, no losses and perfect interference. In a real setup the paths never rejoin perfectly (the path lengths differ, so one wave arrives later than the other), so with the dial at 0 you would still see some black.
- On the first plot the dashed analytic curves are drawn after the legend is made, so they are missing from the legend.

## Running it

Needs Python with numpy and matplotlib:

    pip install numpy matplotlib
    python mach_zehnder_interferometer.py

It prints the checks and probabilities, then shows two plots: the fringes as the dial turns, and the same with one arm blocked. Close a plot to see the next one. The bomb numbers print at the end.
