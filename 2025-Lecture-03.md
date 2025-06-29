<!--
Cosine simularity: 0.9782794181569573
-->
## Introduction and Lecture Plan

Thanks everyone who found the room and apologies for changing it all the time.  
We are fixed from now on—this room is booked and will be used for the next 10 lectures.  

Today is **Lecture 3**, where we will:  

1. Continue discussing **symmetry** from the last lecture.  
2. Examine the **structure of hadrons**—how they look inside and the experimental evidence that they are not point-like but made of quarks.  

The lecture plan is as follows:  

- Start with **kinematics**, focusing on **cross-section calculations** and **multibody kinematics**.  
- Begin with a simple **classical scattering** example (electron-proton).  
- Discuss **form factors** in scattering and their relation to hadron properties, such as:  
  - Charge distributions  
  - Magnetic moments  

- Analyze these quantities in the **quark model**, linking experimental observations to internal hadron structure.  
- Revisit **symmetry considerations** (flavor symmetry, spin symmetry) from the last lecture.  
- Explore **proton/neutron spin and flavor wave functions**.  
- Compute the **magnetic moment in the quark model** and connect it to observables.  

This structure should bring clarity to the discussion.  

<!--
Cosine simularity: 0.8736494044648536
-->
## Isospin of D Mesons and Quark Content  

Let’s recap with two questions. The first is straightforward: **What is the isospin of the $D^+$ and $D^0$ mesons?** The second is more challenging: **What is the isospin of the $\Xi_{cc}$ baryon and its quark content?**  

For the $D^+$ meson, the quark content is $c\bar{d}$, while the $D^0$ meson is $c\bar{u}$. The charm quark ($c$) has a charge of $+\frac{2}{3}$, and the up ($u$) or down ($d$) antiquarks contribute $-\frac{2}{3}$ or $+\frac{1}{3}$, respectively.  

The isospin of the $D$ mesons arises from their light quark components. The $D^+$ ($c\bar{d}$) and $D^0$ ($c\bar{u}$) form an isospin doublet with $I = \frac{1}{2}$, where $I_3 = +\frac{1}{2}$ for $D^0$ and $I_3 = -\frac{1}{2}$ for $D^+$.  

For the $\Xi_{cc}$ baryon, the quark content is $ccq$, where $q$ is a light quark ($u$ or $d$). Its isospin depends on the light quark flavor: $I = \frac{1}{2}$ if $q = u$ or $d$.  

::: callout-note
The $D$ mesons are part of the **charmed meson** family, where the heavy charm quark ($c$) pairs with a light antiquark to form states with well-defined isospin.
:::
The charge of the $D^+$ meson is $+1$ ($c\bar{d}$), while the $D^0$ is neutral ($c\bar{u}$). This aligns with their quark content and isospin assignments.

<!--
Cosine simularity: 0.9333389560479323
-->
## Orbital Angular Momentum in J/ψ Decay  

The charge of the quark is $-130$ down. We have the charge correct here. The $\Xi_{cc}$ charge is $+++$.  

Now, the second question: **$J/\psi$ decays to a pair of identical vector particles.** The $J/\psi$ has spin-parity $1^-$, and it decays to two vector particles, each with $1^-$. The question is: **What is the orbital angular momentum between these two particles to conserve parity?**  

Possible answers are $0$, $1$, or $\frac{1}{2}$. We will work on this.  

::: callout-note
The $J/\psi$ decay must conserve parity, so the orbital angular momentum ($L$) must satisfy $(-1)^L = +1$ for the final state to match the initial parity.
:::
Isospin symmetry is also relevant here.

<!--
Cosine simularity: 0.9552998881008391
-->
## Isospin Symmetry and Light Quarks

Isospin symmetry is related to the transformation of wave functions with respect to the light quarks. For example, you have a $u$ quark or $d$ quark, which are the two light quarks. The color wave function has two components: $\psi_{\text{up}}$ and $\psi_{\text{down}}$, corresponding to the up and down states.  

This two-component wave function represents a multiplicity of two, with isospin projections $+\frac{1}{2}$ or $-\frac{1}{2}$ along the quantization axis (e.g., the $z$-axis). The total isospin here is $\frac{1}{2}$.  

When you have one light quark, you are dealing with isospin $\frac{1}{2}$. If you have two light quarks, the system is a combination of two $\frac{1}{2}$ states, which can result in total isospin $1$ or $0$. The answer depends on counting the number of light quarks:  

- For one light quark, the isospin is $\frac{1}{2}$.  
- For two light quarks, the possible isospin states are $0$ or $1$.  

::: callout-note
The combination of two $\frac{1}{2}$ isospin states follows the rules of angular momentum addition, leading to either a singlet ($0$) or triplet ($1$) state.
:::
<!--
Cosine simularity: 0.9330001396474008
-->
## Extending Isospin Symmetry to Heavier Quarks

If you see the two light quarks, then you have to think either it's zero or one, but if it's one, no question. The relation to the light quarks raises a question: Why don't you have an isospin for heavier quarks? You can have a symmetry group that relates them.  

Now, consider introducing a symmetry that acts in the space of the light quarks plus charm, or light quarks plus strange. But you must include the lower quarks as well. For example, take the charm and strange quarks. Every wave function we write would consider the dimension related to the charm-strange presence. The charm quark would be the upper component, and the strange quark would be the lower component.  

This consideration is exactly the same as $SU(2)$ isospin symmetry. The problem is that our Lagrangian, our nature, does not respect this symmetry. If you change strange to charm, they do not have equal masses, so the Lagrangian is not symmetric under this transformation.  

The reason we consider $u$ and $d$ quarks as part of the same multiplet is that they have nearly identical masses. If you change $u$ to $d$, the Lagrangian remains unchanged. The mass difference is negligible—6 MeV versus 4 MeV—so they are effectively degenerate.  

Now, compare this to the strange quark, which has a mass of around 100 MeV. At the scale of 1 GeV, where chiral symmetry breaking occurs, 100 MeV is not drastically different from the light quark masses. So, we could consider the strange quark as part of the same multiplet.  

Instead of isospin, we could introduce a quantity reflecting $SU(3)$ symmetry, which accounts for the three quark flavors ($u, d, s$). This extends the concept of isospin to a larger symmetry group, describing the placement of mesons in the three-quark framework. This brings us back from isospin to the full flavor symmetry diagram.

<!--
Cosine simularity: 0.9485029917576888
-->
## Isospin Symmetry and Quark Multiplet Structure

We return to the three-quark symmetry and revisit the diagram of hypercharge versus isospin that was drawn previously. The question arises: where does this measurement lie in the hypercharge versus strangeness plane? This naturally includes the strange quark.  

Further, one could extend this to include the charm quark. While the charm quark is lighter than the top and bottom, we can theoretically consider a world where the charm, strange, and light quarks ($u, d$) have the same mass. In this scenario, mesons occupy points in a three-dimensional symmetry space:  

- One axis for **isospin**,  
- Another for **strangeness**,  
- A third for **charmness**.  

The symmetry implies that mesons like $D^0$ and $D^+$ are nearly identical under strong interactions, differing only by their light quark content ($u$ vs. $d$). Isospin symmetry asserts that swapping $u$ and $d$ quarks preserves particle properties—mass, width, decay modes—since QCD (quantum chromodynamics) does not distinguish them electromagnetically.  

For example, a meson with isospin $I=1$ has a "sibling" obtained by replacing $u \leftrightarrow d$. This reflects the multiplet structure, where particles differing only by isospin are grouped together in experimental data (e.g., the Particle Data Group listings).  

A follow-up question arises: does this symmetry extend to antiquark combinations like $\bar{u}d$ and $\bar{d}u$? Indeed, such pairs would also form part of the multiplet, introducing additional symmetry options.  

This leads to the broader consideration of symmetries beyond isospin, such as $SU(3)$ flavor symmetry, which incorporates $u, d, s$ quarks. The framework generalizes isospin to higher dimensions, mapping mesons into larger symmetry patterns.  

::: callout-note
The near-degeneracy of $u$ and $d$ quark masses (~2–6 MeV) underpins isospin symmetry. For heavier quarks (e.g., charm, strange), mass differences break the symmetry explicitly.
:::
The discussion naturally transitions to extending isospin-like symmetries to heavier quarks, though the Lagrangian’s lack of mass degeneracy limits such generalizations.

<!--
Cosine simularity: 0.9026841588878171
-->
## Charge Conjugation Symmetry and Its Implications

Another symmetry we have not yet considered is the particle-to-antiparticle transformation, known as charge conjugation. For example, the $D^+$ meson (composed of $c\bar{d}$) transforms under charge conjugation to its antiparticle, the $D^-$ ($\bar{c}d$). Similarly, the $D^0$ ($c\bar{u}$) becomes the $\bar{D}^0$ ($\bar{c}u$).  

This symmetry is even more robust than isospin symmetry. Isospin symmetry is slightly broken by quark mass differences and electromagnetic charges—for instance, the $u$ and $d$ quarks do not have identical masses. However, the $D^+$ and $D^0$ mesons are so similar under charge conjugation that we rarely distinguish them unless studying tiny effects like CP violation in the Standard Model.  

::: callout-note
Charge conjugation symmetry is exceptionally precise, with deviations being negligible in most cases. These deviations are typically explored in studies beyond the Standard Model (e.g., PSM—Physics Beyond the Standard Model).
:::
The breaking of isospin symmetry is more noticeable, particularly in observable quantities like decay modes. For example, the $D^+$ and $D^0$ exhibit different decay patterns due to mass differences, even though their underlying quantum couplings remain similar.  

A curious observation in LHCb papers is that charge-conjugated processes are implicitly assumed. For instance, when analyzing $B \to D \mu \nu$, the charge-conjugated decay $\bar{B} \to \bar{D} \mu \nu$ is automatically included in the analysis. This is because the physics is identical for both processes, so they are combined without explicit mention.  

::: callout-important
Charge conjugation symmetry is so fundamental that experimental collaborations like LHCb do not separately report results for particle and antiparticle decays—they are treated as one.
:::
The properties of charge-conjugated mesons are homogeneously identical unless probing extremely subtle effects. This symmetry simplifies theoretical and experimental analyses, as deviations are negligible in most scenarios.  

<!--
Cosine simularity: 0.945709301051296
-->
## Adding Spins and Orbital Angular Momentum in Quantum Systems

The properties of charge-conjugated mesons are homogeneously identical. We might revisit this when discussing deviations of the Standard Model and CP violation.  

Now, let's discuss the second topic. It's easier to address from the final state. You see two vector states, add them, and ask: what are the possible configurations? For example, what is the possible length of a vector made from one stick of 1 meter and another stick of 1 meter?  

Here, we have two vectors:  

- $\vec{J}_1$ with spin 1,  
- $\vec{J}_2$ with spin 1.  

When adding these spins, the possible total spin configurations are quantized in steps of 1: $S = 0, 1, 2$. This is one of the key concepts you'll learn in this course—how to add spins. We'll practice this repeatedly until it becomes clear.  

When combining these two vectors, the total spin can be:  

- $S = 0$ (singlet state),  
- $S = 1$ (triplet state),  
- $S = 2$ (quintet state).  

This is represented as:  

$$
\vec{J}_{\text{total}} = \vec{J}_1 + \vec{J}_2
$$

On one side, we list their individual quantum numbers; on the other, the total $J$. The parity ($P$) is multiplicative when combining them with zero orbital angular momentum ($L = 0$). This means they don't rotate relative to each other—you just take one, add the second, and observe the total $J$. The possible values are $J^P = 0^+, 1^+, 2^+$. This is called the **S-wave** configuration.  

Now, let's introduce orbital angular momentum ($L$). For $L = 0$, the states are straightforward. For $L = 1$ (P-wave), the parity flips to $-$, and the possible $J^P$ combinations become:  

- $1^-$,  
- $2^-$,  
- $3^-$.  

Similarly, for $L = 2$ (D-wave), the possible $J^P$ values are:  

- $2^+$,  
- $3^+$,  
- $4^+$.  

We can continue this for higher $L$ (F-wave, G-wave, etc.), but for most practical purposes, we rarely go beyond F-wave.  

::: callout-note
The parity for a state with orbital angular momentum $L$ is given by $P = (-1)^L$.
:::
This framework allows us to systematically classify quantum states based on their spin and orbital angular momentum combinations.

<!--
Cosine simularity: 0.920172696295298
-->
## Combining Angular Momentum and Parity in Quantum Decays

For this analysis, we need to consider the F-wave because it will be relevant. When addressing this, we focus only on the first row and add two units of orbital angular momentum. The parity-forbidden angular momentum sequence is $0^+, 1^-, 2^+, 3^-, 4^+, 5^-$. Starting from $0^+$, we add a length of 2, resulting in $2^+$. Adding it to $1^-$ requires careful consideration: the minimum value when subtracting is $1$, and the maximum is $3$, with no parity hint allowed.  

Now, for two vectors of length 2, we add another two units of orbital angular momentum. The minimal configuration is $0^+$, and the maximal is $4^+$, with all intermediate values having positive parity. For the F-wave, we introduce a longer stick of $3^-$ and examine the first row, which gives $1, 2, 3, 4, 5$ with alternating negative parity: $1^-, 2^-, 3^-, 4^-, 5^-$.  

The key is to identify which states decay. For example, the $1^-$ state appears in four combinations here. Decays into two identical particles are more restrictive due to symmetry constraints. Identical particles cannot occupy certain configurations, such as those with odd $L + S$. For instance, $L = 3$ combined with $S = 2$ is forbidden because $3 + 2 = 5$ (odd). Only one combination remains for identical particles, while four are possible for non-identical particles.  

::: callout-note
For identical particles, the total wavefunction must be antisymmetric under exchange if they are fermions, or symmetric if they are bosons. This restricts allowed combinations of $L$ and $S$.
:::
The process involves combining any particles with arbitrary spins and orbital angular momenta to determine possible quantum numbers. The total spin and orbital angular momentum must be combined to yield the correct $J^P$ values. This table-filling exercise is essential for understanding decays.  

For example, combining two vectors with spin $1$ each gives total spins $S = 0, 1, 2$. The parity is multiplicative when $L = 0$, so the possible $J^P$ states are $0^+, 1^+, 2^+$ (S-wave). Introducing $L = 1$ (P-wave) flips the parity, yielding $1^-, 2^-, 3^-$. Similarly, $L = 2$ (D-wave) gives $2^+, 3^+, 4^+$.  

$$
\vec{J}_{\text{total}} = \vec{J}_1 + \vec{J}_2 + \vec{L}
$$

The parity for a state with orbital angular momentum $L$ is $P = (-1)^L$. This systematic approach allows us to classify quantum states based on their spin and orbital angular momentum combinations.  

::: callout-important
Higher orbital angular momenta (e.g., F-wave, G-wave) follow the same pattern but are rarely needed in practice. The key is to understand the minimal and maximal configurations when adding spins and orbital angular momenta.
:::
<!--
Cosine simularity: 0.9180174955675205
-->
## Probing Hadron Structure with Electron Scattering

To understand the structure of hadrons, we need to study them using a well-understood probe. We use electromagnetic interactions by scattering electrons off protons and analyzing the reaction in the kinematic phase space.  

The electron is a point-like particle, so its interaction with the proton's electromagnetic field is straightforward and well understood. The proton side, however, is more complex. At low momentum transfer, the electron interacts with the proton's overall charge. At high momentum transfer, the electron begins to resolve the internal quark structure of the proton, probing the properties of the quarks themselves.  

The key idea is that the electron serves as a clean probe:  

- At low $Q^2$ (momentum transfer), the electron sees the proton as a single charged object.  
- At high $Q^2$, the electron scatters off individual quarks, revealing their dynamics inside the proton.  

This method allows us to study strong interactions and how quarks are organized within hadrons. The electromagnetic current insertion on the proton side is what makes this process informative.  

::: callout-note
The momentum transfer $Q^2$ determines the resolution scale: low $Q^2$ probes the proton as a whole, while high $Q^2$ resolves its quark constituents.
:::
The reaction can be described using the electron-proton scattering cross section, which depends on the proton's form factors. These form factors encode information about the proton's internal charge and magnetization distributions.  

$$
\frac{d\sigma}{d\Omega} \propto \left| F(Q^2) \right|^2
$$

Here, $F(Q^2)$ represents the proton's form factor, which varies with $Q^2$ and reflects the proton's internal structure.  

<!--
Cosine simularity: 0.9189024558551755
-->
## Introduction to Electron-Proton Scattering and Regimes

The problem here is like a large cucumber that you get smashed with the electromagnetic current. If the momentum transferred in this reaction is small, you get the characteristics of the proton itself. But if you go to the regime of high transferred momentum, where a lot of energy is taken from the proton, you start probing its internals.  

This is the idea behind elastic scattering experiments at large accelerator facilities, which have been built to study this very process. The U.S. hadron physics program for the next 10 years promises to focus on this, particularly with the Electron-Ion Collider (EIC). Instead of protons, heavier ions like carbon will be scattered with electrons to study quantum electrodynamics in this process.  

There is much to understand about the proton—it is not just a simple object. It contains quarks, gluons, and dynamic interactions between them. We have some understanding of how quarks are distributed inside the proton and what fraction of the proton's momentum they carry. However, what remains unclear is the behavior of perpendicular fluctuations—what happens off the axis of transferred momentum.  

::: callout-note
The momentum transfer $Q^2$ determines whether the electron interacts with the proton as a whole (low $Q^2$) or resolves its internal quark structure (high $Q^2$).
:::
This unresolved question is one of the key motivations for further study of electron-proton scattering. The reaction can be described using the proton's form factor $F(Q^2)$, which encodes information about its internal charge distribution:  

$$
\frac{d\sigma}{d\Omega} \propto \left| F(Q^2) \right|^2
$$

Here, $F(Q^2)$ varies with momentum transfer, reflecting changes in the proton's internal structure as the resolution scale increases.

<!--
Cosine simularity: 0.9290311485783476
-->
## Mandelstam Variables and Kinematic Quantities in 2-to-2 Scattering

In a 2-to-2 scattering process, the observables are relatively simple. The total energy in the system is determined by the colliding beams, and the scattering angle of the electron is the other key observable. More familiar quantities include the total energy-momentum in the system and the scattering angle in the center-of-mass frame.  

However, the Mandelstam variables $s$ and $t$ are more natural and widely used. The variable $s$ is computed as the square of the sum of the four-momenta of the initial-state particles:  

$$
s = (p_1 + p_2)^2
$$

The variable $t$ represents the energy transfer from the initial to the final state and is given by:  

$$
t = (p_e - p_e')^2
$$

Here, $p_e$ and $p_e'$ are the four-momenta of the initial and final electrons, respectively. These quantities are related, and in the center-of-momentum frame, they can be expressed in terms of $s$.  

For example, in the center-of-momentum frame, the total energy $E_{\text{total}}$ is equal to $\sqrt{s}$. The four-momenta can be decomposed into energy and spatial components, where the spatial momenta satisfy $\vec{p}_e^* = -\vec{p}_p^*$ (the asterisk denotes the center-of-momentum frame).  

The Mandelstam variable $t$ can also be written explicitly in terms of energy and momentum components:  

$$
t = m_e^2 + m_e^2 - 2(E_e E_e' - \vec{p}_e \cdot \vec{p}_e')
$$

This simplifies further in the center-of-momentum frame, where the scalar product of the spatial momenta reduces to $|\vec{p}_e^*|^2 \cos \theta$, with $\theta$ being the scattering angle.  

::: callout-note
The Mandelstam variables $s$ and $t$ are Lorentz-invariant, making them particularly useful for analyzing scattering processes across different reference frames.
:::
All kinematic quantities in the center-of-momentum frame can ultimately be expressed in terms of $s$, allowing for a streamlined description of the scattering process. For instance, the energy of each particle in this frame is directly related to $\sqrt{s}$, and the momentum transfer $t$ depends on $s$ and the scattering angle.

<!--
Cosine simularity: 0.8973076569728504
-->
## Kinematics of Elastic Scattering and Q Squared  

The quantity $Q^2$ is defined as:  

$$
Q^2 = -t  
$$  

where $t$ is the Mandelstam variable given by:  

$$
t = \left( \frac{E_e}{p_e} - \frac{E_e'}{p_e'} \right)^2 - m_e^2  
$$  

You can derive this by writing $s$ as the square of the proton plus electron four-momentum. However, what you actually want is to express $\sqrt{s_0}$ as the sum of the proton and electron energies:  

$$
\sqrt{s_0} = E_p + E_e  
$$  

From this, you can solve for the electron momentum $p_e$:  

$$
p_e = \sqrt{s_0} - E_p  
$$  

Squaring this gives:  

$$
m_p^2 + m_e^2 = s_0 + m_e^2 - 2 \sqrt{s_0} E_e  
$$  

From here, you obtain the electron energy $E_e$ and, similarly, its momentum:  

$$
p_e = \sqrt{E_e^2 - m_e^2}  
$$  

This expression is known as the **channel function**, which appears in phase space calculations for two-body decays.  

::: callout-note
The breakup momentum and phase space integrals often involve the channel function, though it may not have been explicitly covered in exercises.
:::
For elastic scattering kinematics, the key variables are:  

- **Total energy $E_{\text{total}}$**, fixed by the beam energy.  
- **Scattering angle $\theta$**, which is measured experimentally.  

Knowing $E_{\text{total}}$ gives $s$, and knowing $\theta$ allows determining $t$ through kinematic relations. The commonly used variable in such processes is $Q^2$, defined as:  

$$
Q^2 = -t  
$$  

This arises because, at high energies, the dominant interaction mechanism involves momentum transfer. The electron passes near the proton, and the exchanged momentum ( $Q^2$ ) governs the physics.  

::: callout-important
The only non-trivial observable in this setup is the angular distribution of scattered electrons, as their change in trajectory encodes the exchanged momentum.
:::
For elastic scattering, $t$ is always negative, meaning the transferred momentum is **space-like**. This can be verified in the lab frame with a fixed target. Since $t$ is negative, $Q^2$ is introduced as a positive quantity:  

$$
Q^2 = -t  
$$  

Thus, $Q^2$ is determined by the scattering angle and defines the kinematic regime of the interaction.

<!--
Cosine simularity: 0.937794002165617
-->
## Charge Distribution and Scattering Angles in Proton  

The quantity $Q$ is fixed by the scattering angle, which defines the kinematic regime of the reaction. For small $Q$, the scattering is shallow, and the electron primarily senses the proton's overall charge distribution rather than its internal quark structure. The charge density inside the proton can be approximated as:  

$$
\rho(r) \sim e^{-r/R}
$$  

where $R$ is the charge radius of the proton. This is an exponential distribution, not Gaussian, as the speaker initially misspoke.  

For large $Q$, the scattering probes the internal quark structure of the proton. Thus, small $Q$ corresponds to small scattering angles, while large $Q$ corresponds to large angles. To study the proton's internal quarks, one must examine high-angle scattering events. Conversely, to measure the proton's charge radius or overall charge distribution, low-angle scattering is used.  

The charge radius $R$ characterizes how the proton's charge is distributed when viewed from a distance. The proton behaves like a diffuse cloud of charge, with the distribution falling off exponentially with distance. Additionally, the magnetic properties of the proton can also be measured through similar scattering experiments.  

::: callout-note
The distinction between small and large $Q$ regimes is crucial: small $Q$ reveals the proton's bulk properties, while large $Q$ exposes its quark substructure.
:::
<!--
Cosine simularity: 0.9117593764830547
-->
## Magnetic Moment and Particle Interaction in Magnetic Fields

The magnetic moment characterizes how particles behave in a magnetic field, describing their interaction with it. If a particle has a magnetic moment, placing it in a magnetic field results in an additional force acting on it.  

In the Lagrangian or Hamiltonian, this introduces an extra energy term due to the magnetic field. For example, in the hydrogen atom, the presence of a magnetic field causes energy level splitting — the states' energies shift because of the magnetic moment and charge radius.  

The magnetic moments of the proton and neutron are given by:  

$$
\mu_p = 2.793 \mu_N  
\mu_n = -1.913 \mu_N  
$$  

where $\mu_N$ is the nuclear magneton. The neutron's magnetic moment can also be expressed in terms of its spin $\vec{S}$:  

$$
\mu_n = \frac{e}{4m} \vec{S}  
$$  

For the proton, the magnetic moment arises from its quark structure:  

$$
\mu_p = \frac{2}{3} \mu_u - \frac{1}{3} \mu_d  
$$  

where $\mu_u$ and $\mu_d$ are the magnetic moments of the up and down quarks, respectively.  

<!--
Cosine simularity: 0.9615875636764135
-->
## Introduction to Cross Sections and Phase Space in Quantum Processes

The cross section is a key observable that connects quantum processes to experimental measurements. To compute the differential cross section, we use the matrix element of the reaction. The squared matrix element $|M|^2$ represents the probability of a reaction occurring at a specific kinematic point. The total cross section is obtained by integrating over the entire kinematic domain, summing the matrix elements weighted by the available phase space configurations.  

Phase space can be thought of as the number of configurations in which a reaction can occur. For discrete variables like spin, this is intuitive, but for continuous kinematic variables (e.g., scattering angle $\theta$), it requires integration. For example, to calculate the total cross section, you must integrate over all possible $\theta$.  

The flux factor normalizes the wave functions of the colliding particles and is given by a kinematic factor like:  

$$
J = 2E_1 2E_2 (v_1 - v_2)
$$  

where $E_1, E_2$ are the energies and $v_1, v_2$ the velocities of the incoming particles. The phase space integral is more complex but follows a standard expression, accounting for all continuous kinematic configurations.  

The differential cross section formula is:  

$$
d\sigma = \frac{1}{M^2} \int |M|^2 d\Phi
$$  

Here, $d\Phi$ is the phase space element, and $M^2$ is the squared matrix element, which for a simple case might be:  

$$
M^2 = \frac{x^2 (s - m_1^2 - m_2^2)}{s}
$$  

where $s$ is the Mandelstam variable and $m_1, m_2$ are the masses of the particles.  

The charge radius, previously discussed, also plays a role in these calculations. The phase space ensures all possible kinematic configurations are accounted for, while the flux factor provides the correct normalization for the colliding particle wave packets.

<!--
Cosine simularity: 0.9420582840025982
-->
## Understanding Two-Body Phase Space Integration

The Lorentz-invariant phase space differential for $n$ particles is given by:

$$
d\Phi_n = \prod_i \frac{d^3 p_i}{(2\pi)^3 2E_i} (2\pi)^4 \delta^4(p_i - \Sigma p_f)
$$

This represents integration over all possible configurations in continuous space. For each particle in the final state, the phase space includes a term like $\frac{d^4p}{(2\pi)^3 2E}$, ensuring every 4-momentum is on-shell. On-shell means the energy and momentum satisfy the mass-shell condition $E^2 = \vec{p}^2 + m^2$.  

The delta function enforces 4-momentum conservation, ensuring the sum of initial momenta equals the sum of final momenta. Phase space is essentially the continuous version of counting possible configurations. For two-body phase space, the calculation is straightforward, but it becomes more complex for three or more bodies.  

To determine the dimensionality of the integral, we count the variables and subtract constraints. For two-body phase space:  

- Each particle has 3 momentum components, so initially, there are 6 degrees of freedom.  
- The 4-momentum conservation delta function imposes 4 constraints.  
- After removing these constraints, we are left with 2 degrees of freedom.  

By systematically trading constraints for differentials, we arrive at the final expression for the two-body phase space:

$$
d\Phi_2 = \frac{1}{8\pi} \frac{\lambda^{1/2}(s, m_1^2, m_2^2)}{s} \frac{d\cos\theta \, d\phi}{4\pi}
$$

Here, $\lambda(x,y,z) = x^2 + y^2 + z^2 - 2xy - 2xz - 2yz$ is the Källén function, and $s$ is the Mandelstam variable (center-of-mass energy squared). The angles $\theta$ and $\phi$ describe the orientation of the outgoing particles.  

This result is analytically tractable and reveals important kinematic properties. It is a foundational exercise in particle physics, as two-body phase space appears frequently in calculations. The simplicity of this case makes it a useful starting point before tackling more complex multi-body phase space integrals.  

The squared matrix element $|M|^2$ is then integrated over this phase space to compute observables like cross sections. The flux factor, as discussed earlier, normalizes the incoming particle states, ensuring the correct kinematic weighting.  

::: callout-tip
The Källén function $\lambda(s, m_1^2, m_2^2)$ encodes the kinematic limits of the process, ensuring physical energy and momentum configurations.
:::
::: callout-note
For numerical computations, multi-body phase space integrals are often evaluated using Monte Carlo methods, but the two-body case remains fully analytic.
:::
<!--
Cosine simularity: 0.9348735368867054
-->
## Understanding Azimuthal Angle Independence in Scattering  

The delta functions and differentials in the expression must be carefully handled, and I recommend practicing this calculation multiple times to fully grasp it. The resulting expression has two remaining differentials, representing an integral over the phase space of spherical angles.  

In $2 \to 2$ scattering, there is one variable that determines the scattering, but there is also another degree of freedom: rotation around the axis of collision. If the problem is unpolarized (no preferred orientation), the squared matrix element $|M|^2$ does not depend on the azimuthal angle $\phi$. This is why $\phi$ can be safely ignored in such cases.  

::: callout-note
The independence of $\phi$ simplifies the phase space integration, reducing it to a dependence only on the polar angle $\theta$.
:::
For visualization, consider the coordinate system: the $z$-axis aligns with the collision axis, while the $x$ and $y$ axes define the transverse plane. The lack of polarization means the scattering process is symmetric under rotations around the $z$-axis.  

$$
d\Phi_2 \propto d\cos\theta \, d\phi \quad \text{(but $d\phi$ integrates trivially if $|M|^2$ is $\phi$-independent)}
$$

This symmetry is crucial for simplifying calculations in unpolarized scattering processes.

<!--
Cosine simularity: 0.9266863010207916
-->
## Kinematic Factors and Phase Space in Scattering

You have a z axis, an x axis, and a Y axis. The colliding particles are represented here: the initial electron and the scattered electron. The angle between the z axis and the scattered electron is $\theta$, and the projection of the scattered electron onto the XZ plane defines the azimuthal angle $\phi$.  

If there are no external spin directions, the matrix element does not depend on $\phi$. When calculating the total cross section, the $\phi$ integral simplifies to $2\pi$ because the process is rotationally symmetric around the z axis. The non-trivial part lies in the $\cos\theta$ dependence, which is directly related to $Q^2$ (the momentum transfer squared) and provides sensitivity to the internal structure of the particles.  

The kinematic factor here describes the number of configurations available at a given energy. For small energy releases (e.g., low beam energy), the number of configurations is limited, reflecting a non-relativistic regime where degrees of freedom are constrained by spatial configurations. In this case, the phase space is proportional to $4\pi$ (covering all possible outgoing directions).  

However, for relativistic particles, the phase space near the threshold (where the energy is close to the particle masses) is suppressed. This suppression vanishes as the energy approaches the threshold, making the phase space very small.  

$$
d\Phi_2 \propto d\cos\theta \, d\phi
$$

When the energy of the system is near the threshold, the phase space effectively vanishes, which is expected since no scattering can occur if the energy is insufficient to produce the final-state particles.  

::: callout-note
The suppression of phase space near threshold is a relativistic effect absent in non-relativistic treatments.
:::
The key physics lies in the $\cos\theta$ dependence, which encodes the kinematic constraints and the structure-dependent dynamics of the scattering process.

<!--
Cosine simularity: 0.9085674765572963
-->
## Future of Knowledge Upload and Interactive Learning  

The mechanism of uploading knowledge into the brain of students in the future will likely resemble a system like ChatGPT, where training is iterative. To truly understand something, you must apply knowledge repeatedly in different contexts. First, information is explained, as in a lecture. Immediately afterward, a test or quiz reinforces the material.  

For example, you might be given a problem to derive everything from scratch using a 3-column block. Alternatively, learning could take a gaming format—solving questions while navigating a virtual environment, like answering: *What is the high-energy behavior of the phase space?* This would resemble "Duolingo for hadron physics," where playful problem-solving leads to discovery.  

After three hours of such interactive learning, you revisit the material the next day with reminders to reinforce retention. After several sessions, mastery is achieved. This approach could extend to all subjects, with tailored interactive modules like Duolingo for every discipline.  

::: callout-tip
Iterative application in varied contexts (e.g., quizzes, derivations, gamified challenges) accelerates skill acquisition.
:::
The key is combining explanation, immediate testing, and spaced repetition in an engaging format. Homework assignments could adopt this model to maximize learning efficiency.  

<!--
Cosine simularity: 0.9474530485245514
-->
## Introduction to Matrix Elements in Scattering Theory  

The matrix element is a key input to reactions. If you have a theory of interaction, you can derive it from the theory. If you don’t have a theory—as often happens in hadron physics—you can use general principles to construct the matrix element.  

For electromagnetic processes, we have a theory: QED combined with QCD. We know how to write an expression that, when squared, gives $|\mathcal{M}|^2$. Summing over final states and averaging over initial states yields a mathematical expression that can be compared to experiment.  

This expression depends on only one variable: the energy of the beam. The matrix element is defined within the domain of phase space variables. As discussed earlier, the phase space is a function of two variables, such as the angle $\theta$.  

::: callout-note
The squared matrix element $|\mathcal{M}|^2$ encodes the transition probability between initial and final states, weighted by phase space.
:::
For electromagnetic processes, the framework of QED provides a systematic way to compute these matrix elements, while in hadron physics, phenomenological models are often necessary.

<!--
Cosine simularity: 0.9431993171813935
-->
## Matrix Elements and Their Properties in Scattering Theory  

The matrix element is a function of two variables, but in the unpolarized case, it reduces to a dependence only on the scattering angle $\theta$. It also depends on the total energy, which is fixed by the energy of the colliding particles.  

Mathematically, the matrix element is a complex function defined in field theory as part of the scattering matrix. It represents the probability amplitude between asymptotic initial states (at $t \to -\infty$) and asymptotic final states (at $t \to +\infty$), where particles are non-interacting. The expectation value of the interaction operator between these states gives the matrix element.  

::: callout-note
The absolute square of the matrix element $|\mathcal{M}|^2$ yields a real value, corresponding to the transition probability.
:::
In field theory, scattering is approached using perturbation theory, expanding order by order in the interaction strength. For electromagnetic processes, each interaction of an electron with a current introduces a factor of $\alpha = \frac{1}{137}$ (the fine-structure constant). The first-order term in this expansion often provides a good approximation for the total cross section.  

For a first-order electromagnetic process, the matrix element can be expressed in terms of Feynman diagrams. For example, a diagram representing a photon-electron interaction translates to a mathematical expression involving form factors.  

::: callout-important
The form factors $F_1(q^2)$ and $F_2(q^2)$ appear because the proton is not a point-like particle. These functions characterize its internal structure and are not predicted by field theory alone.
:::
The matrix element is thus a complex function of the Mandelstam variables $S$ and $T$. When $S$ is fixed, it becomes a function of $T$ alone. The framework of QED provides a systematic way to compute these matrix elements, while phenomenological models are necessary for hadronic processes.

<!--
Cosine simularity: 0.9300928505268605
-->
## Dimensionality and Tensor Analysis in Scattering Theory  

The form factors $F_1(q^2)$ and $F_2(q^2)$ characterize the internal properties of the system, which is not point-like. If the system were point-like, $F_2$ would vanish ($F_2 = 0$), but this is not the case, so these form factors must be introduced and measured experimentally.  

Here, $U$ is a spinor, and $\Gamma$ is a gamma matrix. The term $\sigma$ refers to $i \gamma^\mu \gamma^\nu$, representing the commutator of gamma matrices.  

::: callout-important
It is crucial to identify the dimensionality of expressions and verify that they match expectations. For example, is the matrix element a tensor or a scalar? All objects here are tensors, so indices must contract properly.
:::
Consider the contraction of indices:  

- The term $\gamma^\mu$ (a $4 \times 4$ matrix) contracts with a Lorentz index $\mu$.  
- The spinor $U$ (a column vector in spinor space) contracts with the gamma matrix, resulting in a scalar in spinor indices but a vector in Lorentz indices.  

This pattern continues: when a matrix is contracted with a vector (row or column), the result is another matrix or scalar, depending on the context.  

The dimensionality and index structure ensure consistency in the mathematical framework of scattering theory. For example, the product of spinors and gamma matrices must yield quantities with the correct transformation properties under Lorentz symmetry.  

::: callout-note
The gamma matrices $\gamma^\mu$ are $4 \times 4$ matrices, and their commutator $\sigma^{\mu\nu}$ is also a matrix-valued tensor. Proper index contraction is essential for maintaining Lorentz covariance.
:::
<!--
Cosine simularity: 0.8956337245356337
-->
## Cross Section Derivation and the Rosenbluth Formula  

The matrix element $M$ is contracted by vector and by row and column, resulting in a scalar. The index $\mu$ in $\gamma^\mu$ and the momentum transfer $Q$ are part of this structure. The form factors $F_1$ and $F_2$ are scalar functions, and their proper contraction ensures Lorentz covariance.  

To derive the cross section, we square the matrix element and perform spin summation. There are techniques to eliminate the spinors, but the details are covered in quantum field theory. The final expression for the cross section is the **Rosenbluth formula**:  

$$
\frac{d\sigma}{d\Omega} = \frac{l^2}{4E_i^2 \sin^2 \frac{\theta}{2}} \frac{E_3}{E_1} \left( G_E (Q^2) + \tau G_M (Q^2) \right) \left( 1 + 2\tau \sin^2 \frac{\theta}{2} \right)
$$

Here, $G_E(Q^2)$ and $G_M(Q^2)$ are the electric and magnetic form factors, respectively, defined as:  

$$
G_E (Q^2) = F_1 (Q^2) + \frac{Q^2}{4m^2} F_2 (Q^2)
$$

$$
G_M (Q^2) = F_1 (Q^2) + F_2 (Q^2)
$$

The derivation involves many steps, which are not covered here but can be found in quantum field theory courses or textbooks like *Eskinshar*. The *Mark Thompson* book does not include this derivation.  

::: callout-important
The form factors $F_1(q^2)$ and $F_2(q^2)$ describe the internal structure of the system. If the system were point-like, $F_2$ would vanish, but experimental measurements show this is not the case.
:::
The spinor $U$ and gamma matrix $\Gamma$ structure must respect index contraction rules. For example, $\gamma^\mu$ (a $4 \times 4$ matrix) contracts with the Lorentz index $\mu$, while spinors $U$ (column vectors in spinor space) contract with gamma matrices to yield scalars or tensors.  

::: callout-note
The commutator of gamma matrices, $\sigma^{\mu\nu} = i \gamma^\mu \gamma^\nu$, is also a matrix-valued tensor. Proper index contraction ensures Lorentz invariance.
:::
<!--
Cosine simularity: 0.9420368313243506
-->
## Divergence in Small Angle Scattering and Regularization  

In the book by *Eskinshar*, the derivation is shown step by step, but it is not covered in the *Mark Thompson* book. The expression discussed here is manageable, and you may encounter similar calculations in a field theory course.  

The key physics insight is the $1/\sin^4 \theta$ dependence, which originates from the $1/Q$ term. Here, $Q$ is proportional to $\sin \theta$, but it is more precise to refer to $Q$ directly since it is a measurable quantity. The $1/Q^2$ term in the expression leads to the $1/\sin^4 \theta$ divergence at small angles.  

For very forward scattering (small $\theta$), the dependence becomes $1/\theta^4$, which is non-integrable. This necessitates regularization techniques to handle the divergence.  

::: callout-note
The terms $E_1$ and $E_3$ correspond to the electron's initial and final energies, respectively.
:::
<!--
Cosine simularity: 0.9212503629336526
-->
## Fourier Transformation and Spatial Distribution of Proton Charge  

The form factors $G_E(Q^2)$ and $G_M(Q^2)$ are given by:  

$$
G_E(Q^2) = \int e^{iQr} g(r) \, dr
$$  

$$
G_M(Q^2) = \int e^{iQr} M(r) \, dr
$$  

Regularization is required for these expressions. Here, $E_1$ and $E_3$ correspond to the electron's initial and final energies. Another equation relates $G^*$ to $F$, but for convenience, we replace $F$ with $G$ to simplify the final expressions.  

The $Q$ dependence of these form factors is what people measure experimentally. From this dependence, we can extract properties of the proton. The extraction of $G_E$ and $G_M$ at small $Q$ values involves a particularly elegant experimental technique.  

The $Q$ dependence is dual to the spatial coordinate in the sense of Fourier transformation. If we know the $Q$ dependence of the form factors, we can interpret it as the spatial distribution of the proton charge. These two are related by Fourier transformation:  

::: callout-note
The $Q$ dependence reveals how the proton charge is distributed over large distances in space.
:::
In practice, researchers often assume an exponential dependence for the spatial distribution.

<!--
Cosine simularity: 0.9431335917753649
-->
## Magnetic Moment and Its Quantum Corrections

People often assume an exponential dependence on the spatial coordinate. When you introduce this exponential dependence, you obtain a pole-like behavior, which is referred to as dipole parameterization. This will be explored further in the homework.  

By measuring the $Q$ dependence experimentally (e.g., on the lattice), we extract parameters of the spatial distribution. A key question in the field is: *What is the charge radius of the proton?* Many experiments have attempted to measure this using various techniques, and lattice calculations also address this problem.  

One of the quantities extracted from lattice computations is the $Q$ dependence, obtained through first-principles numerical calculations. Performing a Fourier transformation on this dependence yields the spatial distribution, from which the charge radius can be determined.  

::: callout-note
The magnetic moment of the hadron is another important quantity related to these form factors.
:::
The magnetic moment is derived from $G_M(Q^2)$ at $Q = 0$:  

$$
G_M(0) = \int M(r) \, dr
$$  

This integral represents the total magnetic moment of the hadron. At leading order, this is the dominant contribution, but corrections can be computed up to next-to-next-to-leading order (NNLO). These corrections primarily arise from the electron side, which is well understood. On the proton side, the expression for $G_M(Q^2)$ is the most general form possible.  

While it is possible to derive the form factor functions at higher orders (NLO, NNLO), this is computationally challenging and rarely done in practice. Instead, researchers typically focus on the leading-order contributions.

<!--
Cosine simularity: 0.9403761550267665
-->
## Magnetic Moment and Geomagnetic Ratio in Quantum Mechanics  

In quantum mechanics, the interaction part of the Hamiltonian is given by the product of the magnetic moment of a particle and the magnetic field. This affects the equations of motion, adding an extra energy term to the particle, which then enters the Lagrangian. The magnetic moment for a particle is given by:  

$$
\vec{\mu} = \frac{e}{2m} \vec{S}
$$  

Here, $\vec{S}$ is the spin operator for a fermion (spin-1/2 particle). However, this relation is modified by the geomagnetic ratio (or g-factor), leading to:  

$$
\vec{\mu} = g \frac{e}{2m} \vec{S}
$$  

The standard magnetic moment of the particle is called the geomagnetic ratio, where $\frac{e}{m}$ is the charge-to-mass ratio. For point-like Dirac particles, the g-factor equals 2.  

::: callout-note
The spin operator $\vec{S}$ has eigenvalues $\pm \frac{1}{2}$, which is why the factor of 2 appears in the g-factor for Dirac particles.
:::
For neutral particles, the magnetic moment must be treated differently, but the discussion is cut off here.  

---  

In practice, computing these interactions exactly is challenging, so physicists often parameterize the form factors $F_1$ and $F_2$ instead of modeling the internal structure directly. This approach is common when dealing with complex systems where the internal dynamics are not fully calculable. The magnetic moment and its corrections are central to understanding these parameterizations.

<!--
Cosine simularity: 0.9276237878158763
-->
## Magnetic Moment of Proton and Neutron: Evidence for Composite Structure

The measured magnetic moments of the proton and neutron are:

$$
\mu_p = 2.793 \mu_N
$$

$$
\mu_n = -1.913 \mu_N
$$

For a point-like Dirac particle, the magnetic moment would be:

$$
\mu = \frac{e}{2m} \vec{S}
$$

However, the proton's magnetic moment deviates from this expectation ( $\mu_p \neq 2 \mu_N$ ), and the neutron's magnetic moment is not zero despite being electrically neutral. This is strong evidence that they are not point-like particles.  

The ratio of the proton's magnetic moment to the neutron's is approximately $-3/2$, which aligns with predictions from the quark model. Specifically, the proton's magnetic moment can be expressed in terms of quark contributions:

$$
\mu_p = \frac{2}{3} \mu_u - \frac{1}{3} \mu_d
$$

::: callout-note
The fact that the neutron has a non-zero magnetic moment and the proton's moment deviates from the Dirac value suggests a composite structure, consistent with the quark model.
:::
The experimental results are striking: the neutron's magnetic moment is not zero, and the proton's moment is not 2. The ratio between them is a key observation that fits well with the flavor structure of quarks.  

In quantum mechanics, the magnetic moment is modified by the g-factor:

$$
\vec{\mu} = g \frac{e}{2m} \vec{S}
$$

For point-like particles, $g = 2$, but the observed values for the proton and neutron require a more complex description, such as internal quark dynamics.

<!--
Cosine simularity: 0.9405473434775776
-->
## Quark Model Foundations and Emergent Degrees of Freedom  

If you look at the flavor-spin wave function for the problem, we can write the proton as the composition of the wave function of its core content. Then, we act with the magnetic moment operator on the proton and compute its magnetic moment in terms of the magnetic moments of the quarks. We can do the same for the neutron and find that the ratio is roughly as expected.  

The reason this approach is correct comes from the fact that the strong interaction is confined to small scales where quarks are inside the proton. The entire color interaction sits within the proton. Quarks and gluons interact, and the emergent degrees of freedom arise when we consider multiplets and symmetries based on the quarks. The quarks are the leading degrees of freedom, and they gain mass.  

The quarks in the Standard Model Lagrangian are current quarks with negligible mass, while the emergent (constituent) quarks acquire significant mass and carry most of the degrees of freedom. The quark model integrates gluonic degrees of freedom and attributes mass to the quarks. We start with nearly massless quarks, but after integrating gluons, we end up with a system where three quarks (each roughly 300 MeV) form the proton.  

The up quark ( $u$ ) has a charge of $+2/3$, and the down quark ( $d$ ) has a charge of $-1/3$. These quarks carry $1/3$ of the baryon number and govern the degrees of freedom. The proton's magnetic moment can be expressed as:  

$$
\mu_p = \frac{2}{3} \mu_u - \frac{1}{3} \mu_d
$$  

This framework explains why the proton and neutron have non-trivial magnetic moments, deviating from the Dirac particle expectation. The neutron's non-zero magnetic moment and the proton's deviation from $2 \mu_N$ are key evidence for their composite structure.  

::: callout-note
The ratio of the proton's to neutron's magnetic moments ( $\approx -3/2$ ) aligns with quark model predictions, reinforcing the idea of emergent quark degrees of freedom.
:::
<!--
Cosine simularity: 0.9010261398691429
-->
## Proton Wave Function and Quark Degrees of Freedom  

The down quark ( $d$ ) has a charge of $-1/3$. These quarks constitute and govern the degrees of freedom of baryons.  

We can consider the proton wave function in terms of quark wave functions in a simplified way, combining representations of the flavor wave function and the spin wave function. The proton can be expressed in terms of the lower quark degrees of freedom, as shown in the wave function:  

$$
|p\rangle = \frac{1}{\sqrt{8}} (uud + udu + duu + ...)
$$  

This will be explored further in the next lecture.

<!--
Cosine simularity: 0.9385263353309993
-->
## Kinematics and Regimes of Electron Scattering  

Today we started the discussion with the kinematics of scattering, focusing specifically on electron scattering. We examined different regimes depending on the momentum transfer $Q$.  

In **forward scattering**, the electron barely changes its direction, and the transferred momentum is small. This regime characterizes the proton as a whole, including its charge density and magnetic moment.  

At **high transferred momentum**, we probe the internal structure of the proton, leading to **deep inelastic scattering**. This is where we observe the quark degrees of freedom.  

The **2→2 kinematics** will be discussed further in the next lecture.

<!--
Cosine simularity: 0.9260333841919884
-->
## Phase Space, Flux, and Probability Calculations  

The quarks inside were discussed earlier, but the 2→2 kinematics is something we will revisit. This is a standard piece that I would like you to understand very well: how to calculate phase space, how to calculate flux, and how to derive the probability given the matrix element.  

The differential cross section is given by:  

$$
d\sigma = \frac{1}{M^2} \int |M|^2 d\Phi
$$  

Here, $M$ is the matrix element, and $d\Phi$ is the phase space element. The flux factor $J$ is:  

$$
J = 2E_1 2E_2 (\omega_1 - \omega_2)
$$  

For an $n$-body final state, the phase space is:  

$$
d\Phi_n = \prod_i \frac{d^3 p_i}{(2\pi)^3 2E_i} (2\pi)^4 \delta^4(p_i - \Sigma p_f)
$$  

The squared matrix element $|M|^2$ can be expressed as:  

$$
|M|^2 = \frac{x^2 (s - m_1^2 - m_2^2)}{s}
$$

<!--
Cosine simularity: 0.8787696193822073
-->
## Rosenbluth Formula and Form Factors in Scattering

The matrix element $M$ describes the transition amplitude between initial and final states in scattering. To obtain the probability, we square it and integrate over phase space. The differential cross section is given by:

$$
d\sigma = \frac{1}{M^2} \int |M|^2 d\Phi
$$

Here, $d\Phi$ is the phase space element, and $M$ is the matrix element. The flux factor $J$ accounts for the relative motion of incoming particles:

$$
J = 2E_1 2E_2 (\omega_1 - \omega_2)
$$

For an $n$-body final state, the phase space is:

$$
d\Phi_n = \prod_i \frac{d^3 p_i}{(2\pi)^3 2E_i} (2\pi)^4 \delta^4(p_i - \Sigma p_f)
$$

The squared matrix element $|M|^2$ can be expressed in terms of kinematic variables:

$$
|M|^2 = \frac{x^2 (s - m_1^2 - m_2^2)}{s}
$$

<!--
Cosine simularity: 0.8946935880097974
-->
```
## Magnetic Moment in the Quark Model

The cross section is related to the charge characteristics and magnetic moment of the problem. We started discussing the quark model and will continue next time with the calculation of the magnetic moment.  
The proton's magnetic moment is given by:

$$
\mu_p = \frac{2}{3} \mu_u - \frac{1}{3} \mu_d
$$

where $\mu_u$ and $\mu_d$ are the magnetic moments of the up and down quarks, respectively.  
The neutron's magnetic moment is experimentally measured as $\mu_n = -1.913 \mu_N$.
```

<!--
Cosine simularity: 0.9861379008374461
-->
```
## Introduction to Quark Model

Next time we will continue with the calculation of magnetic moment. All right, thanks for the attention.
```

