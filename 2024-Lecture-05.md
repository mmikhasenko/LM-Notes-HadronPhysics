### Kinematics and Variables in Two-Particle Scattering Processes


Today we are at **lecture number five**.
We'll discuss **angle distributions** and **partial wave analysis**.
But before going there, I would like to start with a recap.

---

Last lecture, we discussed:
- The **phase space** for particle reactions
- Different experiments in their **kinematics**
- A list of experiments worldwide studying **hadrons**, their production mechanisms, and peculiarities

Let’s begin with a recap on **kinematics**.

---

**First question**: *How many variables does one need to describe a two-body scattering process?*

We have two examples:
1. **Scalar particles**: $0^-$ scalars scattering to $0^-$ scalars in the final state.
2. **Particles with spin**: $P^+$ scattering from $0^-$ to $3^-$ and $1^+$.

> [!NOTE]
> The scattering process is represented by a "blob" diagram, indicating interaction via **strong interaction theory**. This is a *unitarity diagram* (not a Feynman diagram), useful for visualization.

---

The **internal dynamics** (electromagnetic, strong, gravity, etc.) do not affect the number of variables.

- Start with $2 \times 2 \times 3 = 12$ degrees of freedom (4 particles, 3 momentum components each).
- Subtract 4 for **energy-momentum conservation**.
- Subtract 6 (3 rotations, 3 boosts) since the system has no preferred frame.
- **Result**: 2 variables.

- The answer is **also 2**.
- Angular distributions of final-state particles do not introduce additional independent variables.

---

- For **scalar particles**, the amplitude is a function of $s$ and $t$:
\[
s = (p_1 + p_2)^2, \quad t = (p_1 - p_3)^2.
\]
Here, $s$ is the **center-of-mass energy squared**, and $t$ is the **momentum transfer squared**.

- For **particles with spin**, the amplitude is higher-dimensional. Example for $3^-$ and $1^+$ final state:
\[
\text{dim}(\mathcal{A}) = (2 \times 3 + 1)(2 \times 1 + 1) = 7 \times 3 = 21.
\]
All 21 amplitudes depend on the **same two variables**, $s$ and $t$.

> [!IMPORTANT]
> If final-state particles **decay**, additional variables may be introduced. But for now, we restrict ourselves to **two variables**.

---

For part C, the two variables to describe the process are:
- **Mandelstam variables** $s$ and $t$ (most common choice).
- These are **Lorentz invariants**—they characterize the process independently of the frame.

The mass of a particle is given by:
\[
m^2 = E^2 - |\vec{p}|^2 = p_\mu p^\mu.
\]

---

*By the way*, I recently learned that "**invariance**" might not be a word in the dictionary.
But it sounds natural to me—I use it all the time to mean "**invariant variables**."

### Variables and Kinematics in Three-Body Decay and the Dalitz Plot



Let's give examples of these sets of variables. We've got one from Hendrik. Everyone should choose their favorite. Ilya, what's your favorite? $S$ and $T$. No, not a single pair—these are sets. We need two variables to describe the process. What are your favorite two variables? Oh, this is it.

What's your second favorite? Or the third variable? Why a third? Just introduce something new. Let's introduce another. Sven, what about you? $P_2 - P_4$. It's called $U$, and it's also a variable $P$. Wait, $P_2 - P_4$ is the same as $P_1 - P_3$. So $P_1 - P_4$ squared is called $U$.

If you do the algebra, you’ll find there are only two independent variables. Your favorite set is $S$ and $U$, and they’re equivalent because $U$ is a linear combination of $S$ and $T$. Some prefer $T$ and $U$.

Alternatively, we can use the **center-of-mass energy** and the **angle**. That’s a great choice—probably my favorite. The center-of-mass energy is $\sqrt{s}$, and the angle is defined in the center-of-mass frame.

> [!NOTE]
> **Mandelstam Variables**:
> - $s = (p_1 + p_2)^2$ (center-of-mass energy squared)
> - $t = (p_1 - p_3)^2$ (momentum transfer squared)
> - $u = (p_1 - p_4)^2$ (related by $s + t + u = \sum m_i^2$)

---


In the **center-of-mass frame** (also called the **center-of-momentum frame**), the momenta sum to zero. You have $P_1$ and $P_3$. The angle between $P_1$ and $P_3$ defines the kinematics. Be careful when drawing this—the lengths of the vectors represent their momenta. In the final state, the momenta must still balance in the same frame.

Any two independent variables work. For example, $E_1$ and $E_3$ in the lab frame are also fine. But you must ensure the variables aren’t redundant. Sometimes, the phase space folds when mapped to certain variables, making the transformation non-bijective.

---


Now, let’s discuss the homework on the **Dalitz plot**. This marks the shift to topics specific to hadron spectroscopy. One key subject is particle representation, particularly **three-body decays**. The Dalitz plot is a powerful tool to visualize interaction dynamics.

For a three-body decay, the diagram has one incoming leg and three outgoing legs, with the blob representing the interaction. The number of kinematic variables is the same as before—two variables fully describe the process. Give me $S$ and $T$, or angles, and I can reconstruct the entire kinematics.

Think of the rigid body analogy: a 3D-printed blob with fixed-length vectors sticking out. The angles and lengths define the kinematics. For a three-body decay, I draw three vectors. The Dalitz plot variables $S$ and $T$ are defined similarly, but now for different final-state particles.

For a three-body decay, we define:
- $s = (p_3 + p_4)^2$
- $t = (p_1 - p_3)^2$

The phase space for three-body decays is flat in these variables. The differential width $\frac{d\Gamma}{dm_{34}^2 dm_{24}^2}$ is constant.

---


The recursive formula for phase space gives:

$$
d\Phi_3 = d\Phi_2(m_{12}^2) \cdot d\Phi_2(m_{23}^2) \cdot \frac{1}{(2\pi)^2} dm_{12}^2 dm_{23}^2
$$

Each two-body phase space contributes:

$$
d\Phi_2 = \frac{1}{8\pi} \frac{2|\mathbf{p}|}{\sqrt{s}} \frac{d\Omega}{4\pi}
$$

The **Jacobian** for transforming to Mandelstam variables is constant, so the density in $(m_{34}^2, m_{24}^2)$ is undistorted. This makes Mandelstam variables ideal for studying interactions directly.

We’ll revisit this in exercises, but the key takeaway is that **three-body phase space is uniform** in these variables, revealing the underlying dynamics clearly.

### Λc Baryon Decay Dynamics and Dalitz Plot Analysis


You can see the example of the $\Lambda_c$ baryon decay: $\Lambda_c \to p K^- \pi^+$.
We measure $\Lambda_c$ produced in proton-proton collisions or other interactions.
In the **BES** and **Belle** experiments, they observe $\Lambda_c$.
This is one of those particles that lives long and is produced abundantly.

---

Particles with charm ground states are produced abundantly and live long enough to fly from the primary vertex.
We reconstruct them, which is why we have a good sample and understanding of their decay kinematics—and dynamics as well.

> [!NOTE]
> The reconstruction relies on the **invariant mass formula**:
> $$
> m_{ij}^2 = (p_i + p_j)^2 = (E_i + E_j)^2 - (\vec{p}_i + \vec{p}_j)^2
> $$
> where $m_{ij}$ is the invariant mass of particles $i$ and $j$.

---

In this decay, there is a charm quark in the initial state but none in the final state, indicating **weak interaction**.
The charm quark decays, transitioning into a strange quark that ends up in the kaon: $c \to s$.
This is a transition within one generation, so it is not suppressed—it’s an allowed process.

---

This is the **golden channel** for detection because the final state has three charged particles:
- The **proton** is charged, travels well, and is stable.
- The **kaon** is stable in our accelerator experiments.
- The **pion** is also stable.

They fly directly from the decay without distraction, leaving clear tracks in the detectors.
We see they point away from the primary interaction, with a ~10 mm shift in $\Lambda_c$ energies between the primary and secondary vertices.
This ~1 cm displacement is due to the boost, as $\Lambda_c$ in the lab frame lives longer than in its rest frame.
It is produced with a few hundred GeV in proton-proton collisions at the LHC.

---

This is a very clean decay, and we’ve studied it extensively.
Here is the result of the analysis, which closely resembles experimental data.
The statistics are so high that the distribution appears smooth.

On the **x-axis** is the invariant mass $m_{pK^-}$, and on the **y-axis** is $m_{K^-\pi^+}$.
The colored region shows all kinematically allowed values for the decay.
The white area represents forbidden kinematics where energy and momentum cannot be conserved.

---

If you select a point inside the plot, you can compute the angles between particles and reconstruct the 3D setup.
But for points in the white region, no configuration satisfies the constraints.
This limited range of invariant masses defines the **Dalitz plot**.

Different colors on the plot indicate varying probabilities for the decay to occur at specific kinematics.
We measure the decay, reconstruct the particle tracks, and map them to kinematic points—since there’s a unique relation between four-momenta and kinematics.

---

It turns out certain kinematics are more probable than others.
Particles prefer specific directions—for example, one alignment might be more likely than another.
You can see this preference as variations in the plot’s density.

Here’s a hint: particles aligned in a straight line lie on the plot’s boundary.
Inside the boundary, they always have an angle between them.
Think about how to maximize the invariant mass and where this point lies on the border.

> [!IMPORTANT]
> The **Dalitz plot boundary condition** is given by:
> $$
> (m_{pK^-} + m_{\pi^+})^2 \leq m_{\Lambda_c}^2
> $$
> This defines the kinematic limits of the decay.

### Maximizing and Minimizing Mass in Three-Body Decay Kinematics



Any thoughts? I think you should be in the bottom right because we want to maximize the mass of $pK$. There are three momenta going out. My idea was that the three momenta are in opposite directions, so the three-momentum of the system should be as small as possible.

The three-momentum of the system? Yes. If we add both momentum vectors, the forward momentum—the sum of the squares—should be as large as possible. So we should be on the right of our diagram. If we add them and they are in the same direction, we should be at the lowest point.

You argue that this mass on the y-axis should be as small as possible. Why? Because the three-momenta are aligned, and we subtract them.

---


Here’s another way to think about it: if you go to their rest frame and boost, the $K$ and $\pi$ fly next to each other. Their relative momentum is small. If you boost to their rest frame, they might both be at rest. Therefore, their mass would just be the sum of their masses. So it’s the maximum or minimum?

You are correct. We are looking for the minimal mass of the $K\pi$ system. Let’s figure out what this point corresponds to. This is the kinematics where the two particles have maximal momentum and are at rest, then go in opposite directions. That corresponds to this point.

---


This plot is from experimental data, right? Yes. But in the experiment, we won’t detect the proton directly. This is the lab frame, not the center-of-momentum frame. Everything we measure is boosted. Even if the proton is at rest in the lab frame, it’s already boosted.

This point is the maximum mass. The particles have maximum momentum and go back-to-back, so this is the maximum mass. The other point minimizes the mass.

---


For the three-body decay, there’s a similar approach. The standard way to define the angle is to boost into the frame of interest. Let me show you the setup—apologies for using proton, $K$, and $\pi$.

I want to fix the mass of the $K\pi$ system and explore how it changes by varying the mass of the proton. To do this, take the setup in the center-of-momentum frame and boost to the $K\pi$ rest frame. In the center-of-momentum frame, the three particles are emitted such that the sum of their three-momenta is zero.

Once I boost, the $\Lambda_c$ has non-zero momentum, and the $K$ and $\pi$ have momenta that add to zero since we’re in their rest frame. If I fix the mass of the $K\pi$ system and explore phase space along this line, the lengths of the momentum vectors are fixed. Only the angle $\theta$ changes.

At this point, I have a specific $\theta$. I can explore all angles from $0$ to $\pi$. At one extreme, the angle is $0$; at the other, it’s $\pi$.

---


Let’s reflect a bit more. Which coordinate corresponds to which? The right should be $0$, and the left $\pi$.

In this setup, the proton and $K$ go in opposite directions, giving the maximum mass of $pK$. For our new setup, since the lengths of all vectors are fixed, we can only rotate them. The mass of two particles depends on the angle $\theta$: the wider the angle, the larger the mass.

For $\theta = 0$, the mass is very high. When the particles go in almost the same direction, the mass is small.

---


I can do the same with the other pair. Let me fix the mass of the proton and $K$ system. The most straightforward way to analyze this is to go to the rest frame of $pK$, where everything is fixed, and scan along this line by changing the angle of the $\pi$ with respect to the rest.

There’s a third variable in 2-to-2 scattering called $u$, which is even more symmetric. For three particles, there’s the mass of $\pi p$. It’s not immediately obvious what this mass is, but if I fix the mass of the $K\pi$ system and scan the angle, the line I move along is easy to understand from the relation:

$$
u = m_{p\pi}^2 = (E_p + E_\pi)^2 - (\vec{p}_p + \vec{p}_\pi)^2
$$

The $u$ variable is a linear combination of the other two. It’s actually a diagonal in this plot. This line corresponds to the mass of $\pi p$ being fixed, and I move from one corner to another by changing the angle.

---

> [!NOTE]
> **Key Formulas for Dalitz Plots**
> The invariant mass for a particle system is given by:
> $$
> M^2 = \left(\sum_i E_i\right)^2 - \left(\sum_i \vec{p}_i\right)^2
> $$
> For $\Lambda_c \to pK\pi$ decay, the Dalitz plot variables are:
> $$
> m_{pK}^2 = (E_p + E_K)^2 - (\vec{p}_p + \vec{p}_K)^2
> $$
> $$
> m_{K\pi}^2 = (E_K + E_\pi)^2 - (\vec{p}_K + \vec{p}_\pi)^2
> $$
> The symmetric representation uses:
> $$
> x = \frac{\sqrt{3}}{2}(m_{K\pi}^2 - m_{p\pi}^2)
> $$
> $$
> y = m_{pK}^2 - \frac{1}{2}(m_{K\pi}^2 + m_{p\pi}^2)
> $$

---


The standard representation in experimental analysis for a Dalitz plot has the mass of one pair on the x-axis and the mass of another pair on the y-axis. But there’s also a more symmetric Dalitz plot where all variables enter symmetrically.

This uses the properties of an equilateral triangle: for any point inside, the sum of the distances to the sides is constant. This allows us to introduce variables where the masses are the distances to the sides.

The variables are:

$$
x = \frac{\sqrt{3}}{2}(m_{K\pi}^2 - m_{p\pi}^2)
$$
$$
y = m_{pK}^2 - \frac{1}{2}(m_{K\pi}^2 + m_{p\pi}^2)
$$

This is a symmetric, nice representation. It’s the same as the standard plot but skewed. To relate Cartesian coordinates to the heights of the triangle, you need a transformation involving $\sqrt{3}/2$ due to the 60-degree angles.

This symmetric representation is elegant, but the standard plot is more common and easier to use. Both represent the kinematics, and we see points where the density increases.

---


The goal of this kinematic representation is to understand the dynamics and the processes driving the interaction. Looking ahead, we’ll see that this decay isn’t just $\Lambda_c \to p K \pi$, but proceeds via intermediate resonances.

For a short time, two particles form an intermediate state that then dissociates, increasing the decay probability. If the energy is in a certain range, these particles interact more strongly, and the probability of the process increases.

### Exploring Hadronic Resonances and Dalitz Plot Structures in Two-Particle Systems


You might have seen **cross sections** for two-particle resonances. These show a **bump** known as the **hadronic resonance**. The physics behind this is that you have a system of two particles whose **quantum numbers** match those of some resonance.

By adjusting the **energy** of the system, you explore how the system behaves and how likely the two particles are to interact at a given energy. If there is an **intermediate resonance**, the system can resonate at this energy, and the interaction probability increases as you pass through the **resonance region**.

This leads to the appearance of **bent structures** in the Dalitz plot distribution. If you project it onto one of the axes, you'll see a **resonance-like shape**. These bent structures can be identified in both representations.

> [!NOTE]
> The **Breit-Wigner formula** describes the resonance cross-section:
> $$
\sigma(E) = \frac{4\pi}{k^2} \frac{(2J+1)}{(2s_1+1)(2s_2+1)} \frac{\Gamma^2/4}{(E-E_R)^2 + \Gamma^2/4}
$$
> Where $E$ is the center-of-mass energy, $E_R$ is the resonance energy, and $\Gamma$ is the resonance width.

This is a **cool example** I brought because there are resonances in all three particle pairs. There are resonances in these two, and these two as well.

Why is there a **larger probability increase** when the proton and pion are near resonance? The same applies to the $K\pi$ system on the right side, not just the two lines on the left. Let's understand the lines—we’ll come back to this in two lectures, but let’s quickly identify them.

---


All **horizontal lines**—which resonances are these? In which mass distribution? This will give us a peak. Looking at the blue plot, the $K\pi$ **invariant mass** $m_{K\pi}$ is fixed, and the probability peaks at a certain value.

All these lines correspond to resonances in the $K\pi$ system. What particle decays to $K\pi$? The $K^*$ (**K-star**). So these are $K^*$ resonances.

Now, let’s look at the **vertical lines**. In which system? By varying $m_{K\pi}$, we scan the energy of another system. Think of this as a **projectile**. These lines correspond to a fixed mass of the proton-$K$ system $m_{pK}$. Moving along the axis scans $m_{K\pi}$.

If you expand it, you’ll see the lines correspond to resonances in the $pK$ system—the $\Lambda$ or $\Sigma$ resonances. I’m pointing to the proton-$K$ resonance.

The third combination is the **pion-proton system**, which gives the $\Delta$ resonances. Another plot can help here because it’s nice to see that the lines are parallel to the sides of the **Dalitz plot triangle**.

---


This line is the same as this one, **parallel to one side**. The $\Lambda$ resonances are parallel to another side. At this point, you can also see the $\Delta$ resonance, which is the line here, parallel to the third side. It’s a bit trickier to see the $\Delta$ resonance here, but it’s there.

> [!TIP]
> For three-body decays like $K\pi p$, the **Dalitz plot variables** are:
> $$
 m_{12}^2 = (p_1 + p_2)^2, \quad m_{23}^2 = (p_2 + p_3)^2 
$$
> where $p_i$ are the 4-momenta of the decay products. These help identify resonance structures.

### Angular Distribution Inhomogeneity in Decay Bands Due to Particle Spin


**Okay, questions about the angular distribution.**

Let me finish this discussion and move to **today's topic**: the angular distribution for a decay within one band.

---

Consider the phase space resonance here. As we discussed before:
* When traversing the Dalitz plot
* Moving through phase space from one end to another while keeping the invariant mass fixed
* We change the angle

This explores **different angular configurations**.

> [!NOTE]
> The angular dependence reveals inhomogeneities—even within the band, one edge may have a different probability than the other. This is due to spin effects in particle decays.

Let's sit in the rest frame of the $K\pi$ system where this band occurs and traverse phase space by varying the angle.

---

Particles often prefer certain alignments. For example:
* They may favor being **parallel** rather than perpendicular
* This is less probable kinematically

Such preferences arise because particles have **spin**.

The intermediate resonance (here, the $K^*$) is not a scalar—it has spin. This spin causes:
1. Inhomogeneities in angular distributions
2. Effects on the Dalitz plot

---

For **spin-1 particles** like vector mesons, the angular distribution follows:

$$
\frac{d\Gamma}{d\cos\theta} \propto 1 + \alpha \cos^2\theta
$$

where $\alpha$ measures the asymmetry.

---

More generally, for a **spin-$J$ resonance**, the distribution is:

$$
W(\theta) = \sum_{k=0}^{2J} a_k P_k(\cos\theta)
$$

where:
* $P_k$ are Legendre polynomials
* $a_k$ depend on the spin density matrix

---

The helicity amplitudes squared determine the angular dependence:

$$
|A_\lambda(\theta)|^2 = |d^J_{\lambda,\Delta\lambda}(\theta)|^2
$$

where:
* $d^J$ are Wigner d-functions
* $\Delta\lambda$ is the helicity difference

---

This **spin-driven anisotropy** is why we observe non-uniform angular distributions.

### Angular Distributions and Spin Determination in Particle Decays


**Very good.**
So 15 minutes before the end, we start with today's lecture.

---

**Angular distribution** is a very powerful tool to understand the properties of particles. As we already discussed, it is our way to measure **spin, parity, and other quantum numbers** in particle interactions.

- **Particles with higher spin** prefer more *bumpy*, more *spiky* angular distributions.
- **Particles with lower spin**—if everything is scalar—produce *no asymmetries at all*, no structures in the angular distributions.

By looking at the angular distribution, especially in the **rest frame of the particle decay**, one examines the ratio of *aligned kinematics* to other types of kinematics. From this, one can infer information about the spin.

---

For most of the particles discovered so far, the quantum numbers are **not initially known**. We discover particles as *bumps in the spectrum*, and the next step is to determine their properties and quantum numbers. This is done by looking at **angular distributions**.

Most of the time, it is as simple as looking at the **Dalitz plot** and seeing if there is a minimum in the angular distribution. If the distribution has several structures—**nodes and maxima**—these indicate the spin.

For **scalar particles** in the final state, the nodes directly tell you the spin:
- **One node** corresponds to spin 1.
- **Two nodes** correspond to spin 2.
- **Three nodes** correspond to spin 3.

The intensity vanishes at certain points, creating **dark spots**. However, if the particles are **not scalar**—and most of the time they are not—the situation becomes more complicated.

---

Let me give an example of scalar resonances. Here, let’s quickly check what spin they have.
- The spin of the **proton** is $1/2$.
- The spin of the **kaon ($K$)** and **pion ($\pi$)** is $0$.
- The spin of the **lambda ($\Lambda$)** is the same as the proton, but the spin averages out in the distribution due to the lack of polarization.

If you consider a **specific spin projection** of the $\Lambda$ and proton, you would again see nodes and zeros in the angular distribution. But since we do not polarize the initial state or measure the spin of the final state, everything is averaged. As a result, you no longer have minima or nodes—the structures are **smoothed out**.

---

A particle with spin $J$ can have $2J + 1$ projections onto the quantization axis. Consider a particle with spin $J$. There is a $z$-axis to quantize the spin, and the operator $J_z$ measures the projection $m$.

The state $|J, m\rangle$ can be thought of as a vector with $2J + 1$ components. Operators in this space are **matrices** that act on these vectors, producing either the same state (as an eigenstate) or a mixture of states.

When you rotate the state, you do not get a single state but a **mixture of different projections**. Unlike classical vectors, you cannot adjust the rotation to get a pure projection. The coefficients for these mixtures are tabulated and known as **Wigner $D$-functions**.

---

> [!IMPORTANT]
> **Key Rotation Formula**:
> The most general rotation is described by three Euler angles $(\alpha, \beta, \gamma)$. In particle physics conventions:
> 1. First rotate by $\phi$ about the $z$-axis.
> 2. Then rotate by $\theta$ about the $y$-axis.
> 3. Finally, rotate by $\gamma$ about the $z$-axis again.

---

Let me be more concrete. Suppose I rotate about the $y$-axis. I have the axes $x, y, z$ forming a right-handed triple. The rotation operator $J_y$ has zeros on the diagonal and coefficients above and below. To apply the rotation, you use the **matrix exponential** $e^{-i \beta J_y}$.

The **Wigner $D$-function** for a general rotation is given by:

$$
D^J_{m'm}(\alpha, \beta, \gamma) = \langle J, m' | \mathcal{R}(\alpha, \beta, \gamma) | J, m \rangle = e^{-i \alpha m'} d^J_{m'm}(\beta) e^{-i \gamma m}
$$

Here, $d^J_{m'm}(\beta)$ is the **reduced Wigner $d$-matrix** for rotations about the $y$-axis.

For example, if I tell you we have a **spin-1 state** initially aligned perpendicular to the $y$-axis and rotated by 30 degrees, you can look up the $D$-functions to find the composition of the final state.

The Wigner $D$-function for this is:

$$
D^J_{m'm}(\phi, \theta, \gamma) = e^{-i \phi m'} d^J_{m'm}(\theta) e^{-i \gamma m}
$$

The $z$-rotations introduce simple **phase factors**, while the $y$-rotation is more complex and involves the $d$-matrix.

---

*Note: The $D$-functions are essential for describing how quantum states transform under rotations in particle physics.*

### Spin-1/2 Rotation and Wigner D Functions in Particle Decay Chains


Let’s consider a small example of **spin-1/2 rotation**.
I’ll rotate the state $|1/2, 1/2\rangle$ by **30 degrees** about the $y$-axis. This will give a combination of $|1/2, 1/2\rangle$ and $|1/2, -1/2\rangle$. I want you to quickly tell me the coefficients.

These coefficients are found in the same tables as the **Clebsch-Gordan coefficients**—they are closely related. This is about the $SU(2)$ group, and you can look up the numbers in the Clebsch-Gordan tables.

Since **30 degrees** is not a standard angle, we won’t go into details here, but we may explore this more in the seminar. Just remember that the **Wigner $D$-matrix** for spin-1/2 is simple:

$$
D^{1/2}_{m'm}(\theta) = \begin{pmatrix}
\cos(\theta/2) & -\sin(\theta/2) \\
\sin(\theta/2) & \cos(\theta/2)
\end{pmatrix}
$$

> [!NOTE]
> The Wigner $D$-matrix for spin-1/2 rotations can be computed using the matrix exponential:
> $$
> D^{j}(\theta) = \exp(-i\theta J_y)
> $$
> where $J_y$ is the angular momentum operator for $y$-axis rotations.

I should have picked **60 degrees**—for 30 degrees, the half-angle is **15 degrees**, which is less convenient. So here, the coefficients would be $\cos(15^\circ)$ and $\sin(15^\circ)$.

Any questions about the **Wigner $D$-functions**? Could you now compute rotations for any spin projection? It’s straightforward, right?

One important note: the convention has a **minus sign**. If you want to compute the matrix exponential yourself, recall that in previous exercises, we derived these matrices. You can do this numerically using **Python** or **Julia**—just compute the matrix exponential. Alternatively, you can look up the Wigner $D$-functions, but be careful with conventions.

- **Mathematica**, for example, uses the **opposite convention**—it has a plus sign here and some indices swapped. Be aware of that.
- **Wikipedia** is the most reliable source for checking conventions—search for "Wigner D-functions," and it provides tables and explanations.
- The **SymPy** library in Python and **ROOT** both implement these functions correctly. Just be cautious with Mathematica.

---

Let me emphasize: what we’ve discussed so far has **nothing to do with weak or strong interactions**. This is purely about **rotations** and the **rotational group**.

The remarkable thing is that to understand particle behavior and angular distributions, you don’t need much from strong interactions. You only need the **general properties of the rotation group**.

- **Angular distributions** are determined by how space rotates, with just a small input from strong interactions—namely, the preference for certain spin states during particle production.
- But the **decay asymmetries** and **kinematics** are entirely governed by the **quantum rotation group**.

This is amazing because it means we now have a **general recipe** to construct any particle decay chain and predict its angular distribution.

---

The text now uses **Markdown elements** to improve readability while preserving all original content.

### Rotational Properties and Aligned Kinematics in Cascade Decays


For simplicity, we are going to consider **aligned kinematics**. We will treat \( X_3 \) as different decay products - one particle from the initial state \( X \) decays through \( R \) to particles 1 and 2.

---

Let's look at the **center-of-mass frame** (CM frame). The general expression is extendable to any cascade decays. I will give you the general formula, and we'll focus on understanding it rather than deriving it.

The formula has two components:
1. **A model-independent part** governed by group theory and angular momentum
2. **Particle interaction terms** that must be inserted

---

The \( H \) terms represent the remaining dynamics hidden inside particle interactions. This includes effects from:
- Weak interactions
- Strong interactions
- Electromagnetic interactions

The physics is contained in \( H \), while the rest describes the **rotational properties** of the system. For hadronic interactions, \( H \) is often unknown because we lack a way to parameterize it.

---

For a particle \( X \) with spin projection \( \lambda_X \) decaying to particles 1 and 2, we write:

$$
A = \sum_{\lambda_X, \lambda_3} H_{\lambda_X \lambda_3} D^{J_X}_{\lambda_X, \lambda_0 - \lambda_3}(0) \times H'_{\lambda_1 \lambda_2} D^{J_X}_{\lambda_X, \lambda_1 - \lambda_2}(\theta, \phi)
$$

Here, \( D \) represents the **rotation orientation** of the decay. The first index indicates the decaying particle, and the second index describes the decay products. The spin is quantized along the direction of motion.

---

> [!IMPORTANT]
> Key rotational transformation:
> $$
> D^{J}_{\lambda, \lambda'}(\theta, \phi) = \langle J, \lambda | e^{-i\phi J_z} e^{-i\theta J_y} | J, \lambda' \rangle
> $$
> This Wigner \( D \)-matrix describes how spin projections change under rotation.

---

For particle \( X \), the spin projection \( \lambda_X \) is along its momentum. When \( X \) decays to particles 1 and 2, they emerge at some angle relative to \( X \)'s motion. To account for this, we must adjust the quantization axis by rotating the spin state.

In **aligned kinematics** (\( \phi = \theta = 0 \)), the rotation simplifies. If the angles are zero, no rotation is needed, and the Wigner \( D \)-matrix reduces to a delta function:

$$
A = \sum_{\lambda_X} H_{\lambda_X (\lambda_0 - \lambda_3)} \delta_{\lambda_X, \lambda_0 - \lambda_3} \times H'_{\lambda_1 \lambda_2} D^{J_X}_{\lambda_X, \lambda_1 - \lambda_2}(0, 0)
$$

This constrains \( \lambda_X = \lambda_0 + \lambda_3 \), leading to the final simplified expression:

$$
A = H_0 D^{J_X}_{\lambda_X, \lambda_3}(\theta) \quad \text{where} \quad \lambda_X = \lambda_0 + \lambda_3
$$

---

This gives the amplitude in the aligned frame, where spin projections are constrained by **angular momentum conservation**.

### Predicting Angle Distributions and Partial Wave Analysis in Particle Decays


How many numbers do I need from you in order to compute? Let’s consider electromagnetic interactions or gravity. How many numbers as input are required to predict the angle distribution? The framework is essentially here, but it’s missing fundamental components.

What is inside these blobs? What’s inside this block, or this blob and that blob? To predict all the values, I just need these two components.

The number of values here is given by the **spin multiplicity factor**:
$$
(2j_1 + 1) \times (2j_2 + 1),
$$
where \( j_1 \) and \( j_2 \) are the spins of the initial particles. These values might also depend on particle masses, such as the mass of \( X \).

---

A similar number of parameters is needed for the other components, but there’s a reasonable way to approximate them. Often, in experimental analysis, we initially assume these are constants or depend only on particle properties.

For simplicity, I’ll say this one is a constant \( c \), and this one is particle-dependent. With this, I should be able to compute the angle distribution.

---

In this case, I’ll fix the mass of one particle and the intensity observed along the line. The **differential cross section** is given by:
$$
\frac{d\Gamma}{d\cos\theta},
$$
where \(\cos\theta\) is used because it has a better Jacobian—no need for the \(\sin\theta\) Jacobian.

The matrix element is proportional to the transition amplitude:
$$
|\mathcal{M}|^2.
$$
Here, \( \mathcal{M} \) is fixed, and the distribution ranges from \(-1\) to \(1\).

If we plot \(\theta\) versus \(\cos\theta\), \(\theta = 0\) corresponds to \(\cos\theta = 1\), and we scan from \(-1\) to \(1\). A flat distribution is one possibility.

For particles with spin, you often see a **parabolic distribution**—a second-order polynomial in \(\cos\theta\):
$$
\frac{d\Gamma}{d\cos\theta} = A + B\cos\theta + C\cos^2\theta.
$$
Alternatively, you might see other shapes.

---

> [!IMPORTANT]
> **Key Note on Quantum Amplitudes**:
> \( \mathcal{M} \) represents the **quantum transition amplitude**—a probability amplitude that is squared to give the observed probability. The helicity amplitude \( G \) appears squared in experiments, as we only measure \( |G|^2 \).

---

Moreover, we often deal with **unpolarized decays**, so distributions are averaged. You square the amplitude, sum over initial and final spin projections, and compare with experimental observations.

The first step in analysis isn’t to guess the amplitude but to project the angular distributions onto **orthogonal polynomials**. This provides a nice basis for expansion.

Any function from \(-1\) to \(1\) can be expanded in **Legendre polynomials** \( P_\ell(\cos\theta) \), which are related to the spin of the produced particle. This is called **partial wave analysis** or, for differential cross sections, **moment analysis**.

Partial wave analysis models the cross section with free parameters for the amplitudes, allowing you to infer what’s inside the blobs by fitting data. As a first step, projecting onto polynomials gives combinations of these parameters, though the interpretation isn’t always straightforward.

---

We haven’t discussed much the differences between canonical states and helicity states, only touching on how states are defined in the rest frame. For deeper insights, I recommend **Chapter 4 of Martin Spearman’s *Elementary Particle Theory***.

This book provides excellent coverage, starting from the Lorentz group, introducing vectors, and lightly touching on group theory without overwhelming detail. It’s a fun and insightful read.

For practice, I’ve prepared an exercise using **Dalitz plots** from CLEO and BaBar. The labels are removed, but the axes are intact. One plot is for a \( D \) decay, another for a \( D_s \) decay. Your task is to identify the decays using kinematics and deduce the masses.

I’ll distribute one plot per group. If you have time tomorrow at 8 AM, we can discuss further. Apologies for the delay today—thank you for your patience!

---

- **Spin multiplicity**:
$$(2j_1 + 1) \times (2j_2 + 1)$$
- **Angular distribution**:
$$\frac{d\Gamma}{d\cos\theta} \propto |\mathcal{M}|^2$$
- **Parabolic distribution**:
$$\frac{d\Gamma}{d\cos\theta} = A + B\cos\theta + C\cos^2\theta$$
- **Partial wave expansion**:
$$\frac{d\sigma}{d\cos\theta} = \sum_{\ell=0}^{L} a_\ell P_\ell(\cos\theta)$$

