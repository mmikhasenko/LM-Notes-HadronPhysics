### Symmetry, Hadron Structure, and Isospin in Meson and Baryon Systems


Thanks everyone who found the room, and apologies for changing it all the time.
We are fixed now. From now on, this room is booked, and we will continue using it—hopefully for the next 10 lectures.

Today we have **lecture number three**.
We will follow the discussion of **symmetry** from the last lecture, but also introduce and look more carefully at what we know about the **structure of hadrons**: how they look inside and what the actual experimental evidence is that they are not point-like, that they're made of quarks.

---

We will go through this list:

1. **Kinematics and cross sections**:
- Calculation of cross sections.
- Multibody kinematics.
- Start with classical scattering of an electron and a proton.

2. **Form factors in scattering**:
- Relation to hadron properties.
- Connection to classical quantities like charge distributions and magnetic moments.

3. **Quark model**:
- Hadrons as quark composites.
- Relating experimental distributions to internal structure.

4. **Symmetry considerations**:
- Flavor symmetry.
- Spin symmetry.

5. **Proton and neutron spin-flavor wave functions**:
- Magnetic moment computation in the quark model.
- Relation to observables.

> [!NOTE]
> **Key Formula**: Magnetic moment in the quark model:
> $$
> \mu = \sum_i \mu_i = \sum_i q_i \frac{e\hbar}{2m_i} \langle \sigma_z \rangle_i
> $$
> where $q_i$, $m_i$, and $\langle \sigma_z \rangle_i$ are the charge, mass, and spin projection of the $i$-th quark.

---

Before starting, I wanted to pose a question to recap. There are two questions:

1. **First question**:
- What is the isospin of the $D$ meson?
- Specifically, the $D^+$ meson ($c\bar{u}$) and the $D^0$ meson ($c\bar{d}$).

2. **Second question**:
- What is the isospin of the $\Xi_{cc}$ baryon and its quark content?

> [!IMPORTANT]
> **Isospin Assignments**:
> - For $D^+$ ($c\bar{u}$) and $D^0$ ($c\bar{d}$): $I = \frac{1}{2}$.
> - For $\Xi_{cc}$ ($ccu$ or $ccd$): $I = \frac{1}{2}$.

---

Isospin symmetry is related to the symmetry of the wave functions with respect to the light quarks.

- You have a $u$-quark or $d$-quark. These are two light quarks, and they get replaced by whatever they are.
- The wave function has two components, $\psi_{up}$ and $\psi_{down}$, corresponding to the up and down as a two-component spinor function.
- This multiplicity-two wave function corresponds to the $+\frac{1}{2}$ or $-\frac{1}{2}$ isospin projections.

**Key Points**:
- One light quark $\implies$ isospin $\frac{1}{2}$.
- Two light quarks $\implies$ combined isospin $1$ or $0$.

---

The second question:
- $J/\psi$ ($J^P = 1^-$) decays to two vector particles ($1^-$ each).
- What is the orbital angular momentum $L$ between them for parity conservation?

> [!NOTE]
> **Parity Constraint**:
> $$
> P_{final} = (-1)^L \cdot P_{V_1} \cdot P_{V_2} = (-1)^L \cdot (-1) \cdot (-1) = (-1)^L
> $$
> Since $P_{J/\psi} = -1$, $L$ must be **odd** ($1, 3, \dots$).

**Possible Configurations**:
- Total spin combinations: $0$, $1$, or $2$.
- Orbital angular momentum: $L = 1$ (P-wave), $L = 3$ (F-wave), etc.

---

Why don’t you have isospin for heavier quarks?

- The Lagrangian doesn’t obey symmetry if quark masses differ significantly.
- Example: Changing $s$ to $c$ breaks symmetry because $m_s \neq m_c$.
- For $u$ and $d$ quarks: masses are nearly equal $\implies$ isospin symmetry holds.

**Extension to SU(3) Flavor Symmetry**:
- Includes $u$, $d$, $s$ quarks:
$$
\text{SU(3)}_f \supset \text{SU(2)}_I \times \text{U(1)}_Y
$$
- Charm quark could be included if masses were equal (hypothetical).

---

- **Isospin partners**: Identify quark content and name (e.g., $D^+$ and $D^0$).
- **LHCb convention**: Charge-conjugated states are implicitly included in analyses.

**Spin-Orbit Combinations**:
- Learn to fill the table of possible quantum numbers for decays.
- Example: For $L = 2$ (D-wave), total angular momentum can be $2^+$, $1^+$, or $3^+$.

### Decay Analysis, Hadron Structure Probes, and Scattering Formalism



The next step is to look at what is decaying and identify within this table what decays.
I'm looking at this list, and one that decays is \(1^-\).
I have it here, here, here—so **four combinations**.
The answer to this question is it decays into two.

Let me remove identical particles because identical particles make it more difficult.
Two identical particles cannot be in a certain configuration of \(S\).
We will come back to this identical particle point later.

> [!IMPORTANT]
> For identical particles:
> - These two are forbidden for \(L=3\)
> - Three combinations forbidden when considering \(L=3\) and the cases shown
> - Only remains when \(L + S\) is even (since \(3 + 2 = 5\) is odd)

But identical particles will make these two forbidden.
For \(L=3\), these two are forbidden.
For \(L=3\) and the two you showed—three forbidden.
I think I remember that \(L + S\) must be even for identical particles.
So \(3 + 2\) is odd.
This is why only one combination remains.
For identical particles, only one decay is allowed, while for non-identical particles, all four combinations are possible.

---


Second question:
You read this and realize you need to:
1. Draw a table like this
2. Quickly fill it—it's **super easy**
3. Identify what is stable

That's it.
Questions?
This is a skill you'll learn so you never have trouble with combinatorics.

---


To understand the structure of hadrons, you need a **well-understood probe**—a standard current insertion into the hadron.
To study strong interactions and how hadrons are organized, we use electromagnetic interactions.
We scatter electrons off protons and analyze the reaction in kinematic phase space.

The electron side is simple: the electron is point-like and interacts with the proton's electromagnetic field.
This is well understood.

The proton side is more interesting:
- At **low momentum transfer**, the electron sees the proton's charge
- At **high momentum transfer**, the electron starts probing the quarks inside the proton

This is like smashing a large cucumber with an electromagnetic current.
At low momentum transfer, you see the proton's characteristics.
At high momentum transfer—visible in large electron scattering angles—you probe the proton's internals.
This is the idea behind **deep inelastic scattering**.
Large accelerators are built to study this process.

---


For a \(2 \to 2\) reaction, the observables are simple:
- **Total energy** (set by beam energy)
- **Electron scattering angle**

More familiar quantities are the center-of-mass energy and scattering angle.
But Mandelstam variables \(s\) and \(t\) are more natural:

$$
s = (p_1 + p_2)^2 \quad \text{(center-of-mass energy squared)}
$$

$$
t = (p_1 - p_3)^2 \quad \text{(momentum transfer squared)}
$$

In the center-of-mass frame:

$$
\sqrt{s} = E_{\text{total}} = E_e + E_p
$$

The proton momentum \(p_p^* = -p_e^*\) (star denotes center-of-mass frame).

For \(t\):

$$
t = m_e^2 + m_e^2 - 2E_e E_e' + 2|\vec{p}_e||\vec{p}_e'|\cos\theta
$$

At high energy, this simplifies to:

$$
Q^2 = -t = 4E_e E_e' \sin^2(\theta/2)
$$

---


To connect theory to experiment, we use cross sections.
The differential cross section depends on the matrix element \(\mathcal{M}\):

$$
\frac{d\sigma}{d\Omega} = \frac{1}{64\pi^2 s} \frac{|\vec{p}_f|}{|\vec{p}_i|} |\mathcal{M}|^2
$$

The total cross section integrates over phase space:

$$
\sigma = \int |\mathcal{M}|^2 \, d\Pi
$$

Phase space counts final-state configurations.
For \(n\) particles:

$$
d\Pi_n = \prod_{i=1}^n \frac{d^3p_i}{(2\pi)^3 2E_i} (2\pi)^4 \delta^{(4)}\left(p_{\text{initial}} - \sum p_i\right)
$$

For 2-body final states:

$$
d\Pi_2 = \frac{|\vec{p}^*|}{8\pi\sqrt{s}} d\Omega^*
$$

The flux factor normalizes the cross section:

$$
F = 4E_1E_2|v_1 - v_2|
$$

---


In elastic scattering, \(Q^2\) (the spacelike momentum transfer) is key.
The beams' energy is fixed; the scattering angle determines \(Q^2\).
Electrons scatter at different angles:
- **Small \(Q^2\)** (small angles): probe proton charge distribution
- **Large \(Q^2\)** (large angles): probe quark structure

For small-angle scattering, we measure:
1. Proton charge radius (approximated by \(\rho(r) \sim e^{-r/R}\))
2. Magnetic moment \(\vec{\mu}\), which interacts with external fields:

$$
H_{\text{int}} = -\vec{\mu} \cdot \vec{B}
$$

### Phase Space: Counting Configurations and Two-Body Kinematics


**Phase space** is nothing else but the continuous version of the counting of possible configurations.
It's very easy for the **two-body phase space**, a little trickier for the **three-body phase space**, and gets rather complicated for **four-body and five-body**.
But it's always a standard integral. We compute this numerically if we need to.

For the **two-body case**, there was a classwork to compute this.
We will meet this expression very often, so I will give the expression for **two-body phase space**.

Let's first count the number of variables:
- Every **delta function** gives the energy-momentum constraint, which removes one integration variable.
- So you can count the number of differentials $d$ that appear—this is the number of variables to integrate—and then subtract the number of constraints.
- Each constraint allows us to remove one integration variable.

For **two-body phase space**, how many differentials do we have initially?
The answer is **six**.
Now subtract **four constraints** (from energy-momentum conservation).
We are left with **two degrees of freedom**.

If we proceed wisely, we can trade each constraint for a differential, leaving us with two remaining variables.
The resulting expression (which Drawn should send you) is:

$$
d(\text{phase space})_2 = \frac{1}{8\pi} \frac{\lambda^{1/2}(s, m_1^2, m_2^2)}{s} \frac{d(\cos\theta) \, d\phi}{4\pi}
$$

> [!IMPORTANT]
> The **Källén function** $\lambda(s, m_1^2, m_2^2)$ appearing in the phase space formula is defined as:
> $$
> \lambda(s, m_1^2, m_2^2) = s^2 + m_1^4 + m_2^4 - 2sm_1^2 - 2sm_2^2 - 2m_1^2m_2^2
> $$
> This governs the energy dependence of the phase space volume.

This is a great exercise because it's **totally analytic** and contains many **physical insights**.
I recommend doing it **three times**: once, then again, and a third time—then you truly understand it.

This expression has **two remaining differentials**, corresponding to an integral over spherical angles.
In **2-to-2 scattering**, there is one variable (the scattering angle $\theta$) that determines the process, but there is also an **azimuthal angle $\phi$**.
If the problem is **unpolarized**, the matrix element does not depend on $\phi$, so we can ignore it.

Imagine a coordinate system:
- The **z-axis** is the collision axis.
- The **x- and y-axes** are transverse.
The scattered electron has an angle $\theta$ relative to the z-axis and an azimuthal angle $\phi$ in the XZ plane.

If there is no spin or preferred direction, the physics is **independent of $\phi$**.
For the **total cross section**, we integrate over $\phi$ and replace it with $2\pi$:

$$
\int d\phi = 2\pi
$$

The **nontrivial part** is the $\cos\theta$ dependence, which relates to $Q^2$ and probes the **parton structure**.

The **kinematic factor** $\lambda^{1/2}(s, m_1^2, m_2^2)/s$ tells us the number of configurations available at a given energy.
- At **low energy** (close to threshold), this factor **suppresses the phase space**.
- It **vanishes** when $s = (m_1 + m_2)^2$, meaning no phase space is available below threshold.

This makes sense:
- If the system energy is **barely enough** to produce the particles, there are very few possible configurations.
- In the **non-relativistic limit**, the phase space is simply given by the number of angular configurations ($4\pi$).
- But for **relativistic particles**, we get this suppression factor near threshold.

**Questions?**

---

I’ve been thinking about how knowledge will be acquired in the future. 
How will we **"upload" knowledge into students' brains**? 
I think it will involve **interactive training**, like a ChatGPT that forces you to apply concepts repeatedly. 
 
1. First, information is explained (like in this lecture). 
2. Then, **immediate testing**—perhaps a quiz or derivation exercise. 
3. Next, a **gaming-like format** where you solve problems interactively. 
 
For example: 
- *"What is the high-energy behavior of phase space?"*—and you figure it out through **guided exploration**. 
 
Imagine **"Duolingo for hadron physics."** 
After a few sessions, you **master the material**. 
This is what we try to do with **homework**—please work on it. 
This is your chance to **learn deeply**. 
 

### Matrix Elements, Form Factors, and Proton Structure in Scattering Theory


We discussed this in scattering. Let me quickly tell you what the matrix element is. The matrix element you see there is a **key input** to the reactions.

This is something we can derive if we have a theory of interaction. If we don't have a theory, as often happens in hadron physics, we can use **general principles** to come up with the matrix element. For electromagnetic processes, we do have a theory: **QED plus QCD**.

We know how to write an expression that, when squared, gives the cross-section. The sum over final states and the average over initial states yields a mathematical expression we can compare to experiment. This expression can only depend on two variables: $s$ and $t$.

> [!NOTE]
> The matrix element for electromagnetic scattering in QED + QCD is given by:
> $$
> \mathcal{M} = \bar{u}(p_3) \gamma^\mu u(p_1) \left( \frac{-ig_{\mu\nu}}{q^2} \right) \bar{u}(p_4) \left[ F_1(q^2) \gamma^\nu + F_2(q^2) \frac{i\sigma^{\nu\rho} q_\rho}{2M} \right] u(p_2)
> $$
> where $F_1(q^2)$ and $F_2(q^2)$ are form factors, and $q = p_3 - p_1$ is the momentum transfer.

---

The matrix element is defined in the domain of the phase space variables. The phase space, as we discussed, is a function of two variables. In the unpolarized case, there is no $\phi$ dependence, so only $\theta$ remains. Therefore, the matrix element in our case will be a function of the **scattering angle**. It also depends on the total energy, which is fixed by the colliding particles.

This mathematical expression is complex. In field theory, it is formally defined as part of the scattering matrix. You have initial states at $t = -\infty$ and final states at $t = +\infty$, with non-interacting particles asymptotically. The matrix element is the expectation of the interacting operator between these asymptotic states.

It is a complex function, but its absolute value squared gives a real value. So it is a complex function of $s$ and $t$. When $s$ is fixed, it becomes a function of $t$ alone.

---

Let me write something you might have seen in field theory. In field theory, scattering is approached using **perturbation theory**, expanding order by order in the number of interactions. Each electron-current interaction introduces a factor of $\alpha = \frac{1}{137}$.

A series expansion works because the first term already gives a good approximation of the total cross-section. For electromagnetic processes, we consider the **first-order interaction**. Each term in this expansion corresponds to a Feynman diagram.

Here, I draw a diagram and write the corresponding mathematical expression. Something here might not be familiar: $F_1$ and $F_2$ are **form factors**. These functions appear because the proton is not point-like. If it were, $F_2$ would vanish, and $F_1$ would be trivial. But they are not, so we must measure them experimentally.

$u$ is a spinor, and $\Gamma$ is a gamma matrix. The dimensionality of the matrix element is important—you must ensure all indices match. For example, this $\mu$ contracts with this $\mu$.

The spinors and matrices combine to form scalars or vectors depending on the contractions. $F_1$ and $F_2$ are scalar functions. To derive the cross-section, we square the matrix element and perform spin summations.

---

The final expression is the **Rosenbluth formula**:

$$
\frac{d\sigma}{d\Omega} = \left( \frac{d\sigma}{d\Omega} \right)_{\text{Mott}} \left[ G_E^2(q^2) + \tau G_M^2(q^2) \right] \frac{1}{1 + \tau} + 2\tau G_M^2(q^2) \tan^2 \left( \frac{\theta}{2} \right)
$$

where:
- $\left( \frac{d\sigma}{d\Omega} \right)_{\text{Mott}}$ is the Mott cross-section,
- $G_E(q^2) = F_1(q^2) + \tau F_2(q^2)$ (electric form factor),
- $G_M(q^2) = F_1(q^2) + F_2(q^2)$ (magnetic form factor),
- $\tau = \frac{q^2}{4M^2}$.

---

It includes a $\frac{1}{\sin^4 \theta}$ term from the $\frac{1}{Q^2}$ dependence, where $Q$ is proportional to $\sin \theta$. This leads to a divergence at small angles, making forward scattering non-integrable without regularization.

For convenience, we replace $F_1$ and $F_2$ with $G_E$ and $G_M$. These are what experiments measure. Their $Q$-dependence reveals properties of the proton.

The $Q$-dependence is dual to the spatial distribution via Fourier transform. Measuring $G_E(Q^2)$ lets us infer the proton's charge distribution. Exponential spatial distributions correspond to dipole parameterizations in momentum space.

One key question is the proton's charge radius. Experiments and lattice QCD calculations extract this from the $Q$-dependence of form factors.

---

The magnetic form factor $G_M$ at $Q = 0$ gives the hadron's magnetic moment. The magnetic moment is:

$$
\vec{\mu} = g \left( \frac{e}{2m} \right) \vec{S}
$$

where $g = 2$ for point-like Dirac particles.

For the proton and neutron, experiments show deviations from this prediction. The proton's magnetic moment is not 2, and the neutron's is not zero. The ratio $\mu_p / \mu_n \approx -1.46$ suggests a composite structure.

In the quark model, the proton's magnetic moment arises from its quark constituents. The up and down quarks contribute differently, explaining the observed ratio. We can write the proton's wave function in terms of quark flavors and spins.

The quark model assumes that gluonic degrees of freedom are integrated out, leaving massive constituent quarks. These quarks carry most of the proton's properties, with up quarks at $+\frac{2}{3}e$ and down quarks at $-\frac{1}{3}e$.

---

Today, we discussed:
- Electron-proton scattering kinematics,
- Form factors and their relation to charge and magnetic properties.

Next time, we will derive the quark model predictions for magnetic moments.

### Closing Remarks


**All right, thanks for your attention.**

---

> [!NOTE]
> This concludes the lecture segment. No technical content was present in this portion to analyze or enhance with nuclear physics formulas.

