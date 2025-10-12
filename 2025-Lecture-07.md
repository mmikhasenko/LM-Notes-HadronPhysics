---
title: (2025) Lecture 7
author: ''
presenter: Mikhail Mikhasenko
note_taker: Anna Zimmer
date: '2025'
format: html
---

**Presenter**: {{< meta presenter >}}

**Note Taker**: {{< meta note_taker >}}

### Helicity Formalism, Weak Decays, and Isospin Violation in $\Lambda^0$ Decay


Welcome everyone.
Today we have a **seventh meeting** on hadron physics.
Today's lecture will expand on the previous lecture on **helicity formalism**.
We will discuss **partial wave expansion**, which you have seen already in homework, and move toward general principles discussing the **Mandelstam plane** and **analyticity**.

Toward the end of the lecture, as always, I invite you to look at the problems to recap the material from the previous lecture.
I will give you **five minutes** to think about them, and then we will discuss together.

---

Which interaction is responsible for the $\Lambda^0$ decay to the proton and pion?

- Is isospin conserved?
- Is parity conserved?
- Is angular momentum conserved?

Demonstrate that the rotations we discussed last time are not different from isospin rotations—they are both represented by an $SU(2)$ group.

- What is the 30-degree isospin rotation about the $Y$-axis?
- How does it act on the $\Delta^+$ state?

Given a **Dalitz plot**, determine which decay case takes more time.

Let’s go through the problems quickly, starting with **1**, then **3**, and then **2**.

---

The **weak interaction** is responsible for the $\Lambda^0 \to p + \pi^-$ decay.
It must be weak because there is a **flavor change**—the $\Lambda^0$ contains a strange quark, while the final state does not.
**Flavor change always indicates weak interaction.**

::: callout-note
We had a seminar yesterday discussing proton-proton to $\Lambda$-proton transitions in neutron stars.
If you compress neutrons in a neutron star, a neutron-neutron interaction could produce a $\Lambda$ and other particles.
This involves a flavor change, so it must be weak.
But weak interactions are too slow for production processes in dense matter—likely a typo or missing quarks in the description.
:::
For ground-state baryons, most decays are weak.

The initial state $\Lambda^0$ has $J^P = \frac{1}{2}^+$, the proton has $\frac{1}{2}^+$, and the pion has $0^-$.
Parity conservation would require orbital angular momentum $L = 1$:
$$
P_{\text{final}} = P(p)P(\pi^-)(-1)^L = (+1)(-1)(-1)^1 = +1
$$
However, the decay also occurs via $L = 0$ (parity-violating):
$$
P_{\text{final}} = (+1)(-1)(-1)^0 = -1
$$
In weak decays, **parity is not conserved**—there is always a parity-violating component.

**Yes**, angular momentum is always conserved in particle physics due to Lorentz symmetry.
For $\Lambda^0 \to p + \pi^-$:
$$
J(\Lambda^0) = \frac{1}{2}, \quad J(p) = \frac{1}{2}
$$
The balance is achieved by $L = 0$ or $L = 1$.

**No.** The $\Lambda^0$ has isospin $I = 0$, the proton has $I = \frac{1}{2}$, and the pion has $I = 1$.
The transition $0 \to \frac{1}{2} + 1$ violates isospin.
**Weak interactions generally break isospin**, similar to parity.

---

1. **Isospin Conservation (broken in weak decays):**
$$
\Delta I \neq 0
$$
Example for $\Lambda^0 \to p + \pi^-$:
$$
I(\Lambda^0) = 0, \quad I(p) = \frac{1}{2}, \quad I(\pi) = 1
$$

2. **Parity Conservation (violated in weak decays):**
$$
P_{\text{initial}} \neq P_{\text{final}}
$$

3. **Angular Momentum Conservation:**
$$
\vec{J}_{\text{initial}} = \vec{J}_{\text{final}} + \vec{L}
$$

4. **SU(2) Rotation (isospin space):**
$$
R_y(\theta) = e^{-i\theta I_y}, \quad \theta = 30^\circ
$$
Acting on $\Delta^+$ ($I = \frac{3}{2}, I_3 = +\frac{1}{2}$).

5. **Dalitz Plot (decay kinematics):**
$$
dm_{12}^2 \cdot dm_{23}^2
$$

### Identifying the Decaying Particle via Dalitz Plot Analysis and Resonance Bands


**All right, question number three.**
We agreed.
**Any guesses:** who decays? How?

* **First, how many particles are in the final state?** Three.
* **How many particles are in the initial state?** One.
* **So it's a 1-to-3 decay.**
* **That's why we represent this on the Dalitz plot.**

---

**What is the final state?** On the first row—Alex, what is the final state? Benjamin? Benedict?
Ah, we are not in France. Benedict.
**What are the particles in the final state?** Right, very good.

**How did you guess?** Because those are the three particles mentioned on the axes.

* On the **X-axis**, you have one pair: proton and K-minus.
* The other pair is on the **Y-axis**.
* That is always the mass of one subsystem versus the mass of the second subsystem.
* **That's how you figure out the Dalitz plot.**

---

**What are the subsystems of the decay?**
This is the X-axis, this is the Y-axis. Something like that.

::: callout-note
**Dalitz plot variables:**
$$
X = (m_{pK^-})^2 \quad \text{vs} \quad Y = (m_{K^-\pi^+})^2
$$
:::
**Now, what remains to figure out is who decays, and what are the clues?**

* On the Dalitz plot, there's a **horizontal band**—the strongest resonance in the plot.
* The particle that decays into the proton and K-minus is that resonance.
* So there will be some proton K-minus.
* **You're talking about which line?** This one.
* That line gets projected into the peak in this dimension.
* So that line would be a resonance in the pion K.
* These are **K-stars**.

---

**Do we have bands in this dimension?** Something that will project to the peaking structure here?

* These are **lambda states**, and these are **K-star states**.

**How do we figure out who decays?**

* One clue is the **internal structure**.
* How does the decay proceed? What are the intermediate states?
* But if the question is: **who decays?** What particle decays into this final state?
* What are the clues? Perhaps masses somehow.
* The initial state should probably be **charged**.

---

**Can we compute the mass of this particle?**

* The phase space will be limited by the mass.
* We can take the upper border of the X-axis, and the square root of that, minus the lower border on the Y-axis, and the square root of that lower.

::: callout-note
**Phase space boundaries:**
$$
(m_{p} + m_{K^-})^2 \leq X \leq (M_0 - m_{\pi^+})^2
$$
$$
(m_{K^-} + m_{\pi^+})^2 \leq Y \leq (M_0 - m_{p})^2
$$
:::
**What do you get?**

* The minimum value on the Y is the masses of the two particles.
* The upper border here is $(M_0 - M_\pi)^2$.
* Here the value is $(M_0 - M_p)^2$.
* The minimum value is $(M_K + M_\pi)^2$.
* Here the minimal value is $(M_p + M_K)^2$.

**So indeed, you find $M_0$ by looking at the highest value.**

* Take the square root, as Henry said, and add the mass of the pion.
* Or take the highest value here, square root, and add the mass of the proton.

**What do you get? 2.24.**

* Add the mass of the proton, 1 GeV, something like that.
* Then we open the PDG and look for a particle with a mass of 2.6 or similar.
* There will be few in this domain.

---

**One has to figure out whether the decay happens weakly or strongly.**

* If it happens strongly, what should the quark content be?
* The proton is $uud$, the K-minus is $s\bar{u}$, and the pion is $u\bar{d}$.
* These could come from the vacuum.
* The rest you cannot cancel with the vacuum: $u d s \bar{u} \bar{d}$.

**Is it a pentaquark that decays strongly? Or a big decay of something?**

* In fact, it's a **weak decay** of the particle called $\Xi_c^+$.

**Wait, why can't you cancel $d\bar{u}$?**

* Oh, it's true. Thanks, Ilia.
* Then who is this? $\Xi$.
* This is the $\Xi^+$ without C.

**What we find is that $\Xi^+$ can decay to this combination $\Sigma^+ \Sigma^+$.**

* Thanks. $\Sigma$ or $\Lambda$? $\Sigma^+$, because $\Lambda$ is only zero.

---

**Now, almost full view.**

* It could be a **strong decay** of the $\Sigma^+$.
* Maybe isospin. Can you make it from isospin?
* The $\Sigma^+$ has isospin 1, the proton has isospin $\frac{1}{2}$, the K-minus has isospin $\frac{1}{2}$, and the pion has isospin 1.
* From $\frac{1}{2}$, $\frac{1}{2}$, and 1, you can make 1.
* So isospin is conserved. Could be conserved.

::: callout-note
**Isospin conservation check:**
$$
I(\Sigma^+) = 1 \quad \text{vs} \quad I(p) = \frac{1}{2}, \quad I(K^-) = \frac{1}{2}, \quad I(\pi^+) = 1
$$
:::
**But in fact, what I did—I looked at the $\Xi_c$ angular analysis and printed that plot of the $\Xi_c$ decay.**

---

**The last question here is about kinematics.**

* It's good that you know these resonances, and we will discuss them more in the lecture.
* But when you just need to know the mother particle, you check the **conservation laws**.
* You can figure out that the mass of the decaying particle is on the borders of the phase space.

::: callout-note
**Quark content conservation (weak decay):**
$$
\Xi_c^+ (usc) \to p(uud) + K^-(\bar{u}s) + \pi^+(u\bar{d})
$$
:::
### Isospin Operators, Rotations in Isospin Space, and QCD Evolution in Two-Body Decays


**Question number two.**
Isospin operators are given.
Is it true that isospin acting on $\Delta^+$ gives $\frac{15}{4}$? $\Delta^+$ is the first state.
Who thinks it's true? Who thinks it's wrong?

The $J^2$ operator acting on the state gives $J(J+1)$.
That's what I meant here.
This is $\frac{3}{2} \times \frac{5}{2}$.

::: callout-important
For $\Delta$ with isospin $I = \frac{3}{2}$:
$$
I^2 |\Delta^+\rangle = I(I+1) |\Delta^+\rangle = \frac{15}{4} |\Delta^+\rangle
$$
:::
$\Delta$ has isospin $\frac{3}{2}$, so the first expression is true.

---

The second expression: the projection to the $z$-axis of $\Delta^+$ is $\frac{1}{2}$.
Who thinks it's true? Who thinks it's wrong?

$\Delta^+$ sits in the multiplet with four states.
The upper one always has the highest isospin projection:

* $\left|\frac{3}{2}, \frac{3}{2}\right\rangle$,
* $\left|\frac{3}{2}, \frac{1}{2}\right\rangle$,
* $\left|\frac{3}{2}, -\frac{1}{2}\right\rangle$,
* $\left|\frac{3}{2}, -\frac{3}{2}\right\rangle$.

The operator $I_z$ gives the $z$-projection of the isospin vector.
It maps states in the multiplet.

::: callout-note
The isospin projection for $\Delta^+$:
$$
I_z |\Delta^+\rangle = \frac{1}{2} |\Delta^+\rangle
$$
:::
If I act with $I_z$ on $\Delta^+$, I get $\frac{1}{2}$.
These states are eigenstates of $I_z$, so this is also true.

---

**Rotations in isospin space:**
If you apply a rotation, as Farah explained last time, states transform under $SU(2)$.
For a rotation acting on $|JM\rangle$, you get a mixed state with coefficients.

Applying a $y$-rotation of 30 degrees to $\Delta^+$ gives a mixed state of different $\Delta$ states.
The $D$ coefficients are known functions, found in the PDG table with Clebsch-Gordan coefficients.
These are trigonometric functions.

Let’s check $D_{3/2,1/2}(30^\circ)$:
$$
D_{3/2,1/2}(30^\circ) = -\frac{\sqrt{3}}{2} (1 + \cos\theta) \cdot \frac{\sin\theta}{2}.
$$
For 30 degrees, you can express $\sin\theta$ as $\sqrt{1 - \cos^2\theta}$.

When you apply a rotation in spin space to an eigenstate, you get an expansion into all states.
The coefficients give the probabilities:
$$
|D_{3/2,3/2}|^2 + |D_{3/2,1/2}|^2 + |D_{3/2,-1/2}|^2 + |D_{3/2,-3/2}|^2 = 1.
$$
Probability is conserved.

This shows rotations in isospin space are no different from regular rotations—both are driven by $SU(2)$.

---

**Questions:**
This was part of the homework.
The last coefficient $D_{3/2,-3/2,1/2}$ isn’t listed.
Is it the same as $D_{3/2,1/2}$?

The parity relations are listed.
If you switch the bottom indices, both get a minus sign:
$$
D_{-M_1,-M_2} = (-1)^{M_1 - M_2} D_{M_2,M_1}.
$$
But $D_{-3/2,-1/2}$ is also not given.

You can swap indices or add a minus sign.
For unitary matrices, there’s another relation:
For a negative rotation, you can complex conjugate and transpose.
Transposing swaps the indices.

This comes from the unitary nature of $SU(2)$.
The two Wigner functions are the same: swapping and adding a minus sign gives the same result.

---

**Today’s lecture: QCD evolution.**
We’ll apply helicity formalism to express amplitudes.
The biggest danger is confusing models with general statements.
We’ll make approximations—ask me to clarify what’s general vs. model-dependent.

---

**Two-body decay reminder:**
In the rest frame of the decaying particle, the matrix element depends on:

* Kinematic variables,
* Spin configurations ($M_0, \lambda_1, \lambda_2$).

The total spin controls the angular dependence:
$$
\mathcal{M}_{M_0,\lambda_1,\lambda_2} = H_{\lambda_1,\lambda_2} \cdot D^{J_0 *}_{M_0,\lambda_1-\lambda_2}(0,\theta,\phi).
$$
The $D$ function comes from active rotations:

1. Rotate about $Y$ by $\theta$,
2. Rotate about $Z$ by $\phi$.

The reduced matrix element $H_{\lambda_1,\lambda_2}$ depends only on mass, not angles.
It projects the helicity states onto the initial state:
$$
M_0 = \lambda_1 - \lambda_2.
$$

---

**Cascade decays:**
For decays with intermediate states, we use the same construction.
The general structure includes:

1. $D$ functions for each decay vertex,
2. Reduced matrix elements $H$,
3. Propagators for intermediate resonances.

The amplitude is:
$$
\mathcal{M} = \sum \left( D^{J_0 *}_{M_0,\lambda_1-\lambda_2} \cdot H^{(1)}_{\lambda_1,\lambda_2} \cdot \text{Propagator} \cdot H^{(2)}_{\lambda_3,\lambda_4} \cdot D^{J_1 *}_{\lambda_1-\lambda_2,\lambda_3-\lambda_4} \right).
$$

This gives a recipe for any cascade decay with spin.

---

::: callout-tip
**Key takeaway**: The helicity formalism provides a systematic way to handle spin-dependent decays, with Wigner $D$-functions capturing the angular dependence and reduced matrix elements $H$ encoding the dynamics.
:::
### Factorization, Helicity Amplitudes, and Angular Parameterization in Cascade Decays


This is the model, and it is a model not because of the angular functions—they are **precise and exact**—but because of the factorization.
We are assuming that the matrix element can be factorized into the initial first decay and the second decay.
The fact that we split the interaction matrix element into two parts—here is the reduced matrix element of the first transition, and here is the second—is our modeling assumption: **factorization**.

::: callout-important
The factorization of the matrix element is expressed as:
$$
\mathcal{M} = \mathcal{M}_1 \cdot \mathcal{M}_2
$$
where $\mathcal{M}_1$ and $\mathcal{M}_2$ are reduced matrix elements for the first and second transitions, respectively.
:::
What is missing here is that we didn't introduce $\lambda$.
You see that the intermediate state appearing here also has a spin projection $\lambda$, and that's the one carried by one of the particles.
This is something up to a sum over the angles that appear as arguments.
They are not the same but are specific to particular transitions here and there, so we better label them differently.
Keeping consistent labeling is always tricky.

When you apply this cascade decay parameterization, you have a million different angles, and labeling them requires some rule to start.
For example, for the pair of particles that go back-to-back, say $IJ$, I can use the $IJ$ index here.
The angles will have indices $\theta_{12}$, $\phi_{12}$.
Here it's 1, 2, 3, and now I would like to invite you to do some **3D imaging**.
I enjoyed this very much, and I hope you seeing this once can also enjoy.

---

I want to sketch on the board in 2D how it looks in 3D—the definition of the axes.
We need axes, and that's how it starts.
Here is the representation that I think is easy to visualize.

We start with particle 0 in the lab frame.
It flies in this frame, and the particle has the helicity $\lambda_0$.
This particle decays into a combination of particles 1, 2, and 3.
We can boost the system to its rest frame following this axis.
In the rest frame, $\lambda_0$, which was the helicity, becomes the canonical spin projection.
If you think of this—here is the $z$-axis, here is $m_0$ (the rest frame of particle 0)—then the spin is quantized along the $z$-axis by our construction, since we boost in this direction.

In this frame, particles 1, 2, and 3 go back-to-back.
To apply the second part, you follow the combination of particles 1 and 2.
It's the same as we started from: in this frame, it flies in a certain direction and decays into two particles.
We need to boost to its rest frame, where it decays into particle 1 going back-to-back.

---

Let's define the angles.
Angles are taken as spherical angles of one of the decay products.
If you boost directly, the spherical angles of one decay product would be $\theta$ and $\phi$.
Here is $\theta_{123}$, and here is $\phi_{12}$.

For the second transition, $\theta$ is the angle with respect to the $z$-axis in the rest frame of the particle.
Here is $\theta_{12}$, and here is $\phi$.
When you deal with this practically, you follow the chain and introduce angles while applying constraints.

In experimental physics, we are given four-vectors.
You're literally given three four-vectors for particles 1, 2, and 3 in the lab frame.
The convention is the active transformation: first, find the spherical angles of the (1, 2, 3) combination, then rotate to align the 1-2-3 vector with the $z$-direction.
Next, boost in this frame, take $\theta$ (the angles of the 1-2 pair), align it with the $z$-axis, boost, and apply rotations.

---

The topology we draw here is not the only one possible.
You could imagine the same transition happening through the combination of particles 2 and 3 or 3 and 1, and you would write the same expression.
Before discussing resonances in other channels, let's note some caveats.
The main caveat is that the helicities in the expressions are taken from different rest frames.
To apply the helicity formalism and replace the expectation value with the reduced matrix element (helicity coupling), we must be in the particle's rest frame.
Thus, the $\lambda$ values here are taken in the rest frame of the pairs.

What does it mean for the quantization axis to be taken from the $z$-axis of the appropriate frame?
From the last homework, we saw that helicity is affected if you boost off-axis.
I prefer to write the amplitude where the $\lambda$ are defined in the same frame: $\lambda_1, \lambda_2, \lambda_3, \lambda_0$.
I get a linear combination of amplitudes.
It's bizarre, but we don't use this literally because we don't care about the $\lambda$ themselves—we sum them up later.
Consistency of the quantization axis only matters for coherent processes using different axes.

---

What's important is the axis in this matrix element where spins are quantized.
$\lambda_0$ comes from the lab frame (helicity in the lab frame).
$\lambda_3$ appears in... and these two are...
It's totally okay.
Once I square the matrix element, the sum over helicities doesn't depend on the quantization axis.
But if I add this amplitude to another (e.g., an expansion in a different topology), I must be careful about the helicity quantization.
**First important note**: watch your helicity quantization axis.

**Second important note**: we implicitly assume factorized vertices.
This is a good assumption, especially for narrow resonances.
Even for broad resonances, if the dynamics are driven by the 1-2 combination, factorization is reasonable.
The Wigner $d$-functions here are properties of rotations—not model assumptions.
Lorentz symmetry requires them.
If we take the expression without factorization, join the matrix elements with the propagator, and compute the largest product of the three, this is model-independent.
It's safe to pull out rotational functions but not to break them.

---

Another note: we've explicitly found the angular dependence for a spin-$J$ particle in the $N2$ combination.
The heuristic formalism identifies the matrix element's dependence on angles.
All I care about is the spin of particles 1 and 2.
This form doesn't give the answer—it's simply $D^J$ with the appropriate angles.
Dealing with spin is complicated, as you’ve seen.

For further discussion, let’s reduce to scalar particles.
If a scalar decays into three scalars, the matrix element has no indices but still depends on dynamic variables.

Look at this expression: the only possible $\lambda$ value is zero.
For spin zero, there's a single state in the multiplet, transformed under rotations.
Only the phase can change, and $\lambda$ must be zero.
This term gives $\delta_{\lambda 0}$, which propagates further.

The expression simplifies: the matrix element depends only on one polar angle.
In the rest frame of two particles, all angles drop out except one.
The convenient way to write this is...

---

I'm moving toward matching this expression to the partial wave expansion in the homework.
That's why I pulled helicity couplings and reduced matrix elements into $X$ and introduced the $2J+1$ coefficient.

::: callout-note
The partial wave expansion for scalar decays is given by:
$$
\mathcal{M} = \sum_J (2J+1) X_J(s) d^J_{00}(\theta)
$$
where $d^J_{00}$ is the reduced Wigner function.
:::
---

Key formulas integrated:

1. **Factorization**: $\mathcal{M} = \mathcal{M}_1 \cdot \mathcal{M}_2$
2. **Helicity amplitude**: $\mathcal{M}_{\lambda_0 \to \lambda_1 \lambda_2 \lambda_3} = \sum_\lambda \mathcal{M}_{\lambda_0 \to \lambda} \cdot \mathcal{M}_{\lambda \to \lambda_1 \lambda_2 \lambda_3}$
3. **Wigner $D$-functions**: $\mathcal{M} \propto D^{J_0}_{m_0,\lambda_0}(\theta,\phi) \cdot D^{J}_{m,\lambda}(\theta',\phi')$
4. **Scalar case**: $\mathcal{M}_{\text{scalar}} = X(s_{12}, s_{23}) \cdot \sqrt{2J+1} \cdot \delta_{\lambda_0,0}$
5. **Partial wave expansion**: $\mathcal{M} = \sum_J (2J+1) X_J(s) d^J_{00}(\theta)$

### Partial Wave Expansion and Resonance Modeling in Dalitz Plots


We started by writing the matrix element for the decay that proceeds through the resonance with spin $J$.
We found that the angular dependence of this matrix element is given by $d^J_{00}$, which are **Legendre polynomials** $P_J(\cos\theta)$.

::: callout-note
The matrix element for resonance decay with spin $J$ is:
$$
\mathcal{M} \propto d^J_{00}(\theta) = P_J(\cos\theta)
$$
where $P_J$ are Legendre polynomials.
:::
---

I would like to match this to the general technique for analyzing the matrix element for any expression with angular dependence.
We can expand this in a series of Legendre polynomials and analyze the coefficients, leaving only the mass dependence.
The coefficients in this expansion represent **dynamics** corresponding to the specific spin $J$ of the resonance.

---

We started from a modeling approach, but it provides interpretation and intuition.
What are the coefficients in the **partial wave expansion**? The total matrix element in this scalar transition depends on only two variables: the scattering angle $\theta$ and the mass $s$.
This is also what we see in the **Dalitz plot**, where the two variables are the masses of the two subsystems.
The dependence can be explored by analyzing the coefficients in the partial wave expansion.

::: callout-note
The partial wave expansion of the matrix element is:
$$
\mathcal{M}(s, \theta) = \sum_{J=0}^\infty (2J+1) a_J(s) P_J(\cos\theta)
$$
where $a_J(s)$ are the dynamical coefficients for each spin $J$.
:::
---

The expansion is an exact representation if the series is infinite.
Truncating the series makes it an approximation.
In experiments, we often truncate the partial wave series because high spins are rare.
Looking at the PDG, particles with large $J$ are not abundant, and amplitudes for high $J$ are suppressed.
This provides a natural limit to the expansion.

---

The highest observed spin is $J = 6$.
While quark models predict higher spins like $J = 7$ or $10$, these have not been observed experimentally.
They are likely too high in the excitation spectrum and too broad to couple effectively.
Practically, we truncate the series at $J = 6$.

---

For channels where resonances appear in one subsystem, the partial wave expansion is a good model.
When resonances appear in multiple channels, we use a sum of truncated series instead of a single infinite expansion.
For example, in Dalitz plots, resonances can appear in pairs $(1,2)$, $(2,3)$, or $(3,1)$.
The model, when projected onto any channel, still contains an infinite number of partial waves.

---

This is key: the angles in the expansion for $(2,3)$ are defined in the $(2,3)$ rest frame, different from the $(1,2)$ channel.
Each term in the full expansion projects onto an infinite number of Legendre polynomials in any single channel.

---

This approximated amplitude is called the **Isobar model** in hadron spectroscopy, where **Breit-Wigner amplitudes** parameterize the peaks phenomenologically.
It works well but is simplistic.
A more general approach is the **cascade decay model**, where three truncated series are used without assuming factorization.

::: callout-note
The Breit-Wigner propagator for resonances is:
$$
\mathcal{BW}(m) = \frac{1}{m_0^2 - m^2 - i m_0 \Gamma(m)}
$$
where $m_0$ is the resonance mass and $\Gamma(m)$ is the energy-dependent width.
:::
---

The **Chew-Mandelstam Ansatz** starts similarly but includes final-state interactions and rescattering.
It introduces theoretical constraints, leading to more sophisticated dynamical functions.
The amplitudes correct each other through rescattering, accounting for triangle-like processes.
While derived from dispersion relations, it still involves modeling assumptions.

---

Finally, let’s return to the Dalitz plot and discuss modeling it using the **helicity formalism**.
The inhomogeneities in the plot reflect resonances (bumps) and spin-angle distributions (structures).
To apply the helicity formalism, we need:

1. The spins of the particles.
2. The reduced matrix elements.
3. The propagator, parameterized via the Breit-Wigner form with mass, width, and spin $J$.

::: callout-note
The Dalitz plot density distribution is:
$$
\frac{d^2\Gamma}{dm_{12}^2 dm_{23}^2} \propto |\mathcal{M}(m_{12}, m_{23}, \theta)|^2
$$
where $m_{ij}$ are invariant masses of particle pairs.
:::
---

Looking at the plot, we identify resonances:

- For $K\pi$, the horizontal band corresponds to $K^*(892)$ with $J^P = 1^-$.
- For $Kp$, the vertical bands include $\Lambda(1520)$ ($J^P = 3/2^-$) and $\Lambda(1690)$.
- The diagonal line is $\Delta(1232)$ ($J^P = 3/2^+$).

With these inputs, we can construct the Dalitz plot.
However, quantization axes complicate the helicity formalism for spin-$\frac{1}{2}$ particles like the proton.
For scalar particles, the approach would be straightforward.

---

Any questions? Next time, we’ll cover **resonance dynamics**, advanced Breit-Wigner parameterizations, and constraints from unitarity and analyticity.

