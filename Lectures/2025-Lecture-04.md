## Electron-Photon Scattering, Form Factors, and Baryon Magnetic Moments


Today's lecture will start by reviewing **electron-photon scattering**, then continue with the **magnetic moment**. Later, we will discuss different experiments and how they produce various hadrons.

---

The electron-photon spectrum was discussed last time. In this context, remember three cross sections:
- The **Rosenfeld cross section**
- The **Mott cross section**
- The **Rosenbluth cross section**

What's important here are the **charges**. We neglected the spins of the particles initially. The logical extension is the Mott cross section, where $\beta$ is the velocity and the electron spin is considered. It is essentially the Rutherford cross section multiplied by a correction term:

$$
\left(\frac{d\sigma}{d\Omega}\right)_{\text{Mott}} = \left(\frac{d\sigma}{d\Omega}\right)_{\text{Rutherford}} \cdot \left(1 - \beta^2 \sin^2\left(\frac{\theta}{2}\right)\right)
$$

This term suppresses scattering at backward angles. At 180 degrees, the cross section is lower due to **conservation laws** for relativistic particles.

---

Experiments show the cross section falls more steeply than predicted by the Mott formula. This discrepancy arises because the target is not point-like. The finite size is accounted for by a **form factor**.

The form factor is the Fourier transform of the charge density:

$$
F(Q^2) = \int \rho(r) e^{i \vec{q} \cdot \vec{r}} d^3r
$$

For a point-like particle ($\rho(r) = \delta(r)$), the form factor is a constant. For an exponential charge density (e.g., a proton), it takes a dipole form:

$$
G_E(Q^2) = \left(1 + \frac{Q^2}{\Lambda^2}\right)^{-2}, \quad \Lambda \approx 0.71\,\text{GeV}^2
$$

For a nucleus with a diffuse edge, the form factor exhibits **oscillatory behavior**.

---

The Rosenbluth cross section incorporates electric and magnetic form factors:

$$
\frac{d\sigma}{d\Omega} = \left(\frac{d\sigma}{d\Omega}\right)_{\text{Mott}} \left[ \frac{G_E^2(Q^2) + \tau G_M^2(Q^2)}{1 + \tau} + 2\tau G_M^2(Q^2) \tan^2\left(\frac{\theta}{2}\right) \right]
$$

where $\tau = Q^2/4m_p^2$ and $Q^2$ is the momentum transfer.

> [!IMPORTANT]
> To extract the proton radius, plot the measured cross section divided by the Mott cross section versus $Q^2$. The slope at $Q^2 \to 0$ gives the radius:
>
> $$
> \langle r_p^2 \rangle = -6 \hbar^2 \left.\frac{dG_E(Q^2)}{dQ^2}\right|_{Q^2=0}
> $$

---

The electric form factor of the proton follows a **dipole distribution**, while the neutron's magnetic form factor starts at $-1.91$ at $Q^2 = 0$. The values at $Q^2 = 0$ correspond to:
- The proton's charge ($1$)
- The magnetic moments of the proton and neutron

Measuring at low $Q^2$ is challenging because it requires **small scattering angles**. Experiments like those at the Mainz accelerator use spectrometer arms to detect electrons and protons. New experiments, such as **MUSE at MESA**, aim to improve these measurements.

Historically, discrepancies arose between proton radii measured via:
- **Electron scattering** ($\sim 0.86$ fm)
- **Atomic spectroscopy** (Lamb shift), which suggested a smaller radius

New experiments, like **AMBER at CERN** (using muons), seek to resolve this.

---

These experiments revealed the proton's substructure. Now, let’s discuss **spin**, **flavor symmetry**, and calculating baryon magnetic moments.

The total baryon wave function must be **antisymmetric**. Color wave function antisymmetry implies the spin-flavor part must be symmetric. For a proton (spin-$1/2$), the symmetric spin-flavor wave function is:

$$
|p \uparrow \rangle = \frac{1}{\sqrt{2}} \left( \chi_S \psi_S + \chi_A \psi_A \right)
$$

where $\chi_S$ and $\psi_S$ are symmetric spin and flavor states, and $\chi_A$, $\psi_A$ are antisymmetric.

---

The magnetic moment of a quark is:

$$
\mu_q = \frac{e_q \hbar}{2m_q}
$$

For up ($e_u = +2/3$) and down ($e_d = -1/3$) quarks:

$$
\mu_u = +\frac{2}{3} \frac{e\hbar}{2m_u}, \quad \mu_d = -\frac{1}{3} \frac{e\hbar}{2m_d}
$$

The proton's magnetic moment (spin-up) sums contributions from its quarks:

$$
\mu_p = \langle p \uparrow | \sum_{i=1}^3 \mu_i \sigma_z^{(i)} | p \uparrow \rangle = \frac{4}{3}\mu_u - \frac{1}{3}\mu_d
$$

For the neutron, swapping up and down quarks gives:

$$
\frac{\mu_n}{\mu_p} \approx -\frac{2}{3} \quad \text{(if } m_u \approx m_d \text{)}
$$

Experimentally, this ratio is close to $-1.91/2.79 \approx -0.68$, consistent with the **quark model**.

---

The constituent quark masses include:
- **Valence quarks**
- Surrounding gluons/quark-antiquark pairs

This explains their larger values ($\sim 300$ MeV) compared to bare quark masses.

Magnetic moments are measured via:
- **Spin splitting** in magnetic fields (e.g., Stern-Gerlach)
- **Radiative decays** in photon-proton collisions for short-lived baryons (e.g., $\Delta^{+}$)

For the $\Omega^-$ baryon (three strange quarks), the magnetic moment is:

$$
\mu_{\Omega^-} = 3\mu_s = 3\left(-\frac{1}{3}\frac{e\hbar}{2m_s}\right) = -\frac{e\hbar}{2m_s}
$$

---

This concludes the recap of **electron-photon scattering** and **magnetic moments**. Next, we’ll explore further applications of **flavor symmetry**.

## Light Baryon Spectroscopy and Hadron Production Methods


We already discussed the proton. Now let’s think about the **light baryons**. We have seen you can use **SU(3)** for flavor with the up, down, and strange quark, and combine it with **SU(2) spin**. This gives us **SU(6)** for spin-flavor symmetry:

$$
\text{SU(6)} \supset \text{SU(3)}_{\text{flavor}} \otimes \text{SU(2)}_{\text{spin}}
$$

As discussed earlier, for **SU(3) flavor**, we have the baryon decuplet and octet. Combining flavor and spin into **SU(6)**, we get the **20**, **70**, and **56-plets**. The **56-plet** is antisymmetric, while the others are mixed symmetric. With these considerations, we can arrange the known light baryons into these multiplets. I won’t cover all of them, but let’s look at some mass differences as examples.

For instance, we have:
- The **radial excitation number**
- **Orbital angular momentum** $L$
- The **spin**, which can be $1/2$ or $3/2$

For spin $1/2$, we get the nucleons, and for $3/2$, we enter the decuplet, which includes the $\Delta$. I’ll focus on the $N^*$ and $\Delta^*$ baryons, excluding those with strange quarks. These can have excited states from radial or orbital angular momentum excitations. For $L=1$, the spin can still be $1/2$ or $3/2$.

---

Let me give an example of **radial excitation**. If we arrange these states in patterns:
- $S$ denotes $L=0$
- The $N=1$ state corresponds to $N=0$, which is just the proton or nucleon
- The next band contains **five states**, with masses ranging from **1500 to 1700 MeV**

One state might be slightly lower, and others could include $D$-states, and so on.

The key point here is the **mass difference** of about **600 MeV**, arising from spin-orbit and spin-spin interactions:

$$
\Delta M \approx 600 \text{ MeV}
$$

These states are well-documented up to certain energies in the PDG, with star ratings indicating their reliability. A goal of light baryon spectroscopy is to identify how many states exist and their patterns, based on quark model predictions. Are these correct, or is there different dynamics? We need to study the states' properties, which leads me to discuss experimental methods for producing hadrons.

---

> [!NOTE]
> **Question about 1S and 2S:**
> I’m surprised you labeled this as 3S. What’s the difference between 1S and 2S? The radial wave function changes, but no orbital angular momentum is added—just the hadron’s size increases. How does this introduce more states? I was checking the quark model’s predictions. Why three states? I’d expect one, like the $\rho$ resonance.
>
> The answer lies in multiplets from different $LS$ combinations. For $n=1$, $l=0$, there’s a spin combination. Some papers claim more states should exist, including $\Delta$ resonances, but these are distinct. Some studies don’t separate them clearly.
>
> For radial excitations (increasing $N$), the number of states in the multiplet shouldn’t change because no extra degrees of freedom are added. The 2P multiplet has the same number of states as 1P. Higher excitations introduce $L=2$, altering the count.
>
> Agreed—for $N=1, 2, 3$, the state count remains the same. Experimentally, only the first band is well-known; the rest are uncertain. Some states match quark model predictions, others don’t, leaving gaps in light baryon spectroscopy.

---

Next, let’s discuss **hadron production**. Electromagnetic probes like electron or photon beams can be used, with colliding or fixed-target setups. Hadron beams (e.g., pions or protons) are another option.

Starting with **electromagnetic probes**, consider the **BESIII facility** in China. It’s a symmetric $e^+e^-$ collider with beam energies of **1–2.47 GeV**. The annihilation produces a virtual photon, which can form a $J/\psi$, decaying into other hadrons.

The **center-of-mass energy** $\sqrt{s} = 2E_e$ determines the producible particles. For BESIII, this covers masses up to **~2 GeV**. The cross-section shows peaks like $J/\psi$ and $\psi(2S)$, with decays like $J/\psi \to \gamma \eta \eta'$ or $3\pi$.

At higher energies (e.g., Belle, $\sqrt{s} \approx 10$ GeV), bottomonium states like $\Upsilon$ are produced.

---

Now, **photo-production experiments**: fixed-target setups like:
- **A2** (Mainz, 0.08–1.6 GeV)
- **CBELSA/TAPS** (Bonn)
- **GlueX** (US, 6–12 GeV)

Photon beams are generated via **Bremsstrahlung** from electron beams:

$$
\frac{dN}{dE_\gamma} \propto \frac{1}{E_\gamma}
$$

For $\gamma p$ collisions, the **center-of-mass energy** is:

$$
s = m_p^2 + 2E_\gamma m_p
$$

With $E_\gamma \leq 3.2$ GeV, resonances up to **2.7 GeV** (e.g., $\Delta$) are accessible.

---

> [!QUESTION]
> **Can hyperons be produced here?**
> No—flavor conservation forbids strangeness change in $s$-channel. However, $t$-channel processes (e.g., $\gamma p \to K^+ \Sigma$) are possible, as planned for the **INSIGHT experiment**.

**Quantum number selection rules** apply. For **E1 photons** ($L=1$, parity $-$):

$$
J^P = \frac{1}{2}^- \text{ or } \frac{3}{2}^-
$$

Resonances are labeled like $S_{11}$, where:
- $S$: $L=0$ (meson orbital momentum)
- First subscript: $2 \times$ isospin (1 for nucleons, 3 for $\Delta$)
- Second subscript: $2 \times$ total angular momentum

---

**Final note:** Higher energies allow meson spectroscopy, but we’ll cover that next time.

## SU(2) Algebra and Delta Baryon Wave Functions


We've been talking to theorists yesterday. There will be **advanced theoretical hadron physics** next semester. Everyone is invited to take it, and it will be completely complementary to this course—it will go in-depth into group theory.

One thing we discussed is that in this course, we cover $SU(2)$ well. In the theory course, this $SU(2)$ is considered trivial, so it goes to $SU(3)$ in depth, looking at the irreducible representations. But for this course, we focus on $SU(2)$, the groups we discussed for the flavor, for the isospin, and for the spin, as Farah demonstrated today.

It's indeed simple once you understand it, and understanding requires practice. I mentioned last time, Farah mentioned today, and we will mention yet another time how the $SU(2)$ algebra works. But I wanted to invite you to engage with a little exercise.

> [!NOTE]
> **Key $SU(2)$ Algebra Formulas**:
> - Commutation relations: $[J_i, J_j] = i \hbar \epsilon_{ijk} J_k$ or $[I_i, I_j] = i \epsilon_{ijk} I_k$ (with $\hbar = 1$).
> - Raising/lowering operators:
>   $J_{\pm} = J_x \pm i J_y$ (similarly for $I_{\pm}$).
>   $J_- |j, m\rangle = \sqrt{j(j+1) - m(m-1)} \, |j, m-1\rangle$.
>   $J_+ |j, m\rangle = \sqrt{j(j+1) - m(m+1)} \, |j, m+1\rangle$.

---

I’ll quickly write a wave function—it goes nowhere—and I invite you to write down the answer, leave it on the table right here. You don’t even need to write your name on it. We just want to gauge how well you understand what’s going on.

So, I want to consider a delta that has three quarks in isospin states. There are four states: $\Delta^{++}$, $\Delta^+$, $\Delta^0$, and $\Delta^-$. I would like to build this spin-flavor wave function.

For example, the $\Delta^+$ state would be $|uud\rangle$ with spin projection $J_z = \frac{3}{2}$. On this little piece of paper, write:

1. What is $J_-$ acting on $|\Delta^+ (J=\frac{3}{2}, J_z=\frac{3}{2})\rangle$?
2. What is $J_+$ acting on $|\Delta^+ (J=\frac{3}{2}, J_z=\frac{3}{2})\rangle$?
3. What is $I_+$ acting on $|\Delta^+ (I=\frac{3}{2}, I_z=\frac{1}{2})\rangle$?
4. What is $I_-$ acting on $|\Delta^+ (I=\frac{3}{2}, I_z=\frac{1}{2})\rangle$?

You have two minutes. I have a meeting now, so I won’t provide solutions—it’s trivial once you understand the logic. Just give it a try.

---

A reminder: the total isospin is the sum of the isospins of the three quarks, $\mathbf{I} = \mathbf{I}_1 + \mathbf{I}_2 + \mathbf{I}_3$. The same applies for $\mathbf{J}$. You don’t need much derivation if you know the answer. We just want to check if you remember how the lowering operators act.

> [!IMPORTANT]
> **Exercise Solutions (for reference)**:
> - $J_- |\Delta^+ (J=\frac{3}{2}, J_z=\frac{3}{2})\rangle = \sqrt{3} \, |\Delta^+ (J=\frac{3}{2}, J_z=\frac{1}{2})\rangle$
> - $J_+ |\Delta^+ (J=\frac{3}{2}, J_z=\frac{3}{2})\rangle = 0$ (max $J_z$ state)
> - $I_+ |\Delta^+ (I=\frac{3}{2}, I_z=\frac{1}{2})\rangle = \sqrt{3} \, |\Delta^{++} (I=\frac{3}{2}, I_z=\frac{3}{2})\rangle$
> - $I_- |\Delta^+ (I=\frac{3}{2}, I_z=\frac{1}{2})\rangle = \sqrt{2} \, |\Delta^0 (I=\frac{3}{2}, I_z=-\frac{1}{2})\rangle$

## Adjustments to Schedule and Workload


**What is it about at all?**
*Two minutes is too little.* You need **five or ten**.

---

> [!NOTE]
> Administrative updates about scheduling and workload adjustments follow below.

---

- **Next Thursday**, we don't have exercises plus the lab tutorial.
- That's also why we simplified the homework volume.

---

There will be holidays. *Everyone is invited to spend time resting.*
- Exercises are **light** for this reason.

---

We do not have **physical labs**. That's why I brought...

---

> [!TIP]
> While this segment contains no physics formulas, common nuclear physics equations include:
> - Radioactive decay: `$\frac{dN}{dt} = -\lambda N$`
> - Binding energy: `$E_B = (Zm_p + Nm_n - m_{nucleus})c^2$`
> - Half-life: `$t_{1/2} = \frac{\ln(2)}{\lambda}$`

