<!--
Cosine simularity: 0.9590622394529223
-->
## Introduction to Lecture Topics and Decay Analysis

We are finishing the lecture cycle with two more to go. Today's lecture will focus more on physics, while next week I will discuss meta-issues related to how the hadron community functions. I will provide background on research structure, collaborations, and how scientists operate in the hadron physics domain. Next week will have less physics, though I may spend the first 20 minutes reviewing recent discoveries and current experimental progress in the field.  

Today, I want to focus on physics, including formulas, and discuss how hadron physics is applied outside its domain. I debated dedicating this lecture to either CP violation, where hadron physics plays a key role, or to $g-2$ and hadronic contributions to the muon magnetic moment. I decided on the latter, as it connects to several topics we’ve already covered.  

The exercise sheet will now include problems on the $R$ ratio, which was previously postponed. We will revisit this at a more advanced level, incorporating the knowledge we’ve gained.  

To start today’s lecture, I will briefly recap our earlier discussion on helicity and chirality, specifically examining the decay of the $\pi^{+}$ meson:  

$$
\begin{align}
\pi^{+} &\longrightarrow \mu^{+}\,\nu_{\mu}\,, \\
\pi^{+} &\longrightarrow e^{+}\,\nu_{e}
\end{align}
$$

These decays illustrate key concepts in weak interactions and lepton universality. Comparing these processes will help us understand the underlying physics.

<!--
Cosine simularity: 0.8667178669593021
-->
## Chirality and Spin Configurations in Pion Decay

The ratio of matrix elements for pion decay into electrons versus muons is given by:

$$
\frac{m_{e}}{E}<\frac{m_{\mu}}{E}\;\Longrightarrow\;  
\frac{|\mathcal{M}_{e}|^{2}}{|\mathcal{M}_{\mu}|^{2}}\ll1
$$

Here, $m_e$ and $m_\mu$ are the masses of the electron and muon, respectively, while $E$ is the energy scale of the decay. The inequality shows that the electron channel is suppressed compared to the muon channel due to the smaller mass of the electron.  

::: callout-important
Chirality is directly related to spin orientation in the high-mass limit, which is why we can clearly observe chiral properties in the decay products.
:::
The weak interaction vertex ( $V-A$ ) produces particles in their chiral configurations. For example, the $W$ boson decay produces a left-handed electron and a left-handed neutrino. Since the neutrino is massless, it is purely left-handed, while the electron has both left and right components, with the right component suppressed by $m_e / E$.  

In the center-of-momentum frame, the spins of the decay products must sum to the spin of the pion ( $J = 0$ ). For the electron and neutrino, their spins are $1/2$, and they must be back-to-back to conserve angular momentum. However, flipping the spin of the right-handed electron is allowed but suppressed by $m_e / E$, whereas the neutrino cannot be flipped due to its zero mass.  

::: callout-note
The suppression factor differs for electrons and muons because $m_e \ll m_\mu$. For the pion decay into muons, the muon is nearly non-relativistic, so the chirality suppression is less pronounced.
:::
The matrix elements for $\pi^+ \to e^+ \nu_e$ and $\pi^+ \to \mu^+ \nu_\mu$ are thus differently suppressed, with the electron channel being heavily suppressed due to its small mass. This explains why the pion predominantly decays into muons rather than electrons.

<!--
Cosine simularity: 0.9401249057468007
-->
## Phase Space and Energy Release in Pion Decay  

The expression for the phase space ratio in pion decay is:  

$$  
\frac{\Phi(\,e^{+}\nu_{e})}{\Phi(\,\mu^{+}\nu_{\mu})} = \frac{s-m_{e}^{2}}{s-m_{\mu}^{2}} > 1  
$$  

However, this does not fully explain the observed decay rates. The correct answer is that the ratio is significantly less than one, which is why pions decay predominantly to muons rather than electrons.  

Phase space represents the number of possible configurations in the decay. For two-body decays, it is determined by angular configurations, but there is also an energy-dependent factor. The larger the energy release, the larger the phase space.  

For the muon decay channel, the initial energy is given by the pion mass, and the final state includes particles with their own masses. The energy release is the difference between these masses. In the electron channel, the mass difference is small, so the energy release is tiny. In contrast, for the muon channel, most of the energy goes into kinetic energy because the neutrino is nearly massless.  

::: callout-note
The phase space is larger when more energy is released, favoring the muon channel despite the phase space ratio formula suggesting otherwise.
:::
The suppression of the electron channel is due to the small mass difference, which limits the available phase space compared to the muon channel. This explains why pions decay predominantly to muons.

<!--
Cosine simularity: 0.9379395322736357
-->
$$
## Magnetic Moment of the Muon and Quantum Corrections

Because the pion is massless and the electron is almost massless, the phase space is much larger. For the second case, however, this does not compensate the suppression. Let's consider the phase space of the electron channel. There is an angle integral which I'm going to implement now, and the neutrino phase space is something like that. The breakup momentum is something I need to evaluate, and I will double-check the calculation.  

The challenge function is the mass of the pion, and another channel function is zero. The chaining function is $xyz$, so it would be $x^2 + y^2 + z^2 - 2 \Delta E$. Once I drop the terms $x^2 + y^2 + z^2 + 2x^2 - 2yz - 2zx$, and then if $b = 0$, this term is dropped. The remaining expression is just the difference, which is a full square. I then substitute $(s - m_e^2) / (s - m_\mu^2)$. This full square is dropped because of the $1/2$ factor, and this is the answer.  

This node does not compensate the suppression, so the dominant decay of the pion is the muon channel. It's important to realize the steps we've taken because this is a nice piece of physics. It explains how parity violation was discovered—by observing that the muon is the predominant decay product. For this vertex to be $V - A$ weak interaction, you need this term to violate parity.  

Another interesting fact is that in this decay, the muon is produced polarized. The pion doesn't carry spin, and the neutrino is not detected—it just flies away. The muon, however, is produced polarized. In 1967, an experiment confirmed this. What's remarkable about the muon is that it is self-analyzing. Its decay to an electron, neutrino, and antineutrino has an angular distribution of electrons that indicates the muon's polarization.  

This is a very elegant setup. You can analyze the vertex here, which has a $V - A$ current that violates parity. The axial term $\gamma_5$ would violate parity, and you can check this easily. The second decay, the muon decay, produces a charged track. The angular distribution of this track in the muon's rest frame tells you whether the muon is polarized.  

If the muon is not polarized, the electron directions are equally probable in the helicity frame. But if it is polarized, the forward direction is preferred—aligned with the spin. The muon carries its spin as it flies, and in its rest frame, you only have spin information. This is called the KTG frame. In this frame, the electron preferentially moves in a certain direction, though it can go anywhere—just with different probabilities.  

Integrating over the electron energies reveals that this is the preferred configuration, even for a linearly polarized muon beam. Shortly after, the same technique was used to measure something more fundamental: the magnetic moment of the muon.  

We discussed this in the second lecture when we calculated the quark content of the proton's magnetic moment. Let me remind you what it is. The magnetic moment of a particle describes its interaction with a magnetic field. For a point-like fermion, it is given by the Bohr magneton and the gyromagnetic factor:  

$$
\vec{\mu} = \frac{e}{2m} g \vec{S}, \quad g = 2 \ \text{(Dirac, pointlike)}
$$

This is a fundamental quantity, and $g = 2$ for a fermion. However, for the proton, we found $g \approx 2.8$. How can this be if the proton is a fermion? This discrepancy indicates that the proton is not pointlike—it is made of quarks.  

In the quark model, we computed the correct value by considering the charges and masses of the constituent quarks. For the proton, the charge $e$ is $+1$, but for quarks, it is fractional. The masses are taken as constituent quark masses, around 0.3 GeV for up and down quarks.  

For the muon, however, we do not doubt that it is an elementary particle with no internal structure. We expect $g = 2$, but this is only true at first order. There are corrections from virtual processes that make $g$ not exactly 2. The quantity $a = (g - 2)/2$ is used to describe these corrections.  

The muon's $g - 2$ is one of the most precisely known numbers in physics. It is a key test of quantum field theory and may hint at new physics if discrepancies with theory are found.
$$

<!--
Cosine simularity: 0.9076887110688191
-->
## Precision in Physics and Quantum Loop Effects

The quantity $a_{\mu}$ is defined as:

$$
a_{\mu} \equiv \frac{g-2}{2} = 0.001165\,8209(63)
$$

This represents the anomalous magnetic moment of the muon. In physics, such precision is rare, and there is a significant effort to measure even more digits. This precision provides sensitivity to quantum loop effects and potential new physics, as corrections arise from virtual quantum processes.  

The muon's $g$-factor characterizes its interaction with photons. By probing the muon with a photon source, $g$ reveals how the muon "sees" light. If the muon were composite, this measurement would resolve its internal structure. However, in this case, the corrections come from quantum loop effects at the vertex.  

<!--
Cosine simularity: 0.931944516559909
-->
## QED Perturbation Theory and Magnetic Moment Corrections

In the case of muon vertex corrections, the function arises from processes like the one drawn here. These processes were first calculated in QED, which is a perturbative theory where the series converges as you include more loops.  

Now, we can start including morphologies like the three- or four-crossing processes. All possible processes are calculated to a fixed order by counting vertices. For example, here we have two vertices, giving the first-order correction.  

The charge of the electron and the muon combine as $e^2 / (4\pi) = \alpha$, where $\alpha$ is the fine-structure constant. The electron mass squared comes from these vertices.  

Currently, we know the corrections up to the fifth order in $\alpha$, meaning we have calculated terms like $\alpha^2$, $\alpha^3$, and so on up to $\alpha^5$. The fifth-order correction is proportional to $\alpha^5$.  

$$
a_{\mu}^{\text{QED}} = \frac{\alpha}{2\pi}
$$

This represents the leading-order QED contribution to the muon's anomalous magnetic moment. Higher-order terms refine this prediction.

<!--
Cosine simularity: 0.8658466478004531
-->
## Experimental Setup for Muon g-2 Measurement

The cyclotron frequency $\omega_c$ is given by:

$$
\omega_{c}=\frac{eB}{m\gamma}
$$

Here, $e$ is the muon charge, $B$ is the magnetic field, $m$ is the muon mass, and $\gamma$ is the Lorentz factor.  

The numerical value in parentheses indicates uncertainty in the last digits. The series converges, and modern calculations rely on numerical techniques rather than manual diagram evaluations, as done by Schwinger. For higher-order corrections (e.g., fifth order), millions of terms must be computed, but the muon mass can often be neglected to simplify loop integrals.  

The first-order correction was derived in the 1770s, and Schwinger later calculated the $\alpha/2\pi$ term, a foundational result for QED. The experimental measurement of $g-2$ uses the decay chain $\pi \to \mu \to e + \nu_\mu + \nu_e$. The setup, proposed decades ago, involves a storage ring with a 20-meter radius, similar to Brookhaven National Lab's experiment.  

Muons are trapped in the ring under a magnetic field, causing them to travel in circular orbits due to the bending force. The spin precession frequency $\omega_s$ is critical, and the difference $\omega_c - \omega_s$ is proportional to the anomalous magnetic moment $a_\mu$:

$$
\omega_c - \omega_s \propto a_\mu = \frac{g-2}{2}
$$

The experiment begins with a proton beam (e.g., hydrogen) striking a target to produce pions. These pions decay into muons, which are then directed into the storage ring. The muons' spin precession is measured to determine $g-2$.  

::: callout-note
The minus sign in the precession formula should be verified, as $\gamma > 1$ could affect the term's sign.
:::
The key insight is that the tilt of the muon's spin after one orbit is proportional to $a_\mu$, enabling precise measurement of the anomaly.

<!--
Cosine simularity: 0.91447047666436
-->
## Muon Spin Precession and Electron Detection

The spin precession frequency $\omega_s$ is given by:  

$$
\omega_{s}= \frac{g eB}{2m} +(1-\delta)\,\frac{eB}{m}
$$

Pions decay and some of them convert to muons, which become trapped in the storage ring. Since pions produce polarized muons, the initial spin configuration is already aligned for measurement.  

When the muon enters the magnetic field, its spin begins precessing as it moves along the circular path. The spin orientation is measured by detecting the electrons from muon decay. The muon bunch contains millions of particles, and as they decay, the emitted electrons are observed.  

The setup includes lead glass calorimeters placed inside the ring. Lead glass is used because its high atomic number ($Z$) ensures particles deposit all their energy within the material. The glass remains transparent to light, allowing photosensors at the ends to collect the energy deposited by incoming particles.  

These calorimeters measure the electron flux. If the muon spin points outward, fewer electrons are detected compared to when it points inward.  

<!--
Cosine simularity: 0.8781745221016476
-->
$$
## Hadronic Contributions to Anomalous Magnetic Moment

The spin precession frequency $\omega_s$ is measured in experiments like the muon $g-2$ experiment. If the spin points outwards, there is a loss of detected electrons, while if it points inwards, more electrons are observed. This creates fluctuations in the energy deposit along the circular path.  

In the $g-2$ measurement setup, the digital flow shows time on the x-axis and a signal related to energy deposit. The frequency of rotation remains constant because it is determined by the charge of the electron. Over time, muons in the batch decay, causing the overall energy deposit to decrease exponentially. However, this decay is modulated by spin rotation fluctuations.  

The analysis is blinded, meaning the true frequency is hidden until the final results are revealed. For instance, in a recent press release, the analysts wrote down the real frequency on a piece of paper in an envelope beforehand. During the press conference, the envelope was opened, and the true frequency was entered to unblind the results.  

The experiment measures $\omega_s$, but the key observable is the difference between $\omega_s$ and the cyclotron frequency $\omega_c$. If these frequencies were identical, the spin configuration would propagate uniformly, and no fluctuations would be observed. The experiment’s sensitivity comes from this difference.  

Muons are naturally polarized when produced in pion decays due to the weak interaction vertex, which enforces a specific chirality. This polarization is crucial for the experiment. The next-generation experiment is currently underway, with the primary challenge being the homogeneity of the magnetic field. Even slight inhomogeneities introduce uncertainties because the integral of the magnetic field experienced by the muon varies.  

The precision of the experiment is quantified in parts per billion (ppb). The current experimental uncertainty is 63 ppb, while the theoretical prediction is around 100 ppb.  

The hadronic contributions to the muon’s anomalous magnetic moment are significant. Beyond QED corrections, there are electroweak and hadronic effects. Two prominent hadronic contributions are:  


1. **Hadronic Vacuum Polarization (HVP)**: A photon produces hadrons, which then recombine into a photon. This is represented by the diagram where a photon splits into hadrons and reforms.  


2. **Hadronic Light-by-Light (HLbL) Scattering**: This involves photons interacting via intermediate hadrons. The process can be visualized as light entering and exiting a hadronic blob, with intermediate hadron states like $\pi^0$ or $\eta$ mesons, which decay into two photons.  

The quantum numbers ($J^{PC}$) of the intermediate hadrons must match those of the photon for the process to occur.  
$$

<!--
Cosine simularity: 0.8568702568782329
-->
## Hadronic Vacuum Polarization and Unitarity

The ratio $R(s)$ is defined as:

$$
R(s) = \frac{\sigma(e^+e^- \to \text{hadrons})}{\sigma_0(e^+e^- \to \mu^+\mu^-)}
$$

This measures the relative cross section of electron-positron annihilation into hadrons compared to muon pair production.  

::: callout-important
The photon has quantum numbers $J^{PC} = 1^{--}$ (spin 1, parity -1, charge conjugation -1).
:::
Examples of mesons with these quantum numbers include:  


- **Light quark sector**: The $\rho$ meson ( $u\bar{u}$ or $d\bar{d}$ ).  


- **Charm sector**: The $J/\psi$ ( $c\bar{c}$ ).  


- **Bottom sector**: The $\Upsilon$ ( $b\bar{b}$ ).  


- **Strange sector**: The $\phi$ ( $s\bar{s}$ ).  

::: callout-note
The $K^*$ meson ( $u\bar{s}$ or $s\bar{u}$ ) is also a vector meson but cannot be produced directly by a photon due to its non-zero flavor quantum numbers.
:::
The photon can only produce neutral flavor states, such as $\rho^0$, $\omega$, $\phi$, $J/\psi$, and $\Upsilon$. These particles dominate the contributions to hadronic vacuum polarization.  

::: callout-tip
The $\rho$ meson alone accounts for more than 50% of the total hadronic vacuum polarization contribution.
:::
Hadronic physics cannot be calculated from first principles. Instead, we rely on experimental data, particularly from $e^+e^- \to \text{hadrons}$ cross sections, due to unitarity. The photon's transition to hadrons and back is related to the $e^+e^- \to \text{hadrons}$ cross section because the quantum numbers match ( $1^{--}$ ).  

This allows a mixed theoretical-experimental approach:  


1. Measure $\sigma(e^+e^- \to \text{hadrons})$ experimentally.  


2. Use unitarity to relate it to the hadronic vacuum polarization contribution.  

The process is represented by diagrams where a photon fluctuates into hadrons and back, contributing to the muon's anomalous magnetic moment.  

::: callout-warning
Hadronic vacuum polarization is a major source of uncertainty in theoretical predictions for the muon $g-2$.
:::
The key idea is that the hadronic vacuum polarization component in quantum field theory is directly tied to the $e^+e^- \to \text{hadrons}$ cross section. This relationship is crucial for precision calculations in particle physics.

<!--
Cosine simularity: 0.8728900200071903
-->
## Cauchy Theorem and Analytic Functions

Let's look at the expression for the Cauchy integral formula:

$$
f(s) = \frac{1}{2\pi i} \oint \frac{f(s')}{s' - s} \, ds'
$$

Here, $f(s)$ is an analytic function, and the integral is taken over a closed contour in the complex plane. The denominator $s' - s$ introduces a pole at $s' = s$, and the residue theorem ensures the value of $f(s)$ is determined by its behavior at this pole.  

::: callout-note
The kernel in the integrand is related to the spin of particles. For scalar particles, the kernel simplifies to 1, but for particles with spin, it involves logarithms and rational functions.
:::
The integration starts at the threshold of the hadron production reaction. The lowest threshold corresponds to the lightest particles that can be produced on-shell. Since quarks cannot be on-shell due to confinement, the minimal process is the production of two pions ($2\pi$).  

::: callout-tip
The two pions must have non-trivial orbital angular momentum to match the quantum numbers $1^{--}$. An S-wave configuration would give $0^+$, so a P-wave is required to achieve $1^-$.
:::
The integral runs from the two-pion threshold to infinity, with a $1/s'$ denominator. This structure is familiar from the Cauchy theorem, which states that for an analytic function, the contour integral equals the sum of residues at its poles.  

$$
\oint f(s') \, ds' = 2\pi i \sum \text{Res}(f, s'_k)
$$

Here, $f(s')$ has a simple pole at $s' = s$, so the residue is just $f(s)$. This allows us to represent $f(s)$ as an integral over its boundary values.  

::: callout-important
The Cauchy theorem is a consequence of analyticity in the complex plane. It provides a way to reconstruct a function from its values on a contour enclosing its domain of analyticity.
:::
The integrand $\frac{f(s')}{s' - s}$ has a single pole, so evaluating the residue at $s' = s$ gives back $f(s)$. This is the essence of the Cauchy integral formula, and it is widely used in theoretical physics to derive dispersion relations and spectral representations.  

The connection to hadronic physics comes from unitarity, where the imaginary part of the amplitude is related to physical production thresholds. The lowest threshold ($2\pi$) dominates the low-energy behavior, while higher thresholds (like $4\pi$ or $K\bar{K}$) contribute at larger $s$.  

::: callout-warning
The analytic structure of amplitudes is crucial for ensuring causality and unitarity in quantum field theory. Incorrect handling of poles and cuts can lead to unphysical results.
:::
The Cauchy theorem thus provides a powerful tool for analyzing scattering amplitudes, vacuum polarization, and other quantities in particle physics. Its application relies on the analyticity of the underlying physical theory.  

<!--
Cosine simularity: 0.8831923492481398
-->
## Dispersion Relation and Contour Integration

The dispersion relation is a consequence of the Cauchy theorem, and it provides a useful representation for functions with specific analytic properties. Consider a function $f(s)$ that is real analytic in the domain below a cut, where the cut starts at a threshold $s_{\text{th}}$. The dispersion relation is given by:

$$
f(s) = \frac{1}{\pi} \int_{s_{\text{th}}}^{\infty} \frac{\operatorname{Im} f(s' + i0)}{s' - s} \, ds'
$$

Now, let’s apply a contour integration trick. Suppose we have a function $G(s)$ that is analytic everywhere except along a cut. We can write:

$$
G(s) = \frac{1}{2\pi i} \oint_C \frac{G(s_1)}{s_1 - s} \, ds_1
$$

Here, $C$ is a contour enclosing the singularity at $s$. By deforming the contour, we encounter two contributions: one from a large circle (which vanishes if $G(s)$ decays sufficiently at infinity) and another from the cut along the real axis.  

The key property we use is the behavior of $G(s)$ near the cut. For $s$ just above the cut ($s + i0$) and just below ($s - i0$), the function satisfies:

$$
G(s + i0) = G^*(s - i0)
$$

This means the real parts are equal, while the imaginary parts have opposite signs.  

::: callout-note
A simple example is $G(x) = \sqrt{1 - x}$, which has a cut starting at $x = 1$. For $x < 1$, the function is real, while for $x > 1$, it acquires an imaginary part.
:::
Let’s verify this for $x = 5$:

$$
G(5 + i0) = \sqrt{-4 - i0} = 2i
$$

This confirms the expected behavior: the real part is zero, and the imaginary part is positive above the cut. Below the cut (for $x = -8$):

$$
G(-8) = \sqrt{9} = 3
$$

This function is real analytic below the cut.  

Using these properties, we can rewrite the contour integral as:

$$
G(s) = \frac{1}{\pi} \int_{s_{\text{th}}}^{\infty} \frac{\operatorname{Im} G(s' + i0)}{s' - s} \, ds'
$$

The minus sign arises because the integral along one side of the cut cancels the integral along the other side, but with opposite directions.  

::: callout-important
If $G(s)$ drops fast enough as $|s| \to \infty$, the contribution from the large circle vanishes, leaving only the integral over the cut.
:::
This is the essence of the dispersion relation, which allows us to reconstruct the full function from its imaginary part along the cut.  

::: callout-tip
The dispersion relation is particularly useful in physics for recovering scattering amplitudes or other analytic functions from their discontinuities across cuts, which are often related to physical processes like particle production thresholds.
:::
The final formula we derived is:

$$
G(s) = \frac{1}{\pi} \int_{s_{\text{th}}}^{\infty} \frac{\operatorname{Im} G(s' + i0)}{s' - s} \, ds'
$$

This is a powerful tool for analyzing functions with known analytic properties and discontinuities.

<!--
Cosine simularity: 0.920522749324565
-->
## Understanding Subtraction in Dispersion Relations

This function allows us to recover the full function from its imaginary part. It tells us what the function is equal to here, and using this relation, we can determine it anywhere in the complex plane.  

This is an advanced subject in dispersion relations, but it's part of the coursework. It's a little exercise that helps you understand better how dispersion works. The key concept here is **subtraction**.  

When people say they perform this dispersion relation with one subtraction, it means two poles are introduced. The integral involves the variable $s'$, and the term $s - a$ appears outside the integral. This term vanishes when $s = a$, so to maintain the correct relation, we include $g(a)$ explicitly.  

This is called a **one-subtracted dispersion relation**. The simplest subtraction occurs at $a = 0$, giving:  

$$
g(s) = g(0) + \frac{s}{\pi} \int_{s_{\text{th}}}^{\infty} \frac{\operatorname{Im}g(s')}{s'(s'-s)} \, ds'
$$

Here, the extra $s$ in the denominator comes from the subtraction. This is necessary when the function does not decrease fast enough at infinity. In such cases, you must use a one-subtracted or even a twice-subtracted relation.  

For a twice-subtracted dispersion relation, the term $(s - a)$ is raised to the second power, modifying the integral further.  

::: callout-important
Subtractions are essential when the function's high-energy behavior does not satisfy the conditions for an unsubtracted dispersion relation. They allow us to still reconstruct the function using its imaginary part, even when it decays too slowly.
:::
This method is widely used in physics, particularly in scattering amplitude analysis, where discontinuities across cuts correspond to physical thresholds.

<!--
Cosine simularity: 0.8047423737876214
-->
$$
## R Ratio and Resonances in Experimental Measurements

The R ratio is defined as:

$$
R(s) = \frac{\sigma(e^{+}e^{-}\!\to\!\text{hadrons})}{\sigma_{0}(e^{+}e^{-}\!\to\!\mu^{+}\mu^{-})}
$$

The function is real up to the threshold, and this implies a specific relation. When the function is real in the vicinity and we approach the threshold, the imaginary part appears with opposite signs on either side of the cut. This is how analyticity introduces the imaginary part consistently from both sides of the cut.  

For example, consider the function $X$ where:  

$$
X - X = \int \frac{X}{5}
$$

The imaginary part of $\sqrt{X(1 - X)}$ can be evaluated explicitly, and we must also include the value at zero, which is one. This may seem surprising, but it works mathematically because we started with an analytic function.  

The imaginary part of the square root is hyperscaling, so we can express it as a real mathematical relation. Now, we relate the imaginary part of this block to the cross section through the optical theorem. The cross section is the observable, and it corresponds to the imaginary part.  

The R ratio's denominator is the theoretical cross section for $e^{+}e^{-}\!\to\!\mu^{+}\mu^{-}$, which is not directly measured in experiments but is very close to what we observe. The exercise sheet highlights the small differences between theory and experiment.  

The R ratio reveals all the resonances that can appear, such as the $\rho$, $\phi$, and $\Upsilon$. These resonances sit on a background of hadronic contributions, which include quark production and subsequent hadronization into multiple pions or other particles.  

::: callout-important
The R ratio is a key observable because it captures both resonant and non-resonant (background) contributions, providing a comprehensive view of the hadronic cross section in electron-positron collisions.
:::
The current status of the problem involves evaluating these contributions, including the challenges of modeling the hadronization process and its impact on the measured cross section.
$$

<!--
Cosine simularity: 0.9605728403376251
-->
## Introduction to Lecture Topics and Decay Analysis

We are finishing the lecture cycle, with two more lectures remaining. Today's lecture will focus more on physics, while next week will cover meta-issues and how the hadron community functions. I will provide background on research structure, collaborations, and how scientists operate in the hadron physics domain. Next week will have less physics, though I may spend the first 20 minutes reviewing recent discoveries and current experimental progress in the hadron physics community.  

Today, I will discuss how hadron physics is used outside its direct domain, particularly its role in other studies. I considered dedicating this lecture to either CP violation, where hadron physics plays a key role, or to the $g-2$ (muon magnetic moment) and its hadronic contributions. I decided to focus on the latter, as it connects to several topics we’ve already discussed.  

The exercise sheet will cover the $R$-ratio, which was originally planned for earlier lectures but was postponed. Now, we will revisit it at a more advanced level, incorporating additional problems and applying the knowledge we’ve gained.  

To begin today’s lecture, I will briefly recap a previous discussion on helicity and chirality, specifically examining the decay of the $\pi^+$ meson:  

$$
\begin{align}
\pi^{+} &\longrightarrow \mu^{+}\,\nu_{\mu}\,, \\
\pi^{+} &\longrightarrow e^{+}\,\nu_{e}\,.
\end{align}
$$

This comparison will help us transition into today’s topic.

<!--
Cosine simularity: 0.9310702380490139
-->
## Introduction to Lecture Topics and Decay Analysis

We will compare the decays involving a neutrino. Start by drawing the two-body decay in the thrust frame of the decaying particle, indicating momenta and chirality. The vertex here corresponds to a weak interaction, meaning the produced particles inherit chiral properties (left- or right-handed).  

Since chirality relates to spin orientation in the high-mass limit, the diagram will clearly display this property. From these chiral configurations, estimate the ratio of the matrix elements for the first and second cases. Consider which phase space is larger — the first or the second — and determine which decay is more probable for the particle $P$.  

Let’s discuss the first case: the decay $\pi^+ \to \mu^+ \nu_\mu$ compared to $\pi^+ \to e^+ \nu_e$. The weak interaction governs these processes, and chirality plays a key role in the matrix elements. The phase space difference arises due to the lepton masses, affecting the decay rates.  

$$
\begin{align}
\pi^{+} &\longrightarrow \mu^{+}\,\nu_{\mu}\,, \\
\pi^{+} &\longrightarrow e^{+}\,\nu_{e}\,.
\end{align}
$$

The heavier muon suppresses its phase space relative to the electron, making the electronic decay less likely despite the larger available energy. This is a direct consequence of the chiral structure in weak interactions.

<!--
Cosine simularity: 0.9138839040390401
-->
## Chirality and Spin Configurations in Pion Decay

Let's discuss the first point. The kinematics indicate chirality in the center-of-momentum decay frame. The neutrino is produced as a particle (not an antineutrino) because the electron comes with its antiparticle.  

The weak interaction vertex involves a $V - A$ structure, represented by $\gamma^\mu (1 - \gamma^5)$. This projects the quark current into left-handed (LH) and right-handed (RH) components. For example, a term like $\bar{u} \gamma^\mu (1 - \gamma^5) u$ ensures the quark is left-handed and the antiquark is right-handed.  

In pion decay, the $W$ boson vertex produces the final-state particles in their chiral configurations:  


- The positron ($e^+$) is right-handed.  


- The electron ($e^-$) would be left-handed.  


- The neutrino ($\nu_e$) is purely left-handed because it is massless.  

For a right-handed particle, the spin component aligned with momentum is dominant. For a left-handed particle, the opposite is true. In the center-of-momentum frame, the spins of the produced particles (e.g., $e^+$ and $\nu_e$) are both $1/2$, leading to a back-to-back configuration. The total spin sum must match the pion's spin ($0$), so certain spin configurations are forbidden or suppressed.  

The neutrino, being massless, has no right-handed component. However, the electron can have a suppressed right-handed component proportional to $m_e / E$. This suppression is stronger for the electron than for the muon due to their mass difference:  

$$
\frac{m_e}{E} \ll \frac{m_\mu}{E} \implies \frac{|\mathcal{M}_e|^2}{|\mathcal{M}_\mu|^2} \ll 1
$$

For the pion decay $\pi^+ \to \mu^+ \nu_\mu$, the muon is nearly non-relativistic because the pion mass is only slightly larger than the muon mass. Thus, the chirality suppression is less severe compared to the electronic decay $\pi^+ \to e^+ \nu_e$, where the electron is highly relativistic and the suppression is stronger.  

<!--
Cosine simularity: 0.9526626422103761
-->
## Phase Space and Energy Release in Pion Decay  

The expression for the phase space ratio in pion decay is:  

$$
\frac{\Phi(\,e^{+}\nu_{e})}{\Phi(\,\mu^{+}\nu_{\mu})} = \frac{s-m_{e}^{2}}{s-m_{\mu}^{2}} > 1
$$  

However, this ratio is not as strong as it might appear. The correct answer is that the ratio is significantly less than one. This explains why the pion decays predominantly to a muon and neutrino rather than an electron and neutrino.  

The phase space represents the number of kinematic configurations available in the decay. For two-body decays, it reduces to angular configurations, which are the same for both cases. But there is also an energy-dependent factor, which determines how much energy is released in the decay.  

The energy release is larger when the mass difference between the initial and final states is greater. For the pion decay:  


- The initial energy is given by the pion mass.  


- The final-state particles (e.g., $\mu^+ \nu_\mu$ or $e^+ \nu_e$) carry their own masses.  

In the case of $\pi^+ \to e^+ \nu_e$, the energy release is tiny because the electron mass is negligible, and most of the energy goes into kinetic energy. For $\pi^+ \to \mu^+ \nu_\mu$, the muon mass is much larger, so the energy release is smaller in comparison. This difference in phase space favors the muonic decay.

<!--
Cosine simularity: 0.9331498811376892
-->
## Parity Violation and Muon Polarization in Pion Decay  

Because the pion is massless (or nearly massless for the electron case), the phase space is much larger for the electron decay channel. However, this does not compensate for the suppression in the second case.  

For the phase space of the electron channel, we evaluate the breakup momentum and include an angle integral. The breakup momentum can be expressed in terms of the squared invariant mass $s$ and the particle masses. The challenge function is constructed as:  

$$
f(s, m_{e}) = s - m_{e}^2
$$  

For another channel, the function would be:  

$$
f(s, m_{\mu}) = s - m_{\mu}^2
$$  

The full expression involves terms like $x^2 + y^2 + z^2 - 2xy - 2yz - 2zx$, but when $b = 0$, certain terms drop out, leaving only the difference in energies. The final phase space ratio is:  

$$
\frac{\Phi(e^{+}\nu_{e})}{\Phi(\mu^{+}\nu_{\mu})} = \frac{s - m_{e}^2}{s - m_{\mu}^2}
$$  

This ratio does not compensate for the suppression, so the dominant decay of the pion is to a muon and neutrino.  

::: callout-important
The parity-violating nature of the weak interaction ( $V - A$ structure) is crucial here. The axial ( $A$ ) term violates parity, which is why the pion predominantly decays to a muon rather than an electron.
:::
Another key observation is that the muon produced in pion decay is polarized. Since the pion is spinless, the decay products (muon and neutrino) must conserve angular momentum. The neutrino is not directly detectable, but the muon's polarization can be inferred from its subsequent decay:  

$$
\mu^+ \to e^+ \nu_e \bar{\nu}_{\mu}
$$  

The muon is "self-analyzing" because the angular distribution of the emitted electron in the muon's rest frame reflects its polarization. If the muon is unpolarized, the electron emission is isotropic. However, if the muon is polarized, the electron preferentially aligns with the spin direction.  

::: callout-note
The 1967 experiment confirmed this polarization effect, providing direct evidence for parity violation in weak interactions.
:::
The $V - A$ structure of the weak interaction ensures that the muon decay vertex also violates parity. The angular distribution of the electron in the muon's rest frame is sensitive to the muon's polarization, making this a powerful experimental signature.  

In the helicity frame of the muon, if the muon is polarized, the electron is more likely to be emitted in the forward direction (aligned with the spin). This asymmetry is a direct consequence of parity violation.

<!--
Cosine simularity: 0.895631932257325
-->
## Magnetic Moment of the Muon and Quantum Corrections

The magnetic moment $\vec{\mu}$ of a particle is given by:

$$
\vec{\mu} = \frac{e}{2m}\,g\,\vec{S}
$$

Here, $g$ is the gyromagnetic factor, which is exactly 2 for a pointlike Dirac fermion. The spin $\vec{S}$ aligns with the magnetic moment.  

In the rest frame of the muon (the KTG frame), the spin information is preserved. The electron emitted in muon decay has a preferred direction due to angular momentum conservation, even for a linearly polarized beam.  

The magnetic moment describes the interaction of a particle with a magnetic field. For a pointlike fermion, it is determined by the Bohr magneton and the gyromagnetic factor $g$.  

::: callout-important
For the proton, $g \approx 2.8$, which deviates from the Dirac prediction of 2. This discrepancy indicates that the proton is not elementary but composed of quarks.
:::
In the quark model, the magnetic moment of the proton can be approximated using constituent quark masses (e.g., 0.3 GeV for up and down quarks) and their fractional charges. This model roughly reproduces the experimental value.  

For the muon, however, we assume it is an elementary particle with no internal structure, so we expect $g = 2$. However, quantum corrections from virtual processes modify this value.  

::: callout-note
The deviation from $g = 2$ is quantified by the anomalous magnetic moment $a$, defined as:
:::
$$
a = \frac{g - 2}{2}
$$  

This quantity is one of the most precisely measured values in particle physics. The corrections arise from higher-order processes in quantum field theory, such as loop diagrams involving virtual particles.  

The $g-2$ experiment for the muon provides a stringent test of the Standard Model, as any significant deviation could hint at new physics beyond it.  

The quark model successfully explains the proton's magnetic moment, but the muon's $g-2$ remains a key precision observable for theoretical predictions and experimental measurements.

<!--
Cosine simularity: 0.9046492833640776
-->
## Precision in Physics and Quantum Loop Effects

We define the anomalous magnetic moment $a_{\mu}$ as:

$$
a_{\mu} \equiv \frac{g-2}{2} = 0.001165\,8209(63)
$$

In physics, such precision is rare. There is a major effort to measure even more digits because this sensitivity allows us to probe quantum loop effects and potential new physics. These corrections arise from quantum processes, similar to the form factor discussed earlier.  

The quantity $g$ characterizes the interaction of a photon with the muon. By probing the muon with a photon source, $g$ reveals how the particle "sees" light. If the muon were composite, we could resolve its internal structure. However, in this case, we observe loop corrections to the vertex.

<!--
Cosine simularity: 0.9333390794665531
-->
## QED Perturbation Theory and Magnetic Moment Corrections  

In the case of muon vertex corrections, the function arises from processes like the one we drew. It was first calculated by Schwinger, who realized that such QED processes impact the magnetic moment.  

QED is a perturbative theory, and the series converges as you include more loops. Now we can start including morphologies like the three- or four-point crossings. All possible processes are calculated to a fixed order. For example, counting vertices here: 1, 2, gives the first-order correction.  

The charge of the electron and muon combine as $e^2 / (4\pi) = \alpha$, where $\alpha$ is the fine-structure constant. The electron mass squared comes from these vertices.  

We now know corrections up to the fifth order: $\alpha^2, \alpha^3, \alpha^4$, and so on. The $\alpha^5$ correction is a known value, though the exact number isn't provided here.  

$$
a_{\mu}^{\text{QED}} = \frac{\alpha}{2\pi}
$$  

This represents the leading-order contribution to the anomalous magnetic moment. Higher-order terms refine this prediction, demonstrating the precision achievable in QED calculations.

<!--
Cosine simularity: 0.8692114618932443
-->
## Numerical Techniques and Convergence in QED  

The value here is approximately $25\alpha$, though the exact number is not critical. The uncertainty is indicated by the last digits in parentheses. For comparison, the fourth-order term is around 130, suggesting the series is converging.  

We now have numerical techniques to evaluate these terms. The fine-structure constant $\alpha$ appears in higher-order corrections, such as $\alpha^4$ and $\alpha^5$, which refine predictions like the anomalous magnetic moment:

$$
a_{\mu}^{\text{QED}} = \frac{\alpha}{2\pi}
$$  

The convergence of the series is confirmed as higher-order terms are included.

<!--
Cosine simularity: 0.9127401590982637
-->
## Historical Context and Early QED Calculations  

The series is converging, and we now rely on numerical techniques. No one computes these diagrams by hand anymore, as Schwinger did. Instead, you set up the computer. For fifth-order calculations, there are likely millions of terms to evaluate, and all loop integrals are interrelated.  

::: callout-tip
The mass of the muon can often be neglected in these calculations, simplifying the process.
:::
The first-order calculations date back to the 1770s. Schwinger's foundational work introduced the fine-structure constant $\alpha$ with his famous result:  

$$
a_e = \frac{\alpha}{2\pi}
$$  

This was a pivotal contribution to quantum electrodynamics (QED). The techniques available at the time were limited, but Schwinger managed to calculate these diagrams manually.

<!--
Cosine simularity: 0.8791079157453252
-->
## Experimental Setup for Muon g-2 Measurement

The cyclotron frequency $\omega_c$ is given by:

$$
\omega_{c}=\frac{eB}{m\gamma}
$$

Here, $e$ is the muon charge, $B$ is the magnetic field, $m$ is the muon mass, and $\gamma$ is the Lorentz factor.  

The experimental setup involves pions decaying to muons, which then decay to electrons and neutrinos. This setup was proposed decades ago and is still used today. The muons are trapped in a ring with a magnetic field, causing them to travel in circular orbits due to the bending force. The ring has a radius of 20 meters, similar to the setup at Brookhaven National Lab (BNL).  

In the magnetic field, the muon spin precesses. The difference between the cyclotron frequency $\omega_c$ and the spin precession frequency $\omega_s$ is proportional to the anomalous magnetic moment $a_\mu$ (the "g-2" term). This relationship allows the experiment to measure the deviation from the Dirac value.  

The experiment begins with a proton beam hitting a target to produce pions. These pions are directed into a decay tunnel, where some decay into muons. The muons are then trapped in the storage ring. The precession of the muon spin is observed, and the tilt in the spin direction after one orbit is proportional to $a_\mu$.  

::: callout-note
The minus sign in the frequency equation should be double-checked, as $\gamma > 1$ could affect the sign convention.
:::
The key insight is that $\omega_c - \omega_s$ directly relates to the g-2 correction, making this setup a precise way to measure the muon's anomalous magnetic moment.

<!--
Cosine simularity: 0.9213939628714057
-->
## Muon Spin Precession and Electron Detection

The spin precession frequency is given by:

$$
\omega_{s}= \frac{g eB}{2m} +(1-\delta)\,\frac{eB}{m}
$$

Here, $g$ is the g-factor, $e$ is the muon charge, $B$ is the magnetic field, $m$ is the muon mass, and $\delta$ is a small correction term.  

Pions decay into muons, which are polarized and trapped in the ring. Since the pions produce muons with aligned spins, the initial configuration is already ideal for measurement. The muon spin precesses in the magnetic field as the muon moves along the circular path.  

The spin orientation is measured by detecting the decay electrons. Muons in the bunch (millions of particles) decay over time, and the resulting electrons are observed. The setup includes lead glass calorimeters inside the ring. These calorimeters are transparent blocks doped with lead to increase the material's atomic number ($Z$). When particles enter, they deposit all their energy, which is then collected by photosensors.  

The electron flux measured by the calorimeters indicates the spin direction: if the spin points outward, fewer electrons are detected.  

<!--
Cosine simularity: 0.9462576222173184
-->
## Muon Decay and Energy Deposit Fluctuations

The observable beat frequency is given by:

$$
\omega_{g}-\omega_{c}=a_{\mu}\,\frac{eB}{m}
$$

If the spin points outwards, there is a loss of electrons. If the spin points inwards, more electrons are detected. Along the circular path, fluctuations in the energy deposit are observed.  

In T-2 measurements, the digital flow shows time on the x-axis and a signal related to energy deposit. The frequency of rotation remains constant, as it is determined by the charge of the electron.  

Some muons in the batch decay over time, causing the overall deposited energy to decrease exponentially. This decrease is modulated by spin rotation fluctuations, creating an up-and-down pattern in the signal.  

<!--
Cosine simularity: 0.9171924527484556
-->
## Blinded Analysis and Frequency Measurement in G2 Experiment

The signal is modulated by spin rotation fluctuations, creating an up-and-down pattern.  
Data is collected over three years to accumulate sufficient statistics for the final measurement.  

The analysis is blinded: before processing the data, the analysts wrote the true frequency value on a piece of paper and sealed it in an envelope.  
During the press conference, the envelope was opened, the true frequency was entered, and the results were revealed by flipping the plot.  

The measurement focuses on the frequency $\omega_S$, which is related to the muon's anomalous magnetic moment $a_\mu$ through the equation:  

$$
\omega_S = a_\mu \frac{eB}{m}
$$

Here, $e$ is the muon charge, $B$ is the magnetic field, and $m$ is the muon mass.  

<!--
Cosine simularity: 0.9070881839103283
-->
## Muon Polarization and Magnetic Field Homogeneity in Precision Experiments

The measured quantity is $\omega_S$, but what actually enters the fit is a different variable related to the difference between $\omega_S$ and $\omega_C$. If the two frequencies were identical, the spin configurations would propagate identically, and no fluctuations would be observed.  

The key is to accumulate a large dataset to resolve the difference between $\omega_S$ and $\omega_C$. The muons are polarized when injected into the storage ring due to the weak interaction vertex in the production process, which enforces a specific chirality.  

The homogeneity of the magnetic field is the most critical factor in the experimental setup. Any inhomogeneity means the field is not exactly $B$ everywhere, causing variations in the integrated magnetic field experienced by the muons. This introduces uncertainty in the measurement.  

The precision required is extremely high, quantified in parts per billion (ppb). The next generation of this experiment is currently underway, aiming to further refine these measurements.  

<!--
Cosine simularity: 0.8723698779227103
-->
## Hadronic Contributions to Anomalous Magnetic Moment

The hadronic vacuum polarization (HVP) contribution to the anomalous magnetic moment is given by:

$$
\begin{equation}
a_{\text{HVP}}=\left(\frac{\alpha\,m_{\mu}}{3\pi}\right)^{2}
              \int_{s_{\text{th}}}^{\infty}\!
              \frac{ds'}{s'}\,K(s')\,R(s')
\end{equation}
$$

The current experimental precision for $a_\mu$ is 63 parts per billion (ppb), with the theoretical prediction also around 100 ppb.  

::: callout-important
Hadronic corrections are crucial for theoretical calculations of the anomalous magnetic moment, alongside QED and electroweak corrections.
:::
There are two prominent hadronic contributions:  


1. **Hadronic Vacuum Polarization (HVP)**: A photon produces hadrons, which then reconvert into a photon. This is a vacuum polarization effect.  


2. **Hadronic Light-by-Light (HLbL) Scattering**: Photons interact via intermediate hadronic states. The diagram involves photons entering and exiting a hadronic "blob."  

::: callout-note
Prominent contributors to HLbL include mesons like the $\pi^0$ and $\eta$, which decay into two photons.
:::
The hadrons involved must match the quantum numbers of the photon ( $J^{PC} = 1^{--}$ ). Identifying these hadronic states is essential for accurate calculations.  

The precision required for these measurements is extremely high, quantified in parts per billion (ppb). Future experiments aim to further refine these values.  

<!--
Cosine simularity: 0.9402933070339978
-->
## Quantum Numbers and Vector Mesons  

The photon has spin one ($J = 1$), parity ($P$) minus, and charge conjugation ($C$) minus, giving it the quantum numbers $J^{PC} = 1^{--}$.  

::: callout-important
Mesons with the same quantum numbers as the photon ($1^{--}$) are called **vector mesons**.
:::
In the $1S$ multiplet, there are two states: the lower one has $J^{PC} = 0^{-+}$ (pseudoscalar), and the higher one has $1^{--}$ (vector). Examples of vector mesons include:  


- **Light quark sector**: $\rho^0$ ($u\bar{u}$ or $d\bar{d}$), where the quark spins are aligned (e.g., up-up).  


- **Charm sector**: $J/\psi$ ($c\bar{c}$).  


- **Strange sector**: $\phi$ ($s\bar{s}$).  


- **Bottom sector**: $\Upsilon$ ($b\bar{b}$).  

The $K^*$ meson (e.g., $u\bar{s}$) is also a vector meson but has non-zero flavor quantum numbers, so it cannot be directly produced by a photon.  

::: callout-note
The photon can only produce neutral flavor states like $\rho^0$, $J/\psi$, $\phi$, and $\Upsilon$, as these match its quantum numbers.
:::
The vector mesons are crucial in processes like hadronic vacuum polarization, where a photon temporarily converts into a hadronic state (e.g., $\rho^0$) before reconverting back.  

The quark model predicts these states, and their masses follow an excitation pattern where higher energy levels (e.g., $1D$) also contain vector mesons.  

::: callout-tip
The $J/\psi$ and $\Upsilon$ are particularly important due to their narrow widths, making them ideal for precision studies in quantum chromodynamics (QCD).
:::
The photon's quantum numbers restrict the hadronic states it can produce, ensuring only $1^{--}$ mesons contribute in processes like $e^+e^- \to \text{hadrons}$.

<!--
Cosine simularity: 0.8731670269590024
-->
## Hadronic Vacuum Polarization and Unitarity  

The main particles contributing to hadronic vacuum polarization are flavor states, with more than 50% coming from the raw contribution. The calculation of these corrections is straightforward but cannot be done from first principles because hadronic physics is a "dirty business." Instead, we rely on experimental data and theoretical tools to relate processes.  

The photon's transition to hadrons and back is connected to the $e^+e^- \to \text{hadrons}$ cross section. This is due to unitarity, which links the quantum numbers of the initial ($e^+e^-$) and final (hadronic) states. Specifically, the quantum numbers match ($1^+$ for $e^+$ and $1^-$ for $e^-$), allowing us to relate the two processes.  

::: callout-important
The hadronic vacuum polarization component in QED is directly tied to the $e^+e^- \to \text{hadrons}$ cross section.
:::
We proceed with a mixed theoretical-experimental approach, using analyticity and unitarity to connect measurements of one process to another. For example, the photon's virtual hadronic intermediate states (like $\rho^0$) are constrained by the same quantum numbers ($J^{PC} = 1^{--}$) as the photon itself.  

::: callout-note
This method avoids first-principles calculations by leveraging empirical data, such as the measured $e^+e^-$ cross sections, to infer hadronic contributions.
:::
<!--
Cosine simularity: 0.9314782100718904
-->
## Threshold and Integration in Particle Production

Let's look at the expression for $e^+e^- \to \text{hadrons}$ once again. Here, $\alpha$ is the electromagnetic coupling constant, and $m_\mu$ is the mass of the muon. The key part is the integral and its denominator. The kernel $K$ is a mathematical function related to the spin of the particles, consisting of logarithms and rational functions. For scalar particles, $K$ would simplify to 1, and $R$ represents the experimental ratio.  

The integral starts at the threshold of the hadron production reaction. The idea is to "cut" the loop and identify which particles can be produced on-shell inside this block. The lowest threshold determines the integration limit.  

::: callout-important
The lowest threshold corresponds to the lightest possible on-shell particles that can be produced.
:::
Quarks cannot be on-shell, so the lightest particles are two pions ($2\pi$). Thus, the integration begins at the threshold for $2\pi$ production. These pions must satisfy the energy-momentum constraints of the reaction.  

<!--
Cosine simularity: 0.9107445937577817
-->
## Orbital Angular Momentum and Wave Combination  

These two pines must satisfy the energy-momentum constraints, meaning they carry non-trivial orbital angular momentum to have $\ell = 1$ ($\pm 1$ momentum).  

Consider the orbital angular momentum for $2\pi$ with $\ell = 1$. To achieve this, you would combine them in an S-wave. The S-wave combination gives:  

$$
1 + 0 + \pi^0 - 0 - 0 - 0 + \ldots
$$  

This arises from the superposition of the wavefunctions.

<!--
Cosine simularity: 0.8639034387911048
-->
## Cauchy Theorem and Analytic Functions

The expression:

$$
f(s)=\frac{1}{2\pi i}\oint\!\frac{f(s')}{s'-s}\,ds'
$$

represents an integral formula for an analytic function $f(s)$. Here, $s'$ is the integration variable, and the contour encloses the point $s$.  

When integrating from threshold to infinity with a $1/(s'-s)$ denominator, the construction becomes familiar. The Cauchy theorem states that in the complex plane, you can integrate within the domain of analyticity, and the integral equals the sum of $2\pi i$ multiplied by the residues of the function at its poles.  

This provides an integral representation of the function within its domain of analyticity. The function $f(s)$ here is a ratio with a single pole, so evaluating the residue at that pole gives the substitution $s' \to s$. This is the essence of the Cauchy theorem, and the formula above is a direct consequence of it.  

The integrand $f(s')/(s'-s)$ has a pole at $s' = s$, so the integral reduces to the residue of $f(s)$ at that point. This is how the integral representation is derived manually by introducing a pole to match the residue condition.  

::: callout-note
The Cauchy theorem allows representing analytic functions via contour integrals, leveraging their pole structure and residues.
:::
<!--
Cosine simularity: 0.8982182213092448
-->
## Dispersion Relation and Contour Integration

The dispersion relation is a consequence of the Cauchy theorem, and it provides a useful representation for certain functions. Consider a function $f(s)$ that is real analytic in the domain below a cut, with the cut starting at a threshold $s_{\text{th}}$. We can write:

$$
f(s) = \frac{1}{\pi} \int_{s_{\text{th}}}^{\infty} \frac{\operatorname{Im}f(s' + i0)}{s' - s} \, ds'
$$

Now, suppose we have a function $G(s)$ that is real analytic below the cut. We can represent it using contour integration:

$$
G(s) = \frac{1}{2\pi i} \oint_C \frac{G(s_1)}{s_1 - s} \, ds_1
$$

Here, $C$ is a contour enclosing the point $s$. By deforming the contour, we encounter singularities—primarily the pole at $s_1 = s$—and contributions from the cut. The integral splits into two parts: one from a large circular contour and another from the cut along the real axis.  

The key property we use is the behavior of $G(s)$ near the cut. For $s$ just above the cut ($s + i0$) and below ($s - i0$), the function satisfies:

$$
G(s + i0) = G^*(s - i0)
$$

This means the real parts are equal, and the imaginary parts differ by a sign. To illustrate, take the example of $G(x) = \sqrt{1 - x}$, which has a cut starting at $x = 1$. For $x < 1$, the function is real and analytic. For $x > 1$, we evaluate:

$$
G(x + i0) = \sqrt{-(x - 1) - i0} = i \sqrt{x - 1}
$$
$$
G(x - i0) = -i \sqrt{x - 1}
$$

This confirms the relation $G(s + i0) = G^*(s - i0)$.  

Using this, we can rewrite the contour integral. The contribution from the cut reduces to an integral over the discontinuity of $G(s)$ across the cut:

$$
G(s) = \frac{1}{2\pi i} \left( \int_{\text{cut}} \frac{G(s_1 + i0) - G(s_1 - i0)}{s_1 - s} \, ds_1 + \text{circle contribution} \right)
$$

The discontinuity is $2i \operatorname{Im} G(s_1 + i0)$, so:

$$
G(s) = \frac{1}{\pi} \int_{s_{\text{th}}}^{\infty} \frac{\operatorname{Im} G(s_1 + i0)}{s_1 - s} \, ds_1 + \text{circle term}
$$

If $G(s)$ decays sufficiently fast as $|s| \to \infty$, the circle contribution vanishes, leaving only the dispersion integral. This is the dispersion relation, which allows us to reconstruct the full function from its imaginary part.  

::: callout-note
The dispersion relation relies on real analyticity and the behavior of the function near its branch cut. It is a powerful tool for recovering a function from its discontinuity.
:::
<!--
Cosine simularity: 0.9308191098193925
-->
## Understanding Subtraction in Dispersion Relations

This function allows us to recover the full function from its imaginary part. It's quite amazing—it tells us what the function is equal to here, and using this relation, we can determine it anywhere in the complex plane.  

This is an advanced subject in dispersion relations, but it's part of the coursework. It's a little exercise that helps you understand better how dispersion works. The key concept here is **subtraction**.  

When people say they use the dispersion relation with one subtraction, it's not just one subtraction—two poles are introduced. The integral involves $s'$ (the integration variable), and $s - a$ appears outside the integral. This term vanishes when $s = a$, so to maintain the correct relation, we include $g(a)$ here. This is called the **one-subtracted dispersion relation**.  

The simplest subtraction occurs at $a = 0$. Then, the relation becomes:  

$$
g(s) = g(0) + \frac{s}{\pi} \int_{s_{\text{th}}}^{\infty} \frac{\operatorname{Im}g(s')}{s'(s' - s)} \, ds'
$$

This extra $s$ in the denominator is necessary when the function does not decrease fast enough at high energies. In such cases, you must use a one-subtracted or even a twice-subtracted relation. The twice-subtracted form involves raising $(s - a)$ to the second power.

<!--
Cosine simularity: 0.9056060129968065
-->
## Analyticity and Imaginary Parts in Function Behavior  

The twice-subtracted relation involves raising $(s - a)$ to the second power and incorporating it into the formulation. This works surprisingly well, even for functions like the square root of $x$.  

When discussing real analyticity, we mean the function is real for real inputs up to a certain threshold. This property implies specific relations for the function's behavior.  

A key observation is that when a function is real in a certain region, the imaginary part must appear consistently across a branch cut. Specifically, if the function is real on one side of the cut, the imaginary part will emerge with opposite signs on either side of the cut. This is a consequence of analyticity — the imaginary part cannot appear arbitrarily but must follow this symmetry.  

For example, consider a function that is real along the real axis. As we approach the branch cut, the imaginary part will manifest with a positive sign on one side and a negative sign on the other. This ensures the function remains analytic across the cut.  

The subtraction method in dispersion relations helps recover the full function from its imaginary part, maintaining consistency in the complex plane.  

$$
g(s) = g(0) + \frac{s}{\pi} \int_{s_{\text{th}}}^{\infty} \frac{\operatorname{Im}g(s')}{s'(s' - s)} \, ds'
$$  

This relation is essential when the function does not decay sufficiently at high energies, requiring one or even two subtractions to ensure convergence.

<!--
Cosine simularity: 0.9078912375335056
-->
## Analytic Functions and Dispersion Relations

The function minus $X$ is equal to the integral of $X$ over 5. The imaginary part of this expression corresponds to the imaginary part of $\sqrt{X_1 - X}$.  

We must also include the value at zero, which is non-trivial. This behavior arises because we started with an analytic function. By performing a contour integral, we can evaluate this explicitly. The imaginary part of the square root simplifies to a hypergeometric scale, yielding a real mathematical expression that may seem surprising but holds rigorously.  

Now, let's return to the main expression. We relate the imaginary part of this block (through the optical theorem) to the cross section. Observables are given by the cross section, which is the imaginary part. This imaginary part is placed in the numerator, and we perform a dispersive integral to obtain the contribution.  

This explains why we start at the threshold: the function is real below the threshold and only develops an imaginary part beyond it. The polarization is computed via dispersion relations and then linked to the cross section.  

$$
g(s) = g(0) + \frac{s}{\pi} \int_{s_{\text{th}}}^{\infty} \frac{\operatorname{Im}g(s')}{s'(s' - s)} \, ds'
$$  

This dispersion relation is crucial when the function does not decay sufficiently at high energies, requiring subtractions for convergence. The function's analyticity ensures that the imaginary part appears with opposite signs across the branch cut, preserving consistency in the complex plane.

<!--
Cosine simularity: 0.9000976203294188
-->
## R Ratio and Resonances in Experimental Measurements

The R ratio is defined with the denominator being the muon pair production cross section ($\mu^+\mu^-$) calculated theoretically. Although this is not an experimental measurement, it is very close to what is observed in experiments. The exercise sheet highlights minor differences between theory and experiment.  

The R ratio reveals all resonances that can appear. For example, the plot of experimental measurements shows contributions from resonances like the $\rho$, $\phi$, and $\Upsilon$, as well as a background from hadronic contributions. This background arises from quark production and subsequent hadronization into multi-pion states (not just single or double pions).  

The current theoretical calculations for this process align closely with experimental results, but the R ratio remains a powerful tool for studying resonance phenomena.  

$$
R = \frac{\sigma(e^+e^- \to \text{hadrons})}{\sigma(e^+e^- \to \mu^+\mu^-)}
$$  

The background in the R ratio reflects the non-resonant hadronic activity, which must be accounted for when interpreting the data. The resonances sit on top of this continuum, making the R ratio a rich observable for studying QCD dynamics.

<!--
Cosine simularity: 0.9269444622695683
-->
## Five Sigma Mismatch and New Physics Indications  

The current status of the problem is that there is about a five sigma mismatch between theoretical calculations and experimental measurements. This discrepancy has persisted for the last two to three years. Previously, the mismatch was more significant before some issues in the calculations were identified.  

This gap was initially interpreted as an indication of new physics. For example, if you calculate a value of 60 parts per billion in theory and measure 60 parts per billion experimentally, but then calculate 100 parts per billion using a different theoretical technique, the five sigma gap between these results becomes apparent.  

In later years, two works challenged this potential new physics discovery. The first was a lattice calculation on hadronic vacuum polarization.  

::: callout-note
A five sigma discrepancy is statistically significant and often warrants further investigation, as it may hint at physics beyond the Standard Model.
:::
Theoretical and experimental alignment is crucial, but persistent mismatches can lead to breakthroughs or revisions in understanding.

<!--
Cosine simularity: 0.854514629621105
-->
## Lattice vs. Phenomenological Calculations Discrepancy  

Lattice calculations evaluate hadronic vacuum polarization, but they only compute part of the quantity because they operate in the time domain rather than the space domain where $Q^2$ is defined. The two domains are interrelated, and lattice methods calculate the portion of this quantity that is theoretically accessible. However, they disagree with phenomenological calculations using dispersion relations, which raises questions about the technique.  

This discrepancy is not purely theoretical; it involves experimental input, such as the $R$-ratio, which has significant uncertainties. Currently, the disagreement is attributed to the region between $\rho$ and $\phi$ mesons, where experimental data are sparse.  

Recent lattice data show the discrepancy shrinking from 5$\sigma$ to 1.8$\sigma$. A publication from the CMD-3 experiment in Novosibirsk claims new measurements in the fine $\rho$ region are inconsistent with past experiments but align with theoretical predictions for the hadronic vacuum polarization contribution to $(g-2)_\mu$.

<!--
Cosine simularity: 0.9163258722036037
-->
## Experimental and Theoretical Efforts in Hydronic Physics

The experimental value of $G_{\text{master}}$ is consistent if you take their values. This indication for new physics is getting validated slowly, but it remains a significant puzzle. There is an experimental effort to build new facilities for measuring installations and improving precision.  

A large theoretical and terminological effort is underway to properly calculate hydronic effects. Hydronic physics remains the main obstacle in determining whether there is a mismatch.  

When fitting oscillations, a key question is whether you extract $W_C$ or the difference between them. Some papers provide expressions for vacuum polarization, but there seem to be typos, which need clarification.  

::: callout-note
HLBL (Hadronic Light-by-Light) and HVP (Hadronic Vacuum Polarization) are critical terms in this discussion.
:::
A question arises: Why can't we be sure the main contributions are hydronic? The issue is not their magnitude but their leading uncertainty. While they are small, their uncertainty remains too large to reduce further.  

$$
\text{Key issue: Uncertainty in hydronic contributions prevents further reduction.}
$$  

<!--
Cosine simularity: 0.8643772040247728
-->
## Challenges in Calculating H Parts and Contributions  

The H parts are the most difficult to calculate. The uncertainty has been reduced from 600 parts per billion (ppb) to 200 or even 100 ppb with new work, but this remains the main contribution. Other contributions are known much better than this one.  

::: callout-note
The leading uncertainty in hydronic contributions prevents further reduction, despite their small magnitude.
:::
$$
\text{Key challenge: } \Delta \text{(H parts)} \gg \Delta \text{(other contributions)}
$$  

<!--
Cosine simularity: 0.9250612572877351
-->
## Announcements and Event Reminders

Ilya is happy to receive your SSI sheets. Moritz, well done.  

There are two events this week:  


1. **Obstacle course this Thursday** — if the weather does not improve, we will cancel.  


2. **Project meeting on Friday at 2:00** — everyone is invited, even those not interested in projects. There will be sweets from Switzerland.  

The meeting location is at Line by Line Park.  

Regarding calculations, Light by Light has 64 terms, which introduces complexity.  

::: callout-note
The uncertainty in Light by Light contributions is smaller compared to other terms, but the calculation remains challenging due to the number of terms involved.
:::
<!--
Cosine simularity: 0.9403495670969056
-->
## Light-by-Light Scattering and Virtual Photons

The uncertainty in Light-by-Light scattering is smaller, but the calculation is still challenging due to the 64 terms involved.  

::: callout-note
Virtual photons are required for Light-by-Light scattering, not real photons that can be measured. The dependence on $Q^2$ (virtual photon momentum transfer squared) is particularly tricky.
:::
<!--
Cosine simularity: 0.92090446651588
-->
## Representation Theory and Young Tableaus  

The dependence on $Q^2$ is a tricky part. I was looking for a book explaining the representation theory of $SU(N)$. I read in a textbook how you get representations from Young tableaus using representations of $S_n$ (the symmetric group). It's very exciting, but it's hard to find a source for that.  

::: callout-note
Young tableaus provide a combinatorial way to construct irreducible representations of $SU(N)$ and $S_n$. The connection between the two is a key result in representation theory.
:::
I recall that $Z$ was mentioned as a possible reference, but I'm not sure what book that refers to.

<!--
Cosine simularity: 0.9306532924506196
-->
## Motivation for Studying Yugo

I went to Yugo because of the book reference "Z". The level is good, but I'm not sure what "Z" refers to. That's why I studied Yugo — to clarify this reference.  
