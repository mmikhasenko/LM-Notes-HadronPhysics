<!--
Cosine simularity: 0.9237350393996308
-->
## Calculation of Cross Section for Scattering of Massless Particles

The cross section for scattering is computed using the equation:

$$
\sigma = \frac{1}{J} \int |M|^2 \, d\Phi
$$

Here, $J$ is the flux factor, $|M|^2$ is the squared matrix element, and $d\Phi$ is the phase space element.  

For this case, the matrix element squared is $3 + 9 + 1 = 13$. The flux factor is given by:

$$
J = 2E_1 E_2 |v_1 - v_2|
$$

Since the particles are massless, their velocities are $v_1 = v_2 = 1$ (speed of light), so $J = 2 \cdot \frac{\sqrt{s}}{2} \cdot \frac{\sqrt{s}}{2} \cdot 2 = s$.  

The phase space element simplifies to:

$$
d\Phi = \frac{1}{8\pi s}
$$

Combining these, the cross section becomes:

$$
\sigma = \frac{13}{s} \cdot \frac{1}{8\pi s} = \frac{13}{8\pi s^2}
$$

However, the speaker later corrects this to:

$$
\sigma = \frac{13}{4\pi s}
$$

::: callout-note
The momentum for massless particles is $p = \frac{\sqrt{s}}{2}$, and the energy is $E = \frac{\sqrt{s}}{2}$.
:::
To convert units, recall that $1 \ \text{fermi} \cdot \text{MeV} = 200 \ \text{fermi} \cdot \text{MeV} = 1$. Therefore, $1/\text{GeV}^2 = 0.2 \ \text{mb}$.  

The final numerical result is:

$$
\sigma = \frac{13}{4\pi s} \approx \frac{13}{4 \cdot 3 \cdot s} = \frac{13}{12s}
$$

::: callout-important
The key is to start from the correct equation for the cross section, use the right expressions for flux and phase space, and ensure consistent units.
:::
The speaker emphasizes that even if the numerical result is uncertain, the methodology—beginning with the correct formula and applying the proper kinematic relations—is the most important part of the calculation.

<!--
Cosine simularity: 0.9420781424036707
-->
## Imaginary Part and Total Cross Section in Scattering  

The imaginary part of the matrix element is used to calculate the total cross section. This is derived from optical theory, where knowing the imaginary part allows you to compute the total cross section. However, it does not directly give the cross section for a specific process like elastic scattering.  

::: callout-note
The total cross section includes all possible processes (e.g., $AB \to ab$, $AB \to CD$, $AB \to DH$), while the elastic cross section only describes $AB \to ab$. The total cross section must be larger than the elastic one.
:::
If the imaginary part is used to compute the total cross section and the result is negative, this is unphysical. The correct relation ensures the imaginary part is positive, and thus the total cross section remains positive.  

::: callout-important
The Breit-Wigner function, for example, has an imaginary part that remains positive, reinforcing this requirement.
:::
The equation connecting the imaginary part to the total cross section does not involve an absolute value. The minus sign in the relation is unphysical, so only the positive case is valid.  

::: callout-tip
A good exam question would be to derive the elastic and total cross sections from a given expression, using the imaginary part for the total cross section.
:::
The key takeaway is that the imaginary part of the scattering amplitude is intrinsically linked to the total cross section, ensuring positivity and consistency with physical constraints.

<!--
Cosine simularity: 0.9007088942204347
-->
## Matrix Elements and Quantum Numbers in Spin Algebra

In the algorithm diagram, the x-axis represents the real part of the matrix element, while the y-axis represents the imaginary part of the amplitude. Only positive values are allowed for the amplitude, so any value below the ceiling is unphysical and illegal.  

::: callout-note
In spin algebra, determining legal quantum numbers involves checking the counting numbers in the columns of a table, such as in Bosch routes.
:::
For combining spins, you first calculate the quantum numbers in combination. The process involves drawing a table and identifying which columns have the correct counting numbers. For example, the spin composition of the representations for $P_1$ is straightforward:  

$$
P_1 = - - +
$$  

::: callout-important
When working with spin algebra, we focus only on the spin composition of representations. Parity can be computed separately for each multiplet.
:::
The key takeaway is that spin addition and partial wave computation are fundamental skills in spin algebra. The process involves tabulating quantum numbers and verifying their validity through counting rules.  

<!--
Cosine simularity: 0.9264557560801463
-->
## Quantum Numbers and Decay Violations in Meson Physics

The parity for a multiplet is straightforward to compute. Combining $1^-$ and $1^+$ and $1^-$ in an S-wave gives $1^-$, so the S-wave configuration works.  

For higher partial waves:  

- In the D-wave, we have states with $L = 0, 1, 2$.  
- In the F-wave, we have $L = 1, 2, 3$.  

The charge conjugation quantum number is a key consideration here. The $\pi$ meson has quantum numbers $0^- +$, while $B_1$ has $1^+ -$. The decay is possible, but charge conjugation is $+$ in this case, indicating isospin violation.  

::: callout-note
The $\pi_1$ meson has quantum numbers $1^- +$, which are not allowed in the standard quark model.
:::
This suggests that $\pi_1$ is not a conventional quark-antiquark state but rather a hybrid meson. The interpretation involves gluonic excitations within the meson, where the gluonic field connecting the quark and antiquark carries additional degrees of freedom.  

Similarly, the $P_1(1400)$ state shares the same hybrid nature, with excitations arising from the gluonic string interaction rather than a simple confining potential.  

<!--
Cosine simularity: 0.9356893471000975
-->
## Scattering Length and Relativistic Formulation

The scattering length is measured in Fermi (fm), but in relativistic formulations, it appears dimensionless. In quantum mechanics, the scattering length is defined through the expansion of the amplitude in terms of the breakup momentum $K$, which has units of GeV. Therefore, $1/a$ has units of GeV, and $a$ itself is in Fermi.  

The non-relativistic amplitude is given by:  
$$
f_{NR} = \frac{1}{a - i\,k}
$$

In the relativistic formulation, the amplitude becomes:  
$$
f_{R} = \frac{1}{\tilde a^{-1} - i\,\frac{2k}{\sqrt{s}}}
$$

::: callout-note
The imaginary part of the relativistic amplitude is related to the dimensionless phase space. The first expansion term resembles the scattering length but is itself dimensionless.
:::
To relate the two formulations, we match them at the threshold. At threshold ($k \to 0$), the non-relativistic amplitude reduces to $f_{NR} = a$, while the relativistic amplitude becomes $f_{R} = \tilde a$. However, they are not directly equal—there is a numerical constant relating them.  

The key is to equate the numerators or denominators up to a numerical factor. The difference arises from the relativistic phase space factor:  
$$
\frac{2k}{\sqrt{s}} = -i\,k \cdot \left(\frac{1}{8\pi^2 s}\right)
$$

At threshold, $\sqrt{s}$ is the sum of the masses involved. For example, if the scattering length $a$ is 3 Fermi, we can determine $\tilde a$ by matching the amplitudes at threshold.  

::: callout-important
The conversion between $a$ and $\tilde a$ involves the threshold energy and masses. Specifically, $\tilde a = a / (8\pi^2 s_{\text{threshold}})$, where $s_{\text{threshold}}$ is the squared invariant mass at threshold.
:::
This exercise demonstrates how relativistic effects modify the low-energy expansion of scattering amplitudes. The dimensionless $\tilde a$ in the relativistic case must be rescaled by the threshold kinematics to recover the conventional scattering length $a$ in Fermi.  

---

The discussion also touches on meson states, such as the $P_1(1400)$, which was initially misidentified in older data but later corrected to appear at 1600 MeV in more precise analyses. This highlights the importance of accurate measurements in determining resonance properties.  

::: callout-note
The $\pi_1$ meson has quantum numbers $1^- +$, which are forbidden in the standard quark model, suggesting it is a hybrid meson with gluonic excitations. Similarly, the $P_1(1400)$ exhibits a hybrid nature due to gluonic string interactions rather than a simple quark-antiquark configuration.
:::
The parity and charge conjugation quantum numbers play a crucial role in identifying such exotic states. For instance, the $\pi$ meson has $0^- +$, while the $B_1$ meson has $1^+ -$. Decays involving these states may exhibit isospin violation, particularly when charge conjugation conservation is enforced.  

In higher partial waves (D-wave, F-wave), the allowed orbital angular momentum states further constrain the possible quantum numbers and decay patterns of mesons. This underscores the complexity of meson spectroscopy and the need for careful theoretical and experimental scrutiny.

<!--
Cosine simularity: 0.920611986690305
-->
## Dirac Equation and Spinor Conventions  

The Dirac equation for a spin-1/2 particle is given by:  

$$
(\mathrlap{/}p - m)\,\tilde u = 0
$$

Here, $\tilde u$ is a spinor ( $\tilde u \leftarrow \mathrm{spinor}(\xi)$ ), and $\mathrlap{/}p = p^\mu \gamma_\mu$ is the Feynman slash notation.  

The $\gamma$ matrices are defined in the Dirac representation as:  

$$
\gamma^0 = \begin{pmatrix}I & 0\\[6pt]0 & -I\end{pmatrix},\quad
\gamma^i = \begin{pmatrix}0 & \sigma^i\\[4pt]\sigma^i & 0\end{pmatrix}
$$

::: callout-note
There are two common conventions for solving the Dirac equation: the **Dirac convention** and the **Weyl (or chiral) convention**. The Weyl convention is more convenient when dealing with right-handed and left-handed particles, but we will stick to the standard Dirac convention here.
:::
The Dirac equation describes spin-1/2 particles, where the spin information is encoded in the spinor field. The $\gamma$ matrices are four-dimensional and satisfy the Clifford algebra.  

::: callout-important
The chirality of particles (left-handed or right-handed) is related to their spin orientation, particularly for massless particles. This symmetry is called **chirality**, and it plays a crucial role in understanding the behavior of spin-1/2 particles.
:::
The Dirac equation is the fundamental equation of motion for spin-1/2 particles, and its solutions (spinors) represent the quantum states of these particles. The matrices $\gamma^\mu$ are essential in constructing Lorentz-invariant quantities and ensuring the correct transformation properties under relativistic boosts and rotations.  

::: callout-tip
When working with spinors, it is often useful to switch between different representations (Dirac, Weyl, Majorana) depending on the physical context, but the Dirac representation is the most familiar for introductory purposes.
:::
The study of spinors and their conventions is foundational for quantum field theory, particularly in understanding fermionic fields and their interactions.

<!--
Cosine simularity: 0.9232111081396577
-->
## Four-Vector Contraction and Spinor Solutions  

The four-momentum in spherical coordinates is given by:  

$$
\mathcal P = \bigl(E,\;p\sin\theta\cos\phi,\;p\sin\theta\sin\phi,\;p\cos\theta\bigr)
$$

The gamma matrices ($\gamma^\mu$) are four-dimensional matrices, and $\mathcal P$ is the four-vector. When you contract the two, a summation over $\mu$ is performed, resulting in the expression:  

$$
\mathrlap{/}p - m
$$

Here, $\mathrlap{/}p = p^\mu \gamma_\mu$ (Feynman slash notation), and $m$ is the scalar mass term — though it is implied that this is not multiplied by the $4 \times 4$ identity matrix.  

The spinor $u$ (or "Spiner" in German) is a four-dimensional object that depends on the particle's orientation and momentum. The equation has two solutions, $u_1$ and $u_2$, corresponding to the spin states quantized along the $z$-axis. These solutions can be written as:  

$$
u_1 = \begin{pmatrix}1 \\ 0 \\ p \cos\theta \\ p \sin\theta \end{pmatrix}, \quad u_2 = \begin{pmatrix}0 \\ 1 \\ -p \sin\theta \\ p \cos\theta \end{pmatrix}
$$

These represent canonical states with spin projections $+\frac{1}{2}$ and $-\frac{1}{2}$ along the $z$-axis. The states are obtained by acting with the spin operator, where $u_1$ corresponds to a spin projection of $+\frac{1}{2}$ and $u_2$ to $-\frac{1}{2}$.  

::: callout-note
The spinor solutions are related to states like $|p; J, m\rangle$, where the particle has momentum $p$, spin $J$, and projection $m$ along the quantization axis.
:::
The Dirac equation $(\mathrlap{/}p - m)u = 0$ describes these spin-1/2 solutions, and the $\gamma$ matrices ensure the correct transformation properties under Lorentz boosts and rotations.

<!--
Cosine simularity: 0.9155485350584712
-->
## Helicity States and Linear Combinations  

The eigenvalue for the first spinor $u_1$ is $+\frac{1}{2}$, and for the second spinor $u_2$ it is $-\frac{1}{2}$. These states have a phase dependence on $\phi$, which must be symmetrically present in both solutions.  

The two spinors $u_1$ and $u_2$ are independent solutions of the Dirac equation. Any linear combination of these two will also satisfy the Dirac equation.  

To transform these states into helicity states — where spin is quantized along the direction of motion — we use the same method as before. This involves relating the canonical states to the helicity states through a linear combination.  

Before performing this transformation, it is important to recall how the canonical states are defined. They are obtained by applying a pure boost to the rest-frame spinors, which is a standard procedure in relativistic quantum mechanics.  

::: callout-note
The helicity states correspond to spin projections aligned with the particle's momentum, unlike the canonical states, which are quantized along a fixed axis (e.g., the $z$-axis).
:::
The Dirac equation $(\mathrlap{/}p - m)u = 0$ governs these solutions, ensuring their consistency under Lorentz transformations. The spinor solutions $u_1$ and $u_2$ represent the two possible spin states of a spin-$\frac{1}{2}$ particle.

<!--
Cosine simularity: 0.8955185924219884
-->
## Transformation of Canonical to Helicity States

The canonical state $|p; j, m\rangle_\text{can}$ is defined as a pure boost $B_{\vec{p}}$ acting on the rest-frame state $|0; j, m\rangle_\text{can}$. Under a rotation $R$, the transformation becomes $R B R^{-1} |0; j, m\rangle_\text{can}$.  

The helicity state $|p; j\rangle_{\hat{p}}$ is constructed by applying the boost and rotation:  

$$
|p; j\rangle_{\hat{p}} = R B |0; j, m\rangle = R B R^{-1} R |0; j, m\rangle
$$

This can be expanded using the Wigner rotation matrix $\mathcal{D}^{(j)}_{m\lambda}(\theta, \phi)$ as:  

$$
|p; j\rangle_{\hat{p}} = \sum_m \mathcal{D}^{(j)}_{m\lambda}(\theta, \phi)\,|p; j, m\rangle
$$

The key step in relating canonical to helicity states is introducing an extra $R^{-1}$ to match the transformation properties of the canonical state. Applying $R$ transforms the state, and $R B R^{-1}$ acts on the transformed rest-frame states.  

::: callout-note
The helicity states are obtained by quantizing spin along the momentum direction, unlike canonical states, which are quantized along a fixed axis.
:::
The method involves applying $R B$ and $R$ to the rest-frame states to obtain the canonical states, which are then related to helicity states through the Wigner rotation matrix.

<!--
Cosine simularity: 0.9352745627755749
-->
## Conventions and Definitions of the D Function in Rotational Matrices  

The canonical states are obtained by applying a pure boost $B_{\vec{p}}$, which is a linear combination of canonical states with coefficients given by special matrices.  

::: callout-note
There are two different conventions for defining the capital $D$ function for spherical arguments (angles). The first convention is standard and uses two angles. This is found in the *Review of Particle Physics* (RPP) for experimentalists, as used by Chung and others. However, the second convention appears simpler for constructions involving helicity states, though many particle physics books do not explicitly state these conventions.
:::
The first case corresponds to the rotation sequence $R = R_z(\phi) R_y(\theta)$, where you first rotate by $\theta$ about the $y$-axis and then by $\phi$ about the $z$-axis. The second convention gives the same result when acting on a vector with only a $z$-component, since the initial rotation about $z$ does nothing. However, this introduces an extra phase to the states, which is an unobservable phase.  

The $D$ function (capital $D$) is the rotational matrix for cases beyond just $y$-axis rotations. Rotations about the $y$-axis are special because they require tabulated functions, whereas rotations about the $z$-axis simply introduce phase coefficients.  

$$
\mathcal{D}^{(j)}_{m\lambda}(\theta, \phi)
$$

This notation represents the Wigner rotation matrix, which provides weight coefficients for the transformation between states. The $D$ function is crucial for describing rotations in systems with angular momentum, particularly when relating canonical and helicity states.  

::: callout-important
The distinction between conventions is subtle but significant, especially when working with helicity states or tensor representations. The phase differences arising from the choice of convention must be accounted for in calculations.
:::
<!--
Cosine simularity: 0.9550385202782324
-->
## Helicity States and Spin Projection in Particle Physics

The notation like our $G$ function gives you weight coefficients for the transformation of the helicity state or dynamical state. You apply a notation to the $j u jn$ and then reject $j'$. These vectors are given by that expression depending on your rotations.  

Coming back to our problem, we want to rotate the vector $\vec{p}$ from zero. This rotation is meant to rotate these two components:  

$$
\begin{pmatrix}
\sin\theta \cos\phi \\
\sin\theta \sin\phi \\
\cos\theta
\end{pmatrix}
$$

When we apply this notation to the helicity state, the $D$ function appears. It depends on the two angles $\theta$ and $\phi$. Depending on the convention used, this $D$ may or may not have an extra phase.  

Applying the transformation relates the helicity state for spin-$\frac{1}{2}$ with the spin projected along the direction of motion. This is given by the vector:  

$$
\begin{pmatrix}
\cos\frac{\theta}{2} \\
\sin\frac{\theta}{2}\,e^{i\varphi} \\
\cos\frac{\theta}{2}\,p / (E + m) \\
\sin\frac{\theta}{2}\,p / (E + m)
\end{pmatrix}
$$

I introduced the normalization constant $N = \sqrt{E + m}$, which is standard and appears everywhere. Both $u_1$ and $u_2$ include this $N$ to ensure the correct state density.  

The expression for $u_{\text{down}}$ is similar, with the lower part of the spinor containing the factor $p / (E + m)$. This factor approaches 1 when the mass $m$ is small compared to the energy $E$, since $p \approx E$ in this limit. The state then simplifies to $(\cos, \sin, \cos, \sin)$.  

::: callout-note
The $D$ function conventions are subtle but important. The first convention follows $R = R_z(\phi) R_y(\theta)$, while the second introduces an unobservable phase.
:::
Now, let me introduce projection operators to proceed further.

<!--
Cosine simularity: 0.9243843053675861
-->
## Introduction to Chiral Projection Operators and Their Properties

Now let me introduce projection operators which will cause us to move on. The Gamma 5 matrix is introduced as the product of the gamma matrices with the Levi-Civita tensor. In the convention we choose, it is given by:

$$
\delta^5 = \delta^0\delta^1\delta^2\delta^3 = 
\begin{pmatrix}
I & 0 \\ 0 & -I
\end{pmatrix}
$$

It is very convenient in the consideration of our interactions to introduce right-handed and left-handed projection operators:

$$
P_R = \frac{1 + \delta^5}{2}, \quad P_L = \frac{1 - \delta^5}{2}
$$

These are called projection operators because when they act twice on a state, nothing changes: $P_R^2 = P_R$ and $P_L^2 = P_L$. To see this explicitly, consider:

$$
P_L^2 = \left(\frac{1 - \delta^5}{2}\right)^2 = \frac{1 - 2\delta^5 + (\delta^5)^2}{4} = \frac{1 - \delta^5}{2} = P_L
$$

The same holds for $P_R$. These operators project onto orthogonal subspaces. If you project onto the left-handed space, there are no remaining components of the right-handed space, and vice versa. This means $P_R P_L = 0$.

Another important property arises because $\delta^5$ anti-commutes with any $\delta^\mu$ (i.e., $\delta^5 \delta^\mu = -\delta^\mu \delta^5$). This implies that:

$$
P_R \delta^\mu P_L = 0
$$

If you have $P_L$ followed by $\delta^\mu$, swapping the order introduces a sign change, converting $P_L$ to $P_R$, and $P_R P_L = 0$.  

Any spinor can be decomposed into right-handed and left-handed components using these projection operators. The right-handed component is $P_R \psi$, and the left-handed component is $P_L \psi$.  

::: callout-note
The choice of convention for $\delta^5$ affects the explicit form of the projection operators, but their fundamental properties remain unchanged.
:::
Now, I would like to give a physical meaning to these right-handed and left-handed states.

<!--
Cosine simularity: 0.9290599680652246
-->
## Decomposition of Spin States into Chiral Components

The right-handed and left-handed projection operators are given explicitly in matrix form as:

$$
P_R = \frac{1}{2} \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}, \quad P_L = \frac{1}{2} \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}
$$

Using these matrices, we can decompose a spinor into its chiral components. For example, consider a spin-up helicity state represented as $\psi = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$. When we apply the projection operators, we perform block-wise multiplication for convenience.  

The right-handed projection yields:

$$
P_R \psi = \frac{1}{2} \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}
$$

Similarly, the left-handed projection gives:

$$
P_L \psi = \frac{1}{2} \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$

At high energies, where the mass becomes negligible, the left-handed component of a right-handed helicity state is suppressed by a factor of $(1 - \kappa)$, where $\kappa$ is related to the particle's momentum. This component vanishes in the massless limit.  

::: callout-note
There is no single interpretation of right-handed and left-handed states, but they are closely related to spin orientation along the direction of motion. In the zero-mass limit (or when particles move at the speed of light), they become identical. A right-handed state corresponds to spin aligned with momentum.
:::
<!--
Cosine simularity: 0.9355554148441143
-->
## Chiral States and Helicity in Particle Physics

When you hear "right-handed," it means the particle travels with its spin aligned with the direction of motion. "Left-handed" means the spin is opposite to the direction of motion. However, when the mass is significant or not much smaller than the energy $E$, the states become mixed, and the particle is no longer purely left- or right-handed—it contains both components.  

::: callout-important
In the Standard Model, the weak interaction mediated by the $W$ boson decays only into right-handed leptons and left-handed anti-leptons. This is due to the structure of the Lagrangian.
:::
The weak interaction vertex is expressed as $V - A$, where $V$ stands for vector ( $\gamma^\mu$ ) and $A$ stands for axial ( $\gamma^\mu \gamma^5$ ). The Lagrangian for lepton interactions contains a term like $\gamma^\mu (1 - \gamma^5)$, which can be rewritten using projection operators. Moving $(1 - \gamma^5)$ to the other side gives $(1 + \gamma^5)$, and the interaction vertex becomes $\gamma^\mu P_L$.  

This vertex structure implies that when a $W$ boson decays, it produces an electron and an antineutrino in specific chiral states:  

- The electron ( $e^-$ ) is left-handed (spin opposite to motion).  
- The antineutrino is right-handed (spin aligned with motion).  

::: callout-note
The direct relationship between handedness and spin orientation is only exact in the high-energy limit or when the mass is zero. For neutrinos, this is always the case—all neutrinos are left-handed, and all antineutrinos are right-handed.
:::
Before neutrino masses were established, right-handed neutrinos were considered candidates for new physics, with proposals that they could be heavy and even explain dark matter.  

In the massless case, right-handed and left-handed particles are orthogonal and do not interact. They could even be different particles with unrelated masses. Relativity connects them—once a mass is introduced, you can boost to another frame and change the spin configuration. However, for massless particles, this is impossible because they lack a rest frame.  

::: callout-caution
The terms "right-handed" and "left-handed" refer to chiral states (chirality), not just helicity. The chiral limit is defined as the case where mass is zero, and the states are purely right- or left-handed.
:::
<!--
Cosine simularity: 0.9554759262345949
-->
---
## Helicity and Chirality in Particle Physics  

The massless limit is the case where mass equals zero, and the states are purely right-handed or left-handed. Helicity describes the spin orientation relative to the direction of motion, providing a visual picture under Lorentz transformations. Chirality, however, is closely related but only coincides with helicity in the zero-mass limit.  

::: callout-note
There is no intuitive picture for chiral states unless the particle is ultra-relativistic.
:::
On the Lagrangian level, chiral states are easier to work with because they are defined by projection operators:  

$$
P_L = \frac{1 - \gamma^5}{2}, \quad P_R = \frac{1 + \gamma^5}{2}
$$  

These project left- and right-handed states, respectively. Helicity states mix under boosts—changing frames alters the spin configuration. However, chiral states remain invariant: a left-handed chiral state stays left-handed under boosts or rotations.  

::: callout-caution
While helicity is frame-dependent, chirality is a fundamental property tied to the Lagrangian structure.
:::
For massless particles, chirality and helicity align perfectly, but this correspondence breaks for massive particles due to mixing. Relativity connects these states once mass is introduced, but massless particles lack a rest frame, making their helicity fixed.

<!--
Cosine simularity: 0.928798819531198
-->
## Introduction to QCD Lagrangian and Flavor Symmetry

Here is the Lagrangian of QCD (not QCT):

$$
\mathcal{L}_\text{QCD} = -\frac{1}{4} G_{\mu\nu}^a G^{\mu\nu}_a + \bar{\Psi}_i (i\,\mathrlap{\,/}D - m) \Psi_i
$$

This describes the dynamics of quarks and gluons. The term $G_{\mu\nu}^a$ represents the gluon field strength tensor, which is the gauge part of the Lagrangian. The term $\bar{\Psi}_i (i\,\mathrlap{\,/}D - m) \Psi_i$ includes the quark fields:  

- $i\,\mathrlap{\,/}D \Psi_i$ is the kinetic term,  
- $m \bar{\Psi}_i \Psi_i$ is the mass term,  
- $\mathrlap{\,/}D$ contains the interaction with the gluon field via the covariant derivative.  

The index $i$ labels the quark flavor (e.g., up, down, strange, etc.), and there are six flavors in total. The index $a$ corresponds to color, and $T^a$ are the generators of the gauge group $SU(3)_c$, connected to local gauge symmetry.  

::: callout-note
The Lagrangian has multiple symmetries, including local gauge symmetry, which allows adjusting the phase of the quark wavefunction's color components at every spacetime point.
:::
The quark wavefunction $\Psi$ is a fermionic field with color components in a three-state vector. The local gauge transformation is implemented via matrix exponentials with space-dependent parameters $\theta^a(x)$, ensuring the Lagrangian remains invariant. This transformation dictates how quarks and gluons interact and defines the form of the covariant derivative.  

::: callout-important
For light quarks (up, down, strange), the masses are much smaller than the QCD scale ($\sim 1 \ \text{GeV}$). This justifies the chiral limit ($m \to 0$), enabling low-energy expansions and simplifications in theoretical treatments.
:::
<!--
Cosine simularity: 0.9531392899992741
-->
## Flavor Transformation and SU(3) Symmetry in QCD

The low-energy expansion works because the quark masses are small. There is a small parameter for expansion, which is the ratio of the quark mass to $\Lambda_\text{QCD}$ or the quark momentum to $\Lambda_\text{QCD}$. This leads to effective field theory.  

Now, let's discuss flavor transformation. This means the flavor indices of the wave function can be rotated. We consider a global $SU(3)_\text{flavor}$ symmetry. The flavor part of the wave function has three components:  

$$
\Psi_i = \begin{pmatrix} u \\ d \\ s \end{pmatrix}
$$

Here, we simplify our consideration to the light quarks (up, down, strange). The transformation relating these quarks is a global $SU(3)$ rotation, represented by a $3 \times 3$ matrix. We can perform any rotation or adjustment of this wave function.  

::: callout-important
The transformation is global because we do not allow the rotation parameters $\alpha$ to depend on spacetime coordinates. This ensures we avoid dealing with derivatives.
:::
The QCD Lagrangian is symmetric under these global flavor transformations.

<!--
Cosine simularity: 0.9044505121078811
-->
## Chiral Symmetry and Phase Cancellation in QCD  

The QCD Lagrangian is symmetric with respect to any transformation of chiral symmetry. The fermion field $\Psi$ is decomposed into left- and right-handed components:  

$$
\Psi = \Psi_L + \Psi_R
$$  

When applying a phase transformation to $\Psi_L$ and $\Psi_R$, the phases cancel each other. This cancellation is straightforward to verify.  

::: callout-important
The transformation involves the generator $T$, which is a flavor matrix. However, the covariant derivative $D$ also contains $T$, but here it acts in the color space, not the flavor space.
:::
In the flavor space, the transformation is diagonal (identity matrix $I$), so the flavor transformation is simple. The phase difference introduces a relative minus sign between the left- and right-handed components.

<!--
Cosine simularity: 0.9289380400918554
-->
## Gamma Matrices and Flavor Space Transformations

The transformation space is straightforward, with the phase introducing a minus sign. The bar operation denotes $\gamma^0$, so it's better to label indices as $\alpha_I$ where $I = 1, 2, 3$. Alternatively, we can use $Z = 1, 2, 3$ or $D$ for clarity.  

We replace all states here with left- and right-handed components using the projection operator. The sum can be written explicitly, leveraging the properties of gamma matrices under Hermitian conjugation. The vector part of the interaction is given by:

$$
\bar{\Psi}_L \gamma^\mu \Psi_L + \bar{\Psi}_R \gamma^\mu \Psi_R
$$

There is no interaction mixing right- and left-handed components. The covariant derivative $D_\mu$ has no flavor space indices, so it remains unaffected.  

The current symmetry corresponds to independent transformations of the left- and right-handed components. We consider a global symmetry where the transformation is parameterized by eight numbers for the left-handed rotation and eight for the right-handed rotation, totaling 16 real parameters. Applying this transformation leaves the Lagrangian invariant if the mass term is zero, since left- and right-handed states decouple.  

Here, the three-component vector operates in the flavor space (SU(3)), and $\alpha$ is a $3 \times 3$ matrix independent of coordinates. The parameters for left- and right-handed rotations are weighted differently, but the Lagrangian remains unchanged unless a mass term is introduced.

<!--
Cosine simularity: 0.924951473491417
-->
## Spontaneous Symmetry Breaking in QCD

The left-handed and right-handed states do not talk to each other, so there is an extra phase here and another extra phase there. These phases cancel each other, and the symmetry is only broken when mass terms are introduced. This breaks the scale symmetry. The mass term mixes the two states, so the phase appears in one combination of the $\alpha$ parameters and disappears in the other.  

The mass term explicitly breaks chiral symmetry, but there is another effect: chiral symmetry is also spontaneously broken. Even if you start with no mass term in QCD, the quarks generate a non-zero expectation value through their interactions. This means the quarks appear massive even without an explicit mass term in the Lagrangian.  

The QCD vacuum has a non-zero expectation value, expressed as:

$$
\langle 0 |\, \bar{\Psi}_L \Psi_R \,| 0 \rangle \ne 0 \quad \text{for } m_q = 0.
$$

This is a spectacular result — the entire symmetry is broken. To visualize this, imagine a field space where the vacuum state is not at zero but at a shifted location. The potential of the theory has a shape similar to the Higgs potential, resembling a Mexican hat.  

When quantum fluctuations are integrated out, the effective potential takes this form, and the vacuum settles at a non-zero expectation value. This is the essence of spontaneous symmetry breaking. The theory could have a vacuum with exact chiral symmetry (located at zero), but energetically, it is favorable for the vacuum to have a non-zero expectation value.  

This mechanism appears in many areas of physics: superconductivity (where electron pairs form Cooper pairs), the Higgs mechanism, and other examples. The common feature is an exact symmetry at the origin of the field space, but the physical vacuum is displaced due to interactions.  

The spontaneous breaking is driven by the shape of the potential. The interaction terms, when integrated over quantum fluctuations, produce a potential that favors a non-zero vacuum expectation value. This is the origin of the mass gap in QCD, even in the absence of explicit mass terms.  

The current symmetry corresponds to independent transformations of the left- and right-handed components. For a global symmetry, there are eight parameters for the left-handed rotation and eight for the right-handed rotation, totaling 16 real parameters. The Lagrangian remains invariant under these transformations if the mass term is zero, since left- and right-handed states decouple.  

The flavor space (SU(3)) is described by a three-component vector, and $\alpha$ is a $3 \times 3$ matrix independent of coordinates. The left- and right-handed rotations are weighted differently, but the Lagrangian stays unchanged unless a mass term is introduced.

<!--
Cosine simularity: 0.9270950875855584
-->
## Introduction to Chiral Perturbation Theory  

In addition to spontaneous symmetry breaking, chiral perturbation theory also accounts for explicit symmetry breaking. This is introduced by assigning non-zero masses to the quarks. Spontaneous symmetry breaking is the dominant effect, but it is fully captured by the theory. Explicit symmetry breaking is a smaller effect since the quark masses are much smaller than the QCD scale $\Lambda_{\text{QCD}}$.  

Because of this hierarchy, perturbation theory can be applied — and that is the essence of chiral perturbation theory. The theory is built on the existence of a chiral symmetry, and spontaneous symmetry breaking emerges as a consequence. This breaking is treated as a perturbation parameter.  

::: callout-note
The quark masses act as a small perturbation compared to the QCD scale, allowing the use of chiral perturbation theory.
:::
We will not go into a detailed discussion of chiral perturbation theory here, but the key idea is that it systematically incorporates both spontaneous and explicit symmetry breaking.

<!--
Cosine simularity: 0.9153992836731415
-->
## Discussion of Field Expectation Values and Potential  

I will start the next lecture by writing the chiral Lagrangian, and then we will move forward. We won’t have time for a detailed consideration of chiral perturbation theory here, but I encourage you to explore dedicated courses. The theory department has experts in this field, and they are world-leading in their work. My goal today is to introduce the general concepts and provide an experimentalist’s perspective.  

Let me address some questions. The variable in this plane represents the vacuum expectation value. When you write this, the point you choose is the corrected state. It is the expectation value for the correlation. The possibility of $Q$ on both sides is not necessarily zero — it depends on the context.  

The axis represents the expectation value of the field. Strictly speaking, in quantum field theory, the potential itself is undefined. What is defined is the expectation value of the field. You can plot the potential as a function of this expectation value. Here, the expectation value is along the $x$-axis, and the potential $V$ is on the $y$-axis.  

::: callout-note
The quark masses act as a small perturbation compared to the QCD scale $\Lambda_{\text{QCD}}$, allowing the use of chiral perturbation theory.
:::
The key idea is that chiral perturbation theory systematically incorporates both spontaneous and explicit symmetry breaking. The expectation value of the field is central to this discussion, as it defines the potential landscape of the theory.

<!--
Cosine simularity: 0.9311018340240912
-->
## Quasi-Classical Expansion and Field Theory Analogy

I would like this analogy to incorporate complex space, even though we typically expect the potential to be real. The quasi-classical expansion in field theory is a useful framework for this.  

I recall seeing this approach in several books, but I want to discuss its strict definition. Often, we encounter well-defined potentials, but how do we derive them from first principles? This is related to the $\hbar$ expansion.  

$$
H = H_0 + \hbar H_1 + \hbar^2 H_2 + \cdots
$$

Here, $H$ is expanded in powers of $\hbar$, allowing us to systematically approximate the theory. I will find a reference to clarify this further.  

::: callout-note
The quasi-classical expansion provides a bridge between quantum field theory and classical approximations, particularly useful when analyzing potentials and expectation values.
:::
<!--
Cosine simularity: 0.9434389906546551
-->
## Spontaneous Symmetry Breaking and Cooper Pairs in Superconductors

To better understand this, we can look at a simpler model related to spontaneous symmetry breaking in superconductors, where the potential appears explicitly without requiring quantum field theory.  

You mentioned an interaction between particles and antiparticles, such as electrons and positrons. However, in superconductors, it is two electrons that form the Cooper pair.  

::: callout-note
The Cooper pair mechanism involves two electrons binding together at low temperatures, leading to superconductivity.
:::
If you have taken a particle physics course, you might recall the electroweak and Higgs mechanism. This is a key part of understanding symmetry breaking in particle physics, though it is not strictly necessary for the Cooper pair discussion. The underlying principles are similarly strong in both contexts.  

<!--
Cosine simularity: 0.8755107649761839
-->
## QED, Electricity, and Quark Dynamics in QCD

We discussed QED in the particle physics course but did not cover electricity explicitly.  

For heavy quarks, the expansion is different — it is not $\text{quark} / \Lambda_{\text{QCD}}$ but rather non-relativistic. In this regime, you can use the momentum $P$ and the non-relativistic QCD framework (NRQCD) with $r_{\text{QCD}}$ as the characteristic scale.  

::: callout-note
NRQCD simplifies quark dynamics for heavy quarks by treating them non-relativistically, where $P \ll m_Q c$ and $r_{\text{QCD}}$ defines the confinement scale.
:::
<!--
Cosine simularity: 0.9212222031542752
-->
## Project Discussion and Internship Opportunities  

We discussed RQ (Relativistic QCD) and NRQCD (Non-Relativistic QCD) in the context of momentum $P$.  

For summer project discussions, we will organize an event on **June 28th**, inviting bachelor's, master's students, and others interested in available projects and internships.  

::: callout-note
NRQCD simplifies quark dynamics for heavy quarks where $P \ll m_Q c$ and $r_{\text{QCD}}$ defines the confinement scale.
:::
<!--
Cosine simularity: 0.9571312503858783
-->
## Assignment Distribution and Instructions  

I will send out details about available projects and internships on **June 28th**.  
