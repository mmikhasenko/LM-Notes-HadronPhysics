### Symmetries in Hadron Physics and Estimating Hadronic Cross Sections


::: callout-note
**Recap of Previous Lecture**  
The homework problems last week were deemed too easy, so we’ll **increase the problem level** this week. Some problems recur across courses—like **Clebsch-Gordan coefficients**, which appear in nuclear physics, particle physics, and quantum field theory. This week’s homework will include them, but they should be manageable.
:::
---

We’ll explore:  
1. **QCD** with the **SU group** (as previously discussed).  
2. The **phenomenology of the SU flavor group**, including:  
   - **Isospin**  
   - **SU flavor** by interchanging *u/d* and squarks.  
3. Connection to the **Lorentz group**, where **SU(2)** is a subgroup responsible for rotations.  

You’ll see how **spin addition** relates to **quark addition inside hadrons**. This builds on **quantum mechanics** material you’ve already seen, and I hope it’s easy to follow.  

::: callout-tip
This is a particularly enjoyable section because the **spin algebra** can be derived independently—just isolate yourself from books and the internet, and you can work through it elegantly.
:::
---

Let’s start with a question from last lecture:  
**How would you estimate the typical cross section of hadronic reactions?**  

The **exact approach** involves:  
$$\sigma = \frac{1}{F} \int |\mathcal{M}|^2 \, d\Phi$$  
where:  
- $\sigma$ = cross section  
- $F$ = flux factor  
- $\mathcal{M}$ = matrix element  
- $d\Phi$ = phase space differential  

This gives the **exact value** in inverse GeV (convertible to cm²).  

---

But what’s the **scale**? We’re dealing with **barns** ($1\,\text{barn} = 10^{-24}\,\text{cm}^2$).  

::: callout-important
**Key Insight**: The cross section represents the **effective interaction area**. For a proton (radius ~$1\,\text{fm} = 10^{-13}\,\text{cm}$):  
$$\sigma \approx \pi r^2 = \pi (10^{-13}\,\text{cm})^2 \approx 3 \times 10^{-26}\,\text{cm}^2 \approx 30\,\text{mb}$$
:::
This is the **typical scale** for hadronic reactions. The **strong interaction** is powerful but **short-range**—particles must overlap to interact.

### Charge Definitions in QED and QCD, and Introduction to SU(2) Group Theory


The second question addressed is how to define charge in **QED** and **QCD**.  

::: callout-important
In QED, the **electric charge** is physical and conserved. It corresponds to a symmetry, as per **Noether's theorem**, which guarantees a conserved current. The charge is defined as the integral of the zero component of this current:  
$$ Q = \int d^3x \, J^0 = \int d^3x \, \psi^\dagger \psi. $$
:::
For a Dirac field, $\bar{\psi}\psi$ involves conjugation with $\gamma^0$, yielding $\psi^\dagger \psi$—a positive quantity. This implies that if $\psi$ represents an electron, it has a **positive charge**. However, this is a convention:  

::: callout-note
The observed charge $Q$ is matched to $-e$ for electrons to align with experimental conventions. The current in QED is:  
$$ J^\mu = -e \bar{\psi} \gamma^\mu \psi. $$  
The $-e$ ensures consistency with standard definitions, but the **conservation** of the quantity is the key takeaway from field theory.
:::
---


The approach in **QCD** is analogous but involves **color indices** and **generators** of $SU(3)$:  

::: callout-important
The QCD current for color charge is:  
$$ J^\mu_a = \bar{\psi} \gamma^\mu T_a \psi, $$  
where $T_a$ are the **Gell-Mann matrices** (generators of $SU(3)$). Unlike QED, quarks have **eight color charges**, corresponding to the gluon probes.
:::
For example, given a quark field $\psi_{\text{color}} = (1, 2, i\sqrt{3})$, its charge is an **eight-component vector**—each component depends on the gluon used to probe it.  

::: callout-tip
This structure arises from **group theory**: QED uses $U(1)$, while QCD uses $SU(3)$. Today, we’ll also discuss $SU(2)$, which shares similar principles.
:::
---


The $SU(2)$ group is fundamental in particle physics. It is a **special unitary group** of $2 \times 2$ matrices with determinant one:  

::: callout-note
For $U \in SU(2)$, the conditions are:  
$$ U U^\dagger = I \quad \text{and} \quad U^\dagger U = I. $$  
The **determinant** is restricted to $1$ (the "$S$" in $SU(2)$).
:::
- **Inverse**: If $g \in SU(2)$, then $g^{-1} \in SU(2)$.  
- **Closure**: For $g_1, g_2 \in SU(2)$, $g_1 g_2 \in SU(2)$.  
- **Identity**: The identity matrix $I$ is included.  

Any $SU(2)$ element can be written as:  
$$ U = \exp\left(-i \alpha_a \sigma_a / 2\right), $$  
where $\sigma_a$ are the **Pauli matrices**:  
$$ \sigma_1 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \sigma_2 = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad \sigma_3 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}. $$  

::: callout-tip
For **nilpotent matrices**, the exponential simplifies. For example:  
$$ \exp\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = I + \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}. $$
:::
---


In quantum mechanics, **spin operators** $J_i$ satisfy:  
$$ [J_i, J_j] = i \epsilon_{ijk} J_k. $$  
The **raising/lowering operators** are:  
$$ J_\pm = J_1 \pm i J_2, $$  
acting on states $|j, m\rangle$ as:  
$$ J_\pm |j, m\rangle = \sqrt{j(j+1) - m(m \pm 1)} \, |j, m \pm 1\rangle. $$  

::: callout-note
The eigenvalues are:  
$$ J^2 |j, m\rangle = j(j+1) |j, m\rangle, \quad J_3 |j, m\rangle = m |j, m\rangle. $$
:::
For quark states (e.g., $\Xi$ particles), **flavor symmetry** treats $u$ and $d$ quarks similarly due to nearly equal masses ($m_u \approx m_d \approx 3 \text{MeV}$).  

::: callout-warning
The $\Xi_{cc}$ (with $ccu$ or $ccd$) shows a **puzzling mass difference**, violating the expected $SU(2)$ symmetry. This remains a **hot topic** in particle physics.
:::
---


We’ve covered:  
1. **Charge definitions** in QED and QCD.  
2. **$SU(2)$ group theory** and its generators.  
3. **Applications** to spin and flavor symmetry.  

Next, we’ll delve deeper into **$SU(2)$ representations** and their role in particle physics.

### Symmetries of the QCD Lagrangian and Quark Mass Hierarchy


When we speak about the symmetries of the Lagrangian of QCD, we have in mind the Lagrangian itself. It consists of two key terms:

1. **Gluon term**: Describes the dynamics of the gluon fields.
2. **Quark term**: The Dirac term, which includes a mass parameter for the quarks.

::: callout-note
The QCD Lagrangian is given by:
$$\mathcal{L}_{\text{QCD}} = -\frac{1}{4}G^{a}_{\mu u}G^{a\mu u} + \sum_{f}\bar{\psi}_f(i\gamma^\mu D_\mu - m_f)\psi_f$$
where:
- $G^{a}_{\mu u}$ is the gluon field strength tensor,
- $\psi_f$ represents quark fields of flavor $f$,
- $m_f$ are the quark masses,
- $D_\mu$ is the covariant derivative.
:::
---

If the quark masses are **not the same**, the mass term will break the symmetry. For the **u and d quarks**, since their masses are almost identical ($m_u \approx m_d$), the symmetry is **not broken** by the mass terms, and this remains a good symmetry.

::: callout-important
The mass term in the Lagrangian is:
$$\mathcal{L}_{\text{mass}} = -\sum_{f=u,d,s} m_f \bar{\psi}_f \psi_f$$
When $m_u \approx m_d$, this preserves an approximate **SU(2) isospin symmetry**.
:::
### Combining Isospin and Spin Representations in SU(2)

**Group.**  
This is so **ud**. Let me sketch this like this: **U to D**. Rotation in the space is a good scene. Then my cascade particle would be in that case, if I consider **U** and **D** to be the same particle as the **SSL** where **L** is the number in the **ISIS spin wave function**. It's clear that cascade.

---

::: callout-note
The **cascade particle** is historically named due to its decay pattern. While its original name is difficult to pronounce (except by Greek speakers), it’s universally referred to as "cascade" in particle physics.
:::
Let me also introduce the language that you might not be familiar with: **Cascade** is the same as this guy. It's just historically people saw this guy decaying in the cascade of particles. That's why. And no one can actually pronounce this correctly except Greek people. So if you want to make sure you spell it correctly, call it **cascade**. Everyone calls it **cascade**.  

The **cascade particle** is now a single particle in our consideration with respect to the **strong interaction** and has **ISIS spin wave function**. This is very similar to the **spin**. We again have a **two-dimensional vector space** in which we can act with the group elements.  

::: callout-important
The **SU(2) Rotation Operator** for isospin transformations is given by:  
$$  
U = e^{-i \alpha \cdot \mathbf{G}}  
$$  
where $\mathbf{G}$ are the generators of **SU(2)** and $\alpha$ are rotation parameters.
:::
So **U** is equal to $e^{-i\alpha G}$. Then what is the charge of the group of this vector? Take it in right? You put it to the equation for the charge and then we get essentially now it's clear what the spin stands for.  

**Isospin** is the same way as the spin would give **one half** for this and **minus one**. You get it right? Acting well, it's a **doublet** corresponds to the two components. The dimension of the representation is **2**, it corresponds to the spin or isospin **1/2**. We just counted.  

::: callout-tip
The **Isospin Doublet Representation** for $u$ and $d$ quarks is:  
$$  
\begin{pmatrix} u \\ d \end{pmatrix}, \quad \text{isospin } I = \frac{1}{2}  
$$
:::
So if I get a multiplet of **four dimensions**, what would be the isospin? Okay, let's come back. **Four dimensions** is **three half**. If it's **95 dimensions**, it'll be **47**.  

Now you might wonder, wait a second, how do we get more than two? We've got two quarks, right? **U** and **D**. How do we get more dimensions if we are not...  

I mentioned here that in grouping mock quarks actually changes the group. We are going to consider a different group. It will be **SU**. We are not talking about **SU**. Now we stick with the **SU** and we only permute two unique quarks.  

**How do we get higher representations, higher dimensions, more particles?** Exactly. The next word: **combining particles, combining representations**.  

---

::: callout-important
The **Clebsch-Gordan Series** for combining two spin-$1/2$ particles is:  
$$  
\frac{1}{2} \otimes \frac{1}{2} = 0 \oplus 1  
$$
:::
The higher dimension of representations appear when I start combining considering particles more than one quark. Because in that case I have to deal with the polling situation. There is one system. There is another system with spin **one half**. But I want to consider them as a system, as a combined system. And I want to characterize the total system by the total either spin or isospin and the projection.  

In that case for **SU**, we are still sitting with the **SU2 group**. You can think of the system as a system of two vectors. The total spin of the system has again constantly. And the total **J** is one of the numbers from...  

Don't remember that. Just think of the vector you have in one hand, one vector with **J1**, another hand, another vector with **G2**. And you want to obtain some of them in our regular vector space. In our regular vector sense, you want to take one and then you stick the other one right.  

The resulting vector can have different lengths depending on the angle between these two. But there are **minimal and maximal values**. And all values in between are possible, but they have to contain them. Essentially that's what's written here.  

::: callout-tip
The **General Spin Addition Rule** is:  
$$  
j_1 \otimes j_2 = |j_1 - j_2| \oplus \cdots \oplus (j_1 + j_2)  
$$  
Example: For $j_1 = 3$, $j_2 = 2$:  
$$  
3 \otimes 2 = 1 \oplus 2 \oplus 3 \oplus 4 \oplus 5  
$$
:::
The minimum you obtain by combining in this direction and then maximum combining and all intermediate values are possible. What we have here is combining the **1/2**. Let's know the notations that we often use. That tells you you combine two vector spaces coming from the cross product to the irreducible representations.  

You combine spin **1/2** and spin **1/2**. The total system can have spin **0** or **1**. Let's do exactly another example. We combine spin **3** and spin **2**. What do I get? Just anyone output **5** or **55** again? Yes, **5, 4, 3, 1, 2**. Put plus.  

What amazed me is that the dimension on the left and right is the same. Can we count that? This would be common dimensional **3**. Spin **3** is **7**, spin **2** is **5**. Here is **3, 5, 7, 9, 11**. Can someone tell me if it works or not? It might.  

::: callout-note
**Dimension Check for Representations**:  
For the combination $3 \otimes 2$:  
$$  
\text{Dim}(3) \times \text{Dim}(2) = 7 \times 5 = 35  
$$  
$$  
\text{Dim}(1) + \text{Dim}(2) + \text{Dim}(3) + \text{Dim}(4) + \text{Dim}(5) = 3 + 5 + 7 + 9 + 11 = 35  
$$
:::
Right, **20, 35** on the left, **35** on the right. Isn't it amazing? We just, I mean probably formally prove that by counting all intermediate states from one to another. But that tells you the way to check yourself if you want to combine spins and write it with recombinations.  

You can always count dimensions and see what essentially we do when we map this to that. Here we have a vector. The basis in this dimension is the... Let's say **1, 1**. This is an example of the **7 into 7** and then this is **5**. This is one unit vector in that dimension.  

In that case I have a **35 dimensional vector** which has blocks. The first block is **3, 3** is the second block, **3**. The second block is **5, 7, 9, 11**. So I have blocks. We map this to that.  

Moreover, what group theory tells you is that these blocks did not talk to each other. Once you put this exponent and then consider matrix that acts on these **35 dimensional spaces**, it will rotate different components within the box. They won't talk to each other. That's called **representation**.  

For us it's different sectors that give a total spin. If I have a system with total spin equals to say **three**, there is no rotation that would change the spin to **four**. That's super clear, right? Under rotations the spin is preserved.  

The implication in mathematics is that there is a representation that has a **block diagonal form** of the interaction where the blocks don't talk to each other. Now we know how to combine.  

Before doing a few practical combinations, let's introduce part in **charge conjugation** quickly. I think we are good.  

---

::: callout-important
Is it clear that what we discussed about **spin** is the same applied to **isospin**? Often in particle physics you deal with both and one shouldn't mix them up.
:::
We deal with **isospin** when you construct the quark wave function. But when you combine particles with spin and want to understand angular dependence, you're dealing with **spin**. With rotational group, the same algebra, the same methods, everything is the same.  

Just keep in mind whether you're talking about **flavor SU(2)** or **Lorentz part of the Lorentz Group rotational SU(2)**.

### Parity, Charge Conjugation, and Composite Systems in Particle States

**Number 3, 4, 5** in our discussion: the **parity operator** performs space inversion with respect to the origin. Both parity and charge conjugation act on a state and produce another state.  

::: callout-important
The **parity operator** $\mathcal{P}$ inverts spatial coordinates:  
$$\mathcal{P} \psi(\vec{r}) = \eta_P \psi(-\vec{r}), \quad \eta_P = \pm 1$$  
where $\eta_P$ is the intrinsic parity eigenvalue.
:::
The parity answers how the wave function changes when flipped through the origin. Intuitively, flipping a vector through the origin reverses all spatial components. For any particle, you can determine its parity. Acting twice with parity returns the original state, so the eigenvalue is **modulo 1** (conventionally $\pm 1$).  

---

Charge conjugation flips all charges, converting a particle to its antiparticle.  

::: callout-note
The **charge conjugation operator** $\mathcal{C}$ acts as:  
$$\mathcal{C} |\psi\rangle = \eta_C |\overline{\psi}\rangle, \quad \eta_C = \pm 1$$  
For neutral eigenstates (e.g., $\pi^0$), $\eta_C$ is defined, but charged particles (e.g., $\pi^+$) are not eigenstates since $\mathcal{C} \pi^+ = \pi^-$.
:::
The **prime notation** here indicates the antiparticle. By convention, charge conjugation is defined for the neutral member of a multiplet (e.g., $\pi^0$). The Particle Data Group lists $J^{PC}$ (spin, parity, charge conjugation) for all particles. For $\pi^0$, $J^{PC} = 0^{-+}$; for $\pi^+$, charge conjugation is assigned by analogy to $\pi^0$.  

---

To find $J^{PC}$ for a composite system:  
1. **Total $J$**: Use spin algebra.  
2. **Parity**: Multiplicative, including $(-1)^L$ for orbital angular momentum $L$.  
3. **Charge Conjugation**: Multiplicative (for neutral systems, $C = (-1)^{L+S}$).  

::: callout-tip
**Parity of a composite system**:  
$$P = \eta_{P1} \eta_{P2} (-1)^L$$  
where $\eta_{P1}, \eta_{P2}$ are intrinsic parities.
:::
**Example**: For $L = 0$, combine spins multiplicatively (e.g., $1/2 + 0 = 1/2$). For $L = 1$, add one unit of angular momentum, with parity $(-1)^{L+1}$.  

---

In the quark model, heavy quarks (e.g., charm) are treated without gluons. The $u$ and $d$ quarks form isospin multiplets:  
- **Isospin 1**: Symmetric combination.  

-**Isospin 0**: Antisymmetric combination (matched with antisymmetric spin wave function).  

::: callout-note
For baryons like $\Lambda_c$ (isospin-0), excitations include radial ($n=1s, 2s$) or orbital ($P$-wave, $D$-wave) modes. The Particle Data Group lists ~7 $\Lambda_c$ states, including ground and excited configurations.
:::
---

**Key skill**: Determine allowed $L$ in decays.  

::: callout-important
**Decay selection rules**: For $A \to B + C$, allowed $L$ satisfies:  
$$|J_B - J_C| \leq L \leq J_B + J_C \quad \text{and} \quad P_A = P_B P_C (-1)^L.$$  
Example: $0^+ \to 1^- + 2^-$ requires $L=2$ ($D$-wave) to conserve $J^P$.
:::
---

Neglecting spins, sketch the energy spectrum for $n \leq 3$ (1s, 2s, 2p, 3s, 3d). Recall $L < n$ (no $f$-waves).  

---

Thanks for attending! Questions are welcome—ask directly or anonymously.  

::: callout-caution
**Practice**: Constructing $J^P$ tables and decay $L$ assignments are **essential skills** for particle physics.
:::
