### Angular Distributions, Partial Wave Analysis, and Kinematics in Two-Particle Scattering



Today we are at lecture number five.
We'll discuss **angular distributions** and **partial wave analysis**.
But before going there, I would like to start with a recap.

---


In the last lecture, we discussed:

- The **phase space** for particle reactions
- Different experiments and their **kinematics**
- Experiments worldwide studying **hadrons**, their production mechanisms, and peculiarities

We start with a recap on **kinematics**.

---


**First question:** *How many variables describe a two-particle scattering process?*

We have two cases:

1. **Scalar particles** ($0^-$):
- Initial state: two $0^-$ scalars
- Final state: two $0^-$ scalars
2. **Particles with spin**:
- Example: $1^+$ scattering with $3^-$
- Final state: $3^-$ and $1^+$

::: callout-note
The scattering process is represented by a "blob" (unitarity diagram, not a Feynman diagram). The blob encapsulates the interaction (strong, electromagnetic, etc.), while arrows indicate incoming/outgoing particles.
:::
---


**Task:** Calculate the number of variables needed to fully describe the process.

1. **Without spin**:
- Initial count: 8 (from conservation laws)
- Subtract 6 (3 rotations + 3 boosts due to frame invariance)
- **Result:** 2 variables

2. **With spin**:
- Same as above: **2 variables** (spin orientation doesn’t add independent kinematic variables for 2→2 scattering).

::: callout-important
The **scattering amplitude** for spinless particles is a **scalar function** of $s$ and $t$. For particles with spin, it becomes a higher-rank object (e.g., 21-dimensional for $3^- \times 1^+$), but still depends on **the same two variables**.
:::
---


The process is fully described by **two independent Lorentz-invariant variables**. Common choices:

1. **Mandelstam variables**:
- $s = (P_1 + P_2)^2$ (center-of-mass energy squared)
- $t = (P_1 - P_3)^2$ (momentum transfer squared)
- $u = (P_1 - P_4)^2$ (with $s + t + u = \sum m_i^2$)

2. **Center-of-mass frame variables**:
- $\sqrt{s}$ (center-of-mass energy)
- $\theta$ (scattering angle between $\vec{p}_1$ and $\vec{p}_3$)

::: callout-tip
Any two **independent** variables work (e.g., lab-frame energies $E_1$, $E_3$), but Mandelstam variables avoid frame-specific distortions.
:::
---


For **three-body decay** ($1 \to 2 + 3 + 4$), the kinematics are similarly described by **two variables**:

- $s_{34} = (P_3 + P_4)^2$
- $t_{13} = (P_1 - P_3)^2$

**Key properties**:

- The **phase space** is **flat** in Mandelstam variables ($dN/ds_{34}\,dt_{13} = \text{constant}$).
- This makes the **Dalitz plot** a powerful tool for studying dynamics.

---


The **three-body phase space** is given by:
$$
d\Phi_3 = \frac{1}{(2\pi)^5} \frac{d^3p_2}{2E_2} \frac{d^3p_3}{2E_3} \frac{d^3p_4}{2E_4} \delta^4(P_1 - P_2 - P_3 - P_4)
$$

Using the **recursive formula**:
$$
d\Phi_3 = d\Phi_2(M;m_3,m_4) \times d\Phi_2(M\to m_1; m_2, M_{34}) \times \frac{1}{8\pi^2} ds_{34}
$$

---


The **Dalitz plot** (plotting $s_{34}$ vs. $t_{13}$) directly reveals dynamics:

- No kinematic distortions in Mandelstam variables.
- Deviations from flatness indicate **resonances** or **interactions**.

::: callout-note
This marks the shift from general particle physics to **hadron-specific** topics, focusing on **spectroscopy** and **three-body decays**.
:::
---


- **Exercise**: Study the **Dalitz plot** for three-body decays.
- **Next**: Dive deeper into **angular distributions** and **partial wave analysis**.

Questions? Let’s discuss before moving on!

### Charm Decay Kinematics and the Dalitz Plot in $\Lambda_c$ Baryon Decay


You can see the example of the triple decay that I have here: the $\Lambda_c$ baryon going to the proton, kaon, and pion.
We measure $\Lambda_c$ produced in proton-proton collisions or any other collisions.
In the **BES experiment** and **Belle experiment**, they observe $\Lambda_c$.
This is one of those particles that lives a long time and is produced abundantly.

---

Particles with charm ground states are produced abundantly, and they live sufficiently long to fly from the primary vertex.
We reconstruct them, which is why we have a good sample and a good understanding of their decay kinematics—and not only kinematics but dynamics as well, the content of this blob.

---

In that decay, you see there is a charm quark in the initial state and no charm quark in the final state, indicating this happens via **weak interaction**.
The charm quark disappears between the initial and final states.
It decays, transitioning into the strange quark that ends up in the kaon.
The $c \to s$ transition happens within one generation, so this is **not suppressed**—it’s an allowed process.

::: callout-note
The weak decay process involves:
$$\Lambda_c^+ \to p^+ + K^- + \pi^+$$
$$c \to s + W^+ \quad \text{(with } W^+ \to u\bar{d}\text{)}$$
:::
---

This is the **golden channel** for detection because, in the final state, you have three charged particles.
There are no neutrals.

- The **proton** is a nice charged particle—it travels and is stable.
- The **kaon** is stable in our accelerator experiments.
- The **pion** is also stable.

They fly out from the decay without any distraction, and we see their tracks clearly through all detectors.
We observe them pointing away from the primary interaction.

---

There is roughly a **10-millimeter shift** in $\Lambda_c$ flight distance between the primary vertex and the secondary vertex—about one centimeter.
This is due to the boost and the fact that $\Lambda_c$ in the laboratory frame lives longer than in its rest frame.

::: callout-note
The observed flight path is explained by:
$$\Delta x = \gamma v \tau_0$$
where $\gamma = E_{\Lambda_c}/m_{\Lambda_c}$ is the Lorentz factor.
:::
It is produced with several hundred GeV in proton-proton collisions at the LHC.
This is a very clean decay, and we have studied it extensively.

---

Here is the experimental result of the analysis, which closely resembles the data.
If I showed you the actual experimental data, you wouldn’t distinguish it from this plot because the statistics are so high that the distribution is very smooth.

On the **$x$-axis**, I have the invariant mass squared of the proton and kaon:
$$m_{pK}^2 = (p_p + p_K)^2$$

On the **$y$-axis**, I have the invariant mass squared of the kaon and pion:
$$m_{K\pi}^2 = (p_K + p_\pi)^2$$

All allowed kinematic values for the decay are shown in color.
The white area around it corresponds to kinematics where energy and momentum conservation cannot be satisfied.

---

If I select a point inside the plot, I can compute the angles between particles and their momenta, reconstructing the full 3D decay configuration.
But if you give me kinematics in the white area, I immediately see that energy conservation is violated—it’s impossible.
This is why the range of possible invariant masses is limited, and this surface is called the **Dalitz plot**.

---

This is how we explore the kinematics.
Different colors on the plot indicate different probabilities for the decay to occur in specific kinematic configurations.
We measure the decay, reconstruct the particle tracks, and determine from which kinematic point it originated because there’s a direct mapping between the four-vectors and the Dalitz plot coordinates.

It turns out that certain kinematics are more probable than others.
Particles prefer specific momentum configurations.

---

For this decay, for example, one kinematic configuration is more likely than another.
You should be able to identify this pattern in the plot.
Let’s take a moment to find it.

The hint is that particles are aligned in one line at the plot’s boundary.
Inside the surface, they always have an angle between them, but at the boundary, they become collinear.

::: callout-note
At the Dalitz plot boundaries:
$$\theta_{ij} = 0 \text{ or } \pi \text{ between particles}$$
:::
Think: how do you maximize the invariant mass, and where does this point lie on the boundary?

---

### Maximizing and Minimizing Mass in Three-Body Decay Kinematics



Any thoughts? I think you should be in the bottom right because we should maximize the mass of the PK. There are three momenta going out there. The three momenta are in opposite directions, so the three-momentum of the sum should be as small as possible.

If we add both momentum vectors, the forward momentum—the sum of the squares—should be as large as possible. We should be on the right of our diagram. If we apply and find... The same direction should be on the lowest.

You argue that this mass, on the y-axis, should be as small as possible. Why? Because the three momenta are in line, and we subtract them. If you go to their rest frame, the K and π fly next to each other. Their relative momentum is small. If you boost to their rest frame, they might both be at rest. Their mass would just be the sum of the masses, so it's minimum.

::: callout-note
**Key Relation for Invariant Masses in Three-Body Decay**:
For a decay like $\Lambda_c \to p K \pi$, the invariant masses satisfy:
$$
m_{12}^2 + m_{23}^2 + m_{13}^2 = m_{\Lambda_c}^2 + m_p^2 + m_K^2 + m_\pi^2
$$
where $m_{ij}$ are the invariant masses of particle pairs.
:::
What you're saying is correct. We are looking for the minimal mass of the kinematic. Let's figure out what this point corresponds to. There is kinematics like this: two particles with maximal momentum are at rest and go in opposite directions. That corresponds to this one.

This plot is from experimental data. In the experiment, we would reconstruct such a case because we would not detect the proton. This is the lab frame, but everything we measure is in the lab frame where everything is boosted. Even though the proton is at rest in the lab frame, it's already boosted.

---


This point is the maximum mass. They have maximum momentum and go back-to-back, so this is the maximum mass. This one minimizes the mass. For the three-body decay, there is a similar way to define the angle.

Let me show you the setup. I’m using proton, K, and π. I want to fix the mass of the K-π system. I would like to explore that by changing the mass of the proton.

Think of this in the center-of-momentum frame and boost to the K-π rest frame. In the K-π rest frame, they go back-to-back. In the center-of-momentum frame, three particles are arranged such that the sum of the three-momenta is zero.

Once I boost, the $\Lambda_c$ has non-zero momentum. The K and π also have non-zero momentum, but since I am in their rest frame, these two momenta add to zero. If I fix the mass of the system and explore phase space along the line where the mass of this pair is fixed, the length of these vectors is fixed.

What is changing? Only the angle $\theta$. I explore the whole range of the angle from $0$ to $\pi$. At one corner, $\theta = 0$; at the other, $\theta = \pi$.

---


The right should be zero and the left... Let’s see how you get to that. We fixed the setup where the proton and K-π go in opposite directions. This has the maximum mass of the proton-K system.

For our new setup, as the length of all vectors is fixed, we can only rotate. The dependence of the mass of two particles on $\theta$ is such that the wider the angle, the bigger the mass. For the proton-K system, $\theta = 0$ gives a very high mass. If they go almost in the same direction, they have a small mass.

::: callout-important
**Invariant Mass Relation for Fixed $m_{K\pi}$**:
$$
m_{pK}^2 = m_{\Lambda_c}^2 + m_K^2 + m_\pi^2 - m_{K\pi}^2 - 2E_{K\pi}E_p + 2|\vec{p}_{K\pi}||\vec{p}_p|\cos\theta
$$
where $E_i$ and $\vec{p}_i$ are energies/momenta in the $\Lambda_c$ rest frame.
:::
I can do the same with the other half. Let me fix the mass of the proton-K system again. The most straightforward way to analyze is to go to the rest frame of the proton-K system, where everything is fixed. Then scan along this line by changing the angle of this pair with respect to the rest.

The lines describe the setup where you change the angle in one frame or another. There is a third variable in the 2-to-2 scattering called U, but it's more symmetric. For three particles, there is the mass of the pion-proton system.

If I fix the mass of this system and scan the angle, this is easy to understand from the relation that U is a linear combination of the two. The coefficients are one, so it's a diagonal in this plot.

---


This line is the mass of the pion-proton system fixed. I go from one corner to another, changing the representation. The representation we use in experimental analysis for the Dalitz plot has the mass of one pair on the x-axis and the other on the y-axis.

In the homework, you have an exercise with a more symmetric Dalitz plot where all variables enter symmetrically. This uses properties of an equilateral triangle: every point inside has distances to the sides that sum to a constant.

The variables—masses of particles—are the distances to the sides. I can look at it like this or like that. This is a super symmetric, nice representation. Essentially, it's the same as this.

They're not matching because one and another... Wait, should they match? It's a linear transformation, skewed. To plot this, I had to find the relation between Cartesian coordinates and the heights of the triangle.

What appears is $\sqrt{3}/2$ because of the 60° angles. This is a nice symmetric representation, but the other is more common and easier to plot. Both represent the kinematics.

The objective is to understand the dynamics and processes guiding this interaction. Looking ahead, we realize this process is not just $\Lambda_c$ decaying to three particles but proceeding via intermediate resonances.

For a short moment, two particles form an intermediate state that dissociates, increasing the decay probability. These two particles interact more at certain energies, so the probability increases.

---


You might have seen cross sections for two-particle resonances with bumps known as hadronic resonances. The physics is that the quantum numbers of the system match some resonance.

By adjusting the energy, you explore how likely the particles are to interact. If there is an intermediate resonance, the system resonates at this energy, and the probability increases.

This leads to bent structures in the Dalitz distribution. Projected onto one axis, you see a resonance-like shape. These bent structures appear in all three pairs.

Why is there a bigger probability increase when the kaon and pion are near resonance? Let's understand the lines. We’ll come back to this in two lectures.

All horizontal lines—which resonances are these? In which mass distribution? Horizontal lines in the blue plot correspond to fixed mass for $K\pi$. These are $K^*$ resonances.

Now, the vertical lines—in which system? When changing $K\pi$, I scan a certain energy. This corresponds to fixed mass of the proton and $K\pi$.

The lines correspond to resonances in $K\pi$, proton-K, and pion-proton. The other plot helps because the lines are parallel to the sides of the triangle.

This line is the same as this one, parallel to one side. The lambda resonances are parallel to another side. The delta resonance is parallel to the third side.

---


Okay, questions on the angular distribution. To move past this, let’s discuss the angular distribution for a decay within one band.

The kinematics: traversing the Dalitz plot while keeping the mass fixed changes the angle. This is the kinematics.

In the rest frame of $K\pi$, traversing phase space changes this angle. The angle dependence indicates inhomogeneity. Within the band, one edge might have a different probability than the other.

Particles might prefer to be aligned rather than perpendicular. This happens because particles have spin. The intermediate resonance, like $K^*$, is not scalar—it has spin.

Spin causes inhomogeneity in angular distributions and decay spectra.

Angular distribution is a powerful tool to understand particle properties. It measures spin, parity, and other quantum numbers.

Higher-spin particles produce bumpier angular distributions. Scalar particles produce no asymmetries.

In the rest frame of the decay, examining the ratio of aligned kinematics reveals spin information.

For most discovered particles, quantum numbers are unknown. We find them as bumps, then determine quantum numbers via angular distributions.

Often, it’s as simple as looking for minima or nodes in the Dalitz plot. Nodes indicate spin: one node for spin-1, two for spin-2, etc.

For non-scalar particles, it’s more complicated. The proton has spin-½; kaon and pion are spin-0. The $\Lambda_c$ has spin-½ like the proton.

If we don’t polarize the initial state or measure the final spin, everything is averaged. No minima or nodes remain—just smeared distributions.

### Rotations, Spin Projections, and Wigner $D$-Functions in Quantum Systems


A particle with spin can have $2J + 1$ projections to the quantization axis.
Consider a particle with spin $J$.
There is a $z$-axis that quantizes the spin, and this $z$-axis measures the projection $J_z$.
The state $|JM\rangle$ can be thought of as a vector with $2J + 1$ components.
All operators in this case are matrices that act on these vectors, producing either the same state with an eigenvalue or a mixture of states.

When a rotation acts on the state, it produces not a single state but a mixture of states.
In classical physics, rotating a vector in space can align it to a specific projection, but in quantum mechanics, this is not the case.
Most rotations result in a superposition of all possible states.

The coefficients for these superpositions are tabulated and known as **Wigner $D$-functions**.
Let me be more concrete.
I will rotate about the $Y$-axis.
The coordinate system consists of $X$, $Y$, and $Z$, forming a right-handed triple.
I will rotate the state $|JM\rangle$ about the $Y$-axis.

The operator $J_+$ is represented as $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, and $J_-$ is $\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$.
The $J_y$ operator has zeros on the diagonal and off-diagonal elements above and below.
To apply the rotation, we take the matrix exponential of $J_y$.
This is already computed, and the coefficients $C$ depend on the initial state, which is why the indices $JM$ are kept in the notation.

For example, suppose we have a spin-1 particle initially perpendicular to the $Y$-axis and rotated by 30 degrees.
The resulting state will be a superposition of $|JM\rangle$ states aligned along the $Y$-axis.
The Wigner $D$-functions provide the coefficients for this superposition.

The general form of the $D$-function for any rotation $R$ is given by Euler angles.
In particle physics conventions, we first rotate by $\phi$ about the $Z$-axis, then by $\theta$ about the $Y$-axis, and finally by $\gamma$ about the $Z$-axis again.
This sequence describes any orientation in space.
The $D$-function decomposes into three parts, with the most complex part coming from the $Y$-axis rotation.
The $Z$-axis rotations introduce simple phase factors:

$$
D^J_{M'M}(\gamma, \theta, \phi) = e^{-i\gamma M'} d^J_{M'M}(\theta) e^{-i\phi M}.
$$

---

::: callout-note
**Key Formula**: The Wigner $D$-function for a general rotation (Euler angles $\alpha, \beta, \gamma$) is:
$$
D^J_{M'M}(\alpha, \beta, \gamma) = e^{-iM'\alpha} d^J_{M'M}(\beta) e^{-iM\gamma}.
$$
:::
---

Let’s take a simple example: spin-1/2.
If I rotate the state $|1/2, 1/2\rangle$ by 30 degrees about the $Y$-axis, the result is a superposition of $|1/2, 1/2\rangle$ and $|1/2, -1/2\rangle$.
The coefficients for this rotation can be found in the same tables as the Clebsch-Gordan coefficients, as both are related to the $SU(2)$ group.

For $j = 1/2$, the $D$-matrix is:

$$
D^{1/2}_{m'm}(\theta) = \begin{pmatrix} \cos(\theta/2) & -\sin(\theta/2) \\ \sin(\theta/2) & \cos(\theta/2) \end{pmatrix}.
$$

For 30 degrees ($\theta/2 = 15^\circ$), the coefficients are $\cos(15^\circ)$ and $\sin(15^\circ)$.

---

- Can you compute any rotation of the spin projection?
- The convention is important—note the minus sign.
- If you want to compute the matrix exponential yourself, you can use Python or Julia.
- Alternatively, you can look up tabulated $D$-functions, but be cautious with software like Mathematica, as it may use different conventions.
- Wikipedia is reliable for checking conventions.
- The $D$-functions are correctly implemented in SymPy (Python) and ROOT.

---

What we’ve discussed so far is about rotations and the rotational group, not weak or strong interactions.
This is remarkable because angular distributions in particle decays are determined by **rotational symmetry**, not by the details of the interactions.
The only input from strong interactions is the preference for certain spin states.
The decay asymmetries and kinematics are governed by the quantum group properties.
This allows us to construct general formulas for decay chains and predict angular distributions.

---

Now let’s model the "blob" in the decay process.
Assume a cascade decay where the initial particle decays into an intermediate particle $X$ with spin $J$, which then decays into particles 1 and 2.
The amplitude involves summing over intermediate spins and depends on the dimensions:

$$
(2j_0 + 1) \times (2j_1 + 1) \times (2j_2 + 1) \times (2j_3 + 1).
$$

If a particle has spin 0, its dimension is 1.

The general formula for the amplitude has two parts:

1. A model-independent part from rotational symmetry.
2. Dynamics-dependent terms $H$ from weak, strong, or electromagnetic interactions.

The $H$ terms encapsulate the physics of the interactions, while the rest is determined by rotational properties.
The helicity states $\lambda$ are defined with spin quantized along the direction of motion.

---

Consider particle $X$ with spin projection $\lambda_X$.
When it decays into particles 1 and 2, the quantization axis must be adjusted to match the decay direction.
This adjustment is done by rotating the spin state of $X$.

In aligned kinematics (where $\phi = \theta = 0$), the rotation simplifies.
The amplitude reduces to:

$$
A = \sum_{\lambda_X} H_{\lambda_0 \lambda_X \lambda_3} \cdot D^{J_X}_{\lambda_X, \lambda_1 - \lambda_2}(\theta, \phi) \cdot H_{\lambda_X \lambda_1 \lambda_2}.
$$

For zero angles, the $D$-function becomes a delta function $\delta(\lambda_0 - (\lambda_X - \lambda_3))$, enforcing angular momentum conservation.

---

To predict angular distributions, we need the values of $H$.
Often, these are approximated as constants in initial analyses.
The differential decay rate is:

$$
\frac{d\Gamma}{d\cos\theta} \propto |A|^2.
$$

The distribution can be flat, parabolic, or another shape, depending on the spin.

Experimentally, we measure $|A|^2$ averaged over initial and final spins.
To analyze data, we project the distribution onto Legendre polynomials, a technique called **partial wave analysis**.
This helps extract information about the underlying dynamics without knowing $H$ explicitly.

---

::: callout-tip
**Practical Note**: For further reading on canonical vs. helicity states, refer to Chapter 4 of Martin Spearman’s *Elementary Particle Theory*.
:::
---

Finally, here’s an exercise:
I’ve provided Dalitz plots from CLEO and BaBar without labels.
Your task is to identify the decays based on kinematics.
The axes are labeled, but the particles are not named.
Use your knowledge of kinematics to deduce the masses and possible decay channels.

### Addressing an Issue and Scheduling Follow-Up



::: callout-note
*This portion of the transcript appears to be administrative dialogue about scheduling and materials distribution.*
:::

- **Speaker 1:** I have to leave because I have an issue.
- **Speaker 2:** You don't want to take it? No.

*Exchange about assignments:*

- **Speaker 1:** It's a kind of homework.
- **Speaker 2:** Oh, sorry.

*Follow-up arrangement:*

- **Speaker 1:** Okay, come with me and I'll give it to you from my office.
- **Speaker 1:** And you guys as well.

*Closing remarks:*

- **Speaker 1:** Thanks a lot for coming, and sorry for being slightly late.
- **Speaker 1:** Will you have time tomorrow at 8am? Leave.

