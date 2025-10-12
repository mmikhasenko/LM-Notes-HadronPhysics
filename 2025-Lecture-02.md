---
title: (2025) Lecture 2
author: ''
presenter: Farah Afzal
note_taker: Anna Zimmer
date: '2025'
format: html
---

**Presenter**: {{< meta presenter >}}

**Note Taker**: {{< meta note_taker >}}

### Classification of Hadrons and the Role of Isospin


**Welcome everyone to today's lecture.**
We will mostly discuss the **classification of hadrons**.
I will walk you through the history of how important discoveries were made, what we learned from them about hadrons, and how we can group them together.

---

In the **50s and 60s**, there were a lot of new big accelerators built, like the **Bevatron**.

- It came into operation in **1954**.
- It was a proton accelerator with energies of up to **13 GeV**.

These high-energy protons were shot at a fixed target, and a lot of different particles were produced and detected—they found **over 100 new particles**.
This was called the **"particle zoo."** This term was first mentioned by **Oppenheimer** at a high-energy physics conference.

The physicists of the time had to think:

- How can we organize these particles?
- Is there some pattern?
- Are these all fundamental particles?

This is what we will be talking about today.

---

If you think about the **periodic table**, for example, we have all these atoms grouped together according to their proton and neutron numbers.
We also know how many electrons are in the outermost shells, which helped us arrange them in the periodic table.

This is similar to what we want to do now with **hadrons**.
In the context of particle physics, the characteristics we choose to group them together are based on their **quantum numbers**.
We will now discuss different quantum numbers—why they were introduced and how they helped us classify particles.

---

In **1932**, the neutron was discovered by **Chadwick**, and experiments—including those at the Bevatron—showed that:

- **Photon-proton**
- **Proton-neutron**
- **Neutron-neutron**

interactions had **very similar strengths**. The interaction rates were basically the same.
The masses of the proton and neutron are also almost identical at **939 MeV**.
This led to the suggestion that the proton and neutron could be considered the **same particle** in two different states, described by **isospin**.

::: callout-note
**Isospin Symmetry**:
The strong interaction does not distinguish between a proton and a neutron. The only difference appears in an electromagnetic field—they are the same particle, the **nucleon**, in an isospin doublet.
:::
This is analogous to **electron spin**, where we have spin up or spin down.
At the quark level, protons and neutrons are composed of **up and down quarks**, so the strong interaction does not distinguish between up and down quarks.

The **up quark** has an isospin of $I = \frac{1}{2}$, with the third component $I_3 = +\frac{1}{2}$, and the **down quark** has $I_3 = -\frac{1}{2}$.

---

Isospin is not exactly like spin, but mathematically we can treat it similarly, following **$SU(2)$ algebra**.
The generators of $SU(2)$ are the **Pauli matrices**.
For isospin, we write the operators as $I$ instead of $J$ for spin.

The projections $I_3$ range from $I$ to $-I$ in integer steps, giving $2I + 1$ states:
$$
2I + 1
$$

---

For **mesons**, we combine a quark and an antiquark.
If we combine up and down quarks (each with $I = \frac{1}{2}$), the possible total isospins are **0 or 1**.
The dimensions are $2 \times 2 = 3 + 1$, corresponding to:

- A **triplet** ($I = 1$)
- A **singlet** ($I = 0$)

For $I = 1$, there are three projections ($I_3 = +1, 0, -1$), and for $I = 0$, just one ($I_3 = 0$).

In group theory terms, this is written as:
$$
\mathbf{2} \otimes \mathbf{\overline{2}} = \mathbf{3} \oplus \mathbf{1}
$$

The **triplet** consists of pions ($\pi^+, \pi^0, \pi^-$) or rho mesons, while the **singlet** is the $\eta'$.

---

The Clebsch-Gordan coefficients describe how these states combine. For example, combining two $I = \frac{1}{2}$ states gives:
$$
|1, +1\rangle = |\frac{1}{2}, +\frac{1}{2}\rangle |\frac{1}{2}, +\frac{1}{2}\rangle
$$
$$
|1, 0\rangle = \frac{1}{\sqrt{2}} \left( |\frac{1}{2}, +\frac{1}{2}\rangle |\frac{1}{2}, -\frac{1}{2}\rangle + |\frac{1}{2}, -\frac{1}{2}\rangle |\frac{1}{2}, +\frac{1}{2}\rangle \right)
$$
$$
|0, 0\rangle = \frac{1}{\sqrt{2}} \left( |\frac{1}{2}, +\frac{1}{2}\rangle |\frac{1}{2}, -\frac{1}{2}\rangle - |\frac{1}{2}, -\frac{1}{2}\rangle |\frac{1}{2}, +\frac{1}{2}\rangle \right)
$$

For **antiquarks**, the isospin projections are inverted:

- Anti-up has $I_3 = -\frac{1}{2}$
- Anti-down has $I_3 = +\frac{1}{2}$

---

Now consider a **pion beam** hitting a **proton target**.

- The pion has $I = 1$
- The nucleon has $I = \frac{1}{2}$

Combining these gives possible total isospins of $\frac{3}{2}$ or $\frac{1}{2}$:
$$
\mathbf{3} \otimes \mathbf{2} = \mathbf{4} \oplus \mathbf{2}
$$

The $\frac{3}{2}$ states correspond to the **delta resonances** ($\Delta^{++}, \Delta^+, \Delta^0, \Delta^-$), while the $\frac{1}{2}$ states are nucleon-pion interactions.

---

For **baryons**, combining three quarks ($\mathbf{2} \otimes \mathbf{2} \otimes \mathbf{2}$) gives:
$$
\mathbf{2} \otimes \mathbf{2} \otimes \mathbf{2} = \mathbf{4} \oplus \mathbf{2} \oplus \mathbf{2}
$$

The **quadruplet** is the $\Delta$ resonances, and the **doublets** are spin-$\frac{1}{2}$ baryons.

---

Isospin also explains differences in **cross sections**.
For example, the cross section for $\pi^+ p$ scattering is **three times larger** than for $\pi^- p$ in the delta resonance region.

---

This concept originated in the **50s**, before quarks were discovered.
Physicists noticed that:

- **Proton-proton**
- **Proton-neutron**
- **Neutron-neutron**

interactions had **similar strengths**, suggesting the strong interaction doesn't distinguish between them.
Later, this was extended to quarks, where the strong interaction doesn't distinguish between **up and down quarks**.

### Strangeness, Isospin, and the Eightfold Way: Patterns in Particle Multiplets


First, they had this kind of an **isospin doublet**. Then they found all these other particles like the pions and K's and so on. They grouped them together and looked for bigger patterns with also the **strangeness** included as the next quantum number. There are deltas. Do you remember when that was first found? Around the **60s**. With the Bevatron experiment, one of the first large accelerators in Berkeley, they found over 100 particles and didn't know what to do with them. Were they like atoms or not? Later they found out they could decompose them into smaller particles and understand how. We are still trying to understand.

---

Take a three-minute break while I clean the blackboard. Then we will continue with strangeness.

---

**Strangeness**. Some of the particles they detected behaved in a *strange* manner. For example, in cosmic rays, pions hit a carbon target. In a cloud chamber, they saw four tracks forming a V-shape: $ \pi^+ $, $ \pi^- $, proton, and $ \pi^- $. These particles always appeared in pairs and had a fairly long lifetime. They concluded by introducing a new quantum number, **strangeness**, which must be conserved.

::: callout-important
Strangeness conservation:

- **Strong interactions**: $\Delta S = 0$
- **Weak interactions**: $\Delta S \neq 0$ (e.g., $\Lambda \to p^+ + \pi^-$)
:::
---

I forgot to mention earlier that **isospin** is also a quantum number conserved in strong interactions. How do we assign this quantum number? Particles consisting of up and down quarks have strangeness $0$, like pions, neutrons, and protons. For others, like lambda, strangeness is $+1$. These are called **hyperons**. There are different types: lambda, sigmas, cascades, and kaons. We can form isospin doublets with $ K^+ $ and $ K^0 $, and similarly $ K^- $ and $ \overline{K^0} $ in a doublet with strangeness $-1$.

Since these particles always appear in pairs, strangeness must be conserved in strong interactions but not in weak interactions. For example, in the lambda decay $ \Lambda \to p^+ + \pi^- $, neither the proton nor the pion has strangeness, but the decay happens. The long lifetime indicates weak decay. However, they are produced in strong interactions, like $ \pi + p \to \Lambda + K^0 $.

---

We can define **hypercharge** $Y$ as:
$$
Y = B + S
$$
where:

- $B$ is baryon number
- $S$ is strangeness.

For baryons, $B = +1$; for antibaryons, $B = -1$; for mesons, $B = 0$.

---

To clarify, certain reactions are forbidden. For example, if we replaced the lambda with a proton, the reaction wouldn't happen. Similarly, a $ \pi^- $ in a proton beam cannot produce only two mesons—a baryon must also be present, conserving baryon number.

From isospin, we saw a correlation with charge. For the isospin triplet $ \pi^+ $, $ \pi^0 $, $ \pi^- $, the charges are $+1$, $0$, $-1$. This relationship is captured by the **Gell-Mann–Nishijima formula**:
$$
Q = I_3 + \frac{Y}{2}
$$
where:

- $Q$ is charge
- $I_3$ is the third component of isospin
- $Y$ is hypercharge.

---

Let’s test this for the proton:

- $I = \frac{1}{2}$, $I_3 = +\frac{1}{2}$
- Strangeness $S = 0$, baryon number $B = 1$, so $Y = 1$.

Plugging in:
$$
Q = \frac{1}{2} + \frac{1}{2} = +1
$$
which matches the proton’s charge. For the neutron, $I_3 = -\frac{1}{2}$, giving $Q = 0$.

---

Using strangeness and hypercharge with isospin, Gell-Mann and Ne'eman found larger patterns, arranging particles into bigger multiplets. This became known as the **eightfold way**.

For these patterns, they included the **strange quark** alongside up and down, working in $SU(3)$ flavor symmetry. At the time, quarks weren’t known, but we can describe it this way. Plotting the third component of isospin against strangeness for up, down, and strange quarks reveals the structure.

Here are the quantum numbers for these quarks:

- **Baryon number**: $B = \frac{1}{3}$ for each quark (so three quarks give $B = 1$ for a baryon).
- **Charge**: $Q_u = +\frac{2}{3}$, $Q_d = -\frac{1}{3}$, $Q_s = -\frac{1}{3}$.
- **Spin**: all are fermions with spin $\frac{1}{2}$.
- **Strangeness**: $S_s = -1$ for the strange quark, $S_{u,d} = 0$.

---

Now consider baryons, composed of three quarks (up, down, or strange). The combinations form a **decuplet** and **octets**: $3 \otimes 3 \otimes 3 = 10 \oplus 8 \oplus 8 \oplus 1$. We focus on the ground states: an octet and a decuplet.

Plotting the third component of isospin against strangeness (or hypercharge), we see patterns. On the horizontal axis, isospin multiplets appear: a doublet for neutron and proton, a triplet for sigmas, and a doublet for cascades. The quark content varies: one strange quark for some, two for others.

---

**Mass differences** reveal symmetries:

- Along the horizontal axis (same strangeness), masses are nearly equal (e.g., proton and neutron differ by ~1 MeV).
- Vertically (changing strangeness), mass differences are larger (~250 MeV for sigmas, ~130 MeV for cascades).

This shows $SU(2)$ isospin is a good symmetry, but $SU(3)$ flavor symmetry is broken, as masses aren’t equal.

---

The octet baryons have **spin-parity** $J^P = \frac{1}{2}^+$, while the decuplet has $J^P = \frac{3}{2}^+$. At the time, the $\Omega^-$ was predicted by Gell-Mann and discovered two years later in bubble chamber experiments: $K^- + p \to \Omega^- + K^+ + K^0$. Strangeness conservation required additional kaons. The $\Omega^-$ decayed as $\Omega^- \to \Xi^0 + \pi^-$, then further to $\Lambda^0 + \pi^0$, and finally to $p + \pi^-$ and photons.

Gell-Mann also predicted the $\Omega^-$ mass. The mass spectrum shows spacing:

- $\Delta$ at 1232 MeV
- $\Sigma^*$ at 1385 MeV
- $\Xi^*$ at 1530 MeV
- $\Omega^-$ at 1680 MeV

with ~150 MeV between levels.

---

These patterns come from **group theory**, describing particles mathematically. The mass difference between octet and decuplet arises from spin-spin or spin-orbit interactions, reflecting the dynamics.

### Baryon and Meson Multiplets: Quantum Numbers and Decay Constraints


This is for the **baryons**, and we can also do a similar multiplet for the **mesons**.
Let me exchange the blackboards.

For the mesons, if we think again of the up, down, and strange quarks, we have the SU(3) flavor symmetry composition:
$$
3 \otimes \overline{3} = 8 \oplus 1.
$$
Here we have it.

On the diagonal, you always have the **charge**.
For example:

- Here all of these particles on this diagonal have a charge of $-1$.
- In the middle, the charges are $0$, $+1$, and $+2$.

This octet—or **nonet** if we include the $\eta'$—has the quantum numbers $0^-$, $0^+$.
This means the quark-antiquark pair have **antiparallel spins**, resulting in parity $P = -1$.
I will explain charge conjugation shortly—it is $+1$.

For the **parallel spin alignment**, we have:

- A spin of $1$,
- Parity $P = -1$,
- Charge conjugation $C$.

I will explain it.

::: callout-note
**Key Definitions**:

- **Parity** inverts the spatial coordinates.
- **Charge conjugation** converts a particle into its antiparticle.
:::
For **baryons**, if you know the orbital angular momentum $L$, you can calculate parity using:
$$
P = (-1)^L.
$$
For the octet, these are ground states with $L = 0$, so parity is $P = +1$ for both the $\frac{1}{2}^+$ and $\frac{3}{2}^+$ states.

For **mesons**, parity is given by:
$$
P = (-1)^{L+1},
$$
which gives $P = -1$ for both cases here.

**Charge conjugation** is only well-defined for neutral mesons.
For example, applying it to $\pi^0$ gives a $+1$ eigenvalue:
$$
C|\pi^0\rangle = +1|\pi^0\rangle.
$$

When analyzing particle decays, it is important to consider these **quantum numbers**:

- Parity and $C$-parity are **multiplicative**.
- You also need to know how to combine spins of different particles to get the total spin.

---

**Example**: Can an $\omega$ meson decay into two pions?

- Consider $C$-parity: for $\pi^0$, $C = +1$.
- Multiplying for two pions gives $C = +1$, but for $\omega$, $C = -1$, so this decay is **forbidden**.

There are many more examples to explore in the exercises.

### Resolving the Omega Minus and Delta Plus Plus Symmetry Problem with Color Charge


Lastly, I want to discuss one thing.
None of you complained when I wrote down the quark content for the **omega minus** or the **delta plus plus**.
I told you all of these have **spin aligned**—all have spin up.
You see their **flavor content** is also the same.
Do you see a problem here?
What are quarks?
Yes, with **Heisenberg's exclusion principle**.
Exactly.

---

When we have **fermions**, and they form a state, they should be **distinguishable by at least one quantum number**.
Here, everything is the same—**same spin, same flavor**.
Let’s look at the **total wave function** of these baryons.

First, we have the **spatial**, **spin**, and **flavor** wave functions.
For $L = 0$, the spatial wave function is **symmetric**.
The spins are all aligned up, so the spin wave function is also **symmetric**.
If you exchange any quark pair, the state remains the same—that’s what **symmetric** means.
The flavor wave function is also symmetric since all quarks are identical.

---

::: callout-important
The **total wave function** of baryons (fermions) must be antisymmetric under exchange:
$$\Psi_{\text{total}} = \psi_{\text{spatial}} \otimes \psi_{\text{spin}} \otimes \psi_{\text{flavor}} \otimes \psi_{\text{color}}$$
For $L=0$ states like $\Delta^{++}$ or $\Omega^-$, the spatial, spin, and flavor parts are symmetric, so the **color wave function must be antisymmetric**:
$$\psi_{\text{color}} = \frac{1}{\sqrt{6}}(rgb - rbg + brg - bgr + gbr - grb)$$
:::
---

What do physicists do when we can’t solve this?
We introduce a **new quantum number**.
Which quantum number could it be?
Yes, **color charge**.
This was already discussed a little last time.

This part of the wave function must be **antisymmetric** to make the total wave function antisymmetric.
We assign each quark a different color—**red, green, blue**.
That’s what makes them distinct.

---

Key points:

- Quarks are **fermions**, so their total wave function must obey the **Pauli exclusion principle**.
- For baryons with **identical flavor and spin**, the **color charge** provides the necessary distinction.
- The **antisymmetric color wave function** ensures the total wave function is antisymmetric.

### Evidence for Three Quark Colors from $e^+ e^-$ Annihilation Cross-Section Ratios


Let’s very briefly discuss one last experiment, and then we are done.
Last time, I mentioned that we have **three different colors**.
How do we actually know that there are three and not, say, six or something like that? I mean, we have six types of quarks.

---

So there were experiments done that actually showed us that it has to be three.
What they did was look into $e^+ e^-$ annihilation.
Then you can have a **virtual photon** that is exchanged, and you can have different types of particles produced here:

- You can have **quark-antiquark pairs**, or
- You can also have **leptons** like $\mu^+ \mu^-$.

For the quarks, we have the different types that we know.
This gives us basically the **mass of the produced systems**.

---

::: callout-important
The key experimental observable was the **cross-section ratio** $R$, comparing hadronic production to lepton pair production:
$$
R = \frac{\sigma(e^+ e^- \to \text{hadrons})}{\sigma(e^+ e^- \to \mu^+ \mu^-)}
$$
At leading order, this simplifies to:
$$
R = N_c \sum_q e_q^2
$$
where $N_c$ is the **number of colors** and $e_q$ is the **electric charge** of quark flavor $q$.
:::
---

Why measure this ratio? Because for the leptons, we don’t have any color.
So if we divide by this, we should get something **proportional to the number of colors** we have.
That’s the idea behind it.

Here, a photon is exchanged at this vertex, with proportionality to the **charge squared**.
Then we have the different types of quarks.
Initially, you have just **up, down, and strange quarks**, so you can measure, for example, the $\rho$, $\omega$, or $\pi$ mesons as peaks in the spectrum.

When the energy is high enough, you can also produce **charm-anticharm bound states**—these are called $J/\psi$ states, for example.
This is what happens starting here.
Then, at some point, the energy becomes high enough to also have **bottom-antibottom states**.

---

The quark charge contributions change as more flavors become accessible:

- **For the light quarks (u, d, s):**
$$
\sum_q e_q^2 = \left(\frac{2}{3}\right)^2 + \left(-\frac{1}{3}\right)^2 + \left(-\frac{1}{3}\right)^2 = \frac{2}{3}
$$

- **When charm threshold is passed:**
$$
\sum_q e_q^2 = \frac{2}{3} + \left(\frac{2}{3}\right)^2 = \frac{10}{9}
$$

- **And when bottom threshold is passed:**
$$
\sum_q e_q^2 = \frac{10}{9} + \left(-\frac{1}{3}\right)^2 = \frac{11}{9}
$$

---

This can be calculated exactly to determine how large these steps are, and what they found was that the **number of colors must be three**.
We’ll discuss this more later.

### Historic Development of the Quark Model and Particle Discoveries


I just want to leave a couple of minutes for questions.
This was a little bit of **historic background**—how from the different particles that were detected, different patterns were seen using the **eightfold way** ($S$ for strangeness).

::: callout-note
The Gell-Mann–Nishijima formula relates these properties:
$$Q = I_3 + \frac{B + S}{2}$$
where $Q$ is charge, $I_3$ is isospin, $B$ is baryon number, and $S$ is strangeness.
:::
Later, looking into these multiplets, they formed a **quark model** where all these particles consist of smaller particles called quarks.
We said they come in **six different flavors** and have **three types of color**.
This is basically the historic background to this topic.

---

What I always find difficult with histories like this is distinguishing what was known and what wasn't.
For example, when strangeness was introduced with cosmic rays, how did they know it was strangeness ($\Delta S \neq 0$) and not just invariant masses?
They called these particles *strange* because they were confused about why they only appeared in pairs or had longer lifetimes.

---

Practically, you can only look at the **invariant mass**.
You detect the proton and the pions, then analyze the spectra.
That's how you determine the knowns and unknowns.

* Key particle discoveries:
* Pions were discovered quickly
* Proton, then neutron in 1932
* 1950s: antiproton and many other particles (charged, measurable directly)

---

You mentioned **CP symmetry**. How was that introduced?
Was it used to say a decay isn't allowed, or was it the other way around?
If you don't observe a decay, there must be a violated quantum number.

::: callout-important
CP violation occurs when:
$$\frac{\Gamma(P \rightarrow f) - \Gamma(\bar{P} \rightarrow \bar{f})}{\Gamma(P \rightarrow f) + \Gamma(\bar{P} \rightarrow \bar{f})} \neq 0$$
:::
---

I don't know exactly when **charge conjugation** was introduced, but it was early—around the time of the positron, before the antiproton was discovered.
Sometimes concepts come from theory, sometimes from experiments.
For example:

* The omega baryon ($\Omega^- = sss$) was predicted
* Quantum numbers were introduced based on cross sections
It's difficult to track historically.

---

The quark model was mostly correct historically. 
When the multiplets were assembled, it was only postulated that there might be a smaller substructure. 
They were first called **partons**, not quarks. 
 
The mass differences in the deltas, sigmas, and cascades suggested different quark content. 
They saw a mass difference and predicted the next particle would be **150 MeV heavier**, which turned out to be correct. 
The original quark paper is just two pages—you can look it up. 
It was an exciting time: quarks were predicted in 1962, and the Omega minus was discovered in 1964.
