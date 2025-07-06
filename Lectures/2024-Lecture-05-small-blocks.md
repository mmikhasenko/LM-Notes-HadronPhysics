### Kinematics of Two-Body Scattering and Mandelstam Variables


Today we are at **lecture number five**.
We'll discuss **angle distributions** and **partial wave analysis**.
But before going there, I would like to start with a recap.

---

In the last lecture, we discussed:
- The **phase space** for particle reactions
- Different **experiments** and their **kinematics**
- A list of experiments worldwide studying **hadrons**, their **production mechanisms**, and peculiarities

---

And we start with a recap on **kinematics**.
The first question: *How many variables does one need to describe the two-body scattering process?* We have two problems:

1. **Scalar particles** (e.g., 0-minus scalars):
- Initial state: Two 0-minus scalar particles
- Final state: Two 0-minus scalar particles

2. **Particles with spin**:
- Example: $\pi^+$ scattering (0-minus from 0-minus to 3-minus and 1-plus)

> [!NOTE]
> The scattering process is represented by a "blob" indicating strong interaction dynamics. This is a **unitarity diagram** (not a Feynman diagram), where arrows show particles entering/leaving the interaction.

---

Then I ask you to calculate the **number of variables** needed to describe the process entirely—the **full kinematics**.
- The blob's content (EM, strong, gravity) doesn't affect the answer.
- Two cases:
- **(A) Particles without spin**
- **(B) Particles with spin**

For **(C)**, give an example of variables fully describing the process.

---

**Student Discussion**:
- Vivian's calculation:
- Start with $2 \times 2 \times 3 = 12$ (kinematic degrees of freedom).
- Subtract 4 (conservation laws) → 8.
- Subtract 6 (3 rotations + 3 boosts) → **2 variables**.

For **(B)**, the answer is also **2 variables**, though spin introduces more amplitudes (e.g., 21 for spin-3 × spin-1).

---

**Key Variables**:
The process is fully described by **Mandelstam invariants**:
- **$S$ (s-channel)**:
$$
S = (P_1 + P_2)^2 = (E_1 + E_2)^2 - (\vec{p}_1 + \vec{p}_2)^2
$$
- **$T$ (t-channel)**:
$$
T = (P_1 - P_3)^2 = (E_1 - E_3)^2 - (\vec{p}_1 - \vec{p}_3)^2
$$

> [!IMPORTANT]
> - $S$ and $T$ are **Lorentz-invariant**—frame-independent.
> - For spinless particles, the amplitude is a **scalar function** of $S$ and $T$.
> - With spin, amplitudes become higher-rank objects (e.g., 21D for spin-3 × spin-1), but still depend on **the same two variables**.

---

**Henrik's Example**:
- Variables: Mass of particle pairs (e.g., $(P_1 + P_2)^2$ and $(P_1 - P_3)^2$).
- Mass computation:
$$
m^2 = E^2 - \vec{p}^2
$$

**Clarification**:
- Mandelstam variables are **standard** because they avoid frame-specific descriptions.
- "Invariant" is the correct term (despite dictionary quirks!).

---

**Final Notes**:
- Decays of final-state particles (e.g., unstable 3-minus/1-plus) introduce more variables, but for 2-to-2 scattering, **two variables suffice**.
- The amplitude’s **dimensionality** scales with spin combinations but remains a function of $S$ and $T$.

### Variables and Kinematics in Three-Body Decay and the Dalitz Plot


**Example of Kinematic Variables:**
Give an example of these sets of variables. We've got one from Hendrik. Everyone should get their favorite. Ilya, what's your favorite?

- **S, S and T.**
No, not a single pair. These sets. We need two variables to describe the process.

**Choosing Independent Variables:**
What are your favorite two variables? Oh, this is. What's your second favorite? What is the third variable? Why third? Why do you talk about third? Just introduce something new. Let's introduce. Give us. What about you? Sorry, I forgot your name. Sven. Please.

- **P2 minus P4 is 5.**
It's called $U$ and it's also variable $P$. Oh, $P_2 - P_4$. It's the same. Oh, sorry. So it's $P_2 - P_4$.

$$
P_2 - P_4 = P_1 - P_3
$$

So it's $P_1 - P_4$. $P_1 - P_4$ squared is called $U$. And this is the same as. If I do the algebra, you find out that there are only two independent.

> [!NOTE]
> The Mandelstam variable $U$ is defined as $(p_1 - p_4)^2$ and is related to $S$ and $T$ via the constraint $S + T + U = \sum m_i^2$ for a 4-particle system.

**Favorite Variable Sets:**
So your favorite set is $S$ and $U$, and they're equivalent because $U$ is a linear combination of $S$ and $T$. Fine. Sometimes you take $T$ and $U$. No, no, no. Let's do different center-of-mass energy and angle. That's a really good choice. That's probably gonna be my favorite.

**Center-of-Mass Energy and Angle:**
And this is actually $\sqrt{S}$. Center-of-mass energy and then the angle. How do you define the angle? You go to the center of mass and then you make particle. Center of mass is often referred to as center of momentum as well.

In the center-of-momentum frame, it's just easier to call it **center of momentum** because you immediately understand that momentum, the total momentum, has to add to zero for all particles.

**Defining the Angle:**
Do you have a $P_1$ here and $P_Q$? What else do we have? How do you define the angle? They are going in this direction and the angle between $P_1$ and $P_3$. The angle between $P_1$ and $P_3$. Essentially this one. That's my favorite. Indeed.

**Momentum Vectors and Kinematics:**
One has to be careful when drawing that because we know that the length of the vectors indicates their momentum. Particle's momentum. For the final state, it's in the center of momentum. We're still in the same frame, so this has to be equal to that. I'm fine with that choice.

**Variable Choices and Phase Space:**
There are no more common choices. But any two variables work if they are not redundant. We can choose $E_1$ in the lab frame, any frame, and then $E_3$ in the lab frame. That's also fine. Any two variables, if they are independent, they characterize the kinematics.

> [!IMPORTANT]
> The phase space for a 3-body decay is flat in the variables $S$ and $T$, expressed as $\frac{dN}{dS \, dT} = \text{constant}$.

One has to be careful. Sometimes you fold your phase space. By introducing a set of variables, you map your phase space in these variables or these variables to another domain. Sometimes this domain is somewhat smaller, it has a folded coverage. This variable, it's not a bijective transformation, but this is advanced to see. I'm going to ask you an example. Got it. It's okay.

---

**Transition to Dalitz Plots:**
Cool. We discussed two-body kinematics. We're going to continue discussing the angular dependence after the Dalitz plot. Let's quickly look—oh, questions here. Shortly before we move, questions on the variables that characterize kinematics. Cool.

The homework we had the exercise on the Dalitz plot, and this is, as I mentioned, a problem that is now entering into our lectures. Part of the course that is specific to hadrons. It's before where we've been overlapping a lot with particle physics. But now, from this lecture and the next couple of lectures, we will have material really specific to hadron spectroscopy and the approach that we use to discuss hadrons.

**Three-Body Decay and Dalitz Plots:**
One of the subjects that we would like to go deeper into is particle representation—essentially three-body decay. The Dalitz plot is the common technique to indicate the dynamics of the particles, the dynamics of the interactions.

In the case of three-body decay, we deal with a similar diagram as before, but now one leg comes in, three legs go out, and what is inside the blob is an interaction. We can pose all the same questions as before: What are the number of variables? But the answer won’t differ because it’s the same number of legs. Essentially, the same number of legs tells you the number of variables.

**Kinematic Variables for Three-Body Decay:**
For a three-body decay, there are two variables that describe the process completely. Once you give me these two variables—$S$ and $T$, or angles, or any other—I should be able to draw the entire kinematics.

$$
S = (p_1 + p_2)^2 = (p_3 + p_4)^2
$$

$$
T = (p_1 - p_3)^2
$$

Remember my analogy of the rigid body: when you print on a 3D printer a blob out of which the vectors are sticking, this is a rigid body that describes a kinematic point. The angles between all vectors are fixed. The lengths of the vectors are fixed. You have the entire setup of the kinematics at a single point in the phase space.

**Visualizing Three-Body Decay:**
The same goes for three-body decay. Just give me two variables, and I should be able to draw you how the decay looks like in the center of mass.

In that case, I have to draw here two vectors that leave. And in that case, I'm going to draw the three vectors. Essentially, this is the support out of which the vectors stick. The vectors determine the angles and lengths of the vectors, and that’s it—that’s what you have.

**Mandelstam Variables for Decay Kinematics:**
Now, $S$ and $T$ are defined in a similar way, but now we have different particles in the final state. From that kinematics to this kinematics, what it takes is to take one leg and swap it to the other side. It’s done by changing the sign on the momentum.

So, for three-body decay, what we do—let me define it here:
- $S = (p_1 + p_2)^2 = (p_3 + p_4)^2$,
- and $T = (p_1 - p_3)^2$.

I noticed that there was a typo: $p_1$ is the particle that decays. In that case, I don’t know—should I change it? For now, let me stick to the notations that relate to kinematics.

**Phase Space Properties:**
It’s important to realize that the phase space for three-body decay is flat in the variables—it’s actually constant in the variables $(3,4)$ and $(2,4)$. In $S$ and $T$, we write it as $\frac{dN}{dS \, dT}$. Still, everything didn’t miss much.

### Recursive Phase Space Formulas and Mandelstam Invariance in Three-Body Decays


So this is the **recursive formula** that we discussed in the last lecture.
It's easy to use this equation to demonstrate that once you substitute the two phase spaces and apply the proper Lorentz transformation, you end up with the factor \(\frac{1}{(8\pi)^2}\).
This comes from the two phase spaces: \(2\pi\) for each.

From the first phase space—from that decay—you get the **two-body phase space factor**:
$$
\frac{1}{8\pi} \cdot \frac{2p}{\sqrt{s}}
$$

These are **two-body phase spaces**.
From the other, you have this phase space \(\times 2\pi\), and both have the same form:
$$
\frac{1}{8\pi} \cdot \frac{2p}{\sqrt{s}}
$$

What also comes is that every phase space has a **general phase space element** (with angular dependence):
$$
\frac{1}{2\pi} \cdot \frac{1}{(8\pi)^2} \cdot \frac{2p}{\sqrt{s}} \cdot \frac{d\Omega}{4\pi}
$$

That's easy to remember because it's \(\frac{1}{8\pi}\) in the asymptotic limit.
These things approach unity at high energy, and that's a unit integral.
That's what we discussed already.

---

For both of them, you put this expression.
For one of them, the cosine \(\theta\) is described in terms of the cosine of the scattering angle.
Essentially, you express \(m_{34}\) (or whichever mass you want) in terms of the cosine of the scattering angle.

These \(\frac{2p}{\sqrt{s}}\) terms appear here, and you must replace \(E'\) by \(p\).
This appears as a Jacobian, but I think I was incorrect earlier—I never used that properly.

---

We arrived at this in a few lines without details, but I hope we can fill in the details later.
It comes through the exercises.
Evaluating the phase space comes up several times during the course.

> [!IMPORTANT]
> For the three-body case, using the **recursive phase space formula**:
> $$
> d\Phi_n = d\Phi_k \times d\Phi_{n-k+1} \times \frac{dm^2}{2\pi}
> $$
> shows that the Jacobian for the transformation is constant—the Jacobian for transforming the three-body phase space into paired mass variables is constant.

There is no extra dependency.
This means when we look at the differential width or cross section against these variables, there’s no extra stretching or density increase due to the choice of variables.

---

We have several choices, but only **Mandelstam invariance** gives an undistorted representation of the density.
If you plot differential widths against \(m_{34}^2\), \(m_{24}^2\), or \(m_{23}^2\), it will be a constant numerical value with no rescaling.

That’s why representing three-body processes in **Mandelstam variables**:
$$
s_{ij} = m_{ij}^2 = (p_i + p_j)^2
$$
(or linearly related invariants) is so powerful: you see directly the content of the blob—what happens in the interaction.

That’s essentially what the **Dalitz plot** is, where the density is constant:
$$
\frac{d^2\Gamma}{ds_{12}ds_{23}} = \text{constant}
$$

---

The discussion emphasizes how these formulas relate to **Lorentz invariance**, **Jacobian transformations**, and the utility of **Mandelstam variables** in representing undistorted decay distributions.

### Charm Quark Decay in \(\Lambda_c\) Baryon: Kinematics and Dalitz Plot Analysis


You can see the example of the triple decay that I have here of the $\Lambda_c$ baryon going to the proton, kaon, and pion.
We measure $\Lambda_c$ produced in proton-proton collisions or any other collisions.
In the **BES experiment** and **Belle experiment**, they observe $\Lambda_c$.
This is one of the sorts of particles that lives a **long time** and is produced **abundantly**.

---

Particles with charm ground states are produced abundantly, and they live sufficiently long to fly from the primary vertex.
We reconstruct them, which is why we have a good sample and a good understanding of their decay **kinematics**—and **dynamics** as well, the content of this blob.

---

In that decay, you see there is a charm quark in the initial state and no charm quark in the final state, indicating this happens via **weak interaction**.
The charm quark disappears between the initial and final states.
The charm quark decays, transitioning into the strange quark that ends up in the kaon:

$$
c \to s + W^+ \quad \text{(followed by } W^+ \to u\bar{d}\text{)}
$$

This $c \to s$ transition happens within one generation and is **not suppressed**—it’s an allowed process.

---

> [!IMPORTANT]
> This is the **golden channel** for registering because, in the final state, you have three charged particles: proton, kaon, and pion.
> There are **no neutrals**.
> The proton is a nice charged particle—it travels, it's stable.
> The kaon and pion are stable in our experiments.

They fly out from the decay without any distraction, and we see the tracks clearly through all detectors.
We observe them pointing away from the primary interaction.

---

There is around a **10-millimeter shift** in $\Lambda_c$ flight distance between the primary and secondary vertices—roughly one centimeter.
This is due to the boost and time dilation:

$$
\tau = \gamma \tau_0, \quad \gamma = \frac{E_{\Lambda_c}}{m_{\Lambda_c}}
$$

$\Lambda_c$ in the lab frame lives longer than in its rest frame because it’s produced with **high energy** (few hundred GeV) in proton-proton collisions at the LHC.
This is a **super nice decay**, and we studied it extensively.

---

Here is the experimental result of the analysis, which matches the data closely.
If I showed you the actual data, you wouldn’t distinguish it from this plot because the statistics are so high that the distribution is very smooth.

- **X-axis**: Invariant mass squared of the proton and kaon:
$$
m_{pK}^2 = (p_p + p_K)^2
$$

- **Y-axis**: Invariant mass squared of the kaon and pion:
$$
m_{K\pi}^2 = (p_K + p_\pi)^2
$$

---

All allowed kinematic values for the decay are shown in color.
The white area around it represents **forbidden kinematics** where energy-momentum conservation fails:

$$
p_{\Lambda_c} = p_p + p_K + p_\pi
$$

If I select a point inside the plot, I can compute angles between particles and reconstruct the kinematic configuration.
But for points in the white area, **energy conservation cannot be satisfied**—that’s why the range of possible invariant masses is limited.
This surface is called the **Dalitz plot**, and it’s how we explore decay kinematics.

---

Different colors on this plot indicate different **probabilities** for the decay to occur.
We measure the decay, reconstruct the particle tracks, and identify the kinematic point because there’s a direct mapping between four-vectors and Dalitz plot positions.
Certain kinematics are **more probable** than others—particles prefer specific directions.

For this decay, there are **two dominant configurations**:
1. One is longer (rarer),
2. The other is more common.

You can identify these by looking at the borders of the plot.
Here’s the hint: particles align in one line on the border.
Inside the surface, they always have an angle, but at the border, they become **collinear**.
Think about how you maximize the invariant mass and where this point lies.

---

> [!NOTE]
> The Dalitz plot intensity is proportional to the matrix element squared and phase space factors:
> $$
> \frac{d\Gamma}{dm_{pK}^2 \, dm_{K\pi}^2} \propto |\mathcal{M}|^2 \times \text{Phase Space}
> $$
> This explains the color gradients observed in the plot.

---

### Maximizing and Minimizing Mass in Three-Body Decay Kinematics


Any thoughts? I think you should be in the bottom right because we should maximize the mass of the PK system. There are three momenta going out, and my idea was that the three momenta are in opposite directions. The three-momentum of the sum should be as small as possible.

If we add both momentum vectors, the forward momentum—the sum of the squares—should be as large as possible. So we should be on the right of our diagram. Then, if we apply and find... The same direction should be on the lowest.

You argue that this mass, on the y-axis, should be as small as possible. Why? Because the three momenta are in line, and we subtract them. My way of thinking is this: if you boost to the rest frame of the K and π, they fly next to each other. Their relative momentum is small. If you boost to their rest frame, they might both be at rest, and their mass would just be the sum of the masses. So it's minimal.

> [!NOTE]
> **Minimal Mass Configuration**:
> When particles are collinear (e.g., $K$ and $\pi$ back-to-back), the minimal mass is:
> $$
> m_{K\pi,\text{min}} = m_K + m_\pi
> $$

What you're saying is correct. We are looking for the minimal mass of the kinematic system. Let's figure out what this point corresponds to. There is a kinematic configuration where two particles with maximal momentum are at rest and go in opposite directions. That corresponds to this point.

---

This plot is from experimental data. In the experiment, we would reconstruct such a case because we would not detect the proton. This is the lab frame, but the center-of-momentum frame is where everything is boosted. Even though the proton is at rest in the lab frame, it's already boosted.

This point is the maximum mass. The particles have maximum momentum and go back-to-back, so this is the maximum mass. The other point minimizes the mass.

> [!NOTE]
> **Maximal Mass Configuration**:
> The maximal mass occurs when particles have maximal relative momentum:
> $$
> m_{K\pi,\text{max}} = \sqrt{(E_K + E_\pi)^2 - (|\vec{p}_K| - |\vec{p}_\pi|)^2}
> $$

---

For the three-body decay, there is a similar approach. The standard way to define the angle is to boost into the rest frame of a pair. Let me show you the setup. I’ll use proton, K, and π. I want to fix the mass of the K-π system and explore how it changes without altering the proton's mass.

The way to think about this is to take the setup in the center-of-momentum frame and boost to the K-π rest frame. In this frame, they go back-to-back. In the center-of-momentum frame, three particles are arranged such that the sum of their three-momenta is zero.

After boosting, the Λ_c has non-zero momentum, and the K and π also have non-zero momentum. But since we are in the K-π rest frame, their momenta add to zero. If we fix the mass of the system and explore phase space along a line where the pair's mass is fixed, the length of these vectors is fixed. What changes is the angle θ.

We can explore the full range of θ from 0 to π. At one corner, θ = 0, and at the other, θ = π. The right should correspond to θ = 0, and the left to θ = π.

---

In this setup, the proton and K-π go in opposite directions, giving the maximum mass of the proton-K system. For our new setup, since the length of all vectors is fixed, we can only rotate them.

The dependence of the mass of two particles on θ is such that a larger angle gives a larger mass. For the proton-K system, θ = 0 gives a very high mass, while θ where they are nearly in the same direction gives a small mass.

> [!NOTE]
> **Angle-Dependent Mass**:
> The proton-$K$ mass depends on angle $\theta$ as:
> $$
> m_{pK}^2(\theta) = (E_p + E_K)^2 - \left(|\vec{p}_p|^2 + |\vec{p}_K|^2 - 2|\vec{p}_p||\vec{p}_K|\cos\theta\right)
> $$

---

We can do the same with the other half. Let me fix the mass of the proton-K system again. The most straightforward analysis is to go to the proton-K rest frame, where everything is fixed, and scan along this line by changing the angle of the pair.

The lines describe setups where you change the angle in one frame or another. There is also a third variable in 2-to-2 scattering, called U, which is symmetric. For three particles, there is the mass of the pion-proton system, but it's not evident.

If I fix the mass of this system and scan the angle, the U variable is a linear combination of the two masses. It’s a diagonal in this plot. This line represents the fixed mass of the pion-proton system, and we move from one corner to another, changing the representation.

The representation used in experimental analyses for the Dalitz plot has the mass of one pair on the x-axis and the other on the y-axis. In the homework, you’ll see a more symmetric Dalitz plot where all variables enter symmetrically.

This uses properties of an equilateral triangle: the sum of the distances from any point inside to the sides is constant. The masses are represented as distances to the sides, giving a symmetric representation.

This is equivalent to the standard plot but skewed. To relate Cartesian coordinates to the heights of the triangle, we use $\frac{\sqrt{3}}{2}$ due to the 60° angles.

---

The symmetric representation is nice, but the standard one is easier to plot. Both represent kinematics, and we see points where the density increases. The goal is to understand whether the plot shows dynamics and what processes guide the interaction.

Looking ahead, we’ll see that Λ_c decay isn’t just to three particles but proceeds via intermediate resonances. Two particles form a short-lived state, increasing the decay probability. If the energy matches a certain range, the interaction is more likely, and the probability increases.

### Resonances and Kinematic Structures in Two-Particle Systems


You might have seen **cross sections** for the two-particle resonances. That has a **bump** in it known as the **hadronic resonance**. The physics of that is you have a system of two particles, and the **quantum numbers** of the system match the quantum numbers of some other resonance.

By adjusting the **energy** of the system, you explore how the system behaves—how likely two particles are to interact at a certain energy. If there is an **intermediate resonance**, this system can resonate at this energy, and the **probability** is going to increase once you pass through the resonance region. This is described by the **Breit-Wigner formula**:

$$
\sigma(E) = \frac{\pi \hbar^2}{2\mu E} \frac{\Gamma^2}{(E - E_0)^2 + (\Gamma/2)^2}
$$

where:
- $E_0$ is the **resonance energy**
- $\Gamma$ is its **width**

---

This leads to the appearance of the **bent structures** in the Dalitz distribution, or if you project it onto one of the axes, you're going to see the **resonance-like shape**. These bent structures can be identified on both.

This is a **cool example** that I brought because there are resonances in all three pairs. There are resonances in these two particles. These two particles interact.

> [!NOTE]
> **Why is there a bigger probability increase when the kaon and pion are near resonance?**
> The $K$ and $\pi$ also show this, like on the right side, but not only the two lines on the left side.

---

Let's understand the **lines**. We will come back to that in two lectures, but let's quickly identify them now. All **horizontal lines**—which resonances are these? In which mass distribution? This is going to give us a **peak**.

Looking at the **blue plot**, the horizontal lines correspond to **fixed mass** for the $K\pi$ system. When the mass approaches a certain value, it reaches the **maximum**. These lines are the resonances in $K\pi$.

**What particle decays to $K\pi$?** $K^*$, the $K^*$ resonance.

---

Now, let's look at the **vertical lines**—in which system? When changing $K\pi$, you scan a certain energy of the system. You can think of this as a **projectile**. These lines correspond to the **fixed mass** of the proton and $K\pi$. By moving along the axis, you're scanning $K\pi$.

If you **expand it**, you see that the lines correspond to the resonances in:
- $K\pi$
- $K\pi$-proton
- $K$

The **third combination** is pion-proton, and these are $\Delta$ resonances.

---

The other plot helps as well because it's nice to see that the lines are **parallel to the sides** of the triangle. This line is the same as this line, parallel to one of the sides. Then you have the $\Lambda$ resonances parallel to another side.

At this point, you can see the $\Delta$ resonance, which is the line over here, parallel to the third side. It's a bit more **tricky** to see the $\Delta$ resonance here, but it's there.

---


**Dalitz Plot Kinematics**:

$$
m_{12}^2 + m_{23}^2 + m_{13}^2 = M^2 + m_1^2 + m_2^2 + m_3^2
$$

where:
- $m_{ij}$ are the **invariant masses** of particle pairs
- $M$ is the **total energy** of the system

---

**Resonance Identification**:

For $K^* \rightarrow K\pi$:

$$
m_{K\pi}^2 = (E_K + E_\pi)^2 - (\vec{p}_K + \vec{p}_\pi)^2
$$

This reconstructs the **invariant mass** of decay products to identify resonances like $K^*$.

Similarly, for $\Delta \rightarrow p\pi$:

$$
m_{p\pi} \approx m_\Delta
$$

when the invariant mass matches the $\Delta$ resonance mass.

### Angular Distributions in Particle Decays and Spin-Dependent Kinematics


One thing to finish and move past this dull spot to our topic today is the **angular distribution**.
I'm going to discuss now the angular distribution for a decay within one band.
Let me look at the phase space resonance here.

As we discussed before, the **kinematics**: when traversing the double plot and phase space from one end to another while keeping the mass of the combination fixed, the angle changes.
This explores different angles, which is precisely the kinematics.

Let me sit in the rest frame of the $K\pi$ where this band is happening and traverse the phase space by changing this angle.
The angle dependence indicates that within the band, there can be **inhomogeneity**.
Even within the band, one edge might have a different probability than the other.

Particles often prefer to be **aligned** rather than perpendicular.
This less probable kinematics happens because particles have **spin**.
The preference appears only because the intermediate resonance, in this case $K$, is not a scalar particle—it has spin.
The spin of particles causes inhomogeneity in angular distributions and in the decay spectrum.

---

> [!IMPORTANT]
> **Key Insight**: Angular distributions reveal spin effects. Particles with spin produce anisotropic decay patterns, while scalar particles ($J=0$) yield uniform distributions.

---

Angular distribution is a **very powerful tool** to understand properties of particles.
As we discussed, it’s how we measure **spin, parity, and other quantum numbers** in particle interactions.

Particles with higher spin produce more **bumpy, spiky** angular distributions, while scalar particles produce no asymmetries or structures.
By examining the angular distribution in the rest frame of the particle decay, one studies the ratio of aligned kinematics to other types.
This allows inference of **spin information**.

For most particles discovered so far, quantum numbers are not initially known.
We find them as bumps in the spectrum, and the next step is determining their properties through angular distributions.
Often, it’s as simple as looking at the **Dalitz plot** and checking for minima or structures in the angular distribution.

**Maxima and nodes indicate spin for scalar final-state particles**:
- One node means **spin 1**.
- Two nodes mean **spin 2**.
- Three nodes mean **spin 3**.
The intensity vanishes at these nodes—the **dark spots**.

For **non-scalar particles**, which are more common, the situation is more complicated.
Here’s a quick check of spins:
- The proton has spin $\frac{1}{2}$.
- Kaon and pion (except scalars) have spin $0$.
- The spin of $\Lambda$ is the same as the proton.

However, with **unpolarized initial states** and unmeasured final spins, the distribution averages out.
For example, if you consider a specific spin projection of $\Lambda_c$ and proton, you’d see nodes and zeros in the angular distribution.
But without polarization or spin measurement, everything averages, smearing out minima and nodes.

---


1. **Angular distribution for spin-1 particle**:
$$
\frac{d\Gamma}{d\cos\theta} \propto 1 + \alpha \cos^2\theta
$$
where $\alpha$ encodes **spin alignment preferences**.

2. **General spin-$J$ decay distribution (scalar final states)**:
$$
\frac{d\Gamma}{d\cos\theta} \propto |P_J(\cos\theta)|^2
$$
where $P_J$ is the **Legendre polynomial** of order $J$, producing $J$ nodes.

3. **Dalitz plot intensity (spin-dependent decays)**:
$$
I(m_{12}^2, m_{23}^2) \propto \left| \sum_{J} A_J(m_{ij}^2) P_J(\cos\theta_{ij}) \right|^2
$$
where $A_J$ are **spin-dependent amplitudes**.

4. **Spin averaging effect (unpolarized initial states)**:
$$
\left\langle \frac{d\Gamma}{d\Omega} \right\rangle = \frac{1}{2s+1} \sum_{m_s} \left| \mathcal{M}_{m_s}(\theta,\phi) \right|^2
$$
where $s$ is the initial particle’s **spin**.

---

*Note*: The number of **nodes** in the angular distribution directly correlates with the spin $J$ of the decaying particle. This is a cornerstone of **spin determination** in particle physics.

### Spin Projections, Rotation Operators, and Wigner \(D\)-Functions


A particle with spin can have \(2J + 1\) projections to the quantization axis.
Let me consider a particle that has spin \(J\).
There is a \(z\)-axis that we use to quantize the spin, and this \(z\)-axis measures the projection \(J_z\).
One can think of the state \(|JM\rangle\) as a vector with \(2J + 1\) components.

> [!NOTE]
> The **dimension** of the spin state space is given by:
> \[
> \text{Dimension} = 2J + 1
> \]
> where \(J\) is the total spin quantum number.

All operators in this case are matrices that act on these vectors, producing either the same state with a certain eigenvalue or a mixture of states.
When I act with the rotation operator on the state, I produce not a single state but a mixture of different states—it's as simple as that.

If this were a vector in regular space, I could adjust it to have exactly a certain projection.
But in quantum mechanics, it doesn't work this way.
When you rotate the state, most of the time you end up with a mixture of all possible states.

The coefficients for these mixtures are tabulated and known as **Wigner \(D\)-functions**.
You can look them up to see what these coefficients are.

---

Let me be more concrete.
I will rotate about the \(Y\)-axis.
I have the axes \(X\), \(Y\), and \(Z\), forming a right-handed coordinate system.
I will rotate the state \(|JM\rangle\) about the \(Y\)-axis.

The ladder operators \(J_+\) and \(J_-\) are represented as matrices:
\[
J_+ = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \quad J_- = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}.
\]
The \(J_y\) operator has zeros on the diagonal and these coefficients above and below.

To apply the rotation, you take the matrix exponential of \(J_y\):
\[
\mathcal{R}_y(\theta) = e^{-i\theta J_y}.
\]
But this is already computed for you, and the results are the Wigner \(D\)-functions.

---

These coefficients depend on the initial state, which is why the indices \(J\) and \(M\) are kept in the notation.
For example, if I say we have a spin-1 state initially perpendicular to the \(Y\)-axis and rotated by 30 degrees, you can look up the \(D\)-functions to find the composition of the state.

The general form of the Wigner \(D\)-function for any rotation is:
\[
D^J_{M'M}(\alpha, \beta, \gamma) = e^{-iM'\alpha} \, d^J_{M'M}(\beta) \, e^{-iM\gamma},
\]
where \(\alpha\), \(\beta\), and \(\gamma\) are Euler angles.

> [!IMPORTANT]
> The **Wigner D-matrix elements** describe rotation transformations:
> \[
> \langle J M' | \mathcal{R}(\alpha, \beta, \gamma) | J M \rangle = D^J_{M'M}(\alpha, \beta, \gamma)
> \]
> where \(\mathcal{R}\) is the rotation operator parameterized by Euler angles \((\alpha, \beta, \gamma)\).

In particle physics, we use the convention where you first rotate by \(\phi\) about the \(Z\)-axis, then by \(\theta\) about the \(Y\)-axis, and finally by \(\psi\) about the \(Z\)-axis again.
This sequence describes any orientation in space.

The most nontrivial part is the \(\theta\) rotation, since rotations about the \(Z\)-axis simply introduce phases.
The small \(d\)-matrix encodes the \(\theta\) dependence:
\[
d^J_{M'M}(\theta) = \langle JM' | e^{-i\theta J_y} | JM \rangle.
\]

This gives the full relationship:
\[
\langle M' | M \rangle (\psi, \theta, \phi) = e^{-i\psi m'} \, d^l_{m'm}(\theta) \, e^{-i\phi m}.
\]

### Rotations in Spin-1/2 Systems and Wigner D-Matrix Applications in Decay Processes


Let’s consider a small example of **spin one-half**.
I'm going to rotate the state $|1/2, 1/2\rangle$ by **30 degrees** about the **Y axis**.
The result will be a combination $|1/2, 1/2\rangle + |1/2, -1/2\rangle$, and I want you to quickly tell me the coefficients.
These coefficients are analogous to the **Clebsch-Gordan coefficients**—they are closely related.
This is about the **SU(2) group**, and you can find the numbers by checking the Clebsch-Gordan tables.

> [!NOTE]
> The Wigner D-matrix for spin-1/2 rotations is:
> $$
> D^{1/2}(\theta) = \begin{pmatrix}
> \cos(\theta/2) & -\sin(\theta/2) \\
> \sin(\theta/2) & \cos(\theta/2)
> \end{pmatrix}
> $$

For a **30-degree rotation** (half-angle = 15 degrees), the upper-left entry is $\cos(15^\circ)$, and the off-diagonal entry is $\sin(15^\circ)$.

---

Now, questions about the **Wigner D functions**:
- Can you calculate rotations for any spin projection? It looks straightforward, but the **convention matters**—note the minus sign.
- If you want to compute this via **matrix exponentiation**, recall that we derived these matrices in previous exercises.
- You can do this numerically using **Python or Julia**—just perform matrix exponentiation on the generator.

> [!TIP]
> For implementations:
> - **SymPy** (Python) and **ROOT** implement Wigner D functions correctly.
> - **Mathematica** uses the opposite convention (plus sign and swapped indices).
> - **Wikipedia** is reliable for checking conventions—search "Wigner D functions".

---

What we’ve discussed so far is purely about **rotations and the rotational group**—not weak or strong interactions.
This is the **fascinating part**: to predict angular distributions, you don’t need detailed interaction physics—just the properties of the rotational group.

Key insights:
- **Angular distributions** are determined by how space rotates, with only minor input from strong interactions.
- **Strong interactions** tell us which spins are preferred, but the decay asymmetries and kinematics come from the quantum group structure.
- This is **remarkable**—it means we can systematically construct any particle decay chain and predict its angular distribution.

---

Now, let’s examine the **"blob"** from the previous slide and model one possible decay process.
We’ll assume the three final-state particles are produced via a **cascade**:
1. The initial particle decays to an intermediate state $X$ (spin $J$).
2. $X$ then decays to particles 1 and 2.

This is a **two-step process** with discrete spin dimensions. The total spin space dimension is:
$$
\text{dim} = \prod_{i=0}^{3} (2j_i + 1)
$$
- If a particle has **spin 0**, its dimension is 1.
- In general, you’ll have many such terms, and the amplitude is written as a sum over intermediate spins.

---

One more point: for simplicity, we’ll **align the system**.
- Particles $X_3$ are distinct resonances.
- Particles 1 and 2 are in the **rest frame of $X$**, while $X_3$ comes from the initial state’s **center-of-momentum frame**.
- This framework generalizes to any cascade decay.

Here’s the **key formula** (we’ll focus on understanding rather than deriving it):
The amplitude has two parts:
1. A **model-independent rotational component**.
2. A **dynamical part ($H$)** from particle interactions (weak, strong, or EM).

The helicity amplitudes are:
$$
\mathcal{A} = \sum_{\lambda_X, \lambda_3} H_{\lambda_X \lambda_3} D^{J}_{m'm}(\theta,\phi) G_{\text{decay topology}}
$$
- $\lambda$ are helicities.
- $D^J$ is the Wigner matrix.
- $G$ describes the decay orientation.

---

The **angular distribution** reflects this separation:
$$
\frac{d\sigma}{d\Omega} \propto \sum |D^{J}_{m'm}(\theta,\phi)|^2 \times |H|^2
$$
- The **rotational part** is calculable.
- The **dynamics ($H$)** must be measured or modeled.

### Spin Alignment and Decay Kinematics of Particle \( X \) in the Center-of-Mass Frame


Let's now look at the particle \( X \).
The particle \( X \) carries the **spin projection** \( \lambda_X \).
It decays to particles 1 and 2, which move at a certain angle relative to the direction of \( X \)'s motion.

To compensate for this angle, one must adjust the quantization axis by rotating the spin vector of \( X \) to align with its decay direction.
This rotation is indicated by the orientation of the decay.

> [!NOTE]
> The rotation is described by the **Wigner D-matrix**:
> \[
> D^{J}_{\lambda,\lambda'}(\theta,\phi)
> \]
> This transforms spin states under rotation.

---

I would like to evaluate this expression in the **aligned kinematics**—where \( \Phi = \theta = 0 \).
In the center-of-mass frame, the expression simplifies.

If the angles are zero, the transformation reduces significantly because no rotation is needed.
The summation over \( \lambda_X \) simplifies because \( X \) is already moving along the \( Z \)-axis.

Thus, we obtain:
\[
\sum_{\lambda_X, \lambda_3} D^{J}_{\lambda_0, \lambda_X - \lambda_3}(0) \cdot D^{J}_{\lambda_1, \lambda_2}(\theta, \phi) \cdot \text{adjustment for } \lambda_X, \lambda_1 - \lambda_2.
\]

---

This yields a **delta function** enforcing spin conservation:
\[
\delta_{\lambda_0, \lambda_X - \lambda_3}.
\]

The only non-zero contribution occurs when the spin states match, meaning:
\[
\lambda_X = \lambda_0 + \lambda_3.
\]

---

The final expression in aligned kinematics is:
\[
H_0 \, D^{J_X}_{\lambda_X, \lambda_0 + \lambda_3}(\theta) \, D^{J_X}_{\lambda_X, \lambda_1 - \lambda_2}(\theta, \phi).
\]

That's it—**as simple as that**.

---

- **Spin projection conservation**: \( \lambda_X = \lambda_0 + \lambda_3 \).
- **Wigner D-matrix** simplifies for \( \theta = 0 \).

### Angular Distributions and Partial Wave Analysis in Particle Decays


**How many numbers do I need from you in order to compute?** I want to think now about electromagnetic interactions, or let me do gravity.
**How many numbers as input do I need from you to predict the angular distribution?** It's essentially here, but it misses fundamental components.

---

**What is inside of the blobs?** What's inside of this block, this blob or this blob and this blob? In order to predict all of my values, I just need this guy and that guy.
So I have a $(2j_1 + 1)(2j_2 + 1)$ values here, which might be functions of particle masses as well—could be masses of $x$.
And then I need a similar number of these guys, but there is a reasonable way to approximate them.

> [!NOTE]
> The term $(2j_1 + 1)(2j_2 + 1)$ represents the **spin multiplicity factor**, where $j_1$ and $j_2$ are the spins of the particles involved. This counts the number of possible spin states.

---

**So essentially, often in the experiment, in the analysis at the first try, we assume that these are actually constant.**
This is the constant, and that contains only particle properties.
Here I'm going to say that this one is constant one or $c$, and this is particle.
And then once I do that, I should be able to compute what the angular distribution is.

---

**In that case, I am going to fix the mass of the one tube and the intensity that I see along the line.**
What is up to now? These two have a $\frac{d\Gamma}{d\cos\theta}$.
So cosine is just better—it has a better Jacobian.
We don't need to have this sine Jacobian for cosine.

---

**That's why often what is looked at is the cosine, and this is going to be the matrix element proportional to the matrix element.**
And this $|M|^2$ is fixed.
This distribution changes from $-1$ to $1$.
So here is the $\theta$ and the $\cos\theta$.
$\theta$ is going to be null here at $-1$.

---

**We scan from $-1$ to $1$, and if it is flat, that's one possibility.**
What you often see, especially when you deal with particles with spin, is such a parabola—a second-order polynomial in cosine:

$$
\frac{d\Gamma}{d\cos\theta} \propto 1 + \alpha \cos^2\theta
$$

Or what you also often see is this.

---

**Notice the difference.**
Well, it's important to acknowledge that what we wrote here, $A$, is the **quantum transition amplitude**.
So it's a probability amplitude.
It's one that is going to be squared to give us the observed probability.
This $G$ is going to appear squared.

---

**In the experiment, we only see the squared value of the amplitude.**
Moreover, often we deal with unpolarized decays.
Therefore, the distributions are also averaged.
So you have to square this thing and sum over the initial spin projections and final spin projections, and then you're going to obtain that in experiment you see this and you wonder: **What does it tell me?**

---

**The first way to analyze that is not to guess the amplitude, but rather to use or acknowledge these angular distributions by projecting onto orthogonal polynomials** because it gives you a nice basis.
And apparently, this basis is the maximum value that you're going to...
You see some functions from $-1$ to $1$, and you can expand this function as any function in the set of Legendre polynomials:

$$
\frac{d\sigma}{d\cos\theta} = \sum_{\ell} a_\ell P_\ell(\cos\theta)
$$

---

**These Legendre polynomials are related to the spin of the particle that is produced.**
And this is what is called **partial wave analysis**.
Or if you project the differential cross section, this is called **moment analysis**.

---

**So the partial wave analysis is a way to guess these $H$ functions, to model your cross section by amplitudes, and let these guys be free parameters.**
And then try to learn what's inside of the blocks by adjusting them to the data.

---

**But as a first step, often what is done is to project angular distributions onto the polynomials, which will not give you the inside of the blocks directly, but some combination of these conditions.**
There is...
This is not straightforward, I believe, and we will have more chance to discuss that.

---

> [!IMPORTANT]
> Key takeaways:
> - The angular distribution $\frac{d\Gamma}{d\cos\theta}$ is central to analyzing particle decays.
> - Legendre polynomials $P_\ell(\cos\theta)$ provide a basis for partial wave analysis.
> - The observed probability depends on the squared amplitude $|M|^2$.

### Helicity vs. Canonical States and Kinematic Decay Exercise


I didn't tell you much about the differences between the **canonical state** that we introduced at the beginning and the **helicity state** that we introduced later.
We only touched a little bit on how the state is defined in the rest frame, and hopefully we'll get to explore more.

> [!NOTE]
> For reference, helicity state transformations typically involve formulas like:
> $|p,\lambda\rangle = U(L(p)) |k,\lambda\rangle$
> where $L(p)$ is the Lorentz boost and $\lambda$ represents the helicity eigenvalue.

I would like to tell you that this book has the best coverage of this subject:
* **Martin Spearman's *Elementary Particle Theory***
* **Chapter Four** is fundamental

It's really fun reading because:
- It starts from the Lorentz group
- Explains how to introduce the vectors
- Includes a little bit of group theory, but in a nice way without heavy details
- Presents concepts *without too much mass*

It's really a good book. So Chapter Four of Martin Spearman's *Elementary Particle Physics* would give you some insights on the particle definitions.

---

I was just going to hand in an exercise:
- There are some **Dalitz plots** from CLEO and BaBar
- I have removed the labels
- I don't tell you which particles are in the final state
- I just tell you that one of them is the $D$ decay, another one is the $D_s$ decay

> [!IMPORTANT]
> Remember that Dalitz plots involve invariant mass calculations:
> $m_{12}^2 = (p_1 + p_2)^2$
> where $p_1$ and $p_2$ are four-momenta of decay products.

You know a lot about kinematics already. The exercise is to:
1. Figure out what decay this is
2. Use the axis labels (still present)
3. Determine the masses from kinematics
4. Guess what the decay is

I have cases:
- One for your group
- Another one to work on
- And the EP one

### Addressing Homework and Scheduling


**Lecture Segment (Logistics Discussion):**

> [!NOTE]
> *This appears to be an administrative conversation about homework distribution and scheduling.*

- **Instructor:**
*"I have some issues and need to leave."*
*"You don't want to take it? No?"*

- **About the task:**
*"It's a kind of homework."*
*"Oh, sorry."*

- **Follow-up instructions:**
*"Come with me, and I'll give it to you from my office."*
*"You guys as well."*

- **Closing remarks:**
*"Thanks for coming, and sorry for being slightly late."*
*"Will you have time tomorrow at 8am?"*

