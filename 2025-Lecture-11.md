### Thresholds, Branch Points, and Resonances in ππ Scattering


The threshold for **ππ scattering** is at:
$$
\sqrt{s} = 2m_\pi
$$
Are there any other open channels? Let's assume there are no other open channels.

The **branch point** is located at:
$$
s = (2m_\pi)^2
$$
The branch cut should be drawn from the branch point to the right to satisfy causality.

There is also a **cross channel** to this reaction because ππ scattering isn't the only possible process. If we consider backward scattering in energy, another π can scatter to another π. For example:

- **π⁺π⁻** can scatter to **π⁺π⁻**
- Equivalently, **π⁺** can scatter with **π⁺** if we rearrange the particles

This means there is another branch point on the left side from the cross channel.

---

When discussing **scattering amplitudes**, we visualize a "blob" connecting the initial and final states. For ππ scattering:

1. We draw the blob with time moving in one direction
2. Initial pions come together, interact, and then scatter out
3. This defines a physical process with well-defined kinematics

For this process to occur, the total energy must exceed the threshold:
$$
\sqrt{s} > 2m_\pi
$$
The **Mandelstam variables** s and t describe the kinematics:

- **s** is positive above threshold
- **t** is negative for elastic scattering (represents momentum transfer)

::: callout-note
The scattering amplitude is an analytic function of s and t, defined across the entire complex plane - even for unphysical values. This allows us to study processes like π₁π̄₃ → π₂π₄ through **crossing symmetry** by exchanging s and t.
:::
---

In the **s-plane**:

- **Positive s**: s-channel scattering
- **Negative s**: t-channel or u-channel contributions

The amplitude has singularities, but we can **analytically continue** it to a second Riemann sheet, where resonant states appear. For example:

- In ππ P-wave scattering, the **ρ meson** appears as a resonance
- In the quark model, mesons are organized by energy levels (**1s, 1p, 2s**, etc.) with hyperfine splitting due to spin interactions
- The ρ meson and pion differ only in their **spin wavefunctions**

Unlike in electromagnetism (where transitions occur via photon emission), in QCD:

- The ρ meson decays to ππ by emitting another pion
- This occurs because quark-antiquark pairs can be easily created from the vacuum

---

The ρ meson appears as a **resonance** in ππ scattering - when two pions interact, they "feel" the ρ meson, leading to a peak in the cross section. This corresponds to a pole in the complex plane.

To fully understand resonances, we must analytically continue the amplitude to the second sheet. The classification includes:

1. **Resonances**: appear as peaks above threshold
2. **Virtual states**: lie on unphysical sheets below threshold
3. **Bound states**: on the physical sheet below threshold

The cross section σ is related to the amplitude A by:
$$
\sigma \propto (2J + 1) |A_J(s)|^2 \rho(s)
$$
where:
$$
\rho(s) = \frac{2k}{\sqrt{s}}
$$
is the **phase space factor**, and k is the breakup momentum:
$$
k = \frac{\sqrt{s-4m_\pi^2}}{2}
$$

---

For different states:

- **Resonance**: cross section peaks at the resonance mass
- **Bound state**: signal appears below threshold

The **analytic structure** of the amplitude determines these features. In summary:

- Singularities in the scattering amplitude correspond to physical states
- Their positions reveal whether they are resonances, virtual states, or bound states

### Poles, Bound States, and Virtual States in Scattering Amplitudes


For the **bound state** of the virtual state, there should be a peak below threshold. For the **virtual state**, there should just be a threshold cusp.

The peak below the threshold is **divergent**—it goes to infinity at this point. In contrast, the branch point has poles. The amplitude is undefined, or infinity, at the pole. Therefore, the poles are **strong singularities**. They truly make the amplitude infinite.

::: callout-important
**Key distinction**:

- Bound state pole: $E = -E_b$ (with $E_b > 0$)
- Virtual state pole: $E = -E_v + i0^+$ (with $E_v > 0$)
:::
Imagine taking this pole and moving it closer to the physical axis, where measurements are made. The closer it gets, the higher the cross-section value becomes, and the smaller the width. This distance to the pole is called the **width of the resonance**, $\Gamma$. The smaller the width, the narrower the peak, but also the stronger the resonance effect.

$$
E = E_0 - i\frac{\Gamma}{2}
$$

where $E_0$ is the resonance energy and $\Gamma$ is the width.

---

This also explains why **bound states** and **virtual states** produce enhancements. The pole creates an infinity at a specific point, but since measurements start above the threshold, the observed effect is finite. The physical values are still influenced by the pole’s proximity.

For a **bound state**, the amplitude is infinite below the threshold. However, since measurements occur above the threshold, we observe a finite effect. A bound state is a **real particle** that can propagate. Once produced, it does not decay—it lives forever because it has no width.

$$
\sigma(E) \sim \frac{1}{(E - E_{\text{th}} + E_b)^2 + \Gamma^2/4}
$$

---

Real particles are like poles below the threshold but with a small imaginary part. They are slightly shifted due to other interaction channels. Think of these particles as bound states in the limit where other interactions—like electromagnetic or weak forces—are turned off.

For example, if weak interactions are absent, the $B$ meson remains stable because flavor is conserved. In reality, weak interactions cause the $B$ meson to decay. This is why the bound state pole in any amplitude is slightly shifted downward.

::: callout-note
**Flavor conservation in strong interactions**:
$$ [H_{\text{strong}}, Q_{\text{flavor}}] = 0 $$
where $Q_{\text{flavor}}$ is a flavor quantum number.
:::
---

The discussion focuses on **pole positions** in the complex energy plane and their observable effects (peaks, cusps, and enhancements) in scattering amplitudes and cross-sections. The key distinction is between:

- **Bound states** (poles on the real axis below threshold)
- **Virtual states** (poles on the second Riemann sheet near threshold)
- **Resonances** (poles near the physical region with finite width).

For **virtual states**, the threshold cusp behavior is:
$$
\sigma(E) \sim \frac{1}{\sqrt{E - E_{\text{th}}}} \quad \text{near } E = E_{\text{th}}
$$

### Breakup Momentum Plane and Lattice QCD in Scattering Theory


As a main part, another convenient representation of the singularity of the scattering amplitude is the **breakup momentum plane**.
The scattering amplitude is only a function of the breakup momentum $P$ in non-relativistic scattering.
When you consider a non-relativistic problem, you don't have a $\sqrt{s}$ anywhere. You only deal with $P$.

If you look at the expression for $\rho$, where $\rho = \frac{2P}{\sqrt{s}}$, in the non-relativistic limit this simplifies to $\rho = 2P$.
You can expand the amplitude near the threshold by expanding it in $\sqrt{s}$ near the first branch point. This leads to the expression for $P$:

$$
P = 2\mu \sqrt{E - E_{\text{threshold}}}
$$

This quantity has a **branch point** at $s = s_{\text{threshold}}$ because it's under a square root, matching the branch point of the amplitude.
You can also find the inverse relation and determine how $s$ is related to $P$.

The key point is that if the amplitude is only a function of $P$, the square root will never appear. There is no $\sqrt{P}$ in the amplitude—it is actually an **analytic function** of $P$.

What we discussed earlier with the first and second sheets now merges into a single complex plane.

- The **upper part** represents $A(P)$.
- The **lower part** represents $A_2(P)$.
The real physics corresponds to $P$ being real and positive, which maps to $s$.

::: callout-note
**Pole positions in the $P$-plane**:

- **Bound state**: On the positive imaginary axis ($P = i|P|$).
- **Virtual state**: On the negative imaginary axis ($P = -i|P|$).
- **Resonances**: Complex-conjugate pairs in the lower-half plane ($P = \text{Re}(P) - i\text{Im}(P)$).
:::
Let me quickly sketch where the bound and virtual states are in this representation.

- The **bound state** sits on the real axis just below the threshold.
- The **virtual state** is also on the real axis but above the threshold.
- **Resonances** appear as pairs in the complex plane.

This is the breakup momentum plane, often used in non-relativistic field theory. It simplifies visualization because all objects (bound states, virtual states, resonances) appear in one picture.
However, this representation works as an expansion near the threshold and becomes complicated with higher thresholds or additional branch points.

---

To summarize:
We’ve discussed **scattering theory**, widely used in hadron spectroscopy. Unlike field theory, this approach doesn’t start from a Lagrangian but uses general principles of scattering theory—**unitarity**, **analyticity**, and **crossing symmetry**.

- **Resonances** are identified as poles of the scattering amplitude.
- The amplitude is constructed to satisfy these principles and fitted to experimental data.
- Once fixed, it reveals its analytic structure, including branch points and poles on unphysical sheets.

In experimental particle physics, we:

1. Constrain this amplitude using data.
2. Analytically continue it.
3. Locate poles.

The **pole position** gives the mass and width, while the **residue** (from the Cauchy integral) quantifies the coupling strength. These values are tabulated in the **Particle Data Group** for future reference.

**Question:** What changes if we add spin to the particles? For example, in $\rho \rho$ scattering compared to $\pi \pi$ scattering?
The short answer is: nothing fundamental changes except kinematics.

- The amplitude gains extra **kinematic factors** at threshold.
- It becomes a **vector of amplitudes** due to different helicity states.
For $\rho \rho$ scattering, there are multiple amplitudes corresponding to different helicity combinations. However, the **analytic structure** and **pole interpretation** remain the same.

---


QCD is a **gauge theory** with an $SU(3)$ gauge group, featuring **confinement** and **asymptotic freedom**.

- At **high momentum**, quarks behave as free particles.
- At **low energy**, they confine into hadrons.

This makes QCD difficult to study analytically because perturbation theory fails—the coupling is too strong at low energies.

One powerful method is **lattice QCD**, where we:

1. Discretize spacetime into a grid (e.g., a $2 \text{ fm} \times 2 \text{ fm} \times 2 \text{ fm}$ box).
2. Solve the equations numerically.

We use **periodic boundary conditions**, meaning the field at one edge matches the field at the opposite edge. This effectively tiles space with identical copies of the box.

Key parameters:

- **Lattice spacing** $a$ (e.g., $0.1 \text{ fm}$).
- **Box size** $L = N \cdot a$.

We want the lattice:

- Large enough to fit hadrons (e.g., a meson of size $\sim 1 \text{ fm}$).
- Small enough to avoid interactions with mirrored images.

The QCD Lagrangian has few parameters:

- The coupling $g$.
- Quark masses $m_f$.

On the lattice, we tune these parameters to match physical observables (e.g., the pion mass $m_\pi$).
Interestingly, we can explore "alternative universes" by varying quark masses continuously. For example:

- A resonance like the $\rho$-meson can become a **bound state** if quark masses are increased.
- The pion mass follows $m_\pi \propto \sqrt{m_q}$ in the **chiral limit**.

Lattice QCD allows us to study these transitions numerically, providing insights into hadron structure and interactions.

---


- **Lighter quarks** (e.g., up/down) make calculations more expensive because the pion mass appears in denominators, increasing uncertainty.
- The **lattice spacing** $a$ sets the scale—everything is measured in units of $a$.
- **Finer lattices** (smaller $a$) improve accuracy but raise computational costs.

**Question:** How is quark mass defined on the lattice?
It’s **dimensionless**, expressed as $m_q a$, where $a$ is the lattice spacing.
The optimal choice balances precision and computational feasibility.

---

This framework—combining **scattering theory** and **lattice QCD**—provides a powerful toolkit for understanding strong interactions. Next, we’ll dive deeper into the technical details of lattice calculations.

### Lagrangian, Path Integral, and Euclidean Time in QCD


The **Lagrangian** is a scalar quantity and it's written as $G_{\mu \nu} G^{\mu \nu}$.
This is the gluonic tensor energy momentum.
This is a gluonic field tensor contracted with another one.
All repeated indices are contracted among the gluonic fields.
There are eight of them.
And then $\mu \nu$ everywhere.
Here are Lorentz indices.
They are relativistic properties, Lorentz group properties of the fields.

---

There is **gauge invariance** hidden here.
That is enforced by extending the derivative with the gluonic field.
So fermionic fields here are the quarks; they interact with the gluon.
And the way they interact is given by the gauge theory through this term that appears in the combination of the quarks and gluons through these terms.

The mass term is present explicitly.
And then here you see these three parameters or these $N$ parameters of the field.
$g$ is one of them, and the quark masses are others.
The rest is fixed.

---

So we have fields—we have the gluonic fields and the quark fields.
When we say fields, what we really mean is that both $\psi$ and $A_\mu$ are functions of the point in spacetime.
And any physical observable in this can be computed as an expectation value.

This is my notation.
This is an operator.
Let me write: this is an operator that can depend on it.
What kind of operators are we talking about?
You put together quarks and gluons, and you can measure the expectation of this operator by sandwiching it with the vacuum, and this is something you can observe.

---

::: callout-important
The expectation value is something you can compute.
It's no longer a function of the coordinates.
The operator can depend on the fields like $\psi$ and $A_\mu$.
:::
The notion of **local** and **non-local operators** is intuitive.

- **Local**: Evaluated at a single spacetime point.
- **Non-local**: Evaluated across multiple spacetime points.

---

Starting from Feynman's ideas, the **path integral technique** has been developed, and it suggests a way to compute the expectation value of the operator using the functional integral.
Let's spend two minutes discussing what is actually written here, because this expression you might not have seen before, and conceptually this path integral is a difficult object.

So here, all is also a function of the fields—we just write explicitly $\psi$ and $\bar{\psi}$.
Do we have a $T$-product yet? Time-ordered? Yes.
And time ordering is needed here.
If you have several operators, you have to time-order them.
Here we have one.
So if you want to proceed and expand this, you will get time-ordered.
I don't want to go into these details in this case.

---

Did you cover path integrals?
Let's see if all symbols are clear.
Let's start with that.
So $S$ is called the **action**, and this is the integral over all coordinates of the Lagrangian.
This action weights different configurations.

So this is the complex factor that, for any given configuration of the field—you tell me what $A_\mu$ in spacetime is, what $\psi$ and $\bar{\psi}$ are—I can tell you what this weight factor is by just computing the Lagrangian integrated over spacetime.

You can think of spacetime, and at every point in spacetime, you know what your field is.
Then you can compute this integral.
You know the factor; you can weigh this configuration.

---

So the input to this weighting factor is a map of spacetime—how $A_\mu$ and $\psi$ look.
You tell me not just a single value; you need to tell me what $\psi$ and $\bar{\psi}$ are at every point in spacetime.
Therefore, the input to this expression is the functional form.
So what $A_\mu$ is as a function of spacetime, what $\psi$ is as a function of spacetime.
And what I'm going to integrate over is all possible functional forms.
So this is a **functional integral**.

$\psi$ and $\bar{\psi}$ are considered to be independent and are described by **Grassmann variables** (anti-commuting).
I have another variable—I've been looking at Grassmann variables.
It's so much fun preparing this lecture.
Maybe I have time to show you what that means.

---

But if you want to compute any expectation value, this is what you have to do.
That's how your expectation value is defined: integrate over all possible configurations of the fields, your operator that depends on the fields, and weight this with the complex factor.

This is not practical for many reasons, and one of them is that this factor oscillates rapidly.
So it's a complex function.
And if you try to do this on a lattice, you can sample different field configurations, but you quickly realize that this doesn't converge.

---

And then the trick has been invented by changing real time to imaginary time.
So we are going to go from Minkowski time and Minkowski metric to Euclidean time, equating the dimension of time with space.
And then you will see that what happens is the action becomes a real number, and this $e^{iS}$ will become just a real weighting factor—a real number saying that this configuration has a probability of 0.1, this configuration has a probability of 0.5.

So the trick—and this is super important, essential, the main trick on the lattice—is to compute with Euclidean time rather than Minkowski time.
We're going to change the time, introduce a different variable $t_E$, defined as $t_E = it$.

---

Here is an example for the scalar field of how this transformation works.
What I'm trying to demonstrate here is that the Lagrangian changes.
So from the QCD Lagrangian, you're going to get this Euclidean version of the QCD Lagrangian, because the time derivatives are going to pick up an $i$ due to that, and the time derivative term changes sign.

For the fermion field, you have to do a little more.
The gamma matrices also change, and you have to update them.
Well, the derivative here changes, the gamma matrices change.
But that's—I think that's it.

---

But what we are going to write, we find out that the Lagrangian for the action—the action—so what we see here is that for that simple example of the Lagrangian of the scalar field, there is an overall minus sign.
So that term becomes a minus sum over four components of the new Euclidean coordinates minus the mass term.

So the whole expression is real and positive, and the action that we see here becomes real because of the integration variable.
Here we had the action—the Minkowski action had a $d^4x$, but now time is imaginary.
One of the $i$'s pops out and cancels the $i$ here, and the whole weighting factor becomes real.

Moreover, since the Lagrangian now is bound to be positive, the weight factor is bound to be less than 1—between 0 and 1.
So I think I will.

---

::: callout-note
Key formulas discussed:

- Gluon field strength tensor: $G_{\mu\nu} G^{\mu\nu}$
- Euclidean path integral weight: $e^{iS_{\text{Minkowski}}} \rightarrow e^{-S_{\text{Euclidean}}}$
- Wick rotation: $t_E = it$, $S_{\text{Minkowski}} \rightarrow -S_{\text{Euclidean}}$
:::
### Integrating Fermionic Fields and Quenched Calculations in Lattice QCD


So it's quarter to four, guys. I need ten more minutes. I would really like to show you how we get to the **quenched one-page calculations**, and we'll continue next time. I will clarify in a second. Let me just put it on the board.

---

The equations—another trick we are going to use is to get rid of the two fermionic fields. In the original equations, we had three types: $\bar{\psi}$, $\psi$, and fermionic. Despite being correlated, they are the same field but conjugated. It's convenient to consider them independent, taking into account that they have to be anticommuting. For this, we use a trick—a gluonic field.

The gluonic field turns out to be the one that leads to **confinement** and is the trickiest one. It's not easy to get rid of, and it drives thermodynamics. The gluonic field is truly important and is going to remain. But we want to integrate over the fermionic fields.

---

The way to do this is to look at the original expression and notice that the fermionic fields are weighted with an exponential factor that has a Gaussian form. This integral is a well-known integral for **Grassmann variables**. When $\psi$ and $\bar{\psi}$ are anticommuting, this integral is easy to evaluate. What you get is the determinant of $M$.

Here, it's kind of bizarre mathematics because everything here are operators, and you integrate not over $\psi$ but over all possible functional forms of it. But it works similarly to real variables.

::: callout-note
**Grassmann variable anticommutation relation**:
$$
\{X, Y\} = XY + YX = 0 \quad \Rightarrow \quad XY = -YX
$$
$$
X^2 = Y^2 = 0
$$
**Exponential of Grassmann variables**:
$$
e^{1 - XY} = 1 - XY
$$
:::
I was trying to convince myself by looking at a simple example of Grassmann variables. Grassmann means they anticommute: $XY = -YX$. That means $X^2 = Y^2 = 0$. If you write $XYXY$ and swap $Y$ and $X$, you get $X^2Y^2 = 0$. So $e^{1 - XY} = 1 - XY$. Isn't it amazing? You expand it just like that—no higher power terms are needed.

For Grassmann variables, integration is introduced as differentiation. It's a definition:
$$
\int dX \, X = 1, \quad \int dX \, 1 = 0
$$
and
$$
\int dX \, dY \, e^{-XY} = 1
$$
If you put a constant $A$ here, it becomes
$$
\int dX \, dY \, e^{-A XY} = A
$$
After that, I thought I should spend more time learning about this—it's fascinating that such a thing exists.

---

You didn't explain how the determinant pops up, right? How from $M$ you get a determinant. There is a formula. You can do this trick for two variables, say $x_1, x_2$, and even then, you get a determinant. It generalizes to higher dimensions.

::: callout-note
**Fermionic path integral and determinant**:
$$
\int \mathcal{D}\bar{\psi} \mathcal{D}\psi \, e^{-\bar{\psi} M \psi} = \det M
$$
where $M$ is the fermionic operator (Dirac operator in QCD).
:::
---

If we integrate over the gluonic fields, what remains is the integral over all configurations of the quark fields. The operator depends only on the gauge fields, and the determinant represents the effect of virtual quarks. All quarks are integrated, so the only effect is $\bar{Q}Q$ popping up from the vacuum. This expression only cares about gluons, and quarks only appear in loops.

Now, important terminology: **quenched and unquenched calculations** refer to this term. When lattice physicists say "quenched calculations," it means this term is ignored—no quarks in loops. This universe without quark loops is not so different and provides valuable insights into QCD. It's also much cheaper computationally—the integral converges faster without this term. Remember: **"quenched" means no fermion determinant**.

::: callout-note
**Quenched approximation**:
$$
Z_{\text{quenched}} = \int \mathcal{D}A \, e^{-S_{\text{gluon}}[A]}
$$
instead of the full (unquenched) partition function:
$$
Z_{\text{unquenched}} = \int \mathcal{D}A \, \det M[A] \, e^{-S_{\text{gluon}}[A]}
$$
where $S_{\text{gluon}}[A]$ is the gluonic action and $\det M[A]$ represents virtual quark loops.
:::
---

The last thing is how we compute this integral. Naively, you could discretize space and integrate over all lattice values. For a lattice of size $100 \times 200$ (time × space), how many variables are there? The gluon field $A_\mu$ has 4 × 9 components (plus complex parts). That's 8,640 variables per site. If you replace $DA$ with integrals over all these, you'd need $10^{10}$ evaluations. Even with 3 points per dimension, it's $3^{10^{10}}$—impossible to compute in the age of the universe.

Instead, we use **Monte Carlo sampling**. Configurations are sampled randomly with a weight, making the calculation feasible. For lattice QCD, discretize spacetime, use Minkowski transformations, and apply Monte Carlo sampling for the weights. This trick also helps eliminate fermions.

::: callout-note
**Monte Carlo sampling for lattice QCD**:
$$
\langle \mathcal{O} \rangle \approx \frac{1}{N} \sum_{i=1}^N \mathcal{O}[A_i]
$$
where $A_i$ are gauge field configurations sampled with weight $e^{-S[A_i]}$.
:::
---

If you take these five points home, I’d be happy. With that, I’ll take questions and finish here.

### Fermionic Action, Gluon Dependence, and Grassmann Variables in QCD


**Question:** How is it possible that we can split the fermionic and gluon part of the action? If I look at the dimension, I can see that in the long derivative we have terms that give us gluon fields. But then how do we split it?

::: callout-note
The fermionic part of the action in path integral representation is:
$$ e^{-S_{\text{fermionic}}} = \int \mathcal{D}\psi \mathcal{D}\bar{\psi} \, e^{\int d^4x \, \bar{\psi}(D + M)\psi} $$
:::
We don’t split it. The fermionic part is this:
$$ e^{-S_{\text{fermionic}}} = \int \mathcal{D}\psi \mathcal{D}\bar{\psi} \, e^{\int d^4x \, \bar{\psi}(D + M)\psi} $$

Once you integrate over $\psi$, the matrix $M$ still depends on the gluon fields.

---

**Question:** What is the meaning of $M$?
It is $A$.

**Question:** But then how did I split my Lagrangian?
The full QCD Lagrangian is split as:
$$ \mathcal{L}_{\text{QCD}} = \mathcal{L}_D + \mathcal{L}_F $$
Here, $\mathcal{L}_F$ is still dependent on $A$.

**Question:** So $M$ is a function of $A$?
Yes, $M$ is a function of $A$.

---

Ignoring $D_4$, the fermionic part is:
$$ e^{-S_{\text{fermionic}}} = \int \mathcal{D}\psi \, e^{\int d^4x \, \bar{\psi}(D + M)\psi} $$

When you discretize this integral, it becomes:
$$ S_{\text{fermionic}} = \bar{\psi} M(A) \psi $$
Here, $\psi$ in the lattice space appears as an inner matrix product. The discretized version of the Dirac operator $D + M$ is $M(A)$.

---

**Question:** Why is it $+M$ and not $-M$?
The sign change happens when we flip the time derivative. The term $D$ flips as:
$$ \partial_t \rightarrow -\partial_t $$
The gamma matrices are also flipped differently for space and time. For time, it doesn’t flip, but for space, it flips with an $i$. The overall effect is that $D_4$ gets a minus sign.

---

**Question:** Is this what is called "passing"?
These are paths in the gluon field.

**Question:** Does a limit exist for quenched and unquenched calculations? Do they converge?
I don’t see a limit. They are two independent approaches.

---

**Question:** Historically, how was Grassmann algebra developed? How did it come to physics? 
It existed independently in mathematics before physics applications. I don’t know who introduced it to physics, but it turns out to be very useful. 
 
**Question:** Aren’t Grassmann variables limiting? You can’t square them, and series expansions truncate. 
Yes, but you can still use them to describe fields. It’s a trick, but it works. 
 
::: callout-note
The Dirac operator with mass term is: 
$$ D + M = \gamma^\mu(\partial_\mu - igA_\mu) + M $$ 
where the sign change in the discretized version occurs due to flipping time derivatives and gamma matrices.
:::
### Key Nuclear Physics Formulas and Their Interpretations



The **binding energy** of a nucleus can be described by the semi-empirical mass formula:

$$
B(A,Z) = a_V A - a_S A^{2/3} - a_C \frac{Z(Z-1)}{A^{1/3}} - a_A \frac{(A-2Z)^2}{A} + \delta(A,Z)
$$

where each term represents different contributions to the nuclear binding:

* $a_V A$ - Volume term
* $a_S A^{2/3}$ - Surface term
* $a_C \frac{Z(Z-1)}{A^{1/3}}$ - Coulomb repulsion
* $a_A \frac{(A-2Z)^2}{A}$ - Asymmetry term
* $\delta(A,Z)$ - Pairing term

---


Radioactive decay follows an **exponential law**:

$$
N(t) = N_0 e^{-\lambda t}
$$

This leads directly to the **half-life formula**:

$$
t_{1/2} = \frac{\ln 2}{\lambda}
$$

---


For quantum transitions, **Fermi's Golden Rule** gives the transition rate:

$$
\Gamma = \frac{2\pi}{\hbar} |\langle f|H'|i \rangle|^2 \rho(E_f)
$$

The **geometric cross section** for nuclear reactions is simply:

$$
\sigma = \pi R^2
$$

::: callout-note
The Gamow factor describes the quantum tunneling probability, crucial for understanding nuclear fusion rates in stars.
:::
The **Gamow factor** describes tunneling probability in nuclear reactions:

$$
P \approx \exp \left( -2 \sqrt{\frac{2\mu}{\hbar^2}} \int_{R}^{\infty} \sqrt{\frac{Z_1 Z_2 e^2}{r} - E} \, dr \right)
$$

---


The **Q-value** represents energy release in nuclear reactions:

$$
Q = (m_i - m_f) c^2
$$

Fission yields often follow a **Gaussian distribution**:

$$
Y(A) \propto \exp \left( -\frac{(A - A_0)^2}{2\sigma^2} \right)
$$

---


Neutron behavior is modeled by the **diffusion equation**:

$$
D \nabla^2 \phi - \Sigma_a \phi + S = \frac{1}{v} \frac{\partial \phi}{\partial t}
$$

The **Bethe-Bloch formula** describes energy loss of charged particles:

$$
-\frac{dE}{dx} = 4\pi n_e \left( \frac{e^2}{4\pi \epsilon_0} \right)^2 \frac{z^2}{m_e v^2} \ln \left( \frac{2 m_e v^2}{I} \right)
$$

---

Each of these formulas captures **fundamental aspects** of nuclear physics behavior, from binding energies to reaction probabilities. The semi-empirical mass formula, for instance, shows how different effects contribute to nuclear stability - the volume term, surface term, Coulomb repulsion, and asymmetry term all play their roles.

