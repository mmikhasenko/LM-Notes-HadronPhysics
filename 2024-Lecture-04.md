# Lecture 04: Kinematics of reactions

## Recap and Questions on Magnetic Moment Computation

This is lecture number 4. We will have no exercise session this week due to the trip to CERN. There is also a scheduling issue for next week's exercise class, as Thursday is a holiday. I hope Ilya can discuss rescheduling it to another day. Skipping two weeks would be too much, but we will be back from CERN on Monday, and the next lecture will proceed as planned on Tuesday.  

Today's lecture will focus on experiments in spectroscopy and kinematics computations. Before diving into that, let's recap the last lecture and address two key questions:  

1. **Compute the magnetic moment in the current model of the Omega baryon.**  
2. **Compute the lowest $1s$ multiplet excitation of the $\Sigma_p$ parameter (related to ISIS spin factors).**  

For question 1, we first need the quark content of the $\Omega^-$ baryon: three strange quarks ($sss$). The total wave function is a product of color, isospin, spin, and flavor components, but color and isospin are factored out, leaving only flavor and spin. The flavor part is trivial, so we focus on spin.  

The spin configuration must yield a total spin of $3/2$ for the $\Omega^-$ baryon, with parity $+$. This implies orbital angular momentum $L = 1$, and the spin must be $1/2$ to achieve the correct total angular momentum $J = 3/2$.  

For question 2, the $1s$ multiplet excitation of $\Sigma_p$ involves understanding the spin structure of the system, particularly how the spin states align to form the lowest-energy configuration.  

::: callout-note
The $\Omega^-$ baryon's magnetic moment arises from the contributions of its three strange quarks, each with spin $1/2$. The total spin configuration must be symmetric to match the observed $J = 3/2$ state.
:::
::: callout-tip
When computing the $1s$ multiplet, remember that the lowest-energy state corresponds to the most symmetric spin arrangement, minimizing repulsive interactions.
:::
<!--
Cosine simularity: 0.8702025552897326
-->
## Calculation of Magnetic Moment for Omega Baryon

The parity of the Omega baryon is plus, which implies the orbital angular momentum $L = 1$. The spin is $3/2$, giving a total angular momentum $J = 3/2$. The multiplicity of the spin-$3/2$ state is four, corresponding to the four possible projections along the $z$-axis: $+3/2, +1/2, -1/2, -3/2$.  

The wave function for the $\Omega^-$ baryon is constructed from the spin states of the three strange quarks. Acting with the lowering operator on the highest weight state generates the other components, such as $|\downarrow\uparrow\uparrow\rangle$, $|\uparrow\downarrow\uparrow\rangle$, and $|\uparrow\uparrow\downarrow\rangle$, each with a coefficient of $1/\sqrt{3}$.  

The magnetic moment operator is given by:  

$$
\mu_z = \mu_{1z} + \mu_{2z} + \mu_{3z}
$$

When applied to the state, it acts as an eigenoperator. For example, $\mu_{1z}$ acting on $|\uparrow\uparrow\uparrow\rangle$ returns the spin projection multiplied by the charge factor. The charge of each strange quark is $-1/3$, so the total charge contribution is:  

$$
\mu \propto \sum_{i=1}^3 q_i \cdot s_{iz}
$$

For the $\Omega^-$ baryon, the total charge is $-1$, and the dominant contribution comes from the spin alignment. The magnetic moment is then:  

$$
\mu \approx \frac{e\hbar}{2m_s c}
$$

where $m_s$ is the mass of the strange quark (approximately 500 MeV). Compared to the electron's magnetic moment, this is smaller by a factor of $10^3$ due to the larger mass of the strange quark.  

::: callout-note
The $\Omega^-$ baryon's magnetic moment is determined by the spin and charge contributions of its three strange quarks, with the mass scale set by the strange quark mass.
:::
::: callout-tip
When computing magnetic moments, focus on the highest weight state first, as the other states can be generated using ladder operators. The proportionality to spin simplifies the calculation.
:::
The charge of the $\Omega^-$ baryon is $-1$, arising from the sum of the three strange quark charges. The magnetic moment is thus suppressed relative to the electron due to the heavier mass scale involved.

<!--
Cosine simularity: 0.9410176644208754
-->
## Excitation Pattern and Isospin Partners of Sigma B Baryon  

The magnetic moment of the $\Omega^-$ baryon is negative because of its negative charge, but it is 10,000 times smaller than that of the electron. The charge of the $\Omega^-$ is also negative, so our intuition holds that the magnetic moment should be negative. However, the mass scale in the magnetic moment formula is determined by the quark mass rather than the mass of the $\Omega^-$ itself. If the quark mass is roughly 500 MeV, then the mass of the $\Omega^-$ would be around 1500 MeV (three times the quark mass).  

::: callout-tip
When calculating magnetic moments, it is simplest to work with the maximal spin projection state, as it avoids complications from mixed spin configurations.
:::
The excitation pattern of the $\Sigma_b$ baryon is determined by its light diquark configuration, which in the ground state has spin $S = 1$ and parity $1/2^+$. A bonus question concerns the isospin partners of this baryon. Since the isospin of the $\Sigma_b$ is $I = 1$, the isospin multiplet has three charge states corresponding to the projections $I_z = +1, 0, -1$.  

The charges of these states are determined by their quark composition:  

-$\Sigma_b^+$ ( $uu b$ ) has charge $+1$ (like a proton but with a bottom quark).  
- $\Sigma_b^0$ ( $ud b$ ) has charge $0$.  
- $\Sigma_b^-$ ( $dd b$ ) has charge $-1$.  

Acting with the isospin lowering operator reduces the charge by one unit, so the pattern is straightforward.  

::: callout-note
Isospin symmetry is only slightly broken by quark mass differences, so the excitation patterns for all three $\Sigma_b$ states are nearly identical.
:::
The excitation spectrum is determined by spin rather than isospin. Since all three isospin partners are related by symmetry, their properties—including their excited states—are very similar. The small isospin breaking due to quark mass differences is negligible for most practical purposes.  

$$
\mu \approx \frac{e\hbar}{2m_q c}
$$  
where $m_q$ is the quark mass, explains why the magnetic moment is suppressed compared to lighter particles like the electron.  

The wave function for the $\Omega^-$ baryon is constructed from the spin states of the three strange quarks, with the magnetic moment operator given by:  

$$
\mu_z = \sum_{i=1}^3 \mu_{iz}
$$  

For the highest spin projection state, the magnetic moment is straightforward to evaluate, as it depends only on the quark charges and spins. The charge of each strange quark is $-1/3$, so the total charge is $-1$.

<!--
Cosine simularity: 0.9385343176154074
-->
## Heavy Quark Spin Dynamics and Energy Splitting

The excitation pattern remains the same regardless of which state we consider as the lowest. For the diagram, we plot different quantum numbers on the x-axis, typically orbital angular momentum in the excitation spectrum, and the rest mass energy (or hadron mass) on the y-axis.  

To construct this, we start by combining the spins of the light quarks and the heavy quark. For most hadrons (except light mesons), the radial excitation—moving from 1s to 2s orbitals—is much larger than hyperfine splitting. This is always true for heavy quarks. The energy difference from combining spins is suppressed by a factor of the heavy quark mass:  

$$
\Delta E \sim \frac{1}{m_Q}
$$

For an S-wave state, combining a light diquark with spin $S = 1$ and a heavy quark with spin $S = 1/2$ yields two possible states:  

$$
J = \frac{1}{2} \oplus \frac{3}{2}
$$

When adding one unit of orbital angular momentum (P-wave), we must consider both spin combinations separately. The multiplicity for the P-block is 5, while the S-block has a multiplicity of 2. The lowest states are $\frac{1}{2}^+$ and $\frac{3}{2}^+$, followed by five P-wave states. These correspond to distinct particles listed in the PDG, though some (like $\Sigma_b(300)$) were discovered relatively recently.  

The energy splitting between states arises from the heavy quark spin dynamics, while radial excitations are governed by QCD dynamics at the scale of $\Lambda_{\text{QCD}}$ (a few hundred MeV). The splitting within a block is suppressed by the heavy quark mass.  

::: callout-note
The strong coupling diverges at $\Lambda_{\text{QCD}}$, setting the energy scale for radial excitations.
:::
For the $\Omega^-$ baryon, the magnetic moment is negative due to its negative charge, though it is much smaller than the electron's moment. The mass scale in the magnetic moment formula depends on the quark mass ($m_q \approx 500 \ \text{MeV}$) rather than the baryon mass ($\sim 1500 \ \text{MeV}$):  

$$
\mu \approx \frac{e\hbar}{2m_q c}
$$

The $\Sigma_b$ baryon's excitation pattern is determined by its light diquark ($S = 1$, $\frac{1}{2}^+$). Its isospin partners form a triplet ($I = 1$) with charges:  

-$\Sigma_b^+$ ($uu b$): $+1$  
- $\Sigma_b^0$ ($ud b$): $0$  
- $\Sigma_b^-$ ($dd b$): $-1$  

::: callout-tip
Isospin symmetry is nearly exact here, as quark mass differences cause only minor breaking.
:::
The magnetic moment operator for the $\Omega^-$ is:  

$$
\mu_z = \sum_{i=1}^3 \mu_{iz}
$$

where each strange quark contributes $-1/3$ to the total charge.

<!--
Cosine simularity: 0.8966537783587706
-->
## Heavy Quark Mass and Spin Suppression in Effective Theory  

The energy difference between levels arises from the dynamics of the heavy quark spin. Since the quark is heavy, all spin effects are suppressed inversely proportional to its mass. In the Lagrangian (and in all effective theories), the spin-orbit interaction appears in terms where the heavy quark mass is in the denominator.  

For example, the mass of the $b$ quark is around $4 \ \text{GeV}$, which introduces an order-of-magnitude suppression. The QCD scale $\Lambda_{\text{QCD}}$ is a few hundred MeV, setting the typical energy scale for these effects.  

::: callout-note
The spin-orbit coupling in heavy quark systems is suppressed by $1/m_Q$, where $m_Q$ is the heavy quark mass.
:::
The strong coupling diverges at $\Lambda_{\text{QCD}}$, governing the radial excitations, while spin-dependent splittings are smaller due to the heavy quark mass suppression.

<!--
Cosine simularity: 0.9239601881115391
-->
## Exotic Hadrons and Experimental Challenges in QCD

The energy scale $\Lambda_{\text{QCD}}$ is a few hundred MeV, while the typical excitation energies are on the order of a few GeV. The ratio between them is roughly 10:15, which reflects the difference between excitation energies of general quantum states and the splitting between specific levels.  

For example, the energy difference between $\Sigma_b$ with spin $3/2$ and $\Sigma_b$ with spin $1/2$ is of the order of 10 MeV.  

::: callout-note
The splitting between heavy quark states like $\Sigma_b$ is governed by spin-dependent interactions, which are suppressed by the heavy quark mass.
:::
Today's lecture focuses on the kinematics and experimental techniques in hadron physics. This field has been extremely vibrant in the last 10 years, starting around 2004 when the first exotic particles were discovered. Since then, new observations of states that do not fit the conventional quark model (mesons and baryons) have been reported frequently.  

Many experiments worldwide now dedicate part of their programs to studying hadrons, particularly exotic ones. Large laboratories conducting particle collisions contribute to this effort. A key challenge is understanding the fundamental structure of matter—how hadrons form, which combinations are possible, and what rules determine their excitation patterns and properties.  

Quantum Chromodynamics (QCD) describes strong interactions well in regimes where computations are feasible. However, there has been no success yet in systematically classifying and predicting large multiplets of exotic hadrons. Observations are made, but relating them to theoretical predictions remains difficult due to computational limitations and the complexity of QCD dynamics.  

::: callout-important
The strong coupling diverges at $\Lambda_{\text{QCD}}$, setting the scale for radial excitations, while spin-dependent effects are smaller due to heavy quark mass suppression.
:::
<!--
Cosine simularity: 0.9299938499553769
-->
## Transition of Matter and Hadron Spectroscopy  

We cannot do this partly because of the limitations of our computational methods. Lattice QCD, while effective for ground states, is not well-suited for computations at larger scales due to the complexity of the theory.  

The phenomena in QCD reveal emerging behaviors that are not directly described by the Lagrangian's quark and gluon degrees of freedom. Instead, we observe a transition in matter: from configurations where quark degrees of freedom dominate (such as quark-gluon plasma) to configurations where hadrons themselves become the relevant degrees of freedom (such as in atomic nuclei).  

In hadron spectroscopy, this transition manifests as a boundary region where hadrons—composed of elementary quarks—coexist with larger atomic-scale objects. Here, hadrons bind into more complex structures, creating a mixed regime.  

::: callout-note
The transition between quark-dominated and hadron-dominated matter highlights the challenge of modeling QCD across different energy scales.
:::
The theory's complexity arises from the interplay of these scales, where neither perturbative methods nor pure lattice computations fully capture the dynamics. This is particularly evident in spectroscopy, where exotic states blur the line between quark-level and hadron-level descriptions.

<!--
Cosine simularity: 0.9332114090839496
-->
## Hadron Production Mechanisms and Experimental Approaches

Hadrons bind in larger objects, such as atomic nuclei, and some hadrons are complicated because their properties arise from a mixture of different configurations. Some properties require them to be compact hadrons, while others require them to be sparse hadronic molecules, which we refer to as "atoms" in hadron spectroscopy.  

Currently, lattice QCD cannot fully address these complexities, so experiments worldwide provide new data and insights. Researchers understand these phenomena by measuring hadron properties and their decays. One approach is to observe hadrons in new decay configurations, which yield valuable information. Another is to measure the same hadron but from different production mechanisms.  

Several laboratories explore these mechanisms:  

-**Belle II (Japan) and BESIII (China)**: These experiments collide electrons and positrons, which annihilate to produce intermediate states that decay. The resulting particles are studied to understand hadron properties.  
- **LHC (CERN)**: Here, protons (not proton-antiproton pairs) are collided, producing a high-energy environment with many particles. Among these are long-lived particles like $B$ and $D$ mesons, which travel a few millimeters before decaying. Detectors track these particles, distinguishing primary and secondary vertices.  

Another class of experiments uses **hadronic production**, where a hadron is fired at another hadron without fully describing the kinematics. These are typically fixed-target experiments, such as:  

-**GLUEX (Jefferson Lab)**: Uses a photon beam on a hydrogen target.  
- **COMPASS (CERN)**: Uses a pion beam on a hydrogen target.  

In these setups, the target particle is either excited or scatters, providing another way to study hadrons.  

The third major approach is computing hadron properties from **lattice QCD**, though this method has limitations for certain states.  

::: callout-note
Different production mechanisms (lepton collisions, proton collisions, hadronic scattering) provide complementary insights into hadron structure and dynamics.
:::
The interplay between these experimental methods helps clarify the transition between quark-dominated and hadron-dominated matter, a key challenge in QCD.

<!--
Cosine simularity: 0.9338952543991448
-->
## Electron-Positron Collisions and Spin Configurations

The third major way to study hadrons is to compute their properties from lattice QCD, which provides a large piece of information.  

Let's overview the production mechanism and experiments. We start with the **Beijing Spectrometer (BESIII)**, located at the **Beijing Electron Positron Collider (BEPC)**. This accelerator complex collides electrons and positrons. The experiment is dedicated to studying hadrons in the energy regions of charmonium and bottomonium.  

BEPC is a symmetric collider, meaning the electron and positron have the same energy. When they collide, one possible interaction is annihilation, producing a virtual photon that couples to a hadron.  

The spin configurations in these collisions are constrained. An electron has spin $1/2$, and at high energies, it has a specific helicity. When combining two spin-$1/2$ particles (electron and positron), the possible total spin states are $0$ or $1$. However, due to their nature as particle-antiparticle pairs and helicity conservation, the produced system can only have spin $1$ — spin $0$ is forbidden in this combination.  

Additionally, the parity of the system is determined by the combination of the electron ($1/2^-$) and positron ($1/2^+$) in an $S$-wave state.  

::: callout-note
The spin and parity selection rules in electron-positron collisions restrict the possible hadronic states produced, providing a clean environment for studying specific quantum numbers.
:::
<!--
Cosine simularity: 0.917746999673113
-->
## Hadron Production and Resonance Peaks in Collider Experiments

We combine particles with quantum numbers $1/2^-$ and $1/2^+$ in an $S$-wave configuration. This experiment focuses on hadrons produced with quantum numbers $1^-$. The data collection process involves setting the beam energy to accumulate large datasets, such as millions of events for the $J/\psi$ peak.  

When plotting the cross section as a function of energy, the distribution is not homogeneous but exhibits peaking structures. These peaks occur when the system resonates at specific frequencies, corresponding to hadronic states. By tuning the collision energy to match these resonances, the interaction probability (and thus the cross section) increases.  

::: callout-note
The cross section magnitude indicates interaction frequency and directly influences the data volume recorded.
:::
The $J/\psi$ peak is a prominent example. The German spectrum (shown here) plots orbital excitations on the $X$-axis and system energy on the $Y$-axis. The lowest state is followed by higher multiplicities, derived from quark algebra. The $J/\psi$ and $\eta_c$ belong to the same multiplet, with $J/\psi$ being the first discovered charmonium state.  

The $J/\psi$ is a clear peak in the $e^+e^-$ cross section spectrum, with quantum numbers $1^-$. Its production is straightforward due to quantum number selection rules in relativistic collisions. The second peak in the spectrum corresponds to the excited state $\psi(2S)$.  

The naming convention for $J/\psi$ reflects its discovery history, where "J" honors one of the lead researchers. This state is a benchmark for studying charmonium spectroscopy due to its clean experimental signature.  

$$
\sigma(E) \propto \text{Resonance amplitude at energy } E
$$

The cross section enhancement at resonance energies ($E_{\text{res}}$) follows the Breit-Wigner distribution:  

$$
\sigma(E) \sim \frac{\Gamma^2/4}{(E - E_{\text{res}})^2 + \Gamma^2/4}
$$

where $\Gamma$ is the resonance width.  

::: callout-important
Resonance peaks provide direct access to hadronic states with specific quantum numbers, enabling systematic studies of quarkonium spectra.
:::
The $\psi(2S)$ state, as an excitation of the $J/\psi$ system, further probes the dynamics of heavy quark bound states.  

<!--
Cosine simularity: 0.9038947237873494
-->
## J/ψ and Υ Resonance Studies in Electron-Positron Collisions

In the spectrum, the excitation of this system is the $\psi(2S)$, which we refer to simply as "psi" here. The lowest state in the multiplet is called the $J/\psi$, while the four states in the $P$-multiplet are labeled $\chi_{c0}$, $\chi_{c1}$, $\chi_{c2}$, and $h_c$ (with quantum numbers $0^+$, $1^+$, $2^+$, and $1^+$ respectively).  

For data collection, there are two primary methods:  

1.**Resonance peak sitting**: Accumulating data at the $J/\psi$ peak yields billions of events where the $J/\psi$ is produced and decays into various final states.  
2. **Energy scan**: By tuning the beam energy over weeks, we measure the cross section at discrete points, building a profile of the resonance structure.  

The total cross section is a superposition of all possible sub-processes, such as $e^+e^- \to \text{hadrons}$. Some resonances are more prominent in specific decay kinematics, so researchers often analyze a particular final state (e.g., $e^+e^- \to 3\pi$) at a selected scan point to extract hadron properties.  

::: callout-note
The cross section enhancement follows the Breit-Wigner distribution:
:::
$$
\sigma(E) \sim \frac{\Gamma^2/4}{(E - E_{\text{res}})^2 + \Gamma^2/4}
$$

where $\Gamma$ is the resonance width and $E_{\text{res}}$ is the resonance energy.  

The $J/\psi$ and $\Upsilon$ families provide clean signatures for studying quarkonium spectroscopy due to their well-defined quantum numbers ($1^-$) and relativistic production mechanisms. The $\psi(2S)$ serves as an excited-state benchmark, probing the dynamics of heavy quark bound systems.

<!--
Cosine simularity: 0.8993914983087137
-->
## Asymmetric Beam Energies and Boost in B Meson Studies

The BEL2 experiment in Japan was originally designed with the primary goal of studying CP violation, but its data proved extremely valuable for hadron spectroscopy as well. This experiment operates as an electron-positron collider and is located at KEK. It was initially called the Belle experiment, and after an upgrade 10 years ago, it became known as the SuperKEKB experiment. The predecessor was called Belle, and the upgraded version is referred to as Belle II.  

In contrast to the Belle experiment, the colliding beams in Belle II are not symmetric. The center-of-mass energy is adjusted to a specific resonance, primarily to study B mesons and CP violation. The experiment operates at the $\Upsilon(4S)$ resonance, which predominantly decays into a $B\bar{B}$ pair.  

::: callout-important
The $\Upsilon(4S)$ is a short-lived resonance that decays immediately, leaving the primary vertex and producing a $B\bar{B}$ pair. The physics of CP violation is then studied using these decays.
:::
A key question is why the beam energies are asymmetric. This design choice is deliberate and clever. By giving the electron and positron beams different energies, the entire system receives a boost when produced. This boost is in the direction of the higher-energy beam (the electron beam) due to energy conservation.  

The boost has a significant effect on the B mesons:  

-The B mesons gain a substantial longitudinal momentum.  
- They live longer in the laboratory frame due to relativistic time dilation.  
- They travel farther from the primary vertex before decaying.  

This increased flight distance is crucial for precise vertex reconstruction. By measuring the displacement between the primary vertex and the decay point (secondary vertex), we can better identify and reconstruct B meson decays. The charged tracks from these decays do not point back to the primary vertex, providing a clear signature of secondary vertices.  

::: callout-note
The boost effect can be quantified using relativistic kinematics. The Lorentz factor $\gamma$ and the velocity $\beta$ determine the observed lifetime $\tau_{\text{lab}}$ in the lab frame:
:::
$$
\tau_{\text{lab}} = \gamma \tau_0, \quad \gamma = \frac{E}{m}, \quad \beta = \frac{p}{E}
$$

where $\tau_0$ is the proper lifetime, $E$ is the energy, $m$ is the mass, and $p$ is the momentum of the B meson.  

This technique enhances our ability to separate signal from background and improves the precision of CP violation measurements. Before moving away from Belle II, let me connect this back to what we discussed earlier.

<!--
Cosine simularity: 0.864971669763634
-->
## Charmonium and Bottomonium Spectra in Electron-Positron Annihilation

Let me relate to what we just discussed earlier. Essentially, it's the same process of $e^+e^-$ annihilation, so we consider the total cross section $\sigma(e^+e^- \to \text{everything})$.  

The Belle experiment operates in the energy region of $J/\psi$ and $\tau$ production (charmonium), while the Belle II experiment focuses on the bottomonium region. Charmonium consists of $c\bar{c}$ states, while bottomonium is made of $b\bar{b}$ pairs.  

Moving to higher energies, around 10 GeV, we enter the bottomonium system, which is structurally similar to charmonium. However, since the $b$ quark is even heavier, the hyperfine splitting is smaller. The mass difference between the $\eta_b$ and the vector bottomonium state ( $\Upsilon$ ) is reduced compared to charmonium.  

The energy scale between levels remains roughly the same (a few hundred MeV), but within each multiplet, the states are more tightly packed. The $\Upsilon$ is the vector particle (spin $1^{--}$) and is the bottomonium counterpart of the $J/\psi$ in charmonium.  

<!--
Cosine simularity: 0.8645416733979943
-->
## Production and Study of Upsilon Particles in Proton Collisions

The Upsilon ($\Upsilon$) is a vector particle with spin $1^{--}$, analogous to the $J/\psi$ in the charmonium spectrum. The $J/\psi$ is the easiest particle to produce in the charmonium spectrum due to its quantum numbers ($1^{--}$), especially in electron-positron annihilation, making it the most studied state.  

In the bottomonium spectrum, the counterpart of the $J/\psi$ is the $\Upsilon$. The notation $4s$ refers to the fourth excited state in the bottomonium spectrum, arising from the $4 \times$ acceleration of the spectrum. When scanning the energy, the states appear sequentially: first the $\Upsilon(1s)$, then $\Upsilon(2s)$, $\Upsilon(3s)$, and finally $\Upsilon(4s)$.  

All these states lie above the threshold for $B$-meson production, with masses exceeding 9 GeV. For example, the $\Upsilon(1s)$ has a mass around 9.46 GeV, while higher states like $\Upsilon(4s)$ are even heavier.  

Proton-proton collisions are significantly more complex than electron-positron annihilations. The multiplicity of particles produced in such collisions is very high, increasing with energy. At the LHC, with proton beams at 7.7 TeV, the collisions are symmetric. However, since these are not annihilation processes, the produced particles are typically boosted due to the initial quark and gluon interactions.  

The typical multiplicity of particles produced in a single proton-proton collision is on the order of thousands. The transverse momentum ($p_T$) spectrum follows an exponential distribution, with most particles at low momentum and a tail extending to higher energies. The typical energy scale for particles in these collisions is hundreds of GeV, though individual particle energies can range from tens to hundreds of GeV.  

$$
\frac{dN}{dp_T} \sim e^{-p_T / T}
$$

Here, $T$ represents the characteristic temperature of the system, describing the slope of the momentum distribution. Even when the total collision energy is shared among thousands of particles, the typical energy per particle remains in the range of a few GeV, with many low-momentum particles dominating the spectrum.

<!--
Cosine simularity: 0.9107210040415809
-->
## Production Mechanisms and Vertex Analysis in Hadron Spectroscopy

The typical energy scale for light, low-momentum particles is a few hundred GeV. The LHC has been highly productive in discovering new particles, particularly due to its high cross-section. The cross-section for electron-positron annihilation is much smaller than for proton-proton interactions, enabling the study of hadron production.  

There are two main production mechanisms in collider processes:  

1.**Prompt production**: The particle of interest originates directly from the primary vertex.  
2. **Cascade production**: The particle decays weakly, producing a secondary vertex.  

For example, the observation of the $\Omega_c$ baryon and the $\Xi_c^{(*)} $ states in prompt production has significantly impacted hadron spectroscopy. The cascade ($\Xi$) particle, the ground state of the cascade multiplet, decays weakly since the charm or bottom quark is stable under strong interactions.  

The lifetime of such weakly decaying particles is around $10^{-10}$ seconds. If the particle is boosted to 100 GeV, it travels millimeters before decaying, allowing separation from the primary vertex. Ground states of charm or bottom hadrons typically displace by 5–6 millimeters.  

To reconstruct the secondary vertex, charged particles (e.g., proton-kaon pairs) are combined from the thousands of produced particles. By looping over all kaon-proton ($K\pi$) pairs and matching them with identified cascade decays, resonances produced at the primary vertex can be isolated. The mass spectrum of the $\Xi_c K$ system reveals clear peaks corresponding to these resonances.  

$$
\frac{dN}{dp_T} \sim e^{-p_T / T}
$$

Here, $T$ represents the characteristic temperature of the system, describing the exponential slope of the transverse momentum ($p_T$) distribution. Most particles have low momentum, with a tail extending to higher energies.  

::: callout-note
Weak decays of heavy-flavor hadrons (e.g., $\Xi_c$) produce measurable secondary vertices, crucial for distinguishing them from prompt backgrounds.
:::
::: callout-tip
Vertex resolution at the LHC is sufficient to resolve displacements as small as a few millimeters, enabling precise reconstruction of cascade decays.
:::
<!--
Cosine simularity: 0.9312895931241527
-->
## Resonance States and Strangeness in Omega C Model

In the spectrum of the cascade $\Xi_c$ mass, you observe five distinct bumps. These correspond to the highest probability of producing a system, indicating resonant behavior at frequencies matching the excited states in the $\Omega_c$ model.  

The $\Omega_c$ baryon is identified by counting strangeness: it contains two strange quarks ( $s$ ) and one charm quark ( $c$ ), denoted as $ssc$. In contrast, the cascade ( $\Xi_c$ ) is $suc$, and the kaon-nucleon ( $KN$ ) system is $s\bar{u}$.  

Another approach involves studying secondary vertices from $B$ decays. Ground-state hadrons with a $b$ quark include $B$ mesons and $\Lambda_b$ baryons. These are most easily produced via currents carrying the $b$ quark. As ground states, they decay rapidly, with lifetimes on the order of $10^{-9}$ seconds. However, when boosted, they produce secondary vertices several centimeters away from the primary interaction point.  

For example, a displacement of two centimeters is observable in detectors, such as those at CERN. This flight distance separates the primary interaction vertex from the decay products, enabling clean kinematic reconstruction. By measuring the momentum of the $B$ hadron and the decay length, you isolate its decay and study resonances within it.  

A prominent example is the decay $\Lambda_b \to J/\psi \, p \, K^-$. This three-body decay allows analysis of exclusive final-state combinations ( $J/\psi \, p \, K^-$ ). The spectrum of the $pK^-$ system shows bumps corresponding to $\Lambda$ resonances, while the $J/\psi \, p$ spectrum reveals unexpected peaks. These peaks are attributed to pentaquark ( $P_c$ ) resonances, specifically $u u g c \bar{c}$ combinations.  

::: callout-note
The $\Omega_c$ and $\Xi_c$ resonances are key to understanding the spectrum of charm-strange baryons, with their production and decay patterns offering insights into QCD dynamics.
:::
::: callout-tip
Secondary vertex analysis is crucial for isolating weakly decaying heavy-flavor hadrons, as their displaced decays reduce background contamination from prompt production.
:::
<!--
Cosine simularity: 0.9397949583467019
-->
## Fixed Target Experiments and Light Hadron Spectroscopy  

The $u u g c \bar{c}$ combinations represent a resonance. Let’s briefly review fixed target experiments and their techniques, with three examples:  

1. **GLUEX at Jefferson Lab**: Uses a 9 GeV photon beam directed at a liquid hydrogen target, which provides protons as the interaction medium.  
2. **Compass at CERN**: Operates with a pion beam and also employs a liquid hydrogen target.  
3. **CB-ELSA (corrected from "CD alpha tops")**: Utilizes a photon beam at 2 GeV, focusing on light hadron spectroscopy rather than charm or bottom production.  

Most of these experiments study light hadrons, including pions and kaons. The GlueX experiment, in particular, investigates the same physics domain.  

::: callout-note
Fixed target experiments like GlueX and Compass are optimized for precision measurements of light hadron spectra, leveraging controlled beam-target interactions.
:::
::: callout-tip
Liquid hydrogen targets are commonly used due to their purity and simplicity in providing proton targets for beam interactions.
:::
<!--
Cosine simularity: 0.9486278359758714
-->
## Diffraction and S-Channel Scattering in Particle Collisions

The GlueX experiment is doing the same physics but with a different setup, beam type, and energy. CPL setups in Bonn are starting with rns, and it begins in the office.  

It is important to realize that there are two different mechanisms involved in fixed-target experiments at intermediate energies. These are not TVs. The first process is diffraction, and the second is S-channel scattering. The process that occurs when two particles collide depends on the energy.  

In diffraction, the proton acts as a source of the strong interaction field. Here, the proton emits gluons, serving as a source of gluonic fields. A pion or photon then interacts with these gluonic fields and becomes excited. The excited state ($X$) propagates briefly before decaying.  

<!--
Cosine simularity: 0.9180090761478364
-->
## Kinematics and Resonances in Particle Interactions

The excited state "flies" for a brief moment before decaying, though in reality, it doesn't physically move far due to the strong interaction timescales. Hadronic resonances, particularly light ones in detectors, exist for times on the order of $10^{-25}$ seconds, which is insufficient to displace them measurably from the primary vertex. However, we still represent them as separate particles in diagrams for clarity.  

If the system's energy is too high, resonances cannot form — there are no frequencies for the system to "resonate" at. The process becomes more plausible at lower energies, where a proton and an incoming beam (pion or photon) can resonate at specific frequencies. For instance, at energies around 2–3 GeV, this resonant interaction occurs.  

In fixed-target kinematics, experiments like COMPASS study the diffractive regime, while CERN’s CPL focuses on $S$-channel production. These experiments probe baryonic excitations by analyzing resonance decays. The GlueX experiment at Jefferson Lab operates at 9 GeV, an intermediate energy where both diffractive and $S$-channel processes coexist, leading to coherent interference. Ideally, higher energies would isolate one process over the other, but at these scales, all possible interactions occur and must be accounted for.  

<!--
Cosine simularity: 0.9420182752582591
-->
## Diffractive Gluon Interactions and the Pomeron  

In particle interactions, all possible kinematic configurations occur, and we must account for them. The setups and kinematics involve many intricate and interesting aspects that may be explored in future lectures.  

Regarding experiments, some are currently operational, while others are planned for the future. For example, the GlueX experiment is still running but is in its final years. There are proposals to upgrade it to "GlueX2" or a similar configuration, which would focus more on spectroscopy.  

A key question arises about the interaction mechanism in diagrams: is it direct or indirect gluon exchange? The answer lies in the color-neutral nature of the proton. Since a single gluon cannot maintain color neutrality, the proton emits a **gluonic field** instead. This field is color-neutral, and we describe the process as **diffraction** rather than simple gluon exchange.  

The physical interpretation is as follows: the proton acts as a stationary source, emitting this gluonic field. The interaction resembles light scattering off an object, producing a diffractive pattern. The proton behaves like a "black disk," and the resulting diffraction is observed. The exchanged entity — a collective state of gluon fields — is called the **Pomeron**.  

::: callout-note
The Pomeron is not a true particle and does not appear in the Particle Data Group (PDG) listings. It is a phenomenological construct used to describe the behavior of the gluon field in diffractive processes.
:::
This process is not fully understood in terms of individual gluons but is well-established phenomenologically. The Pomeron represents the effective description of the gluon field's role in diffraction.

<!--
Cosine simularity: 0.9227952781857875
-->
## Kinematic Variables in Exclusive Scattering Processes

The sum of momenta in an exclusive scattering process is given by:

$$
\sum_i (\vec{p}_1 + \vec{p}_2 + \vec{p}_3 + ... - \vec{p}_A - \vec{p}_B) = \sum_i \sum_p \sum_p \sum_A
$$

This represents the momentum balance between initial and final states.  

Exclusive reactions are those where all particles are measured and accounted for, such as $1 \to n$ or $2 \to n$ processes. In contrast, inclusive processes involve unmeasured particles produced alongside the system of interest.  

To count the kinematic variables describing such a process, we consider the four-momenta of all particles involved. Each particle has four components in its four-vector, but one constraint (mass-shell condition) reduces this to three independent components. For a $2 \to 3$ process, we have $5$ particles (2 initial + 3 final), each contributing $3$ independent momentum components, totaling $15$ variables.  

We then subtract the constraints from energy-momentum conservation, which imposes four delta functions (one for energy and three for momentum):

$$
\delta^4 \left( \sum_{\text{final}} p_i - \sum_{\text{initial}} p_j \right)
$$

This reduces the number of independent variables to $15 - 4 = 11$ for a $2 \to 3$ process.  

The interaction in such processes is often represented diagrammatically, where a "blob" denotes the interaction and lines represent incoming or outgoing particles. The Pomeron, a phenomenological construct, describes the collective gluon field in diffractive interactions, though it is not a true particle.  

::: callout-note
The Pomeron is color-neutral and represents the effective description of the gluon field's role in diffraction, rather than a single gluon exchange.
:::
This approach is well-established phenomenologically, even if the underlying gluon dynamics are not fully understood.

<!--
Cosine simularity: 0.9137797269581968
-->
## Degrees of Freedom and Frame Fixing in Kinematics  

For a $2 \to 3$ process, we start with 15 variables (5 particles × 3 independent momentum components each). After accounting for energy-momentum conservation, we reduce this to $15 - 4 = 11$ variables needed to describe the kinematics in any frame.  

We can further reduce these degrees of freedom by choosing a specific frame. Fixing the frame eliminates 6 degrees of freedom: 3 for rotations and 3 for boosts.  

The momentum balance is given by:  

$$
\sum_i (\vec{p}_1 + \vec{p}_2 + \vec{p}_3 + ... - \vec{p}_A - \vec{p}_B) = \sum_i \sum_p \sum_p \sum_A
$$

<!--
Cosine simularity: 0.9684183049094974
-->
## Rigid Body Analogy and Euler Rotations in Kinematics

I'm going to lose six degrees of freedom: three for rotation and three for boosts. This gives the number of variables in this type of matrix.  

The boost annotations are important to realize. The analogy is that you can think of the reaction block as a solid rigid bow with arrows sticking out. You can hold it in your hand, and this is essentially a rigid body.  

For rigid bodies, there are three Euler rotations that describe the orientation of the body. These are exactly the three rotations you need to fix. You can think of it this way: for every event, for every set of kinematic variables, you can identify the length of the vectors and their mutual orientation.  

For every set of kinematic variables, you could take a 3D printer and print it. These three rotations would then determine its orientation. In computations, these rotations are crucial for fixing the frame.

<!--
Cosine simularity: 0.9383335911616315
-->
## Lorentz-Invariant Phase Space and Energy-Momentum Conservation  

In computations, we often need the quantity that's essential for calculating cross sections: the number of configurations the system can take. These configurations include not only the overall system's orientation (three rotations and three boosts) but also the mutual orientations of the components.  

The Lorentz-invariant phase space element counts the number of configurations for every particle in the final state. For each particle, the phase space element is:  

$$
d\rho = \frac{d^4 p}{(2\pi)^4} \delta(p^2 - m^2)
$$

Here, $d^4 p$ is the four-momentum volume element, and the delta function enforces the mass-shell condition. By integrating over the energy component, we obtain the familiar form:  

$$
\frac{d^3 p}{2E (2\pi)^3}
$$  

The delta function ensures energy-momentum conservation, and we sum over all zeros of the delta function. To exclude negative-energy solutions, we include a theta function for energy:  

$$
\delta(p^2 - m^2) \rightarrow \delta(E^2 - \vec{p}^2 - m^2) \theta(E)
$$  

Each delta function comes with a factor of $2\pi$, which is straightforward to remember. The energy-momentum conservation constraint is implemented via:  

$$
(2\pi)^4 \delta^4 \left( \sum_i p_i - P_{\text{tot}} \right)
$$  

This ensures the total four-momentum is conserved in the system.  

::: callout-note
The phase space element accounts for all possible kinematic configurations while respecting Lorentz invariance and energy-momentum conservation.
:::
The rigid body analogy helps visualize this: for every set of kinematic variables, the system's orientation is fixed by three Euler rotations, analogous to holding a rigid body in space. These rotations are crucial for defining the reference frame in computations.

<!--
Cosine simularity: 0.9361641999767065
-->
## Recursive Evaluation of Phase Space in Particle Dynamics  

The recursive evaluation of phase space is a straightforward concept, particularly when considering multi-particle systems. Here, we examine the case of a 4-body process. While the mathematical exercise of simplifying the integral is possible, it is not necessary to demonstrate explicitly that this complex integral reduces to a product of two-body phase spaces.  

The diagram in question does not represent the dynamics of the process but rather operates with kinematic variables. The transition from 1 to 4 particles introduces additional degrees of freedom—specifically, 15 variables. When calculating phase space, we account for 3 integrals per particle, hence the factor of 3 in the phase space formula for each particle.  

The initial state does not contribute to the phase space count; only the final state is considered. The four energy-momentum conservation laws are explicitly enforced, reducing the number of remaining integrals. Starting with 12 integrals (3 per particle for 4 particles), we subtract 4 for momentum conservation, leaving 8.  

The remaining kinematic degrees of freedom include 5 variables for overall rotation (3 of which are finite Euler angles) and 3 boosts. The choice of these 5 variables is arbitrary and depends on the most convenient parameterization for calculating dynamics. The recursive approach does not prescribe specific interactions or reaction pathways—it is purely a kinematic parameterization.  

A common choice is to introduce intermediate mass variables, such as $x$ and $y$, and express the phase space as:  

$$
d\rho = \int \frac{dM_x^2}{2\pi} \frac{dM_y^2}{2\pi} \cdot d\rho_2(0 \to y + 3)
$$  

This recursive expression is not limited to 2-body processes but can also be extended to 3-body cases. The key feature is the introduction of intermediate mass variables, over which we integrate. Each such integral includes a factor of $2\pi$ in the numerator.  

The Lorentz-invariant phase space element for each particle is given by:  

$$
d\rho = \frac{d^3 p_i}{2E_i (2\pi)^3}
$$  

and the overall conservation is enforced by:  

$$
(2\pi)^4 \delta^4 \left( \sum_i \vec{p}_i - \vec{P}_{\text{tot}} \right)
$$  

This recursive decomposition simplifies the computation of multi-particle phase space while maintaining Lorentz invariance and energy-momentum conservation. The choice of kinematic variables remains flexible, tailored to the specific problem at hand.

<!--
Cosine simularity: 0.8983028078706422
-->
## Calculation and Simplification of 2-Body Phase Space  

Every integral in phase space comes with a $2\pi$ in the numerator. For example, introducing an intermediate state $Y$ in the process $0 \to Y + 4$ and then $Y \to 1 + 2 + 3$ is a valid decomposition. Once you learn this trick, phase space calculations become straightforward because every 2-body phase space has the form:  

$$
d\rho_2 = \frac{2p}{\sqrt{s}} \cdot \frac{\Omega}{4\pi} \cdot \frac{1}{2\pi}
$$  

This expression does not simplify further and represents a general feature of the 2-body phase space. We had an opportunity to derive this in class, but we did not complete it.  

The Lorentz-invariant phase space for a single particle is given by:  

$$
d\rho = \frac{d^3 p_i}{2E_i (2\pi)^3}
$$  

and the overall energy-momentum conservation is enforced by:  

$$
(2\pi)^4 \delta^4 \left( \sum_i \vec{p}_i - \vec{P}_{\text{tot}} \right)
$$  

The recursive approach allows breaking down multi-particle phase space into simpler 2-body components, making calculations more manageable.

<!--
Cosine simularity: 0.8364749397179856
-->
## Introduction to 3-Body Phase Space and Dalitz Plot

With the formula we derived, you can now calculate any $n$-body phase space. There is an exercise to explore the three-body phase space, which has $3 \times 3 - 4 = 5$ degrees of freedom, minus 3 for rotations, leaving only 2 variables. The distribution is often represented using these two variables, typically chosen as invariant masses. This representation is called the Dalitz plot.  

The Lorentz-invariant phase space for a single particle is:  

$$
d\rho = \frac{d^3 p_i}{2E_i (2\pi)^3}
$$  

and overall energy-momentum conservation is enforced by:  

$$
(2\pi)^4 \delta^4 \left( \sum_i \vec{p}_i - \vec{P}_{\text{tot}} \right)
$$  

The recursive approach simplifies multi-particle phase space calculations by breaking them into 2-body components.

<!--
Cosine simularity: 0.8514463015085423
-->
## Q&A and Exercise Schedule Announcement

The representation is called Dalitz plot. Hope to get the book next time. Let's have a round of questions for a minute. I won't have an exercise tonight. Any questions? Have you seen this before? That's really good, because these computations are not complicated, but they give you a lot of insight into how things work. Thanks for coming today, and don't forget to leave feedback sheets.  

This week we will not have exercises. Next week, would Wednesday or Friday work for you?  
