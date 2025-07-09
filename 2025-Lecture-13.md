### Hadronic Contributions to $g-2$: Vacuum Polarization and Light-by-Light


Let’s start with recording.

**What are the two terms in $g-2$ that receive hadronic contributions?**
The contributions are **vacuum polarization** and **light-by-light**.

- **Vacuum polarization**.
- **Light-by-light**.

---

**Can you draw the diagram for the vacuum polarization?**
For light-by-light?
*I think light-by-light.*

**What is the vacuum polarization diagram?**
*I would have to look it up.*
*I have a guess, but I'm not sure.*
**What's your guess?**

---

The solid lines represent the fermion.
**Which fermion is that?**
The fermion in this drawing is the **muon**.
The wavy line is the **photon**.

That diagram shows how the probe—the muon—interacts with the photon.
Here, something dresses the photon and changes the vertex.
This is the **hadronic vacuum polarization (HVP)**.

---

There is also another component—how it fits here.
HVP sits here.
Another contribution is **hadronic light-by-light (HLbL)**, where hadrons enter.

**If we expand further, where exactly in HLbL do hadrons enter?**
Precisely here.
It could be a loop of pions or kaons.
The particles that matter are those that couple to the photon.

---

In contrast, I don’t call it light-by-light if there’s a vertex with three photon legs.
Mesons that couple to photons contribute the most—like $\eta$ and $\eta'$.
All mesons with a strong two-photon coupling are relevant.

::: callout-important
**Key Formulas**:
The hadronic contributions to $g-2$ are decomposed as:
$$
a_\mu = a_\mu^{\text{QED}} + a_\mu^{\text{EW}} + a_\mu^{\text{HVP}} + a_\mu^{\text{HLbL}}
$$
For HVP:
$$
a_\mu^{\text{HVP}} = \left(\frac{\alpha}{\pi}\right)^2 \int_{m_\pi^2}^\infty \frac{ds}{s} K(s) R_{\text{had}}(s)
$$
For HLbL (simplified):
$$
a_\mu^{\text{HLbL}} \propto \sum_{M=\pi^0,\eta,\eta',...} \int d^4q_1 \, d^4q_2 \, \frac{\mathcal{F}_{M\gamma^*\gamma^*}(q_1^2,q_2^2)}{q_1^2 q_2^2 (q_1+q_2)^2}
$$
:::
---

This is important to realize: **hadron physics provides the input for precision physics**.
Hadronic contributions are critical for $g-2$, which must be calculated to **10 digits**, as shown last time.
Experiments measure this, but theoretical calculations rely on understanding these vertices—what happens inside these blocks.

These days, there’s less discussion about hadronic light-by-light.
The main uncertainty comes from **hadronic vacuum polarization**.

### Time Dependence in Euclidean Correlation Functions and Scattering in Quantum Mechanics with Pöschl-Teller Potential



Second question: What's the time dependence of the correlation functions computed on the lattice once we transform Minkowski space to Euclidean? The expectation between the vacuum and any operator $\mathcal{O}_I$ for the state that's not the vacuum as a function of $q$ has an exponentially falling dependence.

The time dependence in the Heisenberg representation—the time dependence of the operator—is given by the commutation with the Hamiltonian. We change to Euclidean space, and then the time dependence is given by the exponent:
$$
\langle 0 | \mathcal{O}_I(t) | n \rangle \sim e^{-E_n t}.
$$

::: callout-note
This exponential decay in Euclidean time is a key feature of correlation functions in lattice field theory, where $E_n$ represents the energy of the state $|n\rangle$.
:::
---


Today in the lecture, I plan to connect the scattering problem and quantum mechanics. It is the scattering theory that we have discussed during the course, and we will see how resonance phenomena and complex structure emerge in quantum mechanics. Then, we will connect this to the methods used in lattice field theory in a finite box to obtain useful results on the scattering properties of particles.

---


I'm going to start with the scattering problem in quantum mechanics on the basis of the wave functions. The main equation for scattering is the Hamiltonian operator acting on the wave function, giving an eigenvalue. The energy is the same wave function, and the Hamiltonian is the sum of two terms:
$$
H = -\frac{d^2}{dx^2} + V(x),
$$
where:

- The first term is the **kinetic energy** (mapping momentum to the derivative of the coordinate).
- The potential $V(x)$ is a function of the coordinate.

Most of the time in quantum mechanics, we operate in the coordinate space, and the potential in that case is a function of a single variable—the one-dimensional $x$-coordinate. For simplicity, let's drop all of the constants; at any moment, we can recover them from dimensionality. That's why there is no good reason to track them.

That's a differential equation that can be solved numerically. But there are several types of potentials for which there is a closed form for the solution in two dimensions later. I would like to look at one of them to gain insight.

---


Before that, let's discuss what the variables are here. The energy of the system is a fixed parameter in this differential equation. This is something that we have to probe, fix, and then solve. The way to investigate the system with a given potential goes as follows:

1. We fix the energy or the breakup momentum in the system because they are one-to-one related to each other.
2. By solving this equation and finding eigenvalues $P$, we can look at what wave functions satisfy this equation.

But we can also look at the system differently. The solution won't be present for certain values of $E$. You can consider this energy parameter as the parametric variable in this equation and ask: **for which energy values does the equation have a solution?** With that, we are going to realize what are possible regimes or possible values of the energy of the system.

---


I look at the different potentials that have a closed-form solution. One of them is the **Pöschl-Teller potential**:
$$
V(x) = -U_0 \text{sech}^2(\alpha x).
$$
It's nice when you have a closed form because then you can quickly visualize the code for this. The claim is that if you use this potential and do an algebraic change of variables, you can arrive at an analytic, almost analytic, closed-form expression for the wave function. The hyperbolic cotangent here is then related to the tangent. Everything is formulated in terms of hyperbolic functions, and the solution is given by the hypergeometric function.

Special functions are not a problem once someone implements them. For any programming language—Mathematica, Python, Julia—you can find implementations of the hypergeometric functions. So we can plot everything.

---


The physics is very interesting for this system. That potential has two parameters:

- The depth $U_0$
- The size $\alpha$ of the well

$\alpha$ controls how wide the well is, and $U_0$ is how deep it is. Depending on these two parameters, you can have many very nice physics phenomena.

In the scattering problem, the general features are the following. Let me also sketch next to this potential possible energies. The equation has solutions only for certain values of energies. Not every value would lead to a satisfactory wave function.

---


One of the conditions that makes certain energy values unacceptable is the **asymptotic condition**. We want our wave function to be finite—no exponential growth. The usual way we solve that is by saying $\psi$ has the term of the incoming wave and then the reflected term:
$$
\psi(x) \sim e^{ikx} + r e^{-ikx}.
$$

- The term with $+ikx$ is the plane wave going in the positive $x$-direction.
- The term with $-ikx$ goes in the negative direction.

That asymptotic form is a good approximation for the well.

For that potential, the way to solve is to look at the differential equation and recognize it as a type of special function. But what's important here is how the energy spectrum comes about. You take this equation, put it into the differential equation, and find the condition for certain $k$ so that the wave function doesn't grow exponentially at both infinities.

---


Why does the exponential appear in the first place? It appears when $iK$ is real, as soon as we consider energy below zero. Energy has to be looked at on the scale of $V$. Here is zero. The levels will be for the energy positive, and here is the level for the energy negative.

As soon as you look at negative energy, $K$ becomes imaginary, and $iK$ becomes real—one of the exponentials blows up. To avoid this asymptotically, we have to limit some terms. That gives the normalization condition for the wave function. We want this to be finite or oscillating.

You immediately relate this picture to the energy spectrum. Energy is the lines in the potential. As soon as my energy is above the asymptotic values of the potential, all energy values are allowed. That's called the **continuum of states**.

For energies below thresholds, the solution exists as **bound states**. These are bound states in the potential—something with exponential falloff. The wave function for the bound state will have peaks inside the well and exponentially suppressed tails outside.

The number of solutions inside the well is determined by an integer $N$. If the well is very deep ($U_0$ is high), $N$ can have many values (0, 1, 2, ...). As you make the well deeper, there are more states. There is a finite number because levels with energy much lower than the potential cannot exist.

If you make the well narrower ($\alpha$ increases), you can fit more states in it. The energy is related to the maximal energy, which is tied to the potential term:
$$
E_n = -U_0 + \left( \frac{\hbar^2 \alpha^2}{2m} \right) \left( n + \frac{1}{2} - \sqrt{\frac{2m U_0}{\hbar^2 \alpha^2} + \frac{1}{4}} \right)^2.
$$
Energy is always negative here and limited by $U_0$.

---


Now I want to look at this picture once again and then transform it to the way we have seen in the scattering theory. We used to write energy on the $x$-axis—the energy plane—where the continuum was represented by the cut, and bound states appeared as poles.

It's very instructive to map the scattering amplitude in scattering theory to the potential problem. That analytic structure is exactly the same for the transmission and reflection coefficients.

To make it accurate, we have to consider a different problem where we have a clear incoming wave, reflected wave, and transmitted wave. For example, with a potential step:

- On the left, an incoming wave $1 + e^{ikx} + r$.
- On the right, a transmitted wave $T$.

Here, $T$ is the transmission coefficient, and $R$ is the reflection coefficient, with $|T|^2 + |R|^2 = 1$.

When solving the scattering problem, that's the setup you would use. You could also reverse it—send the wave from the right. But for symmetric potentials, it's easier to use symmetric functions (cosine/sine).

The role of the scattering amplitudes is now played by these coefficients, which are functions of momentum and energy. We are dealing with the coordinate space $x$; $e^{ikx}$ is a plane wave, and the scattering amplitude is the coefficient in front that depends on energy.

We can ask: what is the analytic structure of our transmission coefficients in the complex plane? We are going to discover exactly that. In the region where there is a continuum, any value of the energy is possible—you have a branch cut. And then there are bound states that are trapped in the well.

::: callout-important
The analytic structure of scattering amplitudes—branch cuts for continuum states and poles for bound states—is a universal feature in quantum mechanics and quantum field theory. Understanding this helps connect lattice calculations to physical observables.
:::
### Scattering Phase Shifts, Virtual States, and Resonances in a Symmetric Potential Well


When we deal with the **symmetric potential**, instead of using that basis, we can switch to the **cosine and sine basis**. If we use $kx + \delta_0$, then we can use either one or another.
Let's stick to the **even wave functions** that have **positive parity**.

---

Now, I want to give you an intuitive understanding of $\delta_0$.
$\delta_0$ is a **scattering phase shift**. We will look for the solution with **positive energy**.

Here is our potential—that's the energy that's fixed. The wave function is given by:
$$
\psi(x) \sim \cos(kx + \delta_0).
$$
This satisfies the equations **outside the well asymptotically**.

---

Let's say the well is localized in the region of radius $R$.
Outside the well, where the potential saturates at zero, the equation:
$$
\psi'' + E \psi = 0
$$
has a solution given by $\cos(kx + \delta_0)$.

It's clear that this is a solution. If you take the second derivative, the $k^2$ comes out of the cosine, and you still have a cosine with a minus sign.
Since $k^2 = E$, you get exactly the terms.

---

::: callout-important
**Key Insight**: The phase shift $\delta_0$ doesn't spoil the solution—it's still a solution, and it reflects, asymptotically, the properties of the potential.
Despite the potential being localized, the functions at infinity feel the properties of the potential.
:::
That's the essence of **scattering theory**: you send a plane wave toward your potential from minus infinity, and then you check the properties of the wave on the other side asymptotically.
It comes out as a plane wave, but with a slightly different phase. This difference in phase reflects the properties of the potential.

---

Maybe this is also a good moment to think about what happens with these **poles** when we change the potential—that slider we had to move up and down the depth of the well.
What happens with these poles? Clearly, they move continuously with the depth of the potential.

- When we make the potential **shallower**, these poles move toward the threshold and then disappear there.
- But in fact, they don't disappear. They wrap around the branch point and appear on the other **analytic sheet**.
- The function, due to this branch cut, has several **Riemann sheets**.
- What they do is flip, go to the **non-physical sheet**, and become **virtual states**.

---

As soon as the potential is in a regime where it's finite but cannot yet host a bound state, there are only **virtual states**.
If the attraction is not strong enough, there are no bound states in the potential.
But still, the attraction could be felt by particles, and that indicates there are virtual states.
With a certain depth, there are one, two, and then even more states.

---

What are **resonances** then? Following this logic, resonances are phenomena where particles with low energy feel the attraction more strongly.
At certain energies, we want peaks in the amplitudes. This potential does not have any resonance phenomena.
But resonance phenomena could be seen if the probability to pass through the well increases for certain energies.

For low energy, the probability to pass or the reflection—let's think of the **reflection coefficient**—changes with the energy of the particle.
Resonance phenomena correspond to cases where, when you change the energy, the probability of reflection gets lower or higher and then returns to the same value.
If you have a strong dependence of the reflection probability on the frequency of the wave, you have a resonance phenomenon.

---

Now we are ready to put this problem into the box. Solving it in the box is also an **academic problem**.
I'm not sure this potential can be solved in closed form. But what changes is that you impose another condition.

A particle at the value $L$ has to be the same as the one on the other side, as well as the derivative:
$$
\psi(L) = \psi(-L) \quad \text{and} \quad \psi'(L) = \psi'(-L).
$$
These conditions are **strong** and change the phenomena dramatically.

### Finite-Volume Spectrum and Phase Shifts in Scattering Theory


The first condition does nothing.
The function is symmetric, so it is already the same on both sides of the lattice.

But the **second condition** is actually important.
We are still dealing with energies that are **positive**.
From this boundary condition, we realize that not every energy is possible—only those where $E = k^2$.

::: callout-note
The energy-momentum relation $E = k^2$ is a key constraint here, limiting the allowed energy states.
:::
---

Now, in the continuum, certain values are **forbidden**, and only a **discrete spectrum** appears.
Let me first draw it as a line.
I will still have a bound state below the threshold crossing, but now even above the threshold, I have a discrete spectrum.

You can see how this transition happens.
What effectively occurs is that our branch point and the cut starting from zero and extending to positive energies gets replaced by a set of **poles**.
Every allowed value of energy—if it's isolated—is a pole in the scattering amplitude.

A bizarre thing happens: we used to have a cut in the complex plane, and now it becomes an **infinite number of poles** along the real axis.

---

For a larger lattice, in the limit $L \to \infty$, we recover the **infinite box limit**.
In this limit, we resemble the infinite volume with a **continuous spectrum**.
Here, I indicate the distance between poles in the region that used to be continuous, and you see they are very close to each other.
The distance scales as $\Delta E \sim \frac{1}{L}$.

::: callout-important
The scaling $\Delta E \sim \frac{1}{L}$ shows how the discrete spectrum approaches continuity as $L$ grows.
:::
---

Another term in this formula I want to discuss is $\delta_0$.
That term, at infinity, remembers the properties of a potential with **infinite range**.
As you see, this term changes the spectrum—the discrete spectrum we now have in the continuum, or the region that was once continuous.

There is a **shift**, related to the exercise we did earlier.
We took our potential, made it flat by setting $U = 0$; the phase shift $\delta$ vanished, but $\delta_0$ was still present.
Then we pulled the potential down, and $\delta_0$ became significant.

What you observe is that the energy spectrum—both below and above the threshold—gets **adjusted and shifted**.
This shift is related to the properties of the potential.
That’s the **key idea** for our finite-volume scattering computations.

---

Here, we have a way to **numerically solve** the Schrödinger equation and examine the asymptotic values to find $\delta_0$.
We don’t always need to do this, but it’s critical when the potential is not analytically solvable.

If we perform a scattering experiment and only have access to the **asymptotic form** and energy spectrum, we can deduce the potential’s properties from the spectrum.
First, we check the allowed energies without interaction—a simple problem with the solution $E_n = \left( \frac{2\pi n}{L} \right)^2$.
Then, we numerically determine the energies with interaction.
By comparing these two cases, we can deduce $\delta_0$.

Note that $\delta_0$ **depends on energy**.
Here, you probe it with different values of $k$.

::: callout-note
The phase shift $\delta_0(k)$ is energy-dependent and connects the finite-volume spectrum to the infinite-volume scattering properties.
:::
### Connecting Quantum Scattering with Finite-Box Periodic Systems


So far, despite quantum mechanics being a **very well-taught course**, usually the connections with the material that comes after—**quantum field theory** and **particle physics**, or any other courses—are not that easy to grasp.
I think it's important to spell out and discuss all points that are shared and make a connection.

::: callout-note
The **periodic boundary conditions** simplify the problem by making the system translationally invariant—only the *relative distance* between particles matters, not their absolute positions.
:::
I have an intuitive picture of this scattering in my head. If you think of a finite box with periodic boundary conditions, it’s like having two marbles interacting with each other on a ring.
What plays the role of the lattice size is the full circumference of the ring. The variable $x$ is the distance between the two marbles.
If there is a potential $V(x)$ with which they interact, that's precisely the setup we have.

Periodic boundary conditions mean it doesn’t matter where they are—what matters is only the distance.

---


1. **Schrödinger equation** for this system with periodic boundary conditions:
$$
\left[ -\frac{\hbar^2}{2m} \nabla^2 + V(\mathbf{r}) \right] \psi(\mathbf{r}) = E \psi(\mathbf{r})
$$
where $V(\mathbf{r} + \mathbf{a}) = V(\mathbf{r})$ for lattice vector $\mathbf{a}$.

2. For a **short-range interaction** (like the "marbles" analogy), the potential can be modeled as:
$$
V(x) = V_0 \delta(x - x_0)
$$
where $\delta(x)$ is the **Dirac delta function**.

3. The **scattering amplitude** for two-particle interactions in a finite box:
$$
f(k, \theta) = \frac{1}{k} \sum_{\ell=0}^{\infty} (2\ell + 1) e^{i \delta_\ell} \sin \delta_\ell P_\ell (\cos \theta)
$$
where $\delta_\ell$ is the **phase shift** and $P_\ell$ are **Legendre polynomials**.

4. The **finite-volume quantization condition** (e.g., Lüscher’s formula for $\ell = 0$):
$$
\cot \delta_\ell(k) = \frac{n_\ell(kL/2\pi)}{\sqrt{(kL/2\pi)^2 - \ell(\ell+1)}}
$$
where $L$ is the box size.

---

The formulas above tie directly to the **intuitive analogy** of marbles on a ring, bridging conceptual understanding with mathematical rigor.

::: callout-tip
When working with periodic boundary conditions, always check for **translational symmetry**—it often simplifies calculations!
:::
---

Let me know if you'd like further refinements or clarifications!

### Extracting Meson and Baryon Spectra from Lattice Correlation Functions


The last thing I would like to do is to properly connect this to what is actually computed on the lattice.
At the bottom, the first thing one introduces is the quantity and the **main computation**.

::: callout-note
The fundamental quantity computed in lattice QCD is the **correlation function** between operators, which contains all the spectral information of the theory.
:::
The only thing that the lattice computes is the correlation of operators.
This is the vacuum expectation value of the product of two operators:

$$
C_{ij}(t) = \langle 0 | \mathcal{O}_i(t) \mathcal{O}_j^\dagger(0) | 0 \rangle
$$

Here, $i$ is the index that labels the operator.
Say we have 5 of them, or 1, or 2, or 3, or 4.
We compute the $5 \times 5$ matrix of the correlation coefficients as a function of time.

---

The **spectral decomposition** of this correlation function is:

$$
C_{ij}(t) = \sum_{n} \frac{\langle 0 | \mathcal{O}_i | n \rangle \langle n | \mathcal{O}_j^\dagger | 0 \rangle}{2E_n} e^{-E_n t}
$$

It is a combination of exponential functions with coefficients.

---

To get the meson spectrum, you would take $\mathcal{O}$ as the combination of the quark and antiquark fields:

$$
\mathcal{O}_M(x) = \bar{q}(x) \Gamma q(x)
$$

where $\Gamma$ represents **Dirac matrices** that determine the meson's quantum numbers.

* You take this operator and compute its correlation as a function of time
* Then extract $E$, which gives you the energy of the system—all possible energies of the meson system
* These are the ground states—the mesons

---

**Practical example:**
Do this exercise: take $U \bar{U}$, run this correlation on the lattice, and the lowest energy that appears will be the mass of the pion.

---

An important aspect to realize is that:

* The higher the energy, the faster the state's contribution dies
* If you wait long enough, all higher states' contributions exponentially drop, leaving only the ground state:

$$
\lim_{t \to \infty} C_{ij}(t) \approx \frac{\langle 0 | \mathcal{O}_i | 0 \rangle \langle 0 | \mathcal{O}_j^\dagger | 0 \rangle}{2E_0} e^{-E_0 t}
$$

In the meson case, this works well. In the baryon case, it's a problem.

---

There is more information stored in these correlations if your operator basis is larger.
Consider the **generalized eigenvalue problem**:

$$
C(t) \vec{v}_n(t, t_0) = \lambda_n(t, t_0) C(t_0) \vec{v}_n(t, t_0)
$$

This technique:

* Extracts exponentials of the higher states
* For every value of $t$, you can find an eigenvalue
* The diagonal elements of the diagonalized correlation matrix give the time dependence of those higher states
* This optimizes the overlap of different operators to isolate excited states

### Lattice QCD Spectroscopy: Extracting Meson Spectra and Resonances via Finite-Volume Phase Shifts


The **eigenvalue problem** and that technique are quite different. There is a class of algorithms that makes calculations less noisy related to what we use. For this operator that contracts mesons, the operators we input have different **condition numbers**.

If you want to calculate the spectrum of the light spin-1 mesons, the operators have quantum numbers of $0^+$, and you obtain one spectrum. For other quantum numbers, you need different operators.

::: callout-note
The Hamiltonian diagonalization for the meson spectrum is given by:
$$
H|\psi_n\rangle = E_n|\psi_n\rangle
$$
:::
What actually happens—without going into details—is that in a finite volume, **spin is no longer a good quantum number** because you lack full rotational symmetry. The lattice has a reduced symmetry group, not $SU(2)$, so different spins mix.

In practice, the entire meson spectrum is computed simultaneously. The matrix has a large dimensionality—hundreds of sectors with overlapping non-diagonal elements between different spins. This yields many **eigenenergy values** (eigenvalues), which are mapped and presented as meson masses.

---

There is one problem with this approach. Most resonances above decay thresholds are not bound states but **resonances**. Excited mesons like the $\rho$ meson and higher states are resonances in $\pi$-$\pi$ scattering.

Strictly speaking, extracting eigenvalues above the two-pion threshold is not reliable. Below the threshold, you measure the pion mass accurately. Above it, you observe two-pion states rather than stable mesons. These extracted values are not trustworthy, so another method is needed to study resonances, such as those in $\pi$-$\pi$ scattering.

Instead of using two core capacitors, four coil capacitors represent meson-meson combinations. The energy spectrum of these combinations is rich and resembles what we see in a finite box.

---

When two particles are confined in a box, their energy spectrum is discrete above the threshold. The spacing between levels is roughly $2\pi/L$. The deviation of these discrete states from the non-interacting case gives the **phase shift** $\delta(k)$. This is how the phase shift is extracted.

A classic example is $\pi$-$\pi$ scattering in the $P$-wave. The extracted phase shift shows a resonant behavior, peaking at the $\rho$ meson mass. For physical quark masses, the pion mass is $140 \text{ MeV}$, and the $\rho$ meson resonance occurs at $770 \text{ MeV}$, where the phase shift passes $\pi/2$.

::: callout-important
The **energy shift** between interacting and non-interacting systems is key:
$$
\Delta E_n = E_n^{\text{interacting}} - E_n^{\text{free}}
$$
This connects to Lüscher's formula for phase shifts:
$$
\tan\delta(k) = \frac{\pi^{3/2} q}{\mathcal{Z}_{00}(1;q^2)}, \quad q = \frac{kL}{2\pi}
$$
:::
---

This is how modern hadron spectroscopy works on the lattice. The method is accurate if all relevant channels are included. The steps are:

1. Construct a large basis of operators with different quantum numbers.
2. Extract eigenvalues to get the energy spectrum of the interacting system.
3. Compare it to the non-interacting spectrum.
4. The difference $\Delta E_n = E_n^{\text{interacting}} - E_n^{\text{free}}$ gives the phase shift $\delta(k)$.

Plotting $\delta(k)$ versus the breakup momentum reveals resonances. Experienced theorists can spot resonances just from the spectrum.

From first principles—the **QCD Lagrangian**—we obtain scattering spectra and resonance properties. Complications arise from coupled channels. Above thresholds like $2\pi$ or $3\pi$, additional operators ($K\pi$, $\eta'$, etc.) must be included.

The key idea is using the energy shift between interacting and non-interacting systems. This connects to experimental particle physics, where phase shifts and cross-sections are analyzed similarly.

---

Further analysis involves parameterizing phase shifts, extracting pole positions, and couplings—the final results shared in the PDG. The **K-matrix formalism** is often used for coupled-channel cases:
$$
K = \tan\delta \quad \text{or} \quad T = \frac{K}{1-iK}.
$$

Lüscher’s formula links finite-volume energy shifts to infinite-volume phase shifts:
$$
\tan\delta(k) = \frac{\pi^{3/2} q}{\mathcal{Z}_{00}(1;q^2)}, \quad q = \frac{kL}{2\pi},
$$
where $\mathcal{Z}_{00}$ is the Lüscher zeta function.

This machinery bridges lattice calculations and experimental resonance physics.
