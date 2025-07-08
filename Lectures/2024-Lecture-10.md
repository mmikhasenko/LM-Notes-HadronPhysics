### Calculating Cross Sections and Spin Algebra in Scattering Processes


Let me recap what we discussed in the lecture.
I had two excellent problems before moving to the exercise.

I would like you to calculate the cross section for the scattering of two massless particles.
Each matrix element is given for spin-zero scalar particles.
Calculate the cross section and give the answer in **millibarns squared**.

**Steps for the calculation:**
1. First, calculate the cross section—remember the equation for how we compute it.
2. The whole computation is straightforward once you put the numbers in.

The **cross section formula** is:
$$
\sigma = \frac{1}{2s} \times |\mathcal{M}|^2 \times \frac{1}{8\pi} \frac{2p}{\sqrt{s}}
$$

- The matrix element squared gives $3 + 9 + 4 = 13$.
- Here is the **flux**, and here is the **phase space**.

The **phase space** is:
$$
\frac{1}{8\pi} \frac{2p}{\sqrt{s}}
$$

- The term $\frac{2p}{\sqrt{s}}$ must be calculated given the masses and energy.
- For this case, it simplifies to $\sqrt{s}/4$.
- Since momentum equals energy for massless particles, $p = \sqrt{s}/2$.
- Thus, this factor becomes 1, leaving just $\frac{1}{8\pi}$.

Now, consider the **flux**:
$$
\text{Flux} = \frac{1}{2E} \frac{1}{|v_1 - v_2|}
$$
- Both energies are half the total energy, and $v_1 - v_2 = 2$ in the lab frame (since velocities are equal and at the speed of light).
- This simplifies the flux to 2.

**Putting it all together:**
$$
\sigma = \frac{1}{2s} \times 13 \times \frac{1}{8\pi} = \frac{13}{16\pi s}
$$
In $\text{GeV}^{-2}$, this is $\frac{13}{8\pi}$.

For **unit conversion**:
$$
1 \text{ GeV}^{-2} = 0.2 \text{ millibarns}
$$
Thus, the cross section is:
$$
\frac{13}{8\pi} \times 0.2 \text{ millibarns}
$$

> [!NOTE]
> The final numerical result depends on simplifying $\pi \approx 3$, but the **method** is what matters.
> The key is starting with the correct equations for cross section, flux, and phase space.

---

Now, consider the **imaginary part** of the matrix element.
Using the **optical theorem**:
$$
\sigma_{\text{total}} = \frac{\text{Im}\,\mathcal{M}(0)}{2p\sqrt{s}}
$$
This gives the **total cross section**, not just the elastic one.

- The total cross section includes all processes: $AB \to AB$, $AB \to CD$, etc.
- It should be larger than the elastic cross section.
- If the imaginary part gives a negative result, it’s **unphysical**—the imaginary part must be positive.

**Example: Breit-Wigner resonance**
$$
\mathcal{M} = \frac{\Gamma/2}{(E - E_0) - i\Gamma/2}
$$
Its imaginary part is always positive.

- Recall the **Argand diagram**: the imaginary part (y-axis) must be non-negative.
- This constraint ensures physical results.

---

Now, for the second problem: **spin algebra**.
You need to combine spins and compute partial waves.
The brute-force method involves constructing a table of quantum numbers.

**Example:**
- The $b_1$ meson with spin-parity $1^+$.
- Combining $1^-$ and $1^+$ in S-wave gives $1^-$.
- D-wave also allows $0^-, 1^-, 2^-$.

**Exotic Quantum Numbers:**
- The $\pi_1(1600)$ has exotic quantum numbers $1^-+$, forbidden in the quark model.
- It’s interpreted as a **hybrid meson**, with excited gluonic degrees of freedom.
- Originally misidentified as $\pi_1(1400)$, it was corrected with better data.

---

> [!IMPORTANT]
> Key takeaways:
> - Cross section calculations require careful handling of flux and phase space.
> - The optical theorem links the imaginary part of the amplitude to the total cross section.
> - Spin composition rules are essential for understanding particle interactions.

### Scattering Length Dimensionality and Spin-1/2 Particle Representations


I thought it's important to clarify. The notations got mixed up a little bit at the last lecture concerning the scattering length. The scattering length is indeed measured in **Fermi**. However, when you use relativistic notations, it appears **dimensionless**.

In quantum mechanics, the scattering length is defined as an expansion of the amplitude in terms of \( K \), the breakup momentum. \( K \) has units of **GeV**, so \( 1/A \) has units of **GeV**, and \( A \) itself is in **Fermi**. The non-relativistic amplitude has a denominator:
$$
F_{\text{non-rel.}} = \frac{1}{A - iK}
$$

In the relativistic formulation, unitarity tells us that the imaginary part of the amplitude is related to the phase space, which is dimensionless. The first expansion term is again something like the scattering length, but it is dimensionless. If you still want to talk about **Fermi**, you have to relate this to that, and the relation happens at the threshold.

Since it's a threshold expansion, you would like these amplitudes to match up to a numerical constant at the threshold. In this exercise, I want you to relate these two at the threshold and determine what the relativistic amplitude is near threshold. I even give you the answer—the only thing missing is the value of \( \tilde{A} \).

The scattering length is equal to **three Fermi**, corresponding to \( A \). Knowing that, you need to compute \( \tilde{A} \). The way to do this is not simply to equate the amplitudes at threshold, because then you miss the point. If you evaluate the non-relativistic amplitude at threshold (\( K = 0 \)):
$$
F_{\text{non-rel.}} = A
$$
while the relativistic amplitude is \( \tilde{A} \). They are not equal—there is a numerical constant to account for.

To equate them, you must compare numerators or denominators up to a numerical constant and examine the coefficients in front of \( K \). One approach is to Taylor-expand the expression where \( S \) is a function of \( K \) and equate the first term. Alternatively, notice that the only difference between numerators is the factor \( 1/(8\pi^2 s) \).

At threshold, the condition to convert one to the other is:
$$
\tilde{A} = \frac{A}{8\pi^2 s_{\text{thr}}}
$$
To solve this, you need the masses and the threshold value. For example, if \( s_{\text{thr}} = 1 \, \text{GeV}^2 \), then \( \tilde{A} = A / (8\pi^2) \).

---

> [!IMPORTANT]
> **Key Insight**: The relativistic and non-relativistic scattering lengths differ by a factor of \( 8\pi^2 s_{\text{thr}} \). This conversion is essential for matching amplitudes at threshold.

---

This is widely used and provides interesting insights into hydrodynamics, which relies on the extra symmetry observed when particle masses are zero—called **chirality**. This is related to spin orientation for spin-1/2 particles.

We now return to particles carrying spin information, focusing on **spin-1/2** and their field-theoretical representation. Spin-1/2 particles obey the Dirac equation:
$$
(P\!\!\!/ - m)U = 0
$$

**Notations**:
- \( P\!\!\!/ = P_\mu \gamma^\mu \) (contraction of four-momentum with \( \gamma^\mu \) matrices).
- \( \gamma^0 \) is part of the Dirac matrices.

There are two common conventions for solving the Dirac equation:
1. The **Dirac convention**
2. The **Weyl convention**

The Weyl convention is more convenient for right- and left-handed particles, but we will stick to the standard **Dirac convention**.

The \( \gamma^\mu \) are four-dimensional matrices, and \( P \) is a four-vector. Contracting them gives \( P\!\!\!/ \), a \( 4 \times 4 \) matrix. The term \( P\!\!\!/ - m \) implies \( m \) is multiplied by the identity matrix. \( U \) is a four-component spinor (in German, "Spinor").

The Dirac equation has two solutions for a given momentum \( P \). If \( P \) has spatial components, the matrix equation yields two spinors, \( U_1 \) and \( U_2 \):
$$
U_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad U_2 = \begin{pmatrix} P \cos \theta \\ \sin \theta \end{pmatrix}
$$
These correspond to canonical states with spin quantized along the \( Z \)-axis, with projections \( +1/2 \) and \( -1/2 \).

To transform these to helicity states (spin quantized along momentum), we use a linear combination. The canonical state is defined as a pure boost acting on the \( |J, M\rangle \) state at rest.

The transformation between canonical and helicity states involves an extra rotation \( R^{-1} \) to match the canonical state, followed by \( R \). The resulting state is a linear combination of canonical states with coefficients given by **Wigner \( D \)-matrices**.

There are two conventions for the Wigner \( D \)-function:
1. **Standard**: \( R(\phi, \theta, \psi) = R_z(\phi) R_y(\theta) R_z(\psi) \).
2. **Simplified (for helicity states)**: \( R(\phi, \theta, 0) = R_z(\phi) R_y(\theta) \).

The \( D \)-function describes rotations with spherical angles \( \theta, \phi \). The simplified convention omits the unobservable phase from the first \( R_z \) rotation.

Applying this to helicity states, we get:
$$
U_{\text{helicity}} = N \begin{pmatrix} \cos(\theta/2) \\ e^{i\phi} \sin(\theta/2) \\ \cos(\theta/2) \\ e^{i\phi} \sin(\theta/2) \end{pmatrix}
$$
where \( N = \sqrt{E + m} \) is the normalization. For the lower spinor component:
$$
U_{\text{down}} \approx \frac{P}{E + m} \begin{pmatrix} \cos(\theta/2) \\ e^{i\phi} \sin(\theta/2) \end{pmatrix}
$$
When \( m \ll E \), \( P \approx E \), and this factor approaches 1, simplifying the spinor.

### Properties and Applications of Chiral Projection Operators


Now let me introduce **projection operators**, which will allow us to move on.

The $\gamma^5$ matrix is introduced as the product of the gamma matrices with the Levi-Civita symbol:

$$
\gamma^5 = i \gamma^0 \gamma^1 \gamma^2 \gamma^3.
$$

This is the convention we choose.

---

It is very convenient for describing interactions to introduce **right-handed** and **left-handed projection operators**:

$$
P_R = \frac{1}{2}(1 + \gamma^5), \quad P_L = \frac{1}{2}(1 - \gamma^5).
$$

> [!NOTE]
> These projection operators satisfy key properties:
> - $P_R^2 = P_R$, $P_L^2 = P_L$ (idempotence)
> - $P_R + P_L = 1$ (completeness)
> - $P_R P_L = P_L P_R = 0$ (orthogonality)

---

Why are they projection operators? Because when they act twice on a state, nothing changes:

$$
P_R^2 = P_R, \quad P_L^2 = P_L.
$$

Let’s verify this explicitly for $P_L$:

$$
\left(\frac{1 - \gamma^5}{2}\right) \left(\frac{1 - \gamma^5}{2}\right) = \frac{1 - 2\gamma^5 + (\gamma^5)^2}{4}.
$$

Since $(\gamma^5)^2 = 1$, this simplifies back to $\frac{1 - \gamma^5}{2}$.

---

Another key property is that their sum is the identity:

$$
P_R + P_L = 1.
$$

The spaces they project onto are **orthogonal**. If you project onto the left-handed space, there are no right-handed components left:

$$
P_R P_L = P_L P_R = 0.
$$

---

An important consequence arises from the fact that $\gamma^5$ **anti-commutes** with all $\gamma^\mu$:

$$
\{\gamma^5, \gamma^\mu\} = 0.
$$

This implies that:

$$
P_R \gamma^\mu P_L = 0.
$$

Here’s why: if you start with $P_L$, multiply by $\gamma^\mu$, and swap the order using the anti-commutation relation, you get $P_R$, and $P_R P_L = 0$.

---

Any spinor can be **decomposed** into right-handed and left-handed components:

$$
\psi = P_R \psi + P_L \psi = \psi_R + \psi_L.
$$

---

Now, let’s give **physical meaning** to these states. Consider a helicity spinor (spin-up or spin-down). We can decompose it into right-handed and left-handed parts using the explicit matrix forms of the projection operators.

In a simplified representation:

$$
P_R = \frac{1}{2} \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}, \quad P_L = \frac{1}{2} \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}.
$$

> [!NOTE]
> These are symbolic representations; the full forms are $4 \times 4$ matrices in the standard Dirac basis.

Using these, we can decompose the spinor into its **chiral components**. The result is a clean separation, which is very useful for analyzing interactions.

### Chirality, Helicity, and the \(V-A\) Interaction in Particle States


It's cumbersome dealing with \(4 \times 4\) matrices. This product will give me blocks, and the second component gives me what is inside the block.

I have this state acting on the spinor, which is \(\begin{pmatrix} 1 \\ 1 \end{pmatrix}\). When I do multiplication, I multiply in components. That's **super convenient**.

When I do the projection, I realize that the left component from the operator yields a small factor \(1 - \kappa\) that is negligible—vanishing at high energy when mass gets smaller. The component of my right-handed helicity state is a spinor \(\frac{1}{2}\) and has an intrinsically small left-handed component.

---

There is no single interpretation of the right-handed and left-handed states. However, they are closely related to the spin orientation along the direction of motion in the limit of zero mass. When a particle moves at the speed of light, they are literally the same constants.

When you hear **"right-handed,"** it means the particle travels with spin aligned with the direction of motion. When you hear **"left-handed,"** it means the spin is opposite. But when the mass is significant—or when \(m\) is not much smaller than \(E\)—things get mixed, and the state becomes a superposition of both components.

> [!IMPORTANT]
> **Chiral Projection Operators** define right-handed and left-handed states:
> \[
> P_R = \frac{1 + \gamma^5}{2}, \quad P_L = \frac{1 - \gamma^5}{2}
> \]
> These operators are key to understanding the **V-A interaction** structure in the Standard Model.

---

It's very interesting that in the Standard Model, the \(W\) boson, when it decays weakly, produces only the right-handed component for leptons and the left-handed component for antileptons. This happens due to the structure of the Lagrangian.

You’ve likely heard that the dominant interaction in the Standard Model is the \(V-A\) interaction. Here:
- \(V\) stands for **vector** (\(\gamma^\mu\)),
- \(A\) stands for **axial** (\(\gamma^\mu \gamma^5\)).

The \(V-A\) structure means the Lagrangian contains terms like \(\gamma^\mu (1 - \gamma^5)\), which can also be written as \(2 \gamma^\mu P_L\), where \(P_L = \frac{1 - \gamma^5}{2}\) is the left-handed projection operator.

This interaction vertex governs processes like \(W\) boson decay into an electron and antineutrino. The electron (\(e^-\)) is left-handed (spin opposite to motion at high energy), while the antineutrino is right-handed (spin aligned with motion).

---

Have you heard about pion decay and spin suppression due to helicity mismatch? No? Good—I’m glad to be the first to explain it.

One must be careful when relating handedness to spin orientation because this one-to-one correspondence only holds in the high-energy limit or for massless particles. For neutrinos, this is always true:
- All **neutrinos** are left-handed,
- All **antineutrinos** are right-handed.

This is why, before neutrinos were well understood, right-handed neutrinos were proposed as new physics candidates—even as potential dark matter.

---

Due to orthogonality, right-handed and left-handed particles in the massless case do not interact. They could even be entirely different particles with different masses. What connects them is relativity.

For massive particles, you can apply a boost \(\Lambda^{-1}\) to bring them to the rest frame and then analyze their spin. But for massless particles, this is impossible—they have no rest frame, and their helicity cannot be flipped.

Right-handed and left-handed states are called **chiral states**. The **chiral limit** refers to the case where \(m = 0\), and particles are purely right- or left-handed.

Helicity is tied to Lorentz transformations—it’s the spin’s alignment with motion. Chirality is closely related but only equivalent for massless particles. There’s no intuitive picture for chirality unless the particle is ultra-relativistic.

In the Lagrangian, chiral states are easier to work with because they are defined by projection operators (\(P_L, P_R\)) and don’t mix under boosts. Helicity states, while easier to visualize, do mix when you change reference frames. A left-handed chiral state remains left-handed no matter how you boost or rotate it.

### Flavor Symmetry and Chiral Limit in QCD Lagrangian


Here is the **Lagrangian of QCD**. The Lagrangian of QCD is not the Standard Model. We don't talk about electromagnetic interactions here. The dynamics of quarks and gluons is described by this Lagrangian:

$$
\mathcal{L}_{\text{QCD}} = \bar{\psi}_I^A (i \gamma^\mu D_\mu - m_I) \psi_I^A - \frac{1}{4} G_{\mu\nu}^A G^{A,\mu\nu}
$$

> [!NOTE]
> Key components of the QCD Lagrangian:
> - $\bar{\psi}_I^A (i \gamma^\mu D_\mu) \psi_I^A$: Kinetic term for quarks
> - $\bar{\psi}_I^A m_I \psi_I^A$: Mass term
> - $G_{\mu\nu}^A G^{A,\mu\nu}$: Gluon field strength term

The $G$ is the gluon field. This is the **gauge part** of the Lagrangian. There are many things here:
- The $\bar{\psi} \partial \psi$ is the **kinetic term**
- $\bar{\psi} m \psi$ is the **mass term**
- The $G$ inside the covariant derivative gives the **interaction** with the gauge field

---

The $I$ is the index for the **flavor**. The main point is that $I$ gives flavor, which is $U, D, S, C, B, T$—one of the six flavors. The $A$ is the **color index**. The $T$ is connected to the local gauge transformation.

I hope you're not afraid of these words. We discussed them before. "**Gauge**" means you can modify this; you can gauge. It means there is a **symmetry** of the Lagrangian, and there are many symmetries here. One of them, discussed in the first lecture, is the **local gauge transformation**, where you can readjust the phase of the color part of the fermion wave function.

---

The $\psi$ is a **fermion wave function**. It has many components, but the color components are in a three-state vector. This is something we can adjust with a local transformation. We do this using a matrix exponent with parameters that depend on the spacetime point $x$. This adjustment can be done at every point of spacetime—that's what "**local**" means. This local transformation determines how gluons and quarks interact, and that's how we construct the covariant derivative:

$$
D_\mu \psi = (\partial_\mu - i g T^A G_\mu^A) \psi
$$

---

We don't go deeper into this; instead, we look at the **flavor symmetry**. The masses of the light quarks—$U, D,$ and $S$—are very small compared to the scale of quantum chromodynamics, which is about **1 GeV**. That's why we consider the **chiral limit**, setting these masses to zero. This is the basis for the low-energy expansion, where the small parameter is the ratio of the quark mass or momentum to $\Lambda_{\text{QCD}}$. This leads to our **effective theory**.

---

What I wanted to discuss now is the **flavor transformation**. Flavor transformation means the flavor indices of the wave function can be rotated. We consider a global $SU(3)$ flavor symmetry. The flavor part of the wave function has three components. We started with $I$ as one of six flavors, but for simplicity, we now focus on the light quarks. The transformation is a global $SU(3)$, represented by a $3 \times 3$ matrix. We can rotate or readjust this wave function freely.

It's important that this is **global**—we don't allow the transformation parameters $\alpha$ to depend on spacetime coordinates. The QCD Lagrangian is symmetric under this transformation. Wherever $\psi$ appears, the phases cancel each other. This is straightforward to see.

---

What might be confusing is the $T$. $T$ is a **Gell-Mann matrix**, and you might wonder how it interacts with the $D_\mu$, since $D_\mu$ also contains $T$. But the $T$ inside $D_\mu$ is the **color Gell-Mann matrix**, acting in a different space. In the flavor space, it's just the identity—there are no matrices here. So the flavor transformation is simple.

The phase comes from the Hermitian conjugate—or rather, the Dirac adjoint $\bar{\psi} = \psi^\dagger \gamma^0$. For clarity, let's label the indices: $\alpha^a T^a$, where $a$ runs from 1 to 8 for $SU(3)$.

---

Now, we project the states into **left- and right-handed components** using the chirality operators:

$$
\psi_L = P_L \psi = \frac{1 - \gamma_5}{2} \psi, \quad \psi_R = P_R \psi = \frac{1 + \gamma_5}{2} \psi
$$

The **vector part** of the interaction is $\bar{\psi}_L \gamma^\mu D_\mu \psi_L + \bar{\psi}_R \gamma^\mu D_\mu \psi_R$. There is no mixing between left and right components. The covariant derivative $D_\mu$ doesn't affect the flavor space, so it doesn't change anything here. The $\gamma^\mu$ could have been $D_\mu$, but I didn't say that.

### Chiral Symmetry and Its Spontaneous Breaking in QCD



**Possible symmetry.** The **chiral symmetry** is the transformation of the right and left components independently. So we want to consider a symmetry.

Let’s check if everything is fine. Here is a three-component vector in the flavor space, $SU(3)$. And here is a $3 \times 3$ matrix. The parameter $\alpha$ does not depend on the coordinates—this is a **global transformation**.

We introduce parameters for the left-handed rotation and right-handed states rotation. We count eight numbers here and eight numbers there, giving **16 random numbers** in total. We apply this transformation, and the Lagrangian doesn’t change unless it has mass.

> [!NOTE]
> **Chiral Transformation of Quark Fields**:
> $$
> q_L \rightarrow e^{i \theta_L^a T^a} q_L, \quad q_R \rightarrow e^{i \theta_R^a T^a} q_R
> $$
> where $q_L$ and $q_R$ are the left- and right-handed quark fields, $T^a$ are the generators of $SU(3)$, and $\theta_L^a, \theta_R^a$ are transformation parameters.

**How do we see that it doesn’t change if the mass is zero?** Because left-handed and right-handed states don’t talk to each other. An extra phase appears here and cancels with the one there—same for the other terms. The symmetry is only broken when mass terms appear. That’s **chiral symmetry**.

The mass term mixes the two components. Here is one combination of the $\alpha$ parameters, and here is the other one. The phases no longer cancel, so the mass term breaks chiral symmetry explicitly.

> [!NOTE]
> **Mass Term Breaking Chiral Symmetry**:
> $$
> \mathcal{L}_{\text{mass}} = -m \bar{q} q = -m (\bar{q}_L q_R + \bar{q}_R q_L)
> $$
> This term mixes left- and right-handed components, explicitly breaking chiral symmetry.

**Now, something I won’t derive but you might have heard:** chiral symmetry is also **spontaneously broken**. Even if you start with no mass term in QCD at low energy, the quarks generate a non-zero expectation value through their interactions. The quarks appear massive even without a mass term in the Lagrangian.

Here is the vacuum. QCD, left side, right side—it’s quite spectacular that the entire symmetry is broken.

> [!NOTE]
> **Spontaneous Symmetry Breaking via Quark Condensate**:
> $$
> \langle \bar{q} q \rangle \neq 0
> $$
> The non-zero vacuum expectation value of the quark condensate signals spontaneous chiral symmetry breaking.

**Imagine a plane of field excitations.** If you’re at zero, chiral symmetry is exact in the Lagrangian, and you can rotate left and right states independently. But the vacuum we live in is not at zero—it’s at a shifted location in field space.

This happens because the potential of the theory has a shape like the **Higgs potential**. For QCD, quark pairs acquire a non-zero expectation value by interacting, so the vacuum resides at a non-zero point in the field space.

> [!NOTE]
> **Mexican Hat Potential (for Illustration)**:
> $$
> V(\phi) = -\mu^2 |\phi|^2 + \lambda |\phi|^4
> $$
> Analogous to the Higgs mechanism, this potential shape describes spontaneous symmetry breaking, where $\phi$ represents the order parameter (e.g., quark condensate in QCD).

**This continuous symmetry-breaking effect appears in many areas of physics:** superconductors (Cooper pairs), the Higgs mechanism, and others. The mechanism is always the same. You have an exact theory at zero in the coordinate space, but once you move away, symmetry breaks spontaneously.

**Think of a Mexican hat potential.** The interaction integrates over gluons, and the resulting potential has this shape. We could live in a vacuum with perfect chiral symmetry, but energetically, it’s favorable to be where the expectation value is non-zero. That’s **spontaneous symmetry breaking**.

**In addition to spontaneous breaking, QCD has explicit symmetry breaking from non-zero quark masses.** Spontaneous breaking is the major effect, captured by the theory. Explicit breaking is smaller since quark masses are much less than $\Lambda_{\text{QCD}}$.

**This is where chiral perturbation theory comes in.** It builds on chiral symmetry, with spontaneous breaking as an outcome. The breaking is treated as a perturbation.

> [!NOTE]
> **Chiral Lagrangian (Low-Energy QCD)**:
> $$
> \mathcal{L}_{\text{chiral}} = \frac{f_\pi^2}{4} \text{Tr}[\partial_\mu U \partial^\mu U^\dagger] + \cdots
> $$
> Here, $U = e^{i \pi^a T^a / f_\pi}$ encodes the pseudo-Goldstone bosons (pions), and $f_\pi$ is the pion decay constant. The ellipsis represents higher-order terms in chiral perturbation theory.

**We won’t go into details of chiral perturbation theory.** Next lecture, I’ll write the chiral Lagrangian, but we won’t have time to explore it deeply. For that, I’d recommend dedicated courses—we have experts in the theory department.

I wanted to give you the **general concepts** and an **experimentalist’s perspective**.

---


**Question:** What is the variable in this plane? Is it the vacuum expectation value?
**Answer:** Yes, the axis represents the expectation value of the field. The potential is drawn as a function of this expectation value.

**Question:** Is the vacuum state always the correct one?
**Answer:** It’s the state with the lowest energy, where the expectation value is non-zero.

**Question:** What’s on the axis?
**Answer:** The expectation value of the field. Strictly speaking, the potential in quantum field theory is defined via the expectation value.

**I’m not entirely happy with this analogy** because the field space should be complex, but let me think of a simpler model, like superconductors, where this is clearer.

**Question:** You mentioned electron-positron pairs earlier, but Cooper pairs are two electrons.
**Answer:** Correct, Cooper pairs are two electrons.

**Question:** Did you cover the Higgs mechanism in the particle physics course?
**Answer:** Some of it, but not deeply.

**Question:** What about heavy quarks?
**Answer:** For heavy quarks, you use a different expansion—potential non-relativistic QCD (pNRQCD).

---

We’ll have a project discussion on **June 28th** for bachelors, masters, and anyone interested in internships. I’ll send details later.

**Thanks!**

