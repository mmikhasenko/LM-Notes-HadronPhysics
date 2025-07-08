### Magnetic Moment of the Omega Baryon and Excitation Patterns of the Sigma Baryon


Today's lecture is dedicated to **experiments in spectroscopy** and the **computations of kinematics** for these experiments.
But before proceeding, I would like to recap the last lecture and pose two questions:

**Question 1**: Compute the magnetic moment in the current model of the Omega baryon.

**Question 2**: Compute the lowest 1s multiplet excitation of the Σ particle parameter.

For the second question, I'm referring to **isospin fermions**. Let's address this quickly because it's straightforward.

---

First, what's the quark content of the Ω⁻? It consists of **three strange quarks**. What is the wave function? The total wave function is always a product of four parts, though not necessarily a direct product. It lives in the tensor product space of:
- Color coordinates
- Isospin
- Spin
- Spatial coordinates

Flavor is trivial here, so we focus on **spin**. Two quarks should be spin-up, and one spin-down to match the half-spin behavior of the particle. But what is the total spin? The books state it's **$3/2$**, not $1/2$. The parity is $+$, so for $L=1$, the spin would be $1/2$. But in reality, $J$ is $3/2$ precisely.

The Ω⁻ exists in a $J=3/2^+$ state. What's the multiplicity? For spin-$3/2$, how many projections are there?

> [!NOTE]
> The **spin multiplicity** for $J=3/2$ is given by:
> ```latex
> \text{Multiplicity} = 2J + 1 = 4 \quad \text{(for } J=\tfrac{3}{2}\text{)}
> ```

To obtain all components, act with a lowering operator on the maximal projection state. For the **magnetic moment calculation**, we only need one component because the magnetic moment is proportional to spin.

The magnetic moment operator is:
```latex
\hat{\mu}_z = \sum_{i=1}^3 \mu_{iz} = \sum_{i=1}^3 g_i \left(\frac{e \hbar}{2 m_i c}\right) S_{iz}
```
Here, the **g-factor** is the charge number. Since all quarks have charge $-1/3$, the total is $-1$. The magnetic moment is then:
```latex
\mu_{\Omega^-} = -3 \left(\frac{e \hbar}{2 m_s c}\right)
```
where $m_s$ is the strange quark mass (~500 MeV).

The Ω⁻ mass is roughly three times the strange quark mass:
```latex
M_{\Omega^-} \approx 3m_s \approx 1500 \text{ MeV}
```
The magnetic moment is similar to the electron's but **1000 times smaller** due to the larger mass.

**Key takeaway**: For simple wave functions, calculating the magnetic moment is straightforward. You only need the maximal projection state.

---

The ground state of the Σ baryon has:
- A light diquark in a **spin-1** configuration
- A **spin-$1/2^+$** heavy quark

The isospin multiplicity is:
```latex
\text{Multiplicity} = 2I + 1 = 3 \quad \text{(for } I=1\text{)}
```
This gives three charge partners: $+1$, $0$, and $-1$.

For the **excitation pattern**, we combine the spins of:
1. The light diquark (spin-1)
2. The heavy quark (spin-$1/2$)

For the **S-wave**, we get two states: $1/2^+$ and $3/2^+$.

For the **P-wave ($L=1$)**, combining spins gives:
```latex
J = \tfrac{1}{2}^-, \tfrac{3}{2}^-
```
The multiplicity for the P-block is **5**, while the S-block has **2 states**.

The **hyperfine splitting** energy scale is suppressed by the heavy quark mass:
```latex
\Delta E_{\text{hyperfine}} \propto \frac{1}{m_Q}
```

These states correspond to physical particles listed in the PDG. The Σ baryon (300) was discovered roughly **10 years ago**.

### Heavy Quark Spin Effects, Exotic Hadrons, and Electron-Positron Collider Experiments


Now one word about energy splitting.
The energy splitting between this and that state is caused by the spin of the heavy quark.
The radial excitation is the scale given by the quark dynamics, and this is the order of $\lambda_{\text{QCD}}$.
So that's one of the first lectures where we introduced that it's where the strong coupling, the very strong coupling, diverges.
It's roughly a few hundred MeV, and that gives you the separation of the different blocks.

Within the block, the splitting between levels comes from the dynamics of the spin of the heavy quark.
This quark is heavy, so all spin effects are suppressed inversely proportional to its mass.
In the Lagrangian—and in all effective theories—the spin-orbit interaction enters in terms like $\frac{\vec{S}_Q \cdot \vec{L}}{m_Q}$, where the mass of the heavy quark is in the denominator.
The mass of the $b$ quark is about 4 GeV, so it gives an order-of-magnitude suppression.

$\lambda_{\text{QCD}}$ is a few hundred MeV, and the quark mass is a few GeV, so the ratio between them is roughly 1:10 or 1:15.
That's the difference between excitation energies: the general quantum numbers versus the splitting between states.
For example, the energy difference between $\Sigma_b$ with spin 3/2 and $\Sigma_b$ with spin 1/2 is on the order of 10 MeV.
Can someone check that? Does the PDG list $\Sigma_b$ states?

---

Today's lecture is dedicated to kinematics and experimental techniques.
I’ll start by overviewing what we do in experimental physics.
This field has been extremely vibrant and fruitful in the last 10 years.
It began around 2004 when the first exotic particles appeared.
Since then, every few months, new observations of states that don’t fit simple meson or baryon models have been reported.
Many experiments have dedicated part of their programs to studying hadrons, especially exotic ones.

Several large labs worldwide study hadron collisions.
One key question is understanding how hadrons form: which combinations are possible, and what rules govern their excitation patterns and properties.
Quantum chromodynamics (QCD) describes strong interactions well where we can compute, but we still can’t classify or predict large multiplets of exotic hadrons.
This isn’t just due to computational limits—lattice QCD works well for ground states but struggles at this scale—but also because the theory is inherently complex.

The phenomena in QCD involve **emergent degrees of freedom**.
The Lagrangian has quarks and gluons, but these aren’t the relevant degrees of freedom for hadrons.
We’re seeing a transition between configurations where quark degrees of freedom dominate and those where hadrons themselves form larger structures, like atoms.
In spectroscopy, you face this borderline: a mix of compact quark-based hadrons and sparse hadronic molecules.

Lattice QCD can’t yet help much here, so experiments must provide new data.
We study hadrons by measuring their properties and decays, either in new decay configurations or from different production mechanisms.

---

Many labs explore different production mechanisms:

- **Electron-positron colliders**:
- Belle (Japan) and BES (China) collide electrons and positrons, producing intermediate states that decay.
- CERN’s colliders study proton-proton collisions, producing long-lived particles like $B$ and $D$ mesons.
- These travel millimeters before decaying, letting us distinguish primary and secondary vertices.

- **Hadronic production**:
- Fixed-target experiments like GlueX (Jefferson Lab, photon beam) and COMPASS (CERN, pion beam), both using hydrogen targets.

- **Lattice QCD computations**:
- Theoretical approach to complement experimental data.

---

Let’s overview experiments, starting with BES (Beijing Spectrometer).
It’s at the Beijing Electron-Positron Collider (BEPC), colliding electrons and positrons.
BES studies hadrons in the charmonium and tau regions.
The collision produces a virtual photon, which couples to hadrons.

> [!NOTE]
> **Quantum number selection rules for $e^+e^- \to \text{hadrons}$**:
> Electrons and positrons have spin-1/2, so their collision can only produce spin-1 states (not spin-0).
> The parity is also fixed, so BES explores hadrons with $J^P = 1^-$.

BES operates in two modes:
1. **Resonance peak**: Collecting data at specific energies (e.g., $J/\psi$ peak).
2. **Energy scan**: Measuring cross-sections by tuning beam energy.

The cross-section $\sigma(e^+e^- \to \text{hadrons})$ peaks at resonances like $J/\psi$ or $\psi(2S)$.
Analyzing final states (e.g., $\pi^+\pi^-\pi^0$) reveals hadron properties.

---

Belle II (Japan) is another $e^+e^-$ collider, originally for CP violation studies but also useful for spectroscopy.
It’s at the SuperKEKB accelerator (upgraded from KEKB).
Unlike symmetric colliders, Belle II uses asymmetric beam energies to boost produced $B$ mesons.

The center-of-mass energy is set to the $\Upsilon(4S)$ resonance, which decays to $B\bar{B}$ pairs.
The boost makes $B$ mesons travel farther, improving vertex resolution.
This design choice enhances sensitivity to CP violation.

---

1. **Energy splitting**:
$$
\Delta E \sim \frac{\lambda_{\text{QCD}}}{m_Q}
$$

2. **Spin-orbit interaction**:
$$
\mathcal{L}_{\text{spin-orbit}} \sim \frac{\vec{S}_Q \cdot \vec{L}}{m_Q}
$$

3. **Resonance cross-section**:
$$
\sigma \propto \frac{1}{(s - M_R^2)^2 + M_R^2 \Gamma_R^2}
$$

4. **Boosted decay length**:
$$
L = \gamma c\tau \approx \frac{E}{m_B} c\tau
$$

---

The charmonium spectrum includes:
- $J/\psi(1S)$ ($1^-$) and $\eta_c(1S)$ ($0^-$)
- $\psi(2S)$ ($1^-$)
- $P$-wave states: $\chi_{cJ}$ ($J = 0,1,2$, $J^P = 0^+,1^+,2^+$).

### Reconstructing \( e^+e^- \) Annihilation, Bottomonium Spectroscopy, and Hadron Production at Colliders


To reconstruct the schematics before we move away from Belle II, let me relate to what we just discussed.
The process remains the same: **$e^+e^-$ annihilation**. The cross section $\sigma(e^+ e^- \to \text{everything})$ is the **total cross section**.

> [!NOTE]
> **Key formula**: The total cross section for electron-positron annihilation is given by:
> $$
> \sigma(e^+ e^- \to \text{everything})
> $$

Belle's experiment operates in the region of **$J/\psi$** and **$\Upsilon$** production—**charmonium** and **bottomonium**. Belle specifically focuses on **bottomonium**, the bound states of **$b\bar{b}$**. Similarly, **charmonium** consists of **$c\bar{c}$**.

Moving further in energy, the **$\Upsilon(4S)$** resides in the **3 GeV region** (2–4 GeV). At around **10 GeV**, we reach the **bottomonium system**, which is analogous to charmonium but with a heavier quark. Since the **$b$ quark** is more massive, the **hyperfine splitting** $\Delta m = m(1^-) - m(0^-)$ is smaller. The mass difference between **$\eta_b$** and the **vector bottomonium** is reduced, and the energy levels are more condensed. The scale between levels remains roughly a few hundred MeV, but within each block, the spacing is much tighter.

Now, introducing the symbol **$\Upsilon$**: this is the **vector particle** with **spin-parity $1^-$**, the bottomonium counterpart of the **$J/\psi$**. The **$J/\psi$** is the easiest charmonium state to produce in **$e^+e^-$ annihilation** and is the most studied. Its bottomonium equivalent is the **$\Upsilon$**.

The **$\Upsilon(4S)$** is part of the **excitation spectrum**. As we scan the energy, we observe:
- **$J/\psi$**
- **$\Upsilon(1S)$**
- **$\Upsilon(2S)$**
- **$\Upsilon(3S)$**
- **$\Upsilon(4S)$**

All these states are **above threshold**, requiring beam energies above **9 GeV**. For example:
- The **$\Upsilon(1S)$** is at **9.46 GeV**
- Higher states at increasing energies

---

Proton-proton collisions are far messier. At the **LHC**, the energy scale is in the **TeV range**, and annihilation is not the primary process. The **multiplicity** of particles produced is enormous and grows with energy. In symmetric **7.7 TeV collisions**, beam remnants—mostly from quarks and gluons—are highly boosted.

**What is the typical multiplicity in such collisions?** How many particles are produced on average? The answer is roughly **a thousand per collision**. The **transverse momentum $p_T$ spectrum** follows an **exponential distribution**:
$$
\frac{dN}{dp_T} \propto e^{-p_T / T}
$$
with most particles at **low energy** and a tail extending to higher **$p_T$**. The typical energy per particle is **hundreds of GeV**, though many have much lower momentum.

---

LHCb has been highly productive in discovering new hadrons due to the **large cross section** of proton-proton interactions compared to **$e^+e^-$ annihilation**. Two main production mechanisms are explored:
1. **Prompt production**: The particle of interest originates from the primary vertex.
2. **Probe production**: Secondary vertices from decays of heavier particles.

For example, **charm production** has led to observations like the **$\Omega_c$** and **$\Xi_c^*$ baryons**. The ground state of the **cascade multiplet ($\Xi_c$)** decays weakly, with a lifetime of **$\sim 10^{-10}$ s**. At **100 GeV**, such particles travel **millimeters**, creating a **secondary vertex** resolvable from the primary vertex. By reconstructing charged particles (e.g., proton, kaon, pion), resonances appear as peaks in the **invariant mass spectrum**:
$$
M_{\text{inv}}(K^- \Xi_c^+)
$$

Another method involves studying **secondary vertices** from **$B$ hadrons** (e.g., **$B$ mesons** or **$\Lambda_b$ baryons**). These ground states decay with lifetimes of **$\sim 10^{-12}$ s**, but when boosted, they produce secondary vertices **centimeters away**. This separation allows clean reconstruction of their decays.

A prominent example is the decay **$\Lambda_b \to J/\psi p K^-$**, a **three-body process**. Peaks in the **$M_{\text{inv}}(p K^-)$** spectrum correspond to **$\Lambda$ resonances**, while peaks in **$M_{\text{inv}}(J/\psi p)$** reveal **$P_c$ states** (exotic **$u u c \bar{c}$** combinations).

---

Now, let’s briefly discuss **fixed-target experiments**. Three examples are:
1. **GlueX** at Jefferson Lab: **9 GeV photon beam** on liquid hydrogen.
2. **COMPASS** at CERN: **Pion beam** on liquid hydrogen.
3. **CLAS** at Jefferson Lab: **2 GeV photon beam**, focusing on light hadrons.

These experiments study **light hadron spectroscopy** via two mechanisms:
- **Diffraction**: The proton acts as a source of gluonic fields, with the beam (photon/pion) interacting and exciting resonances.
- **s-channel scattering**: Resonant production **$\gamma p \to X \to \text{final state}$**, where **$X$** is a hadronic resonance (e.g., **$N^*$**, **$\Delta$**).

At lower energies (**2–3 GeV**), **s-channel scattering dominates**, while higher energies involve both processes. **COMPASS** separates these regimes, while **GlueX** operates in an intermediate range where both mechanisms interfere.

Some experiments, like **GlueX**, are nearing the end of their runs but may be upgraded (e.g., **GlueX2**) to explore more exotic spectroscopy.

### Gluonic Fields, Exclusive Scattering, and Kinematic Variables in Phase Space Calculations



> [!NOTE]
> The proton remains color-neutral, so it emits a **gluonic field** rather than a single gluon. This is why we describe it as **diffraction** rather than gluon exchange.

I have a quick question regarding the diagram. You said that they interact via gluons. So is that a direct or indirect interaction? One can see that. Essentially, what is here is the layer of gluons. Since it's color neutral, it cannot be a single gluon. The proton should stay color neutral. The thing that it emits to interact is not a single gluon, but rather a gluonic field that is color neutral. We call it diffraction rather than gluon exchange because that's something special.

This process is not well understood in terms of gluons. It's understood physically. The proton sits there and emits the gluonic field. The interaction happens like light would scatter on an object and produce a diffractive picture. A similar thing happens here. The proton sits as the black disk, and what we see is a diffractive picture on the wall.

This particle that is exchanged—this letter of the gluon operators of the gluon fields—actually has a name. It's called the **pomeron**. You won't find this particle in the PDG. It's not really a particle. It's rather a phenomenological way to describe the gluon field and then the end state in delta.

---


In this session, I want to finish today's lecture with small computations and would like to count. So we move to the **K matrix**. Let's discuss **exclusive reactions**, meaning that there are no particles left uncounted in the interactions. It's a **1-to-n** or **2-to-n** scattering. When you see "exclusive," it means all of the particles are measured, all of them are accounted for. If you see the word "inclusive," it means the system is produced, but in parallel along with the system, many other particles are produced and we don't care about them. So it's an inclusive process, and in contrast, exclusive is when you measure everything.

---


Here in this diagram, I am going to draw the cartoons. They are not Feynman diagrams. The blob indicates the interaction, and the lines indicate the particles that either come in or leave. I would like to count how many kinematic variables this process can depend on. The way to do that is to think of the momentum that describes this process and then count the number of independent components and subtract the number of constraints.

It's easier to work with examples. For **2-to-3 scattering**, we have $2 + 3$ particles. Every particle has four components in the four-vector and one constraint. That's why you can remove, say, energy. Every four-vector has three independent components because the fourth is constrained by mass. Then we subtract the conservation constraints mathematically.

---


Energy-momentum conservation comes as the delta function:
$$
\delta^{(4)}\left(\sum p_{\text{final}} - \sum p_{\text{initial}}\right).
$$
It's a product of four delta functions: one for energy, one for each momentum component. The five factors come in the same power as delta functions. You will see this; that's always the case.

For **2-to-3 scattering**, we end up with:
$$
(2 + 3) \times 3 - 4 = 11.
$$
So **11 variables** are needed to describe this kinematics in any frame. But we can reduce this number by choosing a specific frame. By fixing the frame, we lose six degrees of freedom: three for rotation, three for boosts. That gives the number of variables in this type of matrix.

---


If it's clear at this stage—let me confuse you a little. Before that, maybe I should say a few words. The boost and rotation considerations are important to realize. Here's an analogy: think of the reaction—this blob—as a solid rigid body out of which the arrows are sticking. You can hold it in your hand. For rigid bodies, there are three Euler rotations that tell you the orientation. These are exactly the three rotations you have to fix.

For every event, for every set of kinematic variables, you can identify the length of the vectors and their mutual orientation. For every set, you can take a 3D printer and print it. Then these three rotations will come into play to orient it properly.

---


In the computation, we often need the quantity that counts the number of configurations in which the system can be. These configurations include not only the orientations of the overall system—the three rotations and three boosts—but also the mutual orientations of the components. Essentially, the phase space element counts the number of configurations for every particle.

For every particle in the final state, we have **Lorentz-invariant phase space**:
$$
d\Phi_n = \prod_{i=1}^n \frac{d^4 p_i}{(2\pi)^4} (2\pi) \delta(p_i^2 - m_i^2) \theta(p_i^0) \cdot (2\pi)^4 \delta^{(4)}\left(\sum p_{\text{in}} - \sum p_{\text{out}}\right).
$$
You can integrate over the energy of a particle and use the delta function to get $2E$ in the denominator. To avoid summing over negative energy, you often include a $\theta$ function for energy. Every delta function comes with its own $2\pi$. That's easy to remember.

---


The last thing I would like to discuss is the **recursive evaluation**. Here's an example of a 4-body system. Mathematically, we might have an exercise, but I don't think we need to demonstrate that this integral can be simplified to a product of two-body phase spaces. This diagram does not represent the dynamics of the process. It's simply operating with kinematic variables. So **1-to-4** is going to be another degree of freedom.

When you calculate the phase space, you see that 3 integrals come for every particle. For the phase space to count, only the final state counts. The initial state doesn't enter. The four energy-momentum conservations come here explicitly. That's the number of integrals that remain. For **2-to-3**, it's $3 \times 4 - 8 = 4$, leaving **5 kinematic variables**. The three rotations are the Euler angles, but which five you pick to parameterize your kinematics is up to you.

One particular choice is to introduce intermediate masses and write the phase space as:
$$
d\Phi_4 = \frac{dM_x^2}{2\pi} \frac{dM_y^2}{2\pi} d\Phi(0 \to Y + 3) \, d\Phi(Y \to 1 + 2).
$$
This is referred to as the **recursive expression**. It's not only valid for 2, but you can also do this for 3. The important thing is that you introduce intermediate masses and integrate over them, with every integral coming with a $2\pi$ in the denominator.

---


A more general treatment for the **two-body phase space** is:
$$
d\Phi_2 = \frac{|\mathbf{p}|}{4\pi^2 \sqrt{s}} d\Omega.
$$
With this expression, you can calculate any $n$-body phase space. There's an exercise at home to play with the **three-body phase space**. The three-body phase space has $3 \times 3 - 4 - 3 = 2$ variables, often chosen as the invariant masses of pairs, represented in a **Dalitz plot**.

