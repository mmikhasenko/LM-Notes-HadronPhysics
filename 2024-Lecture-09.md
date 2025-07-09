### Personalized Lectures, Homework Encouragement, and Flexible Learning


Similar to courses you've had, **there were always two of us in the lecture**, so it was a personalized education.
I remember my teacher saying that *the quality of the lecture was measured by whether Mikael was sleeping or not*.

::: callout-tip
**Engagement tip**: Use physical cues like eye contact or note-taking as indicators of lecture effectiveness, just like Mikael's wakefulness served as a quality measure.
:::
If he was sleeping, the lecture was bad, and if he was awake, the lecture was good.
So **you're not sleeping—follow along**.
Probably the lecture is good.

---

It was a little bit funny.
We would come to the professor's office.
He had a little board, and we would sit in front of his chair, sketching things on it.
*Not so many people were there*.

---

**Homework discussion**:

- Have you done the exercise sheets?
- Yes, but I don't have anything like I did, at least the first exercise.
- You cannot—because Eva is not here today.
- But I could have collected them.

::: callout-important
**Submission reminder**: Always bring completed exercises even if collection isn't scheduled - you never know when they might be accepted.
:::
Very good—you brought something.
I encourage you to **hand them in**, in addition to looking at them.
It's really good that you looked.

---

**Exam requirements**:

- We proved and wanted to report points on exams
- We set the admission criteria at a low 50% of points
- But you're not there yet—none of the students are there yet

**Action items**:

1. Please work on the homework
2. If you want to have enough at the end, we might allow for:
- A lower number of points
- Or let you submit exercises later

This is something to fulfill, and **I would like you to fulfill that**.

---

**About the exercises**:

- They have been **non-standard** in the sense that you don't find them in books
- Allowed resources include:
- Course materials
- ChatGPT help
- *Everything* - just like in research

::: callout-note
**Problem-solving approach**: While the exercises aren't textbook problems, they're designed to be solvable with available tools and require creative thinking rather than rote memorization.
:::
Have a look.
They are not that difficult, as you probably discovered, but they require **some thinking**.

### Transition from Unitarity to Hadron Spectroscopy: Models and Lecture Schedule


Today we are finishing with **unitarity** and moving toward discussing approaches used in **hadron spectroscopy**.
A few lectures in the future, I want to dedicate to the field—the approaches from theory and experiment, mostly from theory—that use hadron spectroscopy.

::: callout-note
The **unitarity condition** for the S-matrix is a foundational constraint:
$$S^\dagger S = SS^\dagger = I$$
This ensures probability conservation in scattering processes.
:::
So far, we have discussed the **Lorentz group**, **helicity states**, and **angular distributions**, which are model-independent.
We also discussed **unitarity**, another model-independent approach that provides a guiding principle rather than a definitive answer.

---

Now we will move toward **models**.
If you have a Lagrangian, you can derive everything. The models that approximate Lagrangians—we'll discuss:

- **Chiral Perturbation Theory (ChPT)**: A low-energy effective field theory.
The leading-order Lagrangian is:
$$\mathcal{L}_{\text{ChPT}} = \frac{F_\pi^2}{4} \text{Tr}[\partial_\mu U \partial^\mu U^\dagger] + \frac{F_\pi^2 B_0}{2} \text{Tr}[M(U + U^\dagger)]$$
where $U$ is the chiral field, $F_\pi$ the pion decay constant, and $B_0$ relates to the quark condensate.

- **pNRQCD**: A non-relativistic effective field theory for charmonium states.
The Hamiltonian for heavy quarkonia is:
$$H_{\text{pNRQCD}} = \frac{\mathbf{p}^2}{m_Q} + V(r) + \mathcal{O}(1/m_Q^2)$$
where $m_Q$ is the heavy quark mass and $V(r)$ is the QCD potential.

- **Lattice QCD**: We'll explore its methods and applications in hadron spectroscopy.
The action for Wilson fermions is:
$$S_{\text{LQCD}} = \sum_{x} \bar{\psi}(x) D_W \psi(x) + S_G[U]$$
with $D_W$ as the Wilson-Dirac operator and $S_G$ the gauge action.

---

I would like to spend one more lecture on **B meson** and **D meson** physics, where hadron physics plays a crucial role.
While these studies often focus on **CP violation** and searches for **new physics beyond the Standard Model**, hadron physics provides essential input on strong interactions.

::: callout-important
The **weak decay amplitude** for $B \to f$ transitions is:
$$\mathcal{A}(B \to f) = \langle f|\mathcal{H}_{\text{weak}}|B\rangle = V_{ub} V_{uq}^* \mathcal{M}_{\text{strong}}$$
Here, $\mathcal{M}_{\text{strong}}$ encodes hadronic matrix elements, emphasizing the need to understand strong phases.
:::
Determining weak phases almost always requires knowledge of the **strong phase** of the transition.
Understanding how hadrons form and their properties is key.

---

I think we have **four more lectures** to go, possibly fewer.
I plan for four, aiming to finish in the **first week of July**.
The **16th** is a spare lecture in case we need additional discussion.
But the **9th of July** is marked as the last lecture on my calendar.

Does the semester usually run until mid- or late July? I forget the exact schedule.
In my calendar, the semester extends until the **third week of July**.
So the **9th, 16th, and even the 23rd** are still part of the semester.
However, a research school in Bochum will occupy our time, so we aim to finish one week earlier.

### Unitarity Constraints on Partial Amplitudes and the Argand Diagram



Today's lecture—**lecture number one**—will start with the **theoretical unitarity**. We'll discuss the **threshold expansion**, particularly amplitude behavior at the threshold, as well as the **scattering length approximation**. Then we'll move to **effective field theory (EFT)** and compare **EFT and unitarity**. Finally, we'll cover **ππ scattering in S-wave**, where the current perturbation theory gives us the scattering amplitude.

---


The first question is:
*Which values are allowed for the transition as partial amplitude* $F = T \rho$, *where* $T$ *is the scattering amplitude?*

- **Consistency is important**. The scattering amplitude is the scattering amplitude, and this is the partial amplitude.
- If you don't have any clue for the first one, you might just—if you don't do homework, you have no clue for the first one, probably.
- The second one is standard, something we discussed many times.

Let's start with **number two**. First, each partial wave—you can just speak aloud. What are your thoughts? What do you think?

---


We noted last time that we want the function to be **analytical on the right-hand side**, and $A$ isn't analytic in this region. If I put $F$ plane, where is $F$? It's $3 - 2A$. This one is here, somewhere at 45 degrees. And this one is $-1$.

It was just the golden ratio but with an $i$ in it. No, it's not the golden ratio, but I thought it was $1 + \sqrt{2}$ divided by—it's $\sqrt{5}/2$ for the golden ratio. That would have been a point where I could have said it's just invented by you. But it's important to understand the principle—**what's allowed when you talk about something being allowed**.

---

::: callout-important
**Unitarity and the Argand Diagram**

- Unitarity tells us that the imaginary part of the amplitude is driven by the interaction loop.
- The imaginary part of the inverse amplitude is given by:
  $$ \text{Im}(T^{-1}) = -\rho $$

- The amplitude can be written as:
  $$ T = \frac{e^{i\delta} \sin \delta}{\rho} $$

- For elastic scattering, the amplitude lies on a **unitarity circle** in the complex plane.
:::
---


This is about **unitarity**, and I would like to use unitarity here. Last time, and also in the homework exercise sheets, we've seen the **Argand diagram**. This is how we determine the values of the amplitude when you plot them in the complex plane.

For **regular resonances**, the amplitude makes a circle. Unitarity tells us that the imaginary part of the amplitude is driven by the interaction loop, and it's only determined. The imaginary part of the inverse amplitude from this relation is simply $-\rho$, and the amplitude can be written as an inner real function—a real function without singularities—minus $\rho$. From that, once you plot the amplitude, you end up on a circle.

How do you see that? This is $A$ in terms of $F$, or this is $T$, and what I want is atoms. So my $F$ is $A \times \rho$. We haven't done this last time, but it's a straightforward exercise to see that such an amplitude is actually sitting on the circle. **Only values that the amplitude can have are on the circle**.

To see that, one takes this general form and divides by $\rho$, replaces $\rho$ by its form in terms of $\delta$, and ends up with something very simple: $\sin \delta \, e^{i \delta}$. This is the only possible value of $W$. You can write it differently: $e^{2i \delta}/2 - \dots$.

When $\delta = 0$, this is zero. When $\delta$ reaches its maximum value, which is $\pi/2$, this is $1$, and $e^{i \pi/2} = i$. So it reaches the maximum value at $i$.

When $\delta = \pi/2$, this is $e^{2 \pi i} = -1$. But something doesn't work. Between this and this, I made a mistake. The numerator is $i/2$, and then you have $1 - e^{2i \delta}$. This is straightforward to see what's happening. You are sitting—and if this distance term were absent, you'd have $i/2$. But this term gives you a shift in the delta direction, and you move along this circle.

Here is $\delta = 0$, here is $\delta = \pi/2$, and then you move on. Here is $\delta = \pi$. This is the **Argand diagram**.

---


For the **elastic amplitude**—where you have only one channel—all allowed values of the amplitude are located along this circle. There are no other possible ways. Among this list, none of them are sitting on the circle. For the single scattering amplitude, none of them would be allowed values from unitarity.

For **non-elastic scattering**—where particles can transition to other channels—values inside the circle are also allowed. Unitarity tells you that for elastic channels, only the circle is allowed. For inelastic scattering, all values inside the circle are allowed.

You look at the list and quickly see which are inside, which are not. I've already put the values on the complex plane. $A$ is not, $B$ is in. To arrive at the center, you need some inelastic channels. It cannot be $\pi \pi$ to $\pi \pi$. It must be—below the first elastic threshold, the next one is outside. But to make it inside, I think if I put it over eight, this is inside, so $B$ is also valid. $D$ is here, and it's even in the negative domain. I have to modify something significantly to make it inside. Put a plus here, perhaps. Then I'm not sure if it sits inside or outside.

---


**Questions?** $\delta$ is the **scattering phase**, a really important quantity in quantum mechanics. You consider a plane wave that interacts with the source, and there is a spherical wave with the scattering phase. This is exactly the same phase. It determines the scattering.

- If $\delta = 0$, that is essentially trivial—**no scattering**.
- This phase determines the **strength of your scattering**.

### Unitarity and Partial Wave Expansions in Scattering Amplitudes


Is this representation correct? Isn't this just the $T$-matrix represented as the $S$-matrix? This "$ \frac{i}{2}(1 - e^{2i \delta}) $," so just this.

In my bachelor's, I've seen it or used it as the on-shell representation of the $T$-matrix.
But it's not. Not this.

For the $S$-matrix, you have just the phase, no sign.
That's why I said it's the $T$-matrix represented as written.
Yes, that's exactly the $T$-matrix that I discussed.

Now, this $T$ is the expectation of the $T$-matrix.
Because there's also the physical factor $\rho$ in it, but maybe it just dropped out.
Right, exactly.

In quantum mechanics, the same thing appears, but instead of $\rho$, we have $K$, the wave number for the breakup momentum, which is also part of $\rho$.
The factor is slightly different, but $P$ is the breakup momentum.
That's what you see in the quantum mechanics derivation.

There is no "$ \frac{1}{\sqrt{s}} $." This is a relativistic factor that only appears in relativistic scattering.
Overall, it's a normalization constant. But you're absolutely right.

From that, you also see the $T$-matrix. The relation between them is $S = 1 + i \rho T$.
So the $S$-matrix is $S = 1 + 2i \rho T$.
When you substitute this, you should have just $e^{2i \delta}$.
Then you see that unitarity is satisfied with $S^\dagger S = 1$.

---

::: callout-important
Key formulas discussed:

- $T = \frac{i}{2}(1 - e^{2i\delta})$
- $S = 1 + 2i\rho T$
- Unitarity condition: $S^\dagger S = 1$
:::
---

Quickly, exercise number two: in which case does this happen? For the sake of time, we should move on.

The first one applies to all of them.
To determine that, you do simple spin algebra:

- $0^- \rightarrow 1^-$ is a $P$-wave.
- $2^+ \rightarrow 0^-$.
- $1^- \rightarrow 0^-$.

Here, $2^+ \rightarrow 0^+$ in $S$-wave would be $2^-$.
But the answer is... Oh, that's interesting.

For the first one in the $P$-wave, these two combine to $1^-$, matching the quantum numbers of the $\rho$ meson.
The $\rho$ meson is $1^-$, and this decay conserves parity.

The second one is electromagnetic.
If you combine $2^+$ and $0^+$ in $S$-wave, you get $2^-$.
In $D$-wave, you can have $0^-$, $1^-$, $2^-$, $3^-$, or $4^-$.
But the $D$ meson has quantum numbers $1^-$, so this matches.

Importantly, this decay can also happen in different partial waves.
No—wait, it cannot.
This decay doesn't have to conserve parity for this transition.
Both $0^-$ and $0^+$ transitions are possible because it's a weak decay.
From this, you get $S$, but it's not the only answer.
Another possibility is $1^+$.
With two units of orbital angular momentum, you can get $1^+$, $2^+$.

---

I would like to motivate the next subject: how the amplitude $A(s)$ behaves near particle thresholds.
For $A(s) = M_1 + M_2$, we are still discussing general properties.

Let’s look at the partial wave expansion for a particle with spin $j$ and helicity $\lambda$ decaying into two scalar particles.
We can rewrite the decay using Wigner rotations, matching the alignment of the final states.
The initial state has spin projection $\lambda$ along the $z$-axis, and the Wigner $d$-function depends on the helicity difference of the final particles.

In the rest frame, the spin projection is $\lambda$, and the decay angle is $\theta$.
Let’s examine $\lambda = 0$ and the spherical harmonics.

For $l = 1$, it’s $\cos \theta$.
For $l = 2$, it’s $\frac{3}{2} \cos^2 \theta - \frac{1}{2}$.
And the third one is $\frac{3}{2} \cos^2 \theta - \frac{1}{2} - 1$, right?
No, it's just $\cos \theta$.
For $2 \rightarrow 2$, it’s straightforward.

---

::: callout-note
Partial wave expansion for spin $j$ and helicity $\lambda$:
$$
A(s) \propto \sum_j (2j + 1) d^j_{\lambda,0}(\theta) \mathcal{A}_j(s)
$$
where $d^j_{\lambda,0}(\theta)$ is the Wigner $d$-function.
:::
---

The spherical harmonics for $\lambda = 0$ are:

- $Y_1^0(\theta) \propto \cos\theta$
- $Y_2^0(\theta) \propto \frac{3}{2}\cos^2\theta - \frac{1}{2}$

---

The breakup momentum $P$ in relativistic scattering is given by:
$$
\rho \propto P = \frac{\sqrt{(s - (M_1 + M_2)^2)(s - (M_1 - M_2)^2)}}{2\sqrt{s}}
$$

### Kinematic Singularities and Angular Momentum Compensation in Scattering Amplitudes


Earlier we discussed that there are **invariant variables** described by Mandelstam variables: $S$ and $T$. It is often convenient to express the cosine of the scattering angle in terms of these variables. One can use either the basis of the scattering angle and the energy $\sqrt{S}$, or work directly with Mandelstam variables, as they are related. Thus, $\cos \theta$ can be expressed in terms of $T$ and $S$.

::: callout-note
The relation for cosine of the scattering angle is:
$$\cos \theta = f(S, T)$$
where $f(S, T)$ is a polynomial in $T$ and $S$.
:::
For this decay process, we don't have $T$. But for the point I would like to make, let's imagine that this is produced by an external reference—a two-particle scattering that gives us an extra vector to calculate $T$. If $\cos \theta$ is expressed in terms of $S$ and $T$, one finds that it is essentially a polynomial: a first-order polynomial in $T$ and a second-order in $S$, divided by the **Chew-Mandelstam functions**, which are the breakup momentum of the particles in the $S$-channel.

---

For the **S-wave**, there is a constant factor. For the **P-wave**, the breakup momentum appears in the first power in the denominator. For the **D-wave**, it appears in the second power. To compensate for the $p^J$ dependence in the denominator from angular momentum, this factor must appear in the numerator of the partial wave. This ensures the total amplitude is free of kinematic singularities at the threshold. The amplitude does not fully account for the threshold behavior $p^{2L}$, so this compensation is necessary.

::: callout-important
Breakup momentum dependence for partial waves:

- **S-wave ($L = 0$)**: No explicit $p$ dependence
- **P-wave ($L = 1$)**: $\frac{1}{p}$
- **D-wave ($L = 2$)**: $\frac{1}{p^2}$
:::
---

This is often seen in phenomenological constructions. When fitting data, the recipe includes $p^L$ in the partial wave (for $L$-wave) because it compensates for the angular momentum dependence, which scales as $1/p^L$. This is important. For example, in the parameterization of the $\rho$ meson decaying to $\pi\pi$, the $p^2$ factor appears twice: once in the numerator to compensate for angular dependence, and once in the denominator in the width parameter, because the width sums over the $\pi\pi$ scattering phase space.

This leads to a parameterization where, at every vertex, there is a $p^1$. The $p^{2L}$ arises from vertices due to the $p^2$ factor, and another from phase space. For the $\rho$ meson transition, this results in $p^3$ appearing in the denominator of the width parameter.

::: callout-note
Rho meson width parameterization (P-wave decay, $J = 1$):
$$\Gamma_\rho \sim p^3$$
:::
---

Another example is the $D$ meson decay, where $p^L$ also appears. The $D^* \to D\pi$ decay is in P-wave, so there is always a momentum factor. Often, when constructing amplitudes, the kinematic-singularity-free amplitude $\hat{A}$ is introduced, defined as $\hat{A} = A \cdot (2p)^J$ for $L$-wave. This replacement introduces the factor $(2p)^{2J}$ on the right side.

::: callout-note
Kinematic-singularity-free amplitude:
$$\hat{A} = A \cdot (2p)^J \quad \text{(for L-wave)}$$
:::
---

I need to clarify the difference between resonance production and particle scattering. Typically, $A$ denotes the production amplitude, while $T$ denotes the scattering amplitude. The kinematic-free amplitude reduction ensures $T_J$ is free of kinematic singularities. The key difference is that $T$ involves the same initial and final states (e.g., $\pi\pi \to \pi\pi$), while $A$ involves different states (e.g., $X \to \pi\pi$).

For $T_J$, the factor is $(2p)^{2J}$. The amplitude here refers to scattering, not production. In the production amplitude, $p$ and $q$ are distinct, but for identical initial and final states, they are the same, leading to $p^{2J}$. The denominator's parameterization describes how particles scatter, which is why the factor $(2J + 1)$ appears.

::: callout-important
Partial wave expansion:

- **Scattering ($\pi\pi \to \pi\pi$)**: $T_J \sim (2p)^{2J}$
- **Production ($X \to \pi\pi$)**: $A_J \sim (2p)^J$
:::
### Scattering Phase Shift and Amplitude Near Threshold



Let’s think how to derive this in the quickest way.

It is straightforward to see that the **phase shift** $\delta$ near threshold behaves as:

$$
\delta \propto p^{2L + 1}
$$

Transforming this to $\sqrt{s}$, we get:

$$
\delta \propto (\sqrt{s} - (m_1 + m_2))^{2L + 1}
$$

---


For **S-wave scattering**, the amplitude is constant at the threshold, as is the scattering amplitude. We can write this as:

$$
A = \frac{1}{R - i \rho}
$$

For the S-wave at threshold, $\rho$ vanishes because $\rho$ has the momentum in the first power, leaving only the regular function $R$.

The value of $R$ at the threshold is called the **scattering length**. Let’s denote it as $\alpha$ (or $a$).

::: callout-note
**Scattering Length Approximation**:
Replace the unknown $R$ function by a constant. This is valid for all amplitudes near the threshold, where $R$ behaves as a constant.
:::
---


For some amplitudes, this approximation holds even farther from the threshold, especially if no other singularities influence the amplitude. There are two interesting cases:

- **$R > 0$**
- **$R < 0$**

These lead to distinct phenomena.

---


As a function of $s$, $\rho$ starts at the threshold and grows like:

$$
\rho \approx \frac{1}{2} \sqrt{s - (m_1 + m_2)^2}
$$

Near threshold, it behaves as $\sqrt{s}$.

Below the threshold, $\rho$ becomes imaginary. For $s < (m_1 + m_2)^2$:

$$
\rho = i \sqrt{(m_1 + m_2)^2 - s}
$$

So $-i\rho$ has a negative imaginary part.

---


- If $1/a$ is **negative and small**, there is a zero in the denominator.
- If $a$ is **positive**, there is no pole in the physical region. The function continues downward, with $\rho$ negative.

The square root is a **two-valued function**, creating a branch point and a cut. For every point, the square root can be evaluated with:

- **Plus sign** (on the first sheet)
- **Minus sign** (on the second sheet)

For $a > 0$, there is still a pole, but it is hidden—only visible if you go under the cut. This is the **virtual state**: a pole below the threshold on the second Riemann sheet.

---

::: callout-important
**Key Takeaway**:
The scattering length approximation simplifies the amplitude near threshold, but the behavior of $\rho$ and the pole conditions reveal deeper structures like virtual states.
:::
### Scattering Length, Bound States, and Effective Field Theory in Threshold Scattering


The **scattering length** is an important quantity that is measured from any scattering experiment in nuclear physics.
This is one of the **good observables** that people use.
This quantity characterizes the strength of the matrix element at the threshold.

::: callout-note
Near threshold, the transition matrix element simplifies to:
$$ T \approx A $$
where $T$ is the transition matrix and $A$ is the scattering length.
:::
As you see, you just evaluate $T$ at the threshold, this vanishes and $T$ is literally equal to $A$.
But if the validity of the scattering length approximation extends a little further, you find that for large values of $A$, you can get a bound state near the threshold.

---

This bound state is the example of the **deuteron**.
The deuteron, which is formed by the scattering of a proton and neutron, is a bound state of the proton and neutron.
It is a good example where the scattering length approximation works.

When you scatter a proton and neutron near threshold, you find that $A$ is negative, which corresponds to the neutron being below the threshold.
Alternatively, due to the presence of the neutron below threshold, when a proton and neutron scatter, they feel the presence of the neutron and have a negative scattering length.

The scattering length is measured in units of **Fermi**.
For the deuteron, it is approximately $-5.4$ to $-5.5$ Fermi.

---

We will now consider different approaches to quantum physics.
One of them, **effective field theory at low energy**, deals with calculating a low momentum expansion.
This approach gives parameters like the scattering length approximation or the next term in the expansion, called the **effective range**.

::: callout-note
The **effective range expansion** for S-wave scattering is:
$$ k \cot \delta_0 \approx -\frac{1}{A} + \frac{1}{2} r_0 k^2 + \mathcal{O}(k^4) $$
where:

- $k$ is the momentum,
- $\delta_0$ is the S-wave phase shift,
- $A$ is the scattering length,
- $r_0$ is the effective range.
:::
For neutron scattering, measurements are difficult because neutrons are non-magnetic.
Proton scattering is much easier to calculate.

In the notes, I have a value, but the conventions are slightly different.
The units must be corrected—we want something in Fermi.
What I have here is the mass of the pion in the numerator and the low-energy constant $F_\pi$ in GeV.
They cancel each other, so this is not in our usual conventions.

---

For pion s-wave scattering, we can use **effective field theory** to compute scattering near threshold.
The result depends on a single constant, $F_\pi$, which is fixed experimentally.
This low-energy theory uses **spontaneous symmetry breaking**, similar to the Higgs mechanism.
Like all effective field theories, it builds the most general Lagrangian and fixes all constants.

At the lowest order, the amplitude is constant.
This theory does not account for unitarity, so it does not include an imaginary part.
The constant is equal to the scattering length in this sector.
Effective field theory works well near threshold, where it provides constraints for fitting experimental data.

---

**Unitarity** tells us how the amplitude behaves generally, but not the exact functional form.
Constraints on these functions come from other methods, such as effective field theory.

::: callout-note
The unitarity condition for partial wave amplitudes is:
$$ \text{Im}\, f_l(k) = k |f_l(k)|^2 $$
which must be satisfied for elastic scattering.
:::
I planned to cover more today, including **chiral perturbation theory**, but we are out of time.

---

We discussed **kinematic singularities**, which arise because the full amplitude must be free of them.
Angular factors introduce $1/P^j$ due to cosine or sine terms.
The same factor appears in partial wave amplitudes and modifies unitarity.

We introduced $\hat{A}$ and $\hat{T}$, which are kinematic singularity-free functions.
For mean parity equations, an extra factor impacts how we construct the amplitude.

---

The first term in the expansion is related to the partial wave.
For the S-wave, it is simply $P$, and the prefactor is $1/A$.
The next term is $r P^2 / 2$, where $r$ is the effective range.
The function $R$ is regular, and $P^2$ appears because lower powers would introduce a branch point.

---

We examined the **analytic structure** of the scattering length approximation.
A negative scattering length introduces a pole, while a large positive value leads to a virtual state.

::: callout-note
The pole position for a bound state near threshold is:
$$ E_{\text{pole}} \approx -\frac{\hbar^2}{2\mu A^2} $$
where $\mu$ is the reduced mass and $A$ is the scattering length (negative for a bound state).
:::
The closer the pole is to the threshold, the larger the amplitude near threshold.
A large scattering length suggests a nearby pole—either a virtual state (positive) or a bound state (negative).

---

For **proton-neutron scattering**, the interaction strength is high due to the deuteron.
However, scattering cannot form a deuteron because energy conservation prevents it.
The amplitude above threshold reflects the pole below threshold.

If we tune the scattering length from a small negative value, the pole moves toward threshold.
At $A = -\infty$, the pole reaches threshold, then jumps to $+\infty$ and moves away.

An example of a virtual state is **neutron-neutron scattering**.
There is no bound state, but the amplitude is large at threshold due to a virtual state.

---

That concludes today’s discussion.
Next time, we will cover methods for sophisticated matrix element calculations, including **lattice QCD**.
