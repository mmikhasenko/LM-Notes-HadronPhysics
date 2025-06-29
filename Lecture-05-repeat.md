### Angular Distributions, Kinematics Variables, and Dalitz Plots in Two- and Three-Body Scattering



Today we are at lecture number five.
We'll discuss **angular distributions** and **partial wave analysis**.
But before going there, I would like to start with a recap.

---

In the last lecture, we discussed:

- The **phase space** for particle reactions
- Different experiments and their **kinematics**
- A list of experiments worldwide studying **hadrons**, their production mechanisms, and peculiarities

---

We start with a recap on **kinematics**.
The first question: *How many variables does one need to describe the two-particle scattering process?* We have two problems:

1. **Scalar particles** (e.g., 0-minus scalars):
- Scattering of 0-minus → 0-minus, with two 0-minus scalar particles in the final state.
2. **Particles with spin** (e.g., P-plus):
- Scattering of 0-minus → 3-minus and 1-plus.

::: callout-note
The scattering process is represented by a "blob" in diagrams. These are **unitarity diagrams** (not Feynman diagrams), illustrating interactions without specifying dynamics.
:::
---


The question: *How many variables describe the full kinematics?*

- The blob's internal dynamics (strong, EM, gravity) **do not affect** the answer.
- Two cases:
- **(A)** Particles **without spin**
- **(B)** Particles **with spin**

::: callout-tip
For **(C)**, provide an example of a variable combination that fully describes the process.
:::
---

1. Start with **8 variables** (2 particles × 4-momenta, minus 4 conservation constraints).
2. Subtract **6 more** (3 rotations + 3 boosts) due to lack of reference frame.
- Final answer: **2 variables** for **(A)**.

For **(B)**, the answer is also **2 variables**, but the amplitude becomes a higher-rank object (e.g., 21-dimensional for spin-3 × spin-1).

::: callout-important
**Key Insight**: Spin adds more amplitudes, but all depend on the **same two variables** ($s$ and $t$). Decays of final-state particles introduce additional variables, but for pure 2→2 scattering, **two suffice**.
:::
---


The most common choice for kinematic variables:
$$
s = (p_1 + p_2)^2 \quad \text{(center-of-mass energy squared)}
$$
$$
t = (p_1 - p_3)^2 \quad \text{(momentum transfer squared)}
$$
$$
u = (p_1 - p_4)^2 \quad \text{(crossing-related invariant)}
$$
with the constraint $s + t + u = \sum m_i^2$.

::: callout-note
These are **Lorentz-invariant**—they don’t depend on the reference frame.
:::
---


- **Henrik’s choice**: Masses of particle pairs (e.g., $m_{12}^2$, $m_{13}^2$).
- **Sven’s choice**: $s$ and $u$ (equivalent to $s$ and $t$ via linear combinations).
- **Favorite choice**: **Center-of-mass energy** ($\sqrt{s}$) and **scattering angle** ($\theta$).

::: callout-tip
Any **two independent variables** work, but some choices (like Mandelstam) avoid phase-space folding.
:::
---


For **three-body decay**, the kinematics are similarly described by **two variables** (e.g., $s_{12}$ and $s_{23}$).

The **phase space** is flat in these variables:
$$
\frac{dN}{ds_{12} \, ds_{23}} = \text{constant (if no dynamics)}
$$

::: callout-important
**Dalitz plots** visualize dynamics in three-body decays. A uniform distribution implies **no resonant interactions**; deviations reveal underlying physics.
:::
---


For multi-body decays, phase space can be decomposed using:
$$
d\Phi_n = d\Phi_{n-1} \cdot d\Phi_2 \cdot \frac{1}{(2\pi)^3} dp^2
$$

This yields for three-body decays:
$$
d\Phi_3 = \frac{1}{8\pi^2} \frac{2p}{\sqrt{s}} \frac{d\Omega}{4\pi}
$$

::: callout-note
The **Jacobian** for transforming to Mandelstam variables is **constant**, so Dalitz plots directly reflect dynamics.
:::
### Charm Decay Dynamics and Dalitz Plot Analysis of $\Lambda_c \to p K \pi$


You can see the example of the triple decay that I have here of the $\Lambda_c$ baryon going to the proton, kaon, and pion.
We measure $\Lambda_c$ produced in proton-proton collisions or any other collisions.
In the **BES experiment** and **Belle experiment**, they observe $\Lambda_c$.

::: callout-note
The $\Lambda_c$ is one of the particles that lives a long time and is produced abundantly. Particles with charm ground states are produced abundantly, and they live sufficiently long to fly from the primary vertex.
:::
We reconstruct them, which is why we have a good sample and a good understanding of their decay kinematics—and dynamics as well, the content of this blob.

---

In that decay, you see there is a **charm quark** in the initial state and **no charm quark** in the final state, indicating this happens via **weak interaction**.
The charm quark disappears between the initial and final states.
The charm quark decays, transitioning into the **strange quark** that ends up in the kaon.

The $c \to s$ transition happens within one generation, and this is **not suppressed**—it is an allowed process.
This is the **golden channel** for reconstructing because in the final state you have three charged particles—no neutrals.

* The proton is a nice charged particle; it travels and is stable.
* The kaon is stable in our experiments, and the pion is stable.

They fly out from the decay without any distraction, and we see the tracks clearly through all detectors.
We observe them pointing away from the primary interaction.

---

There is around a **10-millimeter shift** in $\Lambda_c$ decay vertices between the primary and secondary vertex—roughly one centimeter.
This is due to the boost and the fact that $\Lambda_c$ in the laboratory frame lives longer than in its rest frame.

$$
\Delta x = \gamma v \tau_0 \approx \text{10 mm (observed)}
$$

where $\gamma = E_{\Lambda_c}/m_{\Lambda_c}$ is the Lorentz factor.

It has a few hundred GeV when produced in proton-proton collisions at the LHC.
This is a super nice decay, and we’ve studied it extensively.

---

Here is the experimental result of the analysis, which resembles the data.
If I showed you the actual experimental data, you wouldn’t distinguish it from this plot because the statistics are so high that the distribution is very smooth.

* **X-axis**: Mass of the proton-kaon system $m_{PK}^2 = (p_P + p_K)^2$.
* **Y-axis**: Mass of the kaon-pion system $m_{K\pi}^2 = (p_K + p_\pi)^2$, covering all allowed values for the decay.

The colored region shows kinematically allowed configurations, while the white area corresponds to forbidden kinematics.

If I select a point inside the plot, I can compute the angles between particles and reconstruct the kinematics.
But if you ask about the white area, I’d find that energy is not conserved—those points are impossible.
The range of possible values for invariants is limited, and this surface is called the **Dalitz plot**.

---

Different colors on this plot indicate different probabilities for the decay to occur.
We measure the decay, reconstruct the particle tracks, and determine the kinematic point since there’s a direct relation between four-vectors and the kinematics.
Certain kinematics are more probable than others—particles prefer specific directions.

For this decay, some configurations are rarer than others.
You should be able to identify this pattern in the plot.
Here’s the hint: particles are aligned in one line on the border of the plot.
Inside the surface, they always have an angle between them, but on the border, they are collinear.
Think about how to maximize the mass and where this point lies.

---

Any thoughts? You should look at the bottom right.
To maximize the mass of $PK$, consider the three momenta in opposite directions.
The sum of the momentum vectors should be as small as possible.
If you add them, the forward momentum—the sum of the squares—should be as large as possible.
So we should be on the right side of the diagram.

For the minimal mass, the three momenta are aligned, and we subtract them.
If you boost to the rest frame of $K$ and $\pi$, they fly next to each other with small relative momentum.
In their rest frame, they might both be at rest, so their mass would just be the sum of their masses—this is the minimum.

We are looking for the minimal mass of the kinematics.
This point corresponds to the case where two particles have maximal momentum and go back-to-back.
This plot is from experimental data, and we reconstruct this in the lab frame where everything is boosted.
Even if the proton is at rest in the lab frame, it’s already boosted.
This point is the maximum mass, where particles go back-to-back.

---

For three-body decay, we define the angle similarly.
Let me fix the mass of the $K\pi$ system.
In the center-of-momentum frame, I have three particles with zero net momentum.
If I boost to the $K\pi$ rest frame, they go back-to-back.
The length of the vectors is fixed, and only the angle $\theta$ changes.
I explore the full range of $\theta$ from $0$ to $\pi$.

The right side corresponds to $\theta = 0$, and the left to $\theta = \pi$.
For the proton-$K$ system, $\theta = 0$ gives a high mass, while $\theta \approx \pi$ gives a small mass.
The same logic applies to the other pair.

There is a third variable in 2-to-2 scattering called $U$, but for three particles, it’s symmetric.
If I fix the mass of one system and scan the angle, the $U$ variable is a linear combination of the other two.
This line represents the fixed mass of the $\pi p$ system.

---

The standard Dalitz plot uses $m_{PK}^2$ and $m_{K\pi}^2$ on the axes.
A more symmetric representation uses an equilateral triangle, where distances to the sides correspond to masses.
This is a linear transformation of the standard plot, involving $\sqrt{3}/2$ due to the 60° angles.

The goal is to understand the dynamics—why certain kinematics are more probable.
In future lectures, we’ll see that intermediate resonances enhance the decay probability.
Two particles briefly form a resonance, increasing the likelihood of decay at specific energies.

---

You’ve seen cross sections for two-particle resonances with bumps indicating hadronic resonances.
If the quantum numbers match, the system resonates at certain energies, increasing interaction probability.
This creates structures in the Dalitz plot—projecting them shows resonance-like shapes.

In this decay, resonances appear in all three pairs:

- **Horizontal lines**: Resonances in $K\pi$ (e.g., $K^*$).
- **Vertical lines**: Resonances in $pK$.
- **Diagonal lines**: Resonances in $\pi p$ (e.g., $\Delta$).

The symmetric plot shows these as lines parallel to the triangle’s sides.
The angular distribution within a resonance band reveals spin effects.
If I fix $m_{K\pi}$ and vary $\theta$, the probability changes because the intermediate resonance (e.g., $K^*$) has spin.
Particles prefer certain alignments—this inhomogeneity comes from spin.

The decay rate depends on the angle as:

$$
\frac{d\Gamma}{d\cos\theta} \propto 1 + \alpha \cos^2\theta
$$

where $\alpha$ depends on the resonance spin.
This explains why some configurations are more probable than others.

### Angular Distributions, Spin, and Wigner D-Functions in Particle Decays


**Very good.**
So 15 minutes before the end, we start with the lecture of today.

::: callout-important
Angular distribution is a **very powerful tool** to understand properties of particles.
As we already discussed, that's our way to measure **spin, parity, and other quantum numbers** in particle interactions.
:::

- **Particles with higher spin** would prefer more bumpy, more spiky angular distributions.
- **Particles with lower spin**—if everything is scalar—are going to produce **no asymmetries at all**, no structures in angular distributions.

By looking at the angular distribution, especially in the **rest frame of the particle decay**, one examines the ratio of the aligned kinematics and other types of kinematics.
And then, with this, one can infer the information about the spin.

---

For most of the particles that we have discovered up to now, the **quantum numbers are not known**.
We discover particles as bumps in the spectrum, and then the next step—in order to understand their properties—is to determine their quantum numbers.
This is done by looking at **angular distributions**.

Most of the time, it's as simple as looking at the **Dalitz plot** and seeing:

- If there is a minimum in the angular distribution.
- If this line has several structures, several nodes.

The **maxima and nodes** indicate, in the case of scalar particles in the final state, the nodes would literally tell you the spin:

- If you have **one node**, you have spin one.
- If you have **two nodes**, you have spin two.
- If you have **three nodes**, you have spin three.

So the intensity would really vanish at certain points—the **dark spots**.

---

But in the case where it's **not scalar**—and most of the time, it's not scalar particles that interact—the situation is a little bit more complicated.
I will have examples of scalar resonances.
But here, let's just quickly check what spin they are giving here:

- **Baryon (proton) spin**: $\frac{1}{2}$
- **Kaon and pion (except scalars)**: spin $0$
- **Lambda**: same as proton, but with the jump, the presence of spin averages out the distribution.

If you consider a certain spin projection of the $\Lambda_c$ and proton, you'll again have nodes and zeros in the angular distribution.
But since we don't polarize the initial-state $\Lambda$, and we don't measure the spin of the final state—**everything is averaged**.
Therefore, you don't have minima, you don't have nodes or zeros any longer; things get smeared.

---


A particle with spin can have $2J + 1$ projections onto the quantization axis.
Let me consider a particle that has spin $J$.
There is a $z$-axis that we need to quantize the spin, and this $z$-axis measures the $J_z$ upper layer is going to give us.

::: callout-note
The state $|JM\rangle$ can be thought of as a vector of $2J + 1$ components.
All operators in this case are matrices that act on these vectors and produce either:

- The same state with a certain eigenvalue, or
- A mixture of the states.
:::
When I act with the rotation on the state, I'm going to produce **not a certain state, but a mixture of different states**—it's as simple as that.
When I rotate the state, if it were a vector in regular space, I could probably adjust this to have exactly a certain projection.
But in quantum mechanics, it doesn't work this way.

Once you act with the rotation, most of the time you're going to end up with a **mixture of all states**.
These coefficients are tabulated, so they are known functions for any state.
You can have a look and check what these coefficients are.
They are called **Wigner $D$-functions**.

---


Let me be more concrete.
I'm going to rotate about the $Y$-axis in a second.
I have a $Z$, I have my $X$, and I have my $Y$—$XYZ$.
They should form the right-handed triple of axes $X$, $Y$, $Z$.

I'm going to rotate about the $Y$-axis and apply it to $|JM\rangle$.
In order to do that, I have to—so $J_+$, as you remember, it's:

$$
J_+ = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \quad J_- = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}
$$

The $J_y$ operator then has zero on the diagonal and these coefficients above and below the diagonal.
To apply the transformation to the state, you have to do the **matrix exponential of $J_y$**.
But this is done for you, and we know what they are.

These are these coefficients—where they are $C$, $C$, $C$, $C$.
You need to know about the initial state as well.
That's why the $JM$ indices are kept in these notations.

---


Let's take an example—a very small one—of spin one-half.
I'm going to rotate the state $|1/2, 1/2\rangle$ by 30 degrees about the $Y$-axis.
I'm going to get a $|1/2, 1/2\rangle$ plus $|1/2, -1/2\rangle$ combination, and I want you to quickly tell me what are the numbers here.

These coefficients are sitting in the same place—where sitting in the same page as the **Clebsch-Gordan coefficients**.
They are closely related.
This is about the $SU(2)$ group, and you just open the Clebsch-Gordan coefficients and check the numbers.

Since 30 degrees is not at all trivial to do it, but now we won't have time to look at details, and hopefully in the seminar we will explore a little bit more.
I just remember this table because it's super simple.

The $D$ for $m' = m = \pm 1/2$ is:

$$
d^{1/2}(\theta) = \begin{pmatrix} \cos(\theta/2) & -\sin(\theta/2) \\ \sin(\theta/2) & \cos(\theta/2) \end{pmatrix}
$$

I should have picked 60 degrees because for 15 degrees it's a little bit inconvenient.
What is going to be here is the cosine of 15 degrees.
What's going to be here is the sine of 15 degrees.

---


::: callout-tip

- **Mathematica** has an **opposite convention** to what we use.
- **Wikipedia** is the most reliable source for Wigner $D$-function conventions.
- They're coded correctly in **Python (SymPy)** and **ROOT**.
:::
---


Let me stress what we discussed so far was **not about weak interactions or strong interactions**.
It was about **rotations and the rotational group**.

That's the fun part—and something that still impresses me—that in order to understand how particles behave and what the angular distributions are, you need little from the strong interaction.
You only need the **general properties of the rotational group**, so to speak.

Angular distributions are determined by:

1. **General properties of how space is rotated**, plus
2. A little bit that we need from strong interactions.

Specifically:

- **Strong interactions** tell us what is the preference for which spin particles are produced.
- **Quantum group properties** determine how they decay and what the asymmetry is in the kinematics.

That's amazing.
Therefore, we can now move on and have a **recipe**, or a general way, to construct any particle decay chain and figure out what the angular distribution is going to be.

---


Let's now explore the blob that I had in the previous slide and then consider one of the possible decay kinematics, one of the possible decay dynamics.
Now we're going to make up a model for what is inside of the blob.

It's not just kinematics—it really comes from a **modeling assumption**, and I'm going to assume that three particles in the final state are produced via a **cascade process** where:

1. The initial particle goes first to the intermediate particle with spin $J$.
2. Then $X$ decays to 1 and 2.

A three-way process with two variable spins just gives the **dimension of the matrix**—discrete dimensions.
For this problem, since all the particles have spin, I'm going to deal with the dimensions, which is a product of:

$$
\text{Dim} = \prod_{i=0}^3 (2j_i + 1)
$$

If a particle's spin is $0$, then the dimension of the corresponding spin is $1$.
That's easy.

But in the general case, you have many of these two-variable functions, and the way to write the amplitude is to **sum over the intermediate spin** and to...

### Helicity Amplitudes and Rotation Matrices in Cascade Decays


Another thing I would like to say is that for simplicity, we are going to align. We are going to consider this $X_3$—they are different resonances, the two resonances from $RTPX$, and $X$ reland has to go through from the initial state.

You look at it in the **center-of-mass (c.m.) frame**, correct? So that's the general expression. It's extendable to any cascade decays.

::: callout-important
The general decay amplitude formula combines a **model-independent part** (carrier group-driven angle independence) and **dynamics** (particle interactions):
$$
\mathcal{A} = \sum_{\lambda} H_{\lambda} D^{J*}_{\lambda_0, \lambda_X - \lambda_3}(\phi, \theta) D^{J_X}_{\lambda_X, \lambda_1 - \lambda_2}(\theta', \phi')
$$

- $H_{\lambda}$: Dynamics (weak/strong/EM interactions)
- $D^{J}$: Wigner rotation matrices
- $\lambda_i$: Helicity states
:::
I'd like to give you a general formula, and we will only have time to understand it rather than derive it. It has two components: a model-independent part, carrier group-driven angle independence, and then bits of the particle interactions that you have to insert.

The $H$'s are the remaining dark blobs that hide inside the dynamics of the particles. This is what comes from the **weak interactions**, **strong interactions**, **electromagnetic interactions**, whatever you have. This physics is actually sitting there, and the rest is the rotational properties of the system.

So this $H$ is the physics, and for the hard interactions, this is something unknown because we don't have a way to parameterize it. By this $H$, what we mean is that you have a particle $\Lambda X$ number three. This is what's three particles: $\Lambda X$, $\Lambda_3^0$, decaying into two.

The other $H$ degree, plus this $X$ going to particles 1, 2, and the $G$. The $G$ is the rotation orientation of the decay.

The first index tells you who decays. The second index gives where it decays. The particles now have their spin in the frame where the particle moves. The most natural way to use the spin—to actually quantize the spin—is the quantized direction of the spin, which is the direction of motion.

In that case, $\Lambda$'s are **helicity projections**—projection to motion to $P$. The $D$ has the first index telling you who decays, and the second index, after rotation, where it decays, and then the particle zero.

Let's look at the particle $X$. The particle $X$ carries the spin projection $\lambda_X$. It decays to particles 1 and 2, which are going at a certain angle with respect to the direction of motion of $X$.

To compensate for this angle, one has to adjust the quantization axis. This is done by rotating the spin—rotating the vector of $X$ to the direction in which it decays. From that combination, one has to rotate to the new combination, and that's what is indicated by the rotation orientation of the decay rotation.

I would like to evaluate this expression in the **aligned kinematics**—$\phi = \theta = 0$. Here is the CM frame. This is the expression.

::: callout-note
In aligned kinematics ($\theta = \phi = 0$), the amplitude simplifies to:
$$
\mathcal{A}_{\text{aligned}} = \sum_{\lambda_X} H_{\lambda_X} \delta_{\lambda_0, \lambda_X - \lambda_3} D^{J_X}_{\lambda_X, \lambda_1 - \lambda_2}(\theta)
$$
The **Kronecker delta** $\delta_{\lambda_0, \lambda_X - \lambda_3}$ enforces angular momentum conservation.
:::
If you evaluate that, what you get is the amplitude $\mathcal{A}$ that depends on $S$ and $C$ and all $\lambda$'s. Let's evaluate when angles are zero.

The transformations reduce because the $D$-matrix appears due to rotation. But if angles are zero, we don't have to rotate. We can significantly reduce the summation over $\lambda_X$.

We don't have to rotate because $X$ is already moving on the $Z$-axis. Therefore, we get a sum over $\lambda_X$, $\lambda_X$, $\lambda_3$, and then $D$ of zero angles: $D^{J}_{\lambda_0, \lambda_X - \lambda_3}(0)$.

Another piece is $\lambda_1$, $\lambda_2$, and the adjustment for $\lambda_X$, $\lambda_1 - \lambda_2$ of $\theta$ and $\phi$.

This gives a **delta function** $\delta_{\lambda_0, \lambda_X - \lambda_3}$. If we don't have to rotate, the only way to get the same state is if the state remains unchanged.

So $X$ is constrained from that. The final expression is:
$$
\mathcal{A}_{\text{final}} = H_0 \, D^{J_X}_{\lambda_0 + \lambda_3, \lambda_3} \, D^{J_X}_{\lambda_0 + \lambda_3, \lambda_1 - \lambda_2}(\theta)
$$
As simple as that.

---

### Predicting Angle Distributions and Partial Wave Analysis in Particle Decays



**How many numbers do I need from you in order to compute?** I want to think now about electromagnetic interactions, or let me do gravity.
**How many numbers as input do I need from you to predict the angle distribution?** It's essentially here, but it misses fundamental components.

---


**What is inside of the blobs?** What's inside of this block, this blob or this blob and this blob? In order to predict all of my values, I just need this guy and that guy.

- The number of spin states for two particles with spins $j_1$ and $j_2$ is given by:
$$
(2j_1 + 1) \times (2j_2 + 1)
$$
These values might be functions of particle masses as well—could be masses of $x$.

- A similar number of these terms is needed, but there is a reasonable way to approximate them.

::: callout-note
**Approximation in Experiments:**
Often, in the first analysis attempt, these terms are assumed to be constant, containing only particle properties.
:::
Here I'm going to say that this one is constant one or $c$, and this is particle.
And then once I do that, I should be able to compute what the angle distribution is.

---


In that case, I am going to fix the mass of the one tube and the intensity that I see along the line.
What is up to now is that these two have a:
$$
\frac{d\Gamma}{d\cos\theta}
$$

**Why cosine?**

- Cosine is just better—it has a better Jacobian.
- We don't need to have this sine Jacobian for cosine.

That's why often what is looked at is the cosine, and this is going to be the matrix element proportional to the matrix element.
And this $|M|^2$ is fixed.

---


This distribution changes from $-1$ to $1$.
So here is the $\theta$ and the $\cos\theta$.
$\theta$ is going to be null here at $-1$.

We scan from $-1$ to $1$, and if it is flat, that's one possibility.
What you often see, especially when you deal with particles with spin, is such a parabola—a second-order polynomial in cosine.
Or what you also often see is this.

**Notice the difference:**

- What we wrote here, $A$, is the **quantum transition amplitude**.
- It's a probability amplitude.
- It's one that is going to be squared to give us the observed probability.
- This $G$ is going to appear squared.

::: callout-important
**Experiment Observations:**

- In experiments, we only see the squared value of the amplitude.
- For unpolarized decays, distributions are averaged:
  $$
  \overline{|M|^2} = \frac{1}{(2s_1 + 1)(2s_2 + 1)} \sum_{\text{spins}} |M|^2
  $$
:::
---


The first way to analyze that is not to guess the amplitude, but rather to use or acknowledge these angle distributions by projecting onto orthogonal polynomials because it gives you a nice basis.

- The differential cross-section can be expanded as:
$$
\frac{d\sigma}{d\cos\theta} \propto \sum_{\ell} a_\ell P_\ell(\cos\theta)
$$
where $P_\ell(\cos\theta)$ are **Legendre polynomials**, and $\ell$ relates to the spin of the produced particle.

This is what is called **partial wave analysis**.
Or if you project the differential cross section, this is called **moment analysis**.

- **Partial wave analysis** models cross-sections by amplitudes, treating these terms as free parameters.
- **Moment analysis** projects angle distributions onto polynomials, yielding combinations of conditions.

---


I didn't tell you much about the differences between the canonical state that we introduced at the beginning and the helicity state that we introduced later.
So we only touched a little bit on how the state is defined in the rest frame, and hopefully, we will get to explore more.

---


I would like to tell you that this book has the best coverage of this subject.
This is Martin Spearman's *Elementary Particle Theory*, and **Chapter 4 is fundamental**.

- It starts from the Lorentz group.
- Introduces vectors with a bit of group theory—without heavy details.
- A **really good book** for insights on particle definitions.

### Identifying Decays via Dalitz Plot Kinematics


I left you with an **exercise**, not a quiz. There are some Dalitz plots from CLEO and BaBar, and I have removed the labels. I don’t tell you which particles are in the final state. I only mention that one of them is a $D$ decay and another is a $D_s$ decay.

You already know a lot about **kinematics**, so the exercise is to figure out what decay this is. The axis labels are still there, but you don’t know the masses. From the kinematics, you can deduce the masses and possibly guess the decay.

I have multiple cases. I would assign one to your group, and then you’d get another one—the EP one.

::: callout-note
**Key Kinematic Relations for Dalitz Plots**:
For a 3-body decay $D \to ABC$, the invariant masses of two-particle combinations are:
$$
m_{AB}^2 = (p_A + p_B)^2, \quad m_{BC}^2 = (p_B + p_C)^2
$$
The total invariant mass constraint is:
$$
m_{AB}^2 + m_{BC}^2 + m_{AC}^2 = m_D^2 + m_A^2 + m_B^2 + m_C^2
$$
Boundary conditions for the Dalitz plot are:
$$
(m_{AB}^2)_{\text{min}} = (m_A + m_B)^2, \quad (m_{AB}^2)_{\text{max}} = (m_D - m_C)^2
$$
:::
I have to leave now. Would you like to take it? No? Okay, it’s more like **homework**.

Sorry about that. Come with me, and I’ll give it to you from my office. The rest of you as well.

Thanks for coming, and sorry for being slightly late. Will you have time tomorrow at **8 a.m.**?

---

For the Dalitz plot analysis of a 3-body decay $D \to ABC$, the relevant kinematic relations are:

- **Invariant masses** of two-particle combinations:
$$
m_{AB}^2 = (p_A + p_B)^2, \quad m_{BC}^2 = (p_B + p_C)^2
$$

- **Total invariant mass constraint**:
$$
m_{AB}^2 + m_{BC}^2 + m_{AC}^2 = m_D^2 + m_A^2 + m_B^2 + m_C^2
$$

- **Boundary conditions** for the Dalitz plot:
$$
(m_{AB}^2)_{\text{min}} = (m_A + m_B)^2, \quad (m_{AB}^2)_{\text{max}} = (m_D - m_C)^2
$$

These formulas are **essential** for reconstructing the decay kinematics and identifying the final-state particles.

