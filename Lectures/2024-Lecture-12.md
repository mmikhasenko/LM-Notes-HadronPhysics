### Pion Decay Dynamics, Chirality Suppression, and the Muon Magnetic Moment


We are finishing the lecture cycle. Two more to go. Today is the month before last. However, content-wise, today will be more on physics, and next week I would like to discuss meta-issues and how the hadron community functions. I will give you a little bit of background on how research is structured in the field, how collaborations work, and what scientists actually do in the hadron physics domain. There will be less on physics next time. Perhaps I will spend the first 20 minutes reviewing recent discoveries, what experiments have brought up, and what the hadron community is currently working on.

---

But today I would like to talk more about physics and still have to write formulas and discuss how particle physics is used outside of particle physics, how it is an important part of many other studies. I considered dedicating one lecture to **CP violation**, where particle physics plays a key role. Another subject I was considering is the **muon magnetic moment** and its hadronic contributions. That’s what we will discuss. I decided on this fundamental topic because it touches on several subjects we’ve already covered. The exercise sheet is on the **R ratio**, something we postponed earlier. Now we enhance it with more problems and discuss it at a more advanced level.

---

> [!NOTE]
> Key formulas discussed in this lecture:
> - Weak interaction vertex: $\mathcal{L}_{\text{weak}} \propto \bar{\psi}\gamma^\mu (1 - \gamma_5)\psi$
> - Pion decay amplitude suppression: $\mathcal{M} \propto m_\ell / E_\ell$
> - Muon magnetic moment: $\vec{\mu} = g \left( \frac{e}{2m} \right) \vec{S}$

---

I would like to start today's lecture with a short recap. Let’s revisit our discussion of **helicity and chirality** and examine pion decay: $\pi^+ \to \mu^+ \nu_\mu$. I would like you to compare this decay. Start by drawing this two-body decay in the rest frame of the pion, indicating momenta and chirality. The vertex is a weak interaction, so the produced particles have definite chiral properties—left or right. On this diagram, chirality is related to spin orientation in the high-mass limit. Given these chiral configurations, what are the ratios of the matrix elements? Which phase space is bigger? And which decay is more likely for the pion? Let’s take three minutes.

---

Let’s discuss the first question. Who found this obvious? No one? That’s fine—we have something to discuss. Draw the center-of-momentum decay kinematics and indicate chirality. Note: it’s a neutrino, not an antineutrino, because the electron comes with an antineutrino. The weak interaction vertex has a **$V-A$ structure**, $\gamma^\mu (1 - \gamma_5)$, which projects the quark current to left-handedness. Here, the vertex produces a left-handed positron and a left-handed neutrino.

For the right-handed positron, the left-handed component is suppressed by its mass. The neutrino is massless, so it’s purely left-handed. For the right-handed particle, the spin aligned with momentum dominates. For the left-handed particle, it’s the opposite. Both particles have spin $\frac{1}{2}$, and their spins add to one, which is incompatible with the pion’s spin-zero nature. Other configurations are possible, but flipping the spin of the right-handed particle is suppressed by $\frac{m}{E}$. The neutrino, being massless, has no opposite component, but the positron does. The $v_R^+$ component is suppressed by $\frac{m}{E}$.

---

This leads to the second question: The matrix elements for the electron and muon are suppressed differently because their masses differ. The lighter the particle, the stronger the suppression—for the electron, it’s severe, but for the muon, especially since the pion mass is close to the muon mass, the chirality suppression is less pronounced. The correct answer is that the ratio is much less than one, explaining why the pion decays predominantly to muons, not electrons.

For phase space, the number of angular configurations is the same, but the energy release differs. The bigger the energy release, the larger the phase space. For the muon, most of the pion mass goes into kinetic energy because the neutrino is massless and the electron nearly so. The phase space is larger for the muon, but this doesn’t compensate for the suppression. The phase space integral is $\frac{s - m_e^2}{s - m_\mu^2}$, but this doesn’t change the conclusion.

---

The dominant decay of the pion is $\pi^+ \to \mu^+ \nu_\mu$. This is **important physics**—it’s how parity violation was discovered. The muon is produced polarized because the pion has no spin, and the neutrino escapes undetected. The muon’s polarization can be measured because its decay $\mu^+ \to e^+ \nu_e \bar{\nu}_\mu$ is self-analyzing. The electron’s angular distribution reveals the muon’s polarization. If the muon is polarized, the electron prefers to align with the spin direction. This setup was used in 1967 to confirm parity violation.

---

Later, the same technique measured the muon’s magnetic moment. Recall from the second lecture that the magnetic moment of a particle describes its interaction with a magnetic field. For a point-like fermion, it’s given by:

$$
\vec{\mu} = g \left( \frac{e}{2m} \right) \vec{S}, \quad \text{where} \quad g \approx 2
$$

For the proton, we found $g \approx 2.8$, indicating it’s composite. But the muon is elementary, so we expect $g = 2$. However, quantum corrections make $g$ slightly larger. The deviation is quantified by $a_\mu = \frac{g - 2}{2}$, one of the most precisely known numbers in physics.

---

The leading QED correction, calculated by Schwinger, is:

$$
a_\mu = \frac{\alpha}{2\pi}
$$

Higher-order terms ($\alpha^2, \alpha^3$, etc.) have been computed up to $\alpha^5$. Modern calculations use computers due to the complexity. The experimental setup involves trapping muons in a magnetic field ring. The muon’s spin precesses at $\omega_s = \omega_c (1 + a_\mu \gamma)$, where $\omega_c$ is the cyclotron frequency. The difference $\omega_s - \omega_c$ isolates $a_\mu$, allowing precise measurements. This technique, pioneered decades ago, remains critical for testing QED and probing new physics.

### Proton Beam to Muon Spin Precession: Measuring Anomalous Magnetic Moment


The experiment is as follows.
You start with the **proton beam**—that's a hydrogen beam, the easiest beam we can get.
You hit the target and you get a bunch of pions flying forward.
You collect the pions and direct them towards your ring.

---

Here is the tunnel through which the pions from the secondary vertex come.
In this tunnel, they decay.
Some of the pions convert to muons, and the muons are trapped.
In the ring, they start moving.

> [!NOTE]
> The muon's anomalous magnetic moment ($a_\mu$) is central to this experiment:
> $$
> a_\mu = \frac{g_\mu - 2}{2}
> $$
> where $g_\mu$ is the g-factor of the muon.

---

Since pions produce **polarized muons**, they already have exactly the configuration we want.
There is a muon, and there is a spin.
By applying a magnetic field, this setup starts working.
The muon moves along the circle, and the spin begins precessing.

---

We measure the spin orientation by looking at the decay electrons.
Muons go along the circle and decay.
There are millions of particles in the bunch, and as they move, some muons decay.

---

Inside the circle, there are **calorimeters**—lead glass calorimeters, as I checked this morning.
It's a big block, a typical setup used in experiments like COMPASS.
Lead glass is a material doped with lead to increase its atomic number ($Z$).
When a particle enters, it deposits all its energy inside.
Because it's glass, it's transparent to light.
You place this heavy block of glass with a photosensor at the end.
A particle comes in, leaves energy, and the sensor collects it.

---

These calorimeters measure the flux of electrons.
- If the spin points **outwards**, you detect fewer electrons.
- If the spin points **inwards**, you detect more electrons.
Along the circle, you see fluctuations in the energy deposit.

---

In **g-2 measurements**, the plot shows time on the x-axis and energy deposit—or something similar.
People cut this piece and start over.

The frequency of rotation stays the same.
To be precise, the frequency doesn’t change.
It is determined by the charge of the muon and the magnetic field.

---

Out of the muons in the batch, some decay.
The overall energy deposited decreases exponentially as:
$$
N(t) = N_0 e^{-t/\tau_\mu}
$$
where $\tau_\mu$ is the muon lifetime.

This decay is modulated by the spin precession, fluctuating up and down.
The signal follows:
$$
S(t) = N_0 e^{-t/\tau_\mu} [1 + A \cos(\omega_a t + \phi)]
$$
where $\omega_a$ is the **anomalous precession frequency**.

---

You collect these statistics for three years, and then you have the number.

The analysis is **blinded**.
Two years ago, there was a big press release for the new g-2 measurements.
Before starting, the analysts wrote the real frequency on a piece of paper in an envelope.
At the press conference, they unblinded the analysis.
They opened the envelope, entered the frequency, and revealed the measured numbers.

---

> [!IMPORTANT]
> The relationship between the anomalous magnetic moment and precession frequency is:
> $$
> a_\mu = \frac{\omega_a}{\omega_c} = \frac{\omega_a m_\mu}{eB}
> $$
> This is the key equation for extracting $a_\mu$ from the measured $\omega_a$.

### Muon Polarization, Anomalous Magnetic Moment, and Hadronic Contributions in \(g-2\) Experiments


You're measuring $\omega_S$—it's actually correct. What enters the field is really this variable.

These fluctuations—are they related to $\omega_C$ or not? As far as you explained, you would measure $\omega_S$ and plot as many data points as possible.

If the two velocities were exactly the same, the spin configurations would propagate identically, so nothing would change. Therefore, up and down fluctuations—no, this is $\omega_C$.

The key point is that it's a ratio, a difference that enters. This plot is sensitive to the difference, but I don't see it now.

For some reason, I thought you saw a difference between them, but no. I'm not sure.

---

> [!NOTE]
> **Key Physics Context**:
> The discussion involves precision measurements of spin dynamics, where $\omega_S$ and $\omega_C$ represent frequencies related to spin and cyclotron motion, respectively. The difference between these frequencies is critical for observing effects like the anomalous magnetic moment ($g-2$).

---

The key question is: Are the other muons polarized when you shoot them into the ring? Does it matter? Muons? Yes, when they come up. Exactly.

In the vector boson binding case, this vertex is a weak interaction vertex, and it produces a certain chirality of the state. Muons are always polarized in the binding case. That's really neat.

This spectacular experiment—the next generation is happening now. The most important concern in the setup is the homogeneity of the field. If the field is not exactly $B$ but slightly different, the integral over the magnetic field that the muon acquires while traveling changes, introducing uncertainty.

To achieve such precision—quantified in parts per billion (**ppb**)—is remarkable. Currently, the uncertainty is **63 ppb** in the experimental value, and the theoretical value is around **100 ppb**.

---

You might ask, *"What does hadronic physics have to do with this?"* Hadronic corrections appear prominently in the theoretical calculation of the anomalous magnetic moment $g-2$.

There are **two major hadronic contributions** to $g-2$:
1. **Hadronic Vacuum Polarization (HVP)**:
- A photon produces hadrons and then turns back into a photon.
- This is *running vacuum polarization*.

2. **Hadronic Light-by-Light (HLbL) Scattering**:
- Light interacts with hadrons and re-emits light.
- Mesons like $\pi^0$ and $\eta$ (which decay into two photons) contribute to HLbL.

---

The photon has quantum numbers $J^{PC} = 1^{--}$. Which mesons share these quantum numbers?

- **Spin one** means **vector mesons**. Examples include:
- $\rho^0$ ($u\bar{u}$)
- $\phi$ ($s\bar{s}$)
- $J/\psi$ ($c\bar{c}$)
- $\Upsilon$ ($b\bar{b}$)

In the quark model, these mesons belong to the same multiplet. For instance, replacing the $u$-quark with a $c$-quark gives $J/\psi$.

In the strange sector, the vector meson is $\phi$ ($s\bar{s}$).

### Dispersion Relations and Analyticity in Complex Analysis


The **Cauchy theorem** tells you that in the complex plane you can integrate in the manner of analyticity. The integral is equal to the integral of the function over \( S' \). This \( S' \) is equal to the sum of the \( 2\pi i \) residues of the function at the poles. Does it look familiar? We discussed this already—that you can use this to have an integral representation of the function for any function in the domain of its analyticity.

You can write this in the following way, and what you do, actually, is manually introduce a pole by hand such that this integral would be equal. In this integral, it will be equal to the residue of the integrand. This function \( F \) that is here is this ratio; it has one pole. Therefore, you have to take the function right at the pole, and that would make you substitute \( S \) for \( S' \), and then it would make the derivation valid. This is known as the **Cauchy theorem**, and this is kind of a little consequence of it.

---

Now, there is a **trick**, especially for real analytic functions. Imagine that you have a function that is real analytic in the domain below the cut, and then the cut starts at that threshold. We would like to use something like that to evaluate the value. So what I'm going to do is write this representation for this contour: my function \( G(S) \) is equal to \( \frac{1}{2\pi i} \) integral over contour \( C \) of \( \frac{G(S_1)}{S_1 - S} dS_1 \). This is my contour \( C \).

> [!IMPORTANT]
> **Key Property of Real Analytic Functions** (cut discontinuity):
> \[
> G(S + i\epsilon) = G^*(S - i\epsilon) \quad \text{(for real } S \text{ below threshold)}
> \]
> implying \( \text{Re}\, G(S + i\epsilon) = \text{Re}\, G(S - i\epsilon) \) and \( \text{Im}\, G(S + i\epsilon) = -\text{Im}\, G(S - i\epsilon) \).

I'm going to blow up the contour. Changing the contour does not change anything. The only singularity that I encounter is the one introduced by hand—it's a pole in the center or somewhere inside of it. So I'm transforming my plane into the following contour. It has two contributions: the one that comes from the circle and the one from the cut. The one from the cut is actually evaluated along the real axis.

I'm going to use the property that \( G(S + i\epsilon) \) (with \( \epsilon \) infinitesimal) is related to \( G(S - i\epsilon) \). This is due to the **real analyticity**. It's rather intuitively clear, but not necessarily so.

---

Let's consider an example just on the side. Any function with such a cut will be real analytic. We had an exercise on that. I want to have an \( x \) domain, and then the function has a cut starting at one, going to the right, and the function should be real here. My favorite example is \( \sqrt{1 - x} \). But \( \sqrt{x} \) could have a cut in the other direction. So I think I should do \( \sqrt{1 - x} \).

This function has a cut to the right; it starts at 1. If I put \( x = 0 \), I can evaluate this, no problem. It's real analytic because for negative \( x \), say \( x = -8 \), then I have \( \sqrt{9} = 3 \).

My claim is that \( G(x + i0) \) has a real and imaginary part. If I calculate this for negative, it has the same real part and negative imaginary part. Let's check it for some value. At \( x = 5 \), \( G(5 + i0) = \sqrt{-4 - i0} = 2i \). Indeed, it's a real analytic function. The value above and below the cut has the same real part and opposite imaginary parts.

That lets me write this integral as a principal value integral over the imaginary part. Plus, another thing I use is that the integral in one direction is equal to minus the integral in the other direction. That's what gave me the minus sign here.

---

If the function drops fast enough when \( S \) goes to infinity, I can blow up my circle even more and drop the contribution from the circle. I forgot a \( 2i \) here—so here in the numerator should be \( 2i \). This is a beautiful formula that we derived, known as a **dispersion relation**.

> [!NOTE]
> **Dispersion Relation** (recovering a function from its imaginary part):
> \[
> G(S) = \frac{1}{\pi} \int_{\text{cut}} \frac{\text{Im}\, G(S')}{S' - S} \, dS'
> \]
> (Assumes \( G \) vanishes sufficiently fast at infinity.)

This function allows us to recover the full function from its imaginary part. It's quite amazing. It just tells you what the function is equal to here, and using this relation, I can give it to you anywhere in the complex plane.

It's an advanced subject, the dispersion relation, but it's part of the classwork. It's a little exercise that helps you understand better how dispersion works.

---

There is also the **subtraction**. People say we do this dispersion relation with one subtraction. It's not just one, but two poles are introduced. Then it's under the integral with the prime. This is the variable I integrate over, and then \( S - a \). Once you do that, you have to multiply this without the prime outside the integral. Then obviously this term is going to vanish once \( S = a \). Therefore, to have the correct relation, you need \( G(a) \) here.

This is called a **once-subtracted dispersion relation**. The easiest subtraction is at zero. Then \( a = 0 \), and you have just \( G(S) = G(0) + \frac{S}{\pi} \) (and then an extra \( S \) for the integration). That's what you have to do when your condition for the high circle is not met—when your function does not decrease fast enough. You can still use this dispersion relation; you just have to do one subtraction or two subtractions.

The twice-subtracted version would be putting this to power two and then having it as well. Quite amazing—I can't believe it works.

---

Just look here. I can use this formulation for my \( \sqrt{1 - x} \) function.

> [!NOTE]
> **Example with \(\sqrt{1-x}\)** (applied dispersion relation):
> \[
> \sqrt{1 - x} = 1 + \frac{x}{\pi} \int_{1}^{\infty} \frac{\text{Im}\, \sqrt{1 - x'}}{x'(x' - x)} \, dx'
> \]
> where \( \text{Im}\, \sqrt{1 - x'} \) is non-zero only for \( x' > 1 \).

(Maybe just a technical question: By real analyticity, you mean that the function is real for real inputs up to the threshold?)

Exactly. And this implies the relation.

So I think we can also understand this in a way that suddenly—where is my drawing?—suddenly my function was real, and then an imaginary part appeared. The fact that it's real in the vicinity when I go towards it means that the imaginary part will appear on one side with one sign and on the other side with the opposite sign. So that's how to understand it.

The cut can only—analyticity can only introduce an imaginary part consistently from both sides of the cut, given that it was real here. Right? Would you believe that?

So \( \sqrt{1 - x} \) is equal to the integral of \( \frac{\text{Im}\sqrt{1 - x'}}{\pi(x' - x)} \). And then I have to add here the value at zero, which is 1. Quite nontrivial—like, would you believe that if you just saw it? But mathematically, it works.

This is because we started with an analytic function. So this is analytic. We do the circle integral, we use... This can be evaluated explicitly. I could actually tell you what this imaginary part of the square root is—it's just a Heaviside step function. So we could just have a real expression.

Mathematically surprising, but it works.

### Dispersion Relations, Cross Sections, and the R Ratio in Hadronic Processes


Now we come back to the expression in the last minutes, and I'll wrap up this sketch of how it works.
We relate the imaginary part of this block, through the **optical theorem**, to the cross section:

$$
\sigma \propto \text{Im}\,\mathcal{M}
$$

The observable is given by the cross section. The cross section is the imaginary part.

You put the imaginary part in the numerator, perform the **dispersion integral**, and we obtain this contribution.
It should now make more sense why we start at the threshold and why we extend to this global function.

---

The polarization is an **analytic function** and only has the right-hand cut. It is real and smooth before the threshold.
Once we cross the threshold, it develops a **branch cut**.
We compute this polarization using the dispersion relation:

$$
\Pi(q^2) = \frac{1}{\pi} \int_{s_{\text{threshold}}}^\infty \frac{\text{Im}\,\Pi(s)}{s - q^2 - i\epsilon} ds
$$

and relate it to the cross section.

---

The quantity $R$ is defined as:

$$
R(s) = \frac{\sigma(e^+e^- \to \text{hadrons})}{\sigma(e^+e^- \to \mu^+\mu^-)}
$$

The denominator is the $\mu^+\mu^-$ cross section calculated theoretically.

> [!NOTE]
> The $R$ ratio compares hadronic production to muon pair production in $e^+e^-$ collisions, serving as a probe for QCD dynamics and resonances.

This is not directly from experimental measurements, but the $R$ ratio we use here is consistent with experimental data.
The theoretical calculations for this process are very close to what is measured in experiments.
The exercise sheet provides the minor differences that arise.

---

The $R$ ratio reveals all the resonances that can appear.
Here is a plot showing the experimental measurement of $R$. It is quite spectacular, as expected.
It includes contributions from resonances like the $\rho$, $\phi$, and $\Upsilon$.

There is also a **background contribution**. All resonances sit on top of this background.
The background comes from hadronic contributions—quarks that hadronize not just into single pions or two pions, but into many particles.

---

The current status of the problem is a **five-sigma mismatch** between theoretical calculations and experimental measurements.
This discrepancy has persisted for the past two to three years.

Earlier, there were issues with QED calculations, but those were resolved.
Now, the gap suggests potential **new physics**.

Theoretical predictions reach a precision of **60 parts per billion**, while experimental measurements also achieve **60 parts per billion**.
Yet, when comparing independent theoretical methods, a five-sigma discrepancy remains:

$$
\Delta a_\mu = a_\mu^{\text{exp}} - a_\mu^{\text{theory}} \approx (251 \pm 59) \times 10^{-11}
$$

### Challenges in Hadronic Contributions and the Weakening New Physics Signal


In later years, two works threatened this new physics discovery.
The first is the **lattice calculation** on hadronic vacuum polarization.
The lattice actually computes this quantity, but only part of it, because they work in different domains.
They don’t work in the space domain with $Q^2$, but in the **time domain**.
They interrelate the two and calculate the part of this quantity that’s also possible to evaluate theoretically.
And they disagree.

> [!IMPORTANT]
> **Key Formula**: The Hadronic Vacuum Polarization (HVP) contribution to muon $g-2$ is given by:
> $$
> a_\mu^{\text{HVP}} = \left(\frac{\alpha}{\pi}\right)^2 \int_{m_\pi^2}^\infty \frac{ds}{s} K(s) R(s)
> $$
> where $K(s)$ is a kernel function and $R(s)$ is the hadronic $R$-ratio from $e^+e^- \to \text{hadrons}$.

Lattice disagrees with **phenomenological calculations** using perturbative methods, which calls part of this technique into question.
This isn’t purely theoretical—there’s experimental input, specifically the $R$-ratio, which has uncertainties.
These uncertainties are still large, and they dominate the error.
Currently, the blame falls on the region between the $\rho$ and $\phi$ resonances, where experimental data is poor.
This mismatch between lattice and experiment likely comes from there.

If you take the new lattice data, the discrepancy shrinks from $5\sigma$ to $1.8\sigma$.
Later last year, the **CMD experiment** in Novosibirsk published new measurements of this region, specifically around the $\rho$ resonance.
They claim these measurements are inconsistent with past experiments but consistent with the experimental value of $g-2$ if their values are used.

This indication for new physics is weakening slowly, but it remains a puzzle.
There’s an experimental effort to build new facilities for more precise measurements.
Theoretically, there’s a major effort to properly calculate **hadronic effects**.
Hadronic physics remains the main obstacle in determining whether there’s a true mismatch.

---

I think we’re done. Questions? We have time.
One thing I’d like to clarify: When fitting these oscillations, do you extract $W_C$ or the difference between them?
I’ve seen papers with expressions for vacuum polarization that seem to have typos, so I’ll check with colleagues.
But roughly, now you have a basic idea—when you hear **HLBL** or **HVP**, you’ll know what they mean.

**Question:** Why can’t we be sure the main contributions are hadronic? Even if we evaluate them correctly, other contributions might just be smaller.
**Answer:** That’s a good point. I misspoke earlier—it’s not that they’re the largest contributions, but they have the leading *uncertainty*.
They’re small, but we don’t know them precisely enough to reduce the uncertainty further.
The hadronic parts are the most difficult to calculate.

The uncertainty was **600 ppb** (parts per billion), but new work has reduced it to 200 or even 100 ppb.
Still, it remains the dominant source of uncertainty—we know other contributions much better.

> [!NOTE]
> **Light-by-light (HLBL)** scattering involves 64 terms and is even more challenging due to virtual photons:
> $$
> a_\mu^{\text{HLBL}} \propto \int d^4q_1 \, d^4q_2 \, \mathcal{K}(q_1, q_2) \Pi^{\mu\nu\rho\sigma}(q_1, q_2)
> $$
> where $\Pi^{\mu\nu\rho\sigma}$ is the hadronic light-by-light scattering amplitude.

**Logistics:**
- **Thursday**: Obstacle course (canceled if weather doesn’t improve).
- **Friday at 2:00**: Project meeting (everyone invited, Swiss sweets provided).

See you at Linde Park.

### Seeking Sources on SU(N) Representation Theory via Young Tableaux


I was wondering—maybe a question for a problem of mine. Maybe you can answer it.

I'm currently looking for a book explaining the **representation theory of SU(N)**. I read in a textbook how you get representations from **Young tableaux** using representations of $S_n$. Very exciting.

> [!NOTE]
> The connection between SU(N) representations and symmetric groups $S_n$ via Young tableaux involves several key formulas:
> - Dimension of SU(N) reps: $\text{dim}(λ) = \prod_{1 ≤ i < j ≤ N} \frac{λ_i - λ_j + j - i}{j - i}$
> - Hook length formula for $S_n$: $\text{dim}(λ) = \frac{n!}{\prod_{(i,j) ∈ λ} h_{i,j}}$
> - Branching rules and tensor products follow Littlewood-Richardson coefficients.

And it's impossible to find a source for that. Z? That's a book? What do you mean, Z? That's why I went to [Yugo?].

This is rather **good level**.

