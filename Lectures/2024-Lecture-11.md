### Exam Participation and Group Coordination Discussion


- "This form of cross section—exactly."
- "The form of a cross section, you have to remember."

> [!NOTE]
> While discussing cross sections, recall that in nuclear physics:
> $$
> \sigma = \frac{\text{Number of reactions}}{\text{Incident flux} \times \text{Target density} \times \text{Thickness}}
> $$
> This formula defines how cross sections are calculated experimentally.

---

*We might still adjust between the 23rd and 25th. Do you know who from our group would come to do the exam? We would need to have Max. Moritz, maybe Fabian.*

*I'm also not sure if she needs the credit points for this, but I will ask them if they will also come. Because Paul—I know he said he's finishing his bachelor.*

*I asked both of them, and I would actually like other guys who also have time to participate in that. Do you want to participate in the exam? We certainly have to make Dhruvanshu participate in that.*

---

**Dhruvanshu is a PhD student in our group** who was partly involved in the typing exercises. Every week he is at CERN doing his hardware work. You might have seen him in the first week he was here. We just made him take the exam. *I think it's fair.* He was skipping the entire semester—**he has to work now.**

---

- *Did you receive my email to look at the symmetry breaking?*
- *I saw it this morning. I went through it and made some notes. I started making some notes on the ideas for that.*

**Moritz**, I briefly saw it yesterday, but then I had a dentist appointment because I sent it on Friday. Yesterday was the first working day. I put a date for Hanin there on Thursday.

---

> [!IMPORTANT]
> - *You're very welcome, together with the information you obtained today.*
> - *Look at it once again and bring it to Ilya for the meeting on Thursday.*
> - **It's also important because it gives you kind of easy points.**

*The exercise is simple, and I think you might need to report—no, we don't need to report, but for our number of points you got over the semester. For every counting, please collect them.*

### Mapping Riemann Sheets and Analytic Structures in the \( S \)-Plane and \( K \)-Plane


It's a pity we started a bit late because the lecture today is very exciting—I'm particularly excited about **lattice QCD** and the **hadron spectroscopy** that we do in lattice. We will get to that next. I tried to start at 11:15, but we should be discussing lattice QCD already. Before that, we have two more items in the program. Let's start with the recap. Today is **Lecture 11**.

---

So far, we've discussed a lot about the **amplitude**, which is a function of $S$. $S$ is the **Mandelstam variable**, calculated as:

$$
S = (P_1 + P_2)^2
$$

for the scattering. This $S$ is a very convenient variable to describe the scattering amplitude, as the **partial wave** is a function of a single variable in this sense. Equivalently, one can consider the **breakup momentum**, the variable $K$, which is essentially the momentum that each particle carries. So $S$ is the squared energy of the system in the center of mass, and $K$ is the momentum of each particle in the center of mass.

---

This $K$ is related to $S$ with the **channeling function**, and the **analytic structure** of the function is somewhat simpler for $K$ in the vicinity of the threshold. What I would like to do now is to look, instead of the **$S$-plane** where the function is analytic except for a few singularities, at the **$K$-plane** and relate structures in the $S$-plane to the $K$-plane—to map these points 1, 2, 3, 4 into the other plane.

---

> [!NOTE]
> **Key mappings between $S$ and $K$:**
> - Physical region ($S > S_{\text{th}}$) maps to **real $K$**.
> - Below threshold ($S < S_{\text{th}}$):
>   - **Bound state** (first sheet) maps to **imaginary $K$** (positive imaginary axis).
>   - **Virtual state** (second sheet) maps to **negative imaginary $K$**.

---

Point 1 and point 2 are the **resonances** sitting on the **second Riemann sheet** with respect to $S$. Point 3 is the **pole on the real axis** in the first Riemann sheet, and this is the **bound state**. Point 4 (0.3) is the **virtual state**, which sits on the unphysical sheet below the threshold. I would like to have these points 1, 2, 3, 4 mapped to the other plane, as well as the real axis.

---

The **real axis above threshold** is the **physical region**, and it gets mapped to the physical region in the $K$-plane. This zero corresponds to the threshold. Below the threshold, $S$ is smaller than the threshold, and the square root of it is imaginary, so $K$ is imaginary.

But what about another square root? This is far away from the square root and does not change the sign when you cross the threshold. This is multiplied to $S - M_1^2$, and nothing happens when you go through this point. This one is always negative.

---

The **branch point** should be somewhere between zero and the threshold on this plane. The area close to zero is more complicated due to this branch point, but I want to focus on the function near the threshold.

If you were to continue that, you would have another real axis—somehow it flips back to the real axis. The dashed line would just come back to real. Number four is straightforward: we just add the dashed line, and it ends up here.

---

For number three, the negative part of the—yes, it needs to be there because it's on another Riemann sheet. This is a value of $S$ which is real but below threshold, on the other sheet. The sheets are related to the **plus/minus sign of the square root**:

$$
K = \pm \sqrt{S - S_{\text{th}}}
$$

- **First sheet**: plus sign.
- **Second sheet**: minus sign.

---

On the $K$-plane, the square root changes sign, but on the $S$-plane, $S$ does not change sign. Both sheets get mapped to the same $K$-plane, just with plus or minus.

Points 3 and 4, 2 and 1 are easy to connect analytically. You can draw lines or half-circles to connect them. The shape doesn’t matter as long as it’s analytic.

---

The $K$-plane is just $S$ mapped differently. For the **momentum plane**, you don’t have a square root because $K$ is the square root itself. If you have a function with a square root, it has two Riemann sheets. But when you replace the square root with $K$, it has a simple **single-sheet structure**.

---

The **two-sheet structure** comes from the plus or minus sign in front of the square root, which is part of the $K$-plane. If you do another mapping, like:

$$
X = K^2
$$

the squaring operation maps the $K$-plane to a **single-sheeted $X$-plane**. This is why the sheets are connected—there is no discontinuity.

---

### QCD Confinement, Chiral Perturbation Theory, and Spontaneous Symmetry Breaking


Now let's go to **physics**.
I would like to start from the discussion we had at the last lecture and discuss **QCD phenomena**—QCD and quark confinement dependence.

---

As you remember, the **fundamental fields** and **fundamental degrees of freedom** in QCD are quarks and gluons.
However, when we go to the regime, one of the important phenomena is **confinement**.
People start realizing the dynamics of QCD by looking at protons and pions—or rather, looking at neutrons.
Nuclear physics and the interactions of the nucleus have these features of confinement.

---

One compares **electron-proton scattering** or **electron-electron scattering**, where there is a coupling constant:
$$
\alpha = \frac{e^2}{4\pi} \approx \frac{1}{137}.
$$
This **electromagnetic coupling constant** is small and allows one to expand and use Feynman diagrams.
In QED, we have $\alpha = \frac{1}{137}$.

Then, for calculations of **pion** and **proton interactions**, you can make an **effective field theory**, match it to the observed phenomena, and figure out that in the **non-perturbative regime**, the theory is not perturbative.
There is **confinement**.

---

We also know that the **degrees of freedom**—all interactions of quarks and gluons—are confined to a small scale.
This makes new degrees of freedom, forming **composite fields** like mesons and baryons, or simpler objects like mesons.

---

What we discussed last time is that at **low energy**, there is an **effective theory** describing interactions: **chiral perturbation theory**.
This is an expansion of the theory in the masses and momentum of particles.
It’s not about interactions being small, but rather about masses and momentum being small.
This small parameter is used for the expansion.

> [!NOTE]
> The expansion parameter in chiral perturbation theory is:
> $$
> \mathcal{L}_{\text{eff}} \sim \sum_n c_n \left(\frac{p}{\Lambda_{\text{QCD}}}\right)^n + \mathcal{O}(m_q),
> $$
> where $p$ is momentum, $\Lambda_{\text{QCD}}$ is the QCD scale, and $m_q$ are quark masses.

---

The picture of this effective theory is that we have it.
The feature is that if you work with these **effective fields**—fermion, anti-fermion, fermion—you realize the theory experiences **spontaneous symmetry breaking**.
The potential of this theory has a **double-well structure**, and the vacuum ends up in one of the minima.

---

It’s important to make this more accurate and realize what the **sigma field** represents.
Last time we touched on this, and I reminded myself how the discussion goes.
The potential can be introduced only when you consider fields as **classical fields**, not quantum fields.
For classical fields, it’s clear what the potential is.

---

If a particle moves in a potential and its energy is below the potential barrier, it turns back.
If you hit a ball against a wall, it reflects.
This is the **classical picture**.

**Quantum fields** are different.
For quantum fields, there is a probability to end up inside the wall, with an exponential tail.
If a particle approaches the wall, the wave function has a tail inside the wall due to **quantum effects**.

---

The relation between particles, quantum fields, and classical fields comes via the **quasi-classical expansion**.
In quantum field theory, there is always $\hbar$, a small number set to one in natural units.
But you can use $\hbar$ as a small parameter and expand.
The first term in the expansion is the average value of the fields—the classical version of $\sigma$.

Now, $\sigma$ is no longer a function of $x$; it doesn’t fluctuate in spacetime but is a fixed value.
We can look at the **quasi-classical potential** of the theory as a function of $\sigma$, and that’s how we define the potential.

---

The potential has a **ring of minima**.
When you solve the problem—like in the previous assignment—you find the relation for the complex $\sigma$.
On the $x$-axis is the real part of $\sigma$, and on the $y$-axis is the imaginary part.
You can replace $\sigma$ with two independent fields, $\sigma_1$ and $\sigma_2$.
The **curvature of the potential** indicates the particle’s mass.

---

In QCD, the degrees of freedom that experience binding in the **confinement regime** are the $\sigma$ field, which is integrated over—an unimportant field.
The important degree of freedom is the **pion field**, which doesn’t experience binding and has no curvature in the potential.

The vacuum is aligned at the center, but due to **spontaneous symmetry breaking**, space is filled with the **quark condensate** of the $\sigma$ field:
$$
\langle \bar{q}q \rangle \equiv \langle \sigma \rangle = v \neq 0.
$$
On top of it, there are small fluctuations of the **massless pion field**.

---

It’s a nice picture: everything is filled with the $\sigma$ field, which fluctuates around a vacuum value rather than zero.
The pion fields are **massless**—they don’t see the curvature of the potential.
This is the **Goldstone theorem**: spontaneous symmetry breaking leads to massless bosons.

In QCD, pions are massless.
The light mesons are massless, and they only gain mass in real life due to the **Higgs mechanism**, which makes quarks massive.
If quarks were massless, pions would be massless Goldstone bosons, and the $\eta$ meson would be too.
The entire $SU(2)$ multiplet would be massless particles.

That’s it.

---

> [!IMPORTANT]
> The **Mexican hat potential** for sigma and pion fields is:
> $$
> V(\sigma, \pi) = \frac{\lambda}{4}\left(\sigma^2 + \pi^2 - v^2\right)^2,
> $$
> where $\sigma$ is the radial mode (massive) and $\pi$ is the angular mode (massless Goldstone boson).

---

The **Goldstone boson (pion) masslessness** (before Higgs mechanism) is given by:
$$
m_\pi^2 \propto m_q \quad \text{(if } m_q \to 0, \text{ then } m_\pi \to 0\text{)}.
$$

### Chiral Symmetry Breaking, Goldstone Bosons, and the η' Mass in QCD


Last time we looked at the **chiral symmetry**, checking if the Lagrangian has the symmetry that you can rotate left quarks and right quarks independently.
The idea is we look at the chiral symmetry for sure.

> [!NOTE]
> The chiral symmetry in the QCD Lagrangian (massless case) is given by:
> $$\mathcal{L}_{QCD} = \bar{\psi}_L i \gamma^\mu D_\mu \psi_L + \bar{\psi}_R i \gamma^\mu D_\mu \psi_R$$
> where $\psi_L$ and $\psi_R$ are left- and right-handed quark fields, and $D_\mu$ is the covariant derivative.

The Lagrangian of QCD has a global $SU(2)$ symmetry when there is no mass term present.
This symmetry is broken **spontaneously** when you move to the minimum of the theory.

If you introduce independent rotations of the right and left fields, it was related to the rotations one can think of.
This is the rotation in the $\sigma$ field—the symmetry of the potential.
Once you move to the spontaneously broken phase, once you move to the minimum, you don't have this symmetry anymore.
This symmetry is broken, and it is a global symmetry.

The breaking of this left-right symmetry leads to the appearance of **Goldstone bosons**, which are pions and they are massless.

> [!IMPORTANT]
> For $SU(2)_L \times SU(2)_R \to SU(2)_V$, the number of Goldstone bosons is:
> $$\text{dim}(G/H) = \text{dim}(SU(2)_L \times SU(2)_R) - \text{dim}(SU(2)_V) = 3$$

When they acquire some mass, if the symmetry is bigger, like $SU(3)$, we have eight mesons now that are massive.
These are two kaons, two or three pions, and eight eta mesons appear to be massless.
Why are they not massless? Because quarks have mass.

> [!NOTE]
> For $SU(3)_L \times SU(3)_R \to SU(3)_V$, the number of pseudo-Goldstone bosons (pions, kaons, eta) is:
> $$8 = \text{dim}(SU(3)_L \times SU(3)_R) - \text{dim}(SU(3)_V)$$

I just made a connection with the **Higgs mechanism** because it's the Higgs interaction with quarks that gives them mass.
These are **Yukawa couplings**.
This discussion is kind of irrelevant for the current perturbation theory.
We just put a mass term explicitly in the Lagrangian.

> [!NOTE]
> The Yukawa coupling for quark masses in the Standard Model is:
> $$\mathcal{L}_{Yukawa} = -y_f \bar{\psi}_L \phi \psi_R + h.c.$$
> where $\phi$ is the Higgs field and $y_f$ is the Yukawa coupling constant.

Now, having discovered the Higgs, we know that something similar to this fundamental symmetry breaking happens with the Higgs field.
The vacuum is filled with the Higgs, through which particles, when moving, obtain mass.
This is something connected but different—a different phenomenon.
For the chiral perturbation theory, the mass term explicitly appears in the Lagrangian and breaks the symmetry explicitly.

The Yukawa coupling in the Higgs mechanism introduces mass.
The original mechanism Yukawa invented was the exchange of pions—the Yukawa potential.
Now, in the Standard Model, the mass matrix is introduced through terms called Yukawa couplings.

It's a bit tricky about the $\eta'$ because even if you consider QCD without mass terms, the $\eta'$ still appears massive.
The $\eta'$ is the one related to the $U(1)$ symmetry.

> [!IMPORTANT]
> The axial $U(1)_A$ anomaly leads to a mass for the $\eta'$ meson even in the chiral limit:
> $$m_{\eta'}^2 \sim \frac{N_f}{F_\pi^2} \chi_{top}$$
> where $\chi_{top}$ is the topological susceptibility and $N_f$ is the number of flavors.

Here, $S$ for both groups means "special," meaning the determinant of the matrix is equal to 1.
The group $U(2)$ is equal to $SU(2) \times U(1)$.

> [!NOTE]
> The relation between $U(N)$ and $SU(N) \times U(1)$ is:
> $$U(N) \simeq SU(N) \times U(1)/\mathbb{Z}_N$$

If you allow the determinant to be a phase, like if $U(1)$ is a unitary group where the determinant of the matrix squared is one, you can consider this being one but have an extra phase for the determinant.
The Lagrangian is seemingly invariant under $U(1)$, under this phase rotation, especially globally, so that all derivatives don't touch this phase.
If you look at the composition of the field, like $\bar{\psi}\psi$, it's invariant under the phase transformation.

But apparently, this symmetry is also broken dynamically.
If you compute higher-order perturbations, you find out that this symmetry is spontaneously broken.
That's related to the mass of the $\eta'$.
Once you see the light meson octet, you remember there is an $\eta'$ there, which is special.

The number of generators in $U(2)$ is 4, and in $U(3)$ it's 9.
For $SU(3)$, 8 generators belong to $SU(3)$, and these 8 are spontaneously broken, giving 8 Goldstone bosons—pions and kaons.
The $U(1)$ is seemingly a symmetry, but it could also be broken.
There are anomalies that make the $\eta'$ massive even when the masses of quarks are zero.

---

1. **Chiral symmetry in QCD Lagrangian (massless case)**:
$\mathcal{L}_{QCD} = \bar{\psi}_L i \gamma^\mu D_\mu \psi_L + \bar{\psi}_R i \gamma^\mu D_\mu \psi_R$

2. **Goldstone bosons from spontaneous symmetry breaking**:
For $SU(2)_L \times SU(2)_R \to SU(2)_V$, the number of Goldstone bosons is:
$\text{dim}(G/H) = \text{dim}(SU(2)_L \times SU(2)_R) - \text{dim}(SU(2)_V) = 3$

3. **SU(3) case with explicit symmetry breaking**:
For $SU(3)_L \times SU(3)_R \to SU(3)_V$, the pseudo-Goldstone bosons (pions, kaons, eta) number:
$8 = \text{dim}(SU(3)_L \times SU(3)_R) - \text{dim}(SU(3)_V)$

4. **Yukawa coupling for quark masses**:
$\mathcal{L}_{Yukawa} = -y_f \bar{\psi}_L \phi \psi_R + h.c.$

5. **U(1) anomaly and $\eta'$ mass**:
$m_{\eta'}^2 \sim \frac{N_f}{F_\pi^2} \chi_{top}$

6. **Group decomposition**:
$U(N) \simeq SU(N) \times U(1)/\mathbb{Z}_N$

### Proton Mass and Chiral Symmetry in the Context of Quark-Gluon Interactions


We discussed so far about **pions** and **kaons**, but the **proton** is also made of three quarks. There is nothing here that tells or that we haven't discussed the mass of the proton yet. But what's your guess? If you go to the **chiral perturbation theory** in the **chiral limit**, you put masses of quarks to zero:
$$ m_u = m_d = 0 $$
What happens with the proton?

* **Pion** is massless.
* **Kaon** is massless,
* so the **proton** should also be massless because all masses are zero.

But maybe the **gluon mass** makes the difference.

---

> [!IMPORTANT]
> Pions and kaons are special—they are **Goldstone bosons** of the chiral symmetry, but the proton is actually massive. The proton has energy of the quark-gluon interaction stored into it. The mass of the proton is purely determined by the quark-gluon interactions:
> $$ m_p \approx \Lambda_{\text{QCD}} \sim \mathcal{O}(1 \text{ GeV}) $$

---

Do we have **quark-gluon interactions** in mesons as well? We do, but we have a **condensate** of the quarks, and this is the **sigma field**.

* **Pions** are little fluctuations on the background of this field.
* **Protons** are something different—they are sort of excitations of this condensate.
* **Rho mesons** are excitations of the gluon condensate, but protons are a different type of object.

---

Pions are special—they are massless. The proton just experiences this heavy gluon condensate. The rest of the hadrons, especially except for those **Goldstone bosons**, have a proper mass related to the quark-gluon interaction, and everything sits on the background of this **gluon condensate**. This is tricky to wrap your mind around.

---

One thing that would help is to look at the **mathematics of the mechanism** to see how **sigma** obtains its vacuum non-trivial expectation value:
$$ \langle \sigma \rangle = v = \sqrt{\frac{\mu^2}{\lambda}} $$
and how **pions** appear as fluctuations in directions where there is no potential.

* The **mass of the particles** is the curvature of the potential.
* **Pions** move in directions where there is no curvature, which is why they don't have masses.
* **Protons, rho mesons, and other excitations** are different because they have this background field excited—they have energy stored and thus have mass.

---

One important point is that the theory itself does not have values of the masses that are special. You can **tune the masses**—you can increase them or make them zero—and then you have a series. But once you introduce the masses, the theory doesn't change very much. Especially because the masses of the light quarks \( u \) and \( d \) are rather small—they are smaller than the **QCD scale** of **1 GeV**. There is no big change in the physics when you introduce small-mass quarks.

---

What happens then? When you introduce **quark masses**, you effectively add a linear term to your potential, skewing it slightly. The picture remains almost the same—it's just that the minimum on one side gets more pronounced. Now there is curvature in the pion direction as well. It's a **Mexican hat potential**:
$$ V(\sigma, \vec{\pi}) = -\frac{\mu^2}{2}(\sigma^2 + \vec{\pi}^2) + \frac{\lambda}{4}(\sigma^2 + \vec{\pi}^2)^2 $$

With quark masses, the potential becomes:
$$ V(\sigma, \vec{\pi}) \rightarrow V(\sigma, \vec{\pi}) - c \sigma $$

This gives pions a small mass:
$$ m_\pi^2 \propto m_q \Lambda_{\text{QCD}} $$

---

Moreover, one of the quantities often introduced is the **mass of the proton over the mass of the rho meson**, which is characterized by the QCD interaction:
$$ \frac{m_p}{m_\rho} \approx \text{constant} $$

This doesn't change much if you increase the quark mass.

---

We will see that computations of the properties of the **chiral perturbation theory** depend very much on the quark masses you put in. It appears easier to calculate when pions are slightly heavier, which is what you do by introducing slightly larger quark masses. Then you do computations for slightly heavier pions. But the properties of the theory—the meson properties—do not change much. The details change, like the mass and width of the particles, but the characteristics remain. You can still learn a lot from **non-physical particle masses**.

You shouldn't be scared by seeing **unphysical pion masses** or quark masses in calculations. Quantitatively, this is a tool we use to learn about the properties of the theory.

---

### Discretization and Grid Setup in Lattice QCD Calculations


Now let's move on to discuss **lattice QCD**.

The fields depend on the four-dimensional coordinate vector $x^\mu = (t, \vec{x})$, which includes time and spatial dimensions.

> [!NOTE]
> The spacetime coordinate is explicitly represented as:
> $$x^\mu = (x^0, x^1, x^2, x^3) = (t, \vec{x})$$

What we do is introduce a **grid** in both the spatial and time dimensions, then compute the **Lagrangian action** or **particle correlations** on this grid.

> [!NOTE]
> The lattice action (simplified form) is:
> $$S_{\text{lattice}} = \sum_{n,\mu,\nu} \text{Re}\, \text{Tr}\left[1 - U_{\mu\nu}(n)\right] + \sum_n \bar{\psi}_n D \psi_n$$
> where $U_{\mu\nu}$ is the plaquette variable and $D$ is the Dirac operator on the lattice.

Typically, lattice QCD setups use a time dimension of around **200 points**, with a spatial lattice size of about **7 Fermi**, discretized into **50 points** in each dimension.

> [!NOTE]
> The lattice spacing $a$ and temporal extent $T$ are given by:
> $$a = \frac{L}{N}$$
> $$T = N_t a_t$$
> where $L = 7$ Fermi, $N = 50$, and $N_t = 200$.

Imagine a box with **50 points on each side**. We then observe how it evolves over time by performing **200 steps**.

These values are determined experimentally by testing what works best for calculations.

### Finite Volume Effects and Discretization Errors in Particle Simulation


The computations are **very numerically heavy**. Therefore, the lower number of points you can take, the better. But there are two main challenges when you put a particle in the box:

1. **Finite volume effect**: Finite box, finite volume—you more often hear "finite volume effect."
2. **Discretization error**: Both of them can be addressed: the first by making the volume bigger, the second by making the steps smaller. This comes with the cost of computation.

> [!NOTE]
> The finite volume effect leads to an energy shift approximated by:
> $$\Delta E(L) \sim \frac{C}{L^3} e^{-m_\pi L}$$
> where $L$ is the box size, $m_\pi$ is the pion mass, and $C$ is a constant.

---

It’s intuitive—you would need an **infinite and continuous space** to avoid these issues. That's all there is to it.

Here’s an analogy to help visualize the lattice: think of Wi-Fi and the point-and-box aspect. This is important because we use **cyclic or periodic boundary conditions**. If you put a proton in the box and calculate its properties, due to the finite size and periodic boundary conditions, it sees its mirror image.

> [!IMPORTANT]
> Periodic boundary conditions enforce:
> $$\psi(x + L) = \psi(x)$$
> This avoids forcing the wave function to vanish at the borders, unlike fixed boundary conditions.

---

Why use periodic boundary conditions? There are advantages. What are the alternatives? You could just say the box ends there. If you only calculate something inside the box, it shouldn’t make a difference. But if the box ends there, the boundary condition would still impose **quantization** and affect the wave function.

For example, if the wave function had to vanish at the borders, you’d have a lower probability there. That’s my explanation.

---

Periodic boundary conditions have advantages—the wave function, in a second quantization context, isn’t forced to vanish at the borders. The two approaches are similar, but one fixes the entire wave function while the other lets it move. One is more like a **static configuration**, the other more **dynamic**.

> [!NOTE]
> Quantized momentum on a lattice with periodic boundary conditions is given by:
> $$p_i = \frac{2\pi n_i}{L}, \quad n_i \in \mathbb{Z}$$

---

I would have assumed it wouldn’t make a difference, but uncertainties introduced by a finite box are **exponentially suppressed** for certain good observables.

> [!NOTE]
> The finite-volume correction to a hadron's mass follows:
> $$m(L) = m_\infty + \frac{A}{L} e^{-m_\pi L} + \cdots$$
> where $m_\infty$ is the infinite-volume mass and $A$ is a constant.

### Finite Volume Effects, Discretization, and Observables in Lattice QCD


I have to be vague since we just decided to spend one lecture on QCD.
I should have started by saying that one can spend a semester or several semesters learning **quantum chromodynamics on the lattice**.
It's a rapidly moving field with many interesting techniques.
Unfortunately, I can only give you a brief overview.

> [!NOTE]
> The lecturer suggests reaching out to John Gulava for a deeper dive into QCD next semester, as he is the ideal expert for detailed explanations.

Can you convince John Gulava to hold a lecture on this topic next semester?
I could talk to him.
He would dream of giving these lectures, and he would be the right person to explain all the details.
But let me just give you some vague arguments, a taste of the computations, and some common knowledge about it.

---

We discussed **finite volume effects**.
My claim is that corrections due to the lattice size for good observables like particle masses or form factors are *exponentially suppressed* with the lightest degrees of freedom of the theory, which is the pion.

The reason for this is that if you put a proton on the lattice, pions are present as well.
The proton is addressed, so pions—these beautiful particles—pop up as **virtual particles**.
They don't propagate; they exist in clouds around the proton, mediating interactions.
Since they are virtual, they cannot sample the boundary of the box.
Because pions are the lightest particles, they set the scale for this suppression.

Another way to see why it scales this way is to look at interactions in momentum space.
The potential has a **Yukawa form**, proportional to:

$$
V(r) \propto \frac{e^{-m_\pi r}}{r},
$$

where $r$ is the distance.
This also gives you an argument for why the effects are exponentially suppressed.

---

This exponential factor is **key**.
It means that once your lattice is large compared to the inverse pion mass, your computations closely approximate infinite-volume quantities.
However, they are still finite-volume quantities.
It's important to realize that physics in a box is... or rather, **infinite-volume physics** is the ideal case.
Once you take $L$ to infinity, you approach infinite-volume quantities, and then you have the physical situation.

Now, **discretization errors**—I won’t discuss them in detail, but they are also important.
The more steps you take, the better.

---

Regarding finite volume effects: would assuming a much larger but mostly empty box make computations much more intensive?
*Empty in what sense? No particles?*
If the box were infinite, most of it would be empty—we wouldn’t see particles except those we put in.
But it’s slightly different.
The nodes of the lattice all have fields defined.
For every node, we have $\psi(x)$ defined.
We work with a box where all fields interact, and even if you don’t insert particles, the vacuum fluctuates.
The box is never empty; it’s filled with **quantum fields**.
There are beautiful animations of virtual particle bubbles appearing and disappearing in this vacuum.

---

It wouldn’t make sense to change discretization to have different spacings.
Maybe varying grid spacing could be considered, but this is related to the **Serber curve** and confinement.
The grid spacing determines the scale at which you cut off the theory.
Small step sizes are crucial because if $a$ is too large, QCD loses confinement.

To answer your question: changing $a$ must be done carefully.
Lattice researchers ensure results aren’t strongly affected by spacing by performing computations at multiple discretization levels.
For example, in lattice papers, you’ll see results for $a = 0.1, 0.05, 0.02$ fm, etc., to demonstrate discretization errors are under control.
This is a tricky subject, often addressed numerically.

---

Now, how are changes in states implemented? Is it some sort of hopping probability for particles?
What we do is compute observables—specifically, **correlation functions**.
These are expectation values of operators at time $t$ and time $0$, formally defined as:

$$
\langle O(t)O(0) \rangle = \frac{\int \mathcal{D} \psi \mathcal{D} \bar{\psi} \, O(t)O(0) e^{-S[\psi, \bar{\psi}]}}{\int \mathcal{D} \psi \mathcal{D} \bar{\psi} \, e^{-S[\psi, \bar{\psi}]}},
$$

where $S$ is the action.
On the lattice, this involves $(L/a)^3 \times (T/a) \times 4$ (Lorentz) $\times 3$ (color) dimensions.
The $\psi$ field is a 4D Dirac spinor with color and flavor (SU(3)).

This integral is enormous—think $10^4$ dimensions or more.
Numerically evaluating it by direct discretization is impossible.
Instead, we use **Monte Carlo methods** from statistical mechanics.
We generate field configurations (samples) and evaluate observables statistically.

---

The key problem is the oscillatory phase factor in Minkowski space, which ruins convergence.
To fix this, we **Wick-rotate** to Euclidean time, making the weights real and the integral tractable.

In Euclidean space, operator correlations decay exponentially with energy gaps.
For example, a two-point function $\langle O(t)O(0) \rangle$ behaves as:

$$
\sum_n |\langle 0|O|n \rangle|^2 e^{-E_n t}.
$$

At large $t$, the lightest state dominates.

To extract energies, we study the **effective mass**:

$$
m_{\text{eff}}(t) = -\log \left( \frac{C(t)}{C(t-1)} \right),
$$

which plateaus at the ground-state energy.
This is how lattice QCD computes particle masses (e.g., pions, rho mesons) and other spectral quantities.

---

> [!IMPORTANT]
> The **exponential suppression** of finite-volume effects and the **Yukawa potential** are central to understanding lattice QCD's accuracy. The Euclidean correlation functions and effective mass method are critical for extracting physical quantities numerically.

### Quantization of Momentum from Periodic Boundary Conditions


Let me say one last thing.
We are already over time, but it's important to note that the homework exercise today is to realize that **the particle in the box is slightly different from the particle in this space**.

> [!IMPORTANT]
> Due to the periodic boundary condition, you have a quantization of the momentum.
> If your wave function is $\psi(x) = e^{i p x}$, and you require that $\psi(x + L) = \psi(x)$, you immediately realize that $p L$ must be $2 \pi n$, where $n$ is an integer.

The key relationships discussed are:

* Wave function periodicity: $\psi(x + L) = \psi(x)$
* Quantized momentum condition: $p = \frac{2\pi n}{L}$
* Phase matching: $e^{i p L} = e^{i 2\pi n} = 1$

---

The $n$ comes in if you take more than one $L$. It's a **phase condition**: for the wave function to match, the exponent must satisfy $p L = 2 \pi n$.
This ensures:

$$
e^{i p L} = e^{i 2 \pi n} = 1
$$

meaning the phase repeats every $L$.

---

I thought $L$ would be just $2 \pi$, and $n L$ could be $2 \pi n$. But this is the same principle as a standard wave.
Even if the phase is $4 \pi$, it still represents a single period.

---

Key points to remember:
* The integer $n$ represents the quantum number for allowed momentum states
* The quantization condition $p L = 2\pi n$ arises from periodic boundary requirements
* The phase must return to its original value after distance $L$

### Quantized Momentum and Energy Shifts in a Periodic Two-Particle System


What I mean is just that it shouldn't be one if it's anything less than \( L \). It shouldn't be one if it's anything less than \( L \). For \( l = \frac{1}{2} \), it could be one. Why not?

So it means that the **momentum of particles is quantized** and can only take values in steps as small as \( \frac{1}{L} \). The quantized momentum condition for particles in a periodic system is:

$$
p_n = \frac{2\pi n}{L} \quad \text{where } n \in \mathbb{Z}.
$$

Therefore, if you consider a two-particle system, it has a **discrete spectrum**. Here, \( M = 1 \), \( n = 2 \), \( n = 3 \), and \( n = 4 \). This is the periodic boundary condition.

You can think of two particles moving in a circle of length \( L \). The one-dimensional case of this box computation would be a circle, and the spectrum is discrete.

---

In that case, the energy of the system is equal to the sum of the energies of the particles. For a **non-interacting system**, the energy spectrum is:

$$
E_{\text{non-int}} = \sum_{i=1}^{2} \frac{p_i^2}{2m} = \sum_{i=1}^{2} \frac{(2\pi n_i)^2}{2mL^2}.
$$

The particles are freely moving and do not interact. However, once interactions are introduced, the energy of the system becomes slightly different. We can still write the total energy, but we must account for the interaction energy.

---

It is natural that the spectrum of an **interacting system** differs from the non-interacting case. There is a shift due to interaction:

$$
\Delta E = E_{\text{int}} - E_{\text{non-int}}}.
$$

This is the idea behind computing interactions on the lattice and performing spectroscopy. First, compute the spectrum without interactions. Then, compute it with interactions and observe how the energy levels shift.

> [!IMPORTANT]
> The difference between these levels gives information about the **phase shift of the interaction**. The relation between the energy shift and the scattering phase is given by Lüscher's formula for periodic boundary conditions:
> $$
> \Delta E = -\frac{4\pi a}{mL^3} \left[1 + c_1 \frac{a}{L} + c_2 \left(\frac{a}{L}\right)^2 \right] + \mathcal{O}(L^{-6}),
> $$
> where \( a \) is the **scattering length** and \( c_i \) are numerical constants.

---

To measure this, you compute the **two-point correlator**:

$$
C(t) = \langle \mathcal{O}(t) \mathcal{O}^\dagger(0) \rangle \propto e^{-Et}.
$$

For example, compute this quantity for two pions. Observe where it saturates at high \( T \). The saturation point gives a measurement of the energy level.

Repeat the same computation for the interacting system. Compare the two results to determine the shift. Relate the shift to the scattering phase.

The way collision data connects to the answer is through another technique, typically analyzed in configuration space with real-valued wavefunctions.

### Exploring Hadron Structure and Scattering Amplitudes in Lattice QCD


This is my latest QCD lecture.
I invite you to the full lectures if someone offers them—it's a **fascinating subject**.
In recent years, we have learned so much about the **hadron spectrum** from lattice QCD.

---

The lattice provides an **isolated setup** free from experimental effects.
You can perform calculations that are **impossible in experiments**.
For example, you can scatter two pions.
While pion scattering is possible experimentally, processes like a photon scattering off a sigma meson are **unattainable in experiments**—but not on the lattice.

> [!NOTE]
> The sigma meson, a pion-pion S-wave state, is one of the low-energy **tetraquark candidates** observed as a "blob" in the spectrum.

By studying pion-pion scattering and inserting a photon current, you can compute **correlation functions** to access form factors.
These form factors reveal the **spatial distribution** of quarks and gluons inside mesons.

---

One exciting frontier of lattice QCD is probing hadron structure by inserting currents.
This allows you to visualize how quarks and gluons are distributed spatially.
Such studies are impossible in QED, where you only have pure electronic states.

In QCD, you can compute form factors, but fixing **low-energy constants** is challenging.
Some researchers working on LPT might disagree, but I’m unaware of a reliable method.

For higher-energy experiments involving low-lying resonances, you produce them via stable particles.
You only access the production amplitude, such as:
$$ \pi + \text{proton} \to \text{target} $$

---

Unitarity constraints, which we discussed earlier, are much stricter for scattering amplitudes.
In the last lecture, I wrote a matrix element on the board, and Henrik pointed out:
*"Shouldn’t the imaginary part be positive due to unitarity?"*

This refers to the scattering amplitude $T(s)$, where:
$$ \text{Im}\,T(s) \geq 0 \quad \text{and} \quad |T(s)| \leq 1 $$
For purely elastic scattering, $|T_{el}(s)| = 1$—it must lie on the **unitary circle**.

---

On the lattice, you can access amplitudes like:
- $\pi\pi \to \pi\pi$
- $\pi\pi \to KK$
- $\pi K \to \pi K$

...all while controlling quark masses.
You can make pions **massless** or **massive**, drastically altering the elastic region.

- With **massless pions**, thresholds for $2\pi$, $3\pi$, and $5\pi$ states coincide.
- With **massive pions**, a large elastic region opens where the $2\pi$ threshold is accessible but higher thresholds (e.g., $3\pi$) remain closed.

---

This allows nearly **parameter-free studies** using unitarity constraints.
By varying quark masses, you can make particles transition in the complex $K$-plane, where:
$$ K(s) = \sqrt{s/4 - m^2} $$

Resonances appear as **poles in the second Riemann sheet**.
You can smoothly connect:
- **Bound states**
- **Resonances**
- **Virtual states**

...all manifestations of QCD.

---

Bound states, virtual states, and resonances are **deeply interconnected**.
Depending on quark masses $m_q$, a bound state can become a resonance or vice versa.
This reveals the **unified nature** of these phenomena in QCD.

### Preparing Exercise Sheets and Closing Remarks


* **On exercise sheets:**
I hope you're going to like the **exercise sheet** that Ilya kindly prepared and printed for you.
I prepared it in the night, and Ilya printed it.

---

> [!NOTE]
> **Acknowledgments:**
> Thank you very much for coming today, and sorry for going a little bit overtime.
> *Well done.*

