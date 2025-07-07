## Production Mechanisms and Kinematic Analysis in Hadron Spectroscopy


Let's start this lecture.

Today, **lecture number five** will be dedicated to the production mechanisms in different directions across the world to study **hadron spectroscopy**.

We will also go into depth on the **kinematics of different reactions**, discuss **numerical algorithms** to produce distributions of particles—particularly decays—and look at one of the most important kinematic setups: **frames** and the kinematic representation of the **phase space** for different reactions.

---

> [!NOTE]
> Key formulas referenced in this lecture:
>
> 1. **Invariant Mass** (Mandelstam variable $s$):
>    $$ s = (p_1 + p_2)^2 = (E_1 + E_2)^2 - (\vec{p}_1 + \vec{p}_2)^2 $$
>
> 2. **Decay Width**:
>    $$ \Gamma = \frac{1}{\tau} = \frac{|\mathcal{M}|^2}{2\pi} \rho_f $$
>
> 3. **Lorentz Invariant Phase Space**:
>    $$ d\Phi_n = (2\pi)^4 \delta^4\left(P - \sum_{i=1}^n p_i\right) \prod_{i=1}^n \frac{d^3p_i}{(2\pi)^3 2E_i} $$
>
> These are foundational for understanding reaction kinematics and phase space representations in hadron spectroscopy.

## Flavor Multiplets, Isospin Symmetry, and Gauge Symmetry in Baryons


Before starting, we go through the recap and I ask you quickly to give me the answers.
**Who feels confident on question number one?** Let's break it down.
So I would ask you guys in the first row to translate the words one by one.

---

- **Flavor**:
*What does "flavor" mean?* It's the charge of the strong interaction.
In this context, *what does "flavor" refer to here?* It's a **quantum number** for the multiplet.
There are many quantum numbers. This is a quantum number—the **flavor quantum number**.

> [!NOTE]
> Flavor quantum numbers include: **up, down, strange, charm** (not to be confused with **color** charges like red, green, blue).

- **Multiplet**:
*What is a multiplet?* There are singlets and multiplets.
It's **different possible combinations** for one quantum number.
Like if I have one total spin and multiple configurations, that's called multiplets.

---

*Alexander, you're up. What's your name again? Benedict.*
**Benedict, what remains for you?** The whole question.
*What are the flavor multiplets of Σ_b?*

- **Σ_b**:
*"Flavor" is clear. "Multiplet" is clear.*
Σ_b is the name of the baryon with this quark content.
We are looking for **flavor multiplets** of this baryon.

- **Baryon Composition**:
$$
\Sigma_b^+ = (u\, s\, b), \quad \Sigma_b^0 = (d\, s\, b), \quad \Sigma_b^- = (d\, d\, b)
$$
These represent the quark content of the Σ_b baryons in the **isospin multiplet**.

---

- **Isospin SU(2)**:
Replace **u** with **d**, and you get Σ_b^0.
Same particle, different isospin projection—different charge.
*What is the charge of Σ_b^0?* It's neutral.

- **SU(3) Flavor Multiplets**:
For baryons composed of three quarks:
$$
3 \otimes 3 \otimes 3 = 10 \oplus 8 \oplus 8 \oplus 1
$$
(or alternatively mentioned as \(6 \oplus \bar{3}\) for 3 ⊗ 3).

---

*What are possible spins for a two-pion system?*
- **Pion**: Quantum numbers \(0^-\).
- **D-wave spin**:
$$
J^P = 2^+
$$
(from combining \(L = 2\) with total intrinsic spin \(S = 0\)).

---

*Is flavor symmetry gauge? Is Lorentz symmetry gauge?*

- **Flavor Symmetry**:
*Anna, flavor symmetry is global.*
$$
\mathcal{L} \rightarrow \mathcal{L}' = \mathcal{L} \quad \text{under global } SU(3)_\text{flavor}
$$

- **Lorentz Symmetry**:
*Can you boost different points of spacetime differently?*
No. In standard treatment, Lorentz is global:
$$
x^\mu \rightarrow \Lambda^\mu_
u x^
u \quad \text{(applied uniformly)}
$$

> [!NOTE]
> In gravity, Lorentz symmetry can be promoted to **local symmetry**, but here it is treated as global.

## Classes of Particle Production Experiments: Fixed Target vs. Collider Setups


Today is **8, 6, 6**, and we start **lecture 5** on **particle production**.
I called the first section *"A Dictionary and Slang of Particle Production,"* but I essentially want to discuss a follow-up to what Farah started last time on different production mechanisms.

---

When we talk about **production kinematics**, it makes sense to distinguish a few different classes.
We will see this classification depending on:
- The **reaction kinematics**
- The **practicalities** of the experiments

---

I want to start by separating the two different classes of experiments:
1. **Fixed target experiments**: where you install the target and shoot it with a beam.
2. **Collider experiments**: where you collide two beams.

There are practical differences in these reactions:
- The energy one can achieve is **much higher** when you collide two particles.
- However, the decay products are also **more boosted** in a fixed target experiment.

Depending on what you want to achieve—either **higher collision energy** or **more forward-boosted decay products**—you should choose different reactions.

---

Most of the time, fixed target experiments study reactions that were **historically easier to perform**.
- You just need the target and the beam, and the setup is much simpler.
- Essentially, you only care about the **beam production**.
- The two particles are directed to your experiment, and the target is a simple fixed setup.

> [!NOTE]
> The **interaction rate** in fixed target experiments can be expressed as:
> $$R = \Phi \cdot \sigma \cdot n \cdot L$$
> where:
> - $\Phi$ = beam flux
> - $\sigma$ = interaction cross section
> - $n$ = target number density
> - $L$ = target length

---

As an example, consider experiments with **fixed target particle production** and **hadron spectroscopy studies**.
I would name the **GlueX experiment** that Farah introduced last time, where we have:
- A **photon beam** on a **hydrogen target**
- **Pion or proton beams**
- Sometimes a **mixed beam of K and N**

There are different targets:
- **Lead**
- **Front targets**
- **Ammonia** (for polarized targets)
But mostly, it’s a **hydrogen target**.

---

To give you an idea, **hydrogen targets** are the most popular in hadron spectroscopy.
- They look like a **1-meter pipe, 30 cm long**, filled with **liquid hydrogen**—which is **highly explosive**.
- Handling this apparatus requires **great care**.
- The hydrogen must be kept **liquid under high pressure**.
- Not every experiment can operate with such a setup.

> [!CAUTION]
> At CERN, setting up **COMPASS** took years of effort to pass security inspections for a liquid hydrogen target.
> - If it exploded, it could destroy the **entire building**.
> - With such a volume of liquid hydrogen (e.g., 1 meter long and 30 cm in diameter), it would be a **major disaster**.

---

The beam interacts with protons in the hydrogen target somewhere inside it.
- By reconstructing **final-state particles** and tracing them back, you can determine the exact **interaction vertex**.
- If you collect data for days and plot the vertex distribution, it matches the **target shape**.

One funny observation is that the target isn’t always filled to **100%**.
- If you plot the **XY coordinates**, you see empty regions where there are no vertices.
- This is a **transverse cut** of the target.

The beam has a **Gaussian profile**:
$$
\frac{dN}{dr} \propto \exp\left(-\frac{r^2}{2\sigma_r^2}\right)
$$
and is slightly **wider than the target** in COMPASS, so the entire target is exposed.
- Ideally, the beam should be **more focused** to avoid wasting particles that miss the target.

---

A **beryllium target** is simpler—just a **3 cm disk**, a few centimeters thick.
- It’s the **cheapest and easiest** target to use.
- At this thickness, it provides a **significant particle production rate**.

**Lead targets** have even higher **Z**, so the cross section is larger.
- The cross section scales with **Z** (the number of protons in the target):
$$\sigma \propto Z^\alpha$$
where $\alpha$ is typically **1-2** depending on the process.
- For some physics programs, **heavy-Z targets** are preferred.

---

Earlier, we discussed how the **Buicks setup** differs slightly.
To produce photons for experiments, you use **bremsstrahlung** from electron scattering:
- When electrons pass through a **thin foil** (a few hundred micrometers), photons are emitted.
- The electron beam is converted into a **photon beam**.
- Electrons that emit bremsstrahlung lose momentum and are deflected by a magnet, while the photons continue forward.
- A **magnetic field** placed after the foil removes all electrons, leaving only the photon beam to hit the target.

> [!NOTE]
> The **bremsstrahlung cross section** for photon production is:
> $$\frac{d\sigma}{dE_\gamma} \propto \frac{Z^2}{E_\gamma}$$
> where $Z$ is the atomic number of the target and $E_\gamma$ is the photon energy.

## Exclusive vs. Inclusive Processes and Kinematic Frames in Particle Production


To discuss the physics of the production mechanism, we draw **cartoons** like this, where the incoming particles enter the blob on the left side and outgoing particles appear on the right side.
When we account for all the particles and none are missing, we call the production **"exclusive,"** which should be contrasted with **"inclusive"** processes.

---

In **inclusive processes**, we characterize the class of reactions as **statistical ensembles**.
We say we don’t care about each individual state—the 2 pions, 3 pions, 2 kaons—they are produced in addition to the one.
We only care that the **1 kaon** is produced and nothing else.

---

**Exclusive and inclusive reactions are complementary to each other.**
If one wants to understand the exact details of the production mechanism—where this kaon comes from, which particular resonance—one has to study **exclusive processes**.
Inclusive processes average over different production mechanisms and in turn provide access to **average quantities** that are sometimes not accessible otherwise.

---

> [!NOTE]
> **Key distinction**:
> - **Exclusive**: All particles accounted for.
> - **Inclusive**: Only specific particles of interest are tracked, others are averaged over.

---

If you want to see how this **strangeness** is produced—well, depending on the case, it would probably be better to use **muons** here.
That’s what is studied in **COMPASS**: a muon gets scattered, and a kaon is detected.
To make these computations more physical—if you want to study the strangeness inside the proton—we would study reactions like this: the **electromagnetic current** from the muon interacts with the proton, and somehow a kaon gets produced.
This gives us access to the **gluon probability distribution function** inside the proton—how strange quarks are produced from the sea of gluons inside the proton.
That’s a typical example of an **inclusive process**.

---

For now, let’s focus on the **kinematics of exclusive reactions**.
I want to introduce two important **kinematic frames** used for studying these reactions.
In particle physics, we deal with **four-vectors**—quantities that, under boost transformations, follow Lorentz group representations.
We know how to boost and rotate four-vectors, and the frame in which you perform computations does not matter in principle.
However, for **practical considerations**, some frames are better suited.
When discussing quantities like angles or specific energy values, it’s crucial to specify the frame.

---

Translating between frames is **mathematically straightforward**—a conceptually simple procedure.
You are in one frame, you boost, and your energy and angles change.
However, it still requires **practice**, which is why it’s worth discussing.

---

Let’s start with the **center-of-momentum frame**.
In this frame, the four-vectors of the beam and target sum to zero—they are **back-to-back**.
Here, I have a **photon**, and here I have a **proton**.
In the center-of-momentum frame, the magnitudes of these two vectors are equal.
Then we have scattered particles: here, a **recoiling proton**, and here, a combination of **two pions**.
Clearly, these two vectors are equal and back-to-back, as are these two.
Thus, we have a **reaction plane**.

---

The total energy is given by the square of the sum of the four-vectors of the target and beam—this is our **Mandelstam variable $S$**, the center-of-mass energy squared:

$$
S = (P_{\text{beam}} + P_{\text{target}})^2
$$

---

There’s a **trick** to evaluate the magnitudes of these vectors and momenta using this relation: for the target four-vector, we write it as the total minus the beam, square it, and obtain $S + m_{\text{beam}}^2$ (which is zero for a photon) minus $m_{\text{target}}^2$.
This formula holds in any rest frame.
If you have two particles at rest, the energy of each particle is computed as:

$$
E_1 = \frac{S + m_1^2 - m_2^2}{2 \sqrt{S}}
$$

---

Another useful relation comes from squaring the energy expression and subtracting the mass: $E^2 - m^2 = p^2$, leading to the **breakup momentum formula**:

$$
p = \frac{\sqrt{\lambda(S, m_1^2, m_2^2)}}{2 \sqrt{S}}
$$

where $\lambda(x, y, z)$ is the **Källén (or triangle) function**:

$$
\lambda(x, y, z) = x^2 + y^2 + z^2 - 2xy - 2xz - 2yz
$$

This function is **symmetric** in its arguments, so the order doesn’t matter.

---

Now, let’s compute momenta for **final-state particles**.
The expression remains the same—just replace the masses with those of the decay products.
For example, for the two-pion system, we use $m_{\pi\pi}^2$, $m_{\text{recoil}}^2$, and $m_{\text{proton}}^2$.

---

A question arises: This only works if we treat the two pions as a **single particle** moving in the same direction.
Why can we do this? The answer is **kinematics, not physics**.
We write momentum conservation as:

$$
P_{\text{target}} + P_{\text{beam}} = (P_{\pi^+} + P_{\pi^-}) + P_{\text{recoil}}
$$

and replace $P_{\pi^+} + P_{\pi^-}$ with $P_{\pi\pi}$.
This composite four-vector has its own energy and momentum, but the pions need not be collinear—they can decay at an angle.

---

Now, let’s expand on the $\pi\pi$ production.
We can go to the **rest frame of the $\pi\pi$ system**—the **Gottfried-Jackson frame**—where the two pions are back-to-back.
This frame is common in **spectroscopy studies**.
It’s obtained by boosting and rotating along the resonance direction, aligning the beam with the $z$-axis and placing the target and recoil in the $xz$-plane.

---

In this frame, $\pi^+$ and $\pi^-$ are back-to-back, and the beam is back-to-back with the difference between the target and recoil.

Absolutely. The same trick that I applied here now can work for these two vectors.
We know that in this frame, the four-vector of the $\pi^+$ and the four-vector of the $\pi^-$ end up as a vector that has no spatial component—it’s in the rest frame.
Therefore, it’s just $(m_{\pi\pi}, \mathbf{0})$.
So let’s just write, for completeness:

$$
P_{\pi^+}^{\text{GJ}} + P_{\pi^-}^{\text{GJ}} = (m_{\pi\pi}, \mathbf{0})
$$

## Kinematics, Collider Experiments, and Particle Decay Analysis


I will probably try to add a few more exercises on kinematics because that's something worth practicing—how you derive these particular expressions—and it's all over the place. It's a very important skill to be able to operate with the **four-vectors**.

But we continue with discussing another type of the class of experiments, particularly **collider experiments**. It's the Beijing Spectrometer. There are a few collider experiments in the world, and depending on the colliding particles, you have different physics.

- **Fermilab**: Antiproton beams were collided here.
- **LHC (Large Hadron Collider)**: The biggest running machine where two protons collide.
- **LHCb**: The most dedicated experiment to study strong interactions.
- **Electron-positron machines**: Currently running are the **BESIII** and **Belle II** experiments.

---

Two important concepts to introduce are **production** and **decays**:

1. **Prompt production**: Hadrons produced directly from the colliding beams (primary vertex).
2. **Delayed production**: Long-lived particles fly away from the primary vertex and decay later.

> [!NOTE]
> The **strong interaction** is called "strong" because it makes the cross section large and processes happen quickly. The **weak interaction** is "weak" because it has a smaller cross section, leading to longer lifetimes for particles decaying weakly.

For example:
- **B meson**, **D meson**, **Lambda baryon**, **Omega baryons** all decay weakly because the strong interaction cannot change flavor or color.

---

When a particle decays weakly, its lifetime is large, allowing it to fly away from the primary vertex before decaying.

- **B meson**: Lifetime $\sim 10^{-9}$ seconds, but due to relativistic boost ($\gamma = \frac{E}{m}$), it lives longer in the lab frame.
- For $E = 500\,\text{GeV}$ and $m = 5\,\text{GeV}$, $\gamma = 100$.
- Lab-frame lifetime: $10^{-7}$ seconds.
- Travel distance: $\sim 20\,\text{mm}$.

- **Charm particles**: Shorter travel distance ($\sim 5\,\text{mm}$).

> [!IMPORTANT]
> The distance a particle travels is **not fixed**—it follows an **exponential distribution** due to quantum decay probabilities:
> $$ N(t) = N_0 e^{-\lambda t} $$

---

In experiments, we reconstruct decays by tracking final-state particles (e.g., pions). Key steps:

1. **Track reconstruction**: Fit trajectories (straight or curved in a magnetic field).
2. **Vertex fitting**: Identify secondary vertices displaced from the primary vertex.
3. **Impact parameter (IP)**: Closest distance of a track to the primary vertex, normalized by uncertainty:
$$ \text{IP} \chi^2 = \left( \frac{d}{\sigma_d} \right)^2 $$

- **Lambda decays**: Can fly meters (e.g., $5\,\text{m}$ at LHCb due to high boost).

---

When analyzing decays (e.g., $B^0 \to 3\pi$), we compute the **invariant mass**:
$$ M = \sqrt{\left( \sum_i E_i \right)^2 - \left( \sum_i \vec{p}_i \right)^2 } $$

The spectrum shows:

1. **Peak**: Centered at $M_B$, smeared by experimental resolution (Gaussian shape).
2. **Background**: Combinatorial noise from random track associations.
3. **Secondary peaks**: Misidentified particles.

> [!NOTE]
> The **multiplicity** of proton-proton collisions at the LHC ($7\,\text{TeV}$) is **a few thousand particles per event**, leading to high combinatorics in track reconstruction.

---

Theoretically, the spectrum should be a **delta function** at $M_B$, but experimental uncertainties widen it into a Gaussian.

- **Key factors**: Tracking precision, hit resolution, and energy/momentum measurements.
- **Background**: Arises from random combinations of pions passing selection cuts.

## Particle Identification and Phase Space in Decay Dynamics


The last feature I want to discuss here is **PID (Particle Identification)**. It's important for all experiments.

When we track particles, we don't measure their mass directly. The momentum is determined by the curvature of the track in the magnetic field. By solving the differential equations of charged particle motion in a magnetic field, we can fit the momentum to the measured points.

The four-vector has energy and momentum components. We measure momentum, but energy is computed under a mass assumption. For these calculations, we must assume the particle is a pion.

Among thousands of charged particles, they all look similar without extra identification. Without PID detectors, we can't distinguish pions, protons, or kaons. This assumption introduces background.

For example, in an event like $B \to K^- \pi^+ \pi^-$, the tracks look identical to our signal. If we misidentify the kaon as a pion, we compute the wrong energy. The momentum is correct, but the energy is not. This leads to an incorrect invariant mass.

If we assume a pion mass for a kaon, the reconstructed mass shifts. Since the kaon mass is larger, using a smaller pion mass distorts the result. Without PID, we'd be in trouble.

That's why experiments need good particle identification detectors, like ring-imaging Cherenkov or time-of-flight systems. These suppress misidentification.

---

> [!IMPORTANT]
> **Key Challenge in PID**:
> Misidentifying particles (e.g., kaons as pions) leads to incorrect energy calculations and distorted invariant mass reconstructions. Proper PID detectors are essential to suppress this background.

---

In experiments, simulation is crucial. We model collisions, decays, and detector interactions using computer programs.

We must know cross-sections and available phase space—the configuration space for particles.

For an $N$-particle phase space, the differential is:

$$ d\Pi_N $$

with $3N - 4$ integrals, reflecting four-momentum constraints.

For two-body phase space:

$$ d\Pi_2 = \frac{1}{8\pi} \frac{2p}{\sqrt{s}} d\Omega $$

After resolving energy-momentum conservation, only angular integrals remain.

For three-body phase space, it's more complex:

$$ d\Pi_3(1,2,3) = d\Pi_2(1,2) \times d\Pi_2((12),3) \times \frac{dM_{12}^2}{2\pi} $$

We split phase space into pairs, introducing intermediate masses.

The **Kibble function** defines the Dalitz plot boundary:

$$ \Phi = \lambda_1 \lambda_2 \lambda_3 - \lambda_1 \lambda_{23}^2 - \lambda_2 \lambda_{13}^2 - \lambda_3 \lambda_{12}^2 \leq 0 $$

where $\lambda$ is the **Källén function**:

$$ \lambda(x,y,z) = x^2 + y^2 + z^2 - 2xy - 2xz - 2yz $$

The differential decay width is:

$$ d\Gamma = \frac{|\mathcal{M}|^2}{2M_0} d\Pi $$

On the Dalitz plot, phase space is flat—only the matrix element introduces structure.

---

Let’s map momenta to a Dalitz plot. Given three momenta summing to zero, we find their coordinates.

Here’s a **COMPASS measurement example**. The mass distribution in a 2D plot reveals dynamics—phase space is uniform, but the matrix element shapes the data.

---

> [!NOTE]
> **Phase Space & Dalitz Plots**:
> - Two-body phase space reduces to angular integrals after momentum conservation.
> - Three-body phase space decomposes into sequential two-body systems with intermediate masses.
> - The Kibble function $\Phi \leq 0$ defines the physical boundary of the Dalitz plot.

