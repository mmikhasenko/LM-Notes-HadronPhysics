## Scattering Matrix, Unitarity, and the K-Matrix Formalism



We start with **recap problems**. Here all three are positive. So:

- $G$ is positive,
- $S$ is positive,
- and also $U$ is positive.

This would happen if we have a constellation where one of the particles decays into the other three, and we then have a **Dalitz plot** here.

For the $S$ channel, we can see that:

- $U$ is negative
- $T$ is negative

Depending on what type of reaction you have—for example, if it's an **elastic scattering** or **non-elastic scattering** reaction—we can also have mass constraints here.

> [!NOTE]
> **Elastic vs. Non-Elastic Scattering**:
> - If it's elastic, then this would be just the masses here four times, and similarly here as well.
> - For non-elastic, the constraints differ.

In general, there's a function called the **Kibble function** that gives us the constraints and how exactly these areas are constrained. We just put some variation here.

What I have sketched is the more general case where we don't have elastic scattering. For elastic scattering, we would have a different kind of border where it would go a little bit over here.

You can look this Kibble function up, for example, in the book by **Spearman and Martin**. There, different cases are discussed on how these borders change when you have inelastic or elastic scattering.

---


Now let's move on to the **scattering matrix**. You have two terms:

1. The **identity matrix** ($\mathbb{I}$)
2. The **transition matrix** ($T$)

This means when we have scattering where basically nothing happens, we use the identity matrix. Here is where the interaction is then included.

Because of the way it's written—it's not clear—let me write it again:

$$
S = \mathbb{I} + 2\pi i \, T
$$

This means **no interaction**.

An important condition we have is that the probability of finding a system in a certain state must sum to one.

- You can have a sum of different possibilities for the probability, and the total should always be one.
- We can't have more than one, so the total conservation of probability is given for $n$ different states for a certain initial state.

This is just the identity. If you take any two different orthogonal states, this conservation of probability means that $S$ has to be a **unitary matrix**. This condition is called **unitarity**:

$$
S^\dagger S = \mathbb{I}
$$

If you now use what we have written down for the scattering matrix—the identity matrix plus $2\pi i$ times the transition matrix $T$—let's put this into the unitarity condition and see what comes out.

This has to satisfy the unitarity condition. What we can do is cross this out and move these two terms, for example, to the other side. You can also divide by $2\pi i$.

---


When we want to calculate, for example, a **cross section** or **transition probabilities**, we do it like this:

1. We have an initial and final state
2. Then the transition between them

If you put this condition here, you sum over different states. In principle, you can also write this as an integral over the **phase space**.

If we look at an initial and final state, we can:

- Sum over all the different spin projections
- Write it either as a sum or as an integral over the phase space

These are basically the **phase space vectors** that come in.

When you insert identity, it's written as the integral over possible states. Here's the insertion of that identity, and it comes within the phase space.

So identity then—if you have two particles with two momenta, the identity can be expressed as the integral over the phase space of these states:

$$
\mathbb{I} = \int d^3p_1 \, d^3p_2 \, (2\pi)^4 \delta^4(p_0 - p_1 - p_2)
$$

When you insert identity, you integrate over all momentum. You don't constrain particles to be on-shell in energy, only in mass. So it's not a $\delta^5$ but rather $d^3p_1 \, d^3p_2$.

The phase space comes once you add the delta function constraint:

$$
(2\pi)\delta(E_2 - E_1 - E_2)
$$

and then for each particle. The difference between phase space and this integral is the $\delta^4(p_0 - p_1 - p_2)$, the energy-momentum conservation that comes from the matrix element.

From any of that, it comes with a $\delta^4$ for energy-momentum conservation, like this:

$$
\langle f | T | i \rangle \propto \delta^4(p_f - p_i) \cdot \mathcal{M}
$$

---


Now let's think about the **scattering amplitude**. Here we have two particles, 1 and 2. We can look, for example, in the **center-of-mass system** where we define the $z$-axis in the direction of motion of $p_1$ and $p_2$.

They are just 180 degrees to each other. Here we have the **scattering angle** $\theta$. In the center-of-mass frame, the momenta are equal and opposite to each other.

This we can then express as the scattering amplitude part and then a part where we have momentum conservation. This scattering amplitude depends on variables like $s$ and $t$.

In practice, we usually fix, for example, $t$ and then look at the $s$-dependence. We can write the scattering amplitude and decompose it into different **partial waves**:

$$
A(s,t) = \sum_j (2j + 1) \, A_j(s) \, P_j(\cos \theta)
$$

A **partial wave expansion** means we decompose the scattering amplitude into an infinite series of these partial waves, where we sum over the spin $j$.

Here we have the **Legendre polynomials** describing the angle dependence. Then you have a term that depends on $s$ minus some variable—this is where the mass dependence goes in, describing the resonance, its mass, width, and so on.

This is practical because what we measure in experiments are **angular distributions**. We know that if you're looking for certain states or resonances, they have a definite spin $j$.

When we do this partial wave decomposition, we can divide up the different contributions we see in the data, making it easier to recognize new states.

These Legendre polynomials can be related to the **Wigner $D$-functions**. I also want to write this down in the notation we had previously, with helicity states.

For example, with two particles, we have the angle $\theta$ and an azimuthal angle $\phi$. This is another way to write this, where we now have the partial wave amplitudes as a reminder:

$$
A(s, \theta, \phi) = \sum_j A_j(s) \, D^j_{\lambda \lambda'}(\theta, \phi)
$$

The big Wigner $D$-functions depend on $\theta$.

---


Before we discuss how to parameterize the mass dependence here, let's first look at what the **unitarity constraints** mean for the scattering amplitude and for $A_j$.

You can see up there the unitarity constraint. If you apply this to the scattering amplitude—and for the partial waves, you can also write this down—$\rho$ is the phase space factor.

What does it mean? These are complex numbers, so you can write this as the real part $A$ plus $i$ times the imaginary part of $A$, and this with a minus in between.

What remains here is $2i$ times the imaginary part if we subtract this.

This is what the unitarity constraints mean for the scattering amplitude and the partial waves. What I want to discuss next is how we can describe the energy dependence for this.

We have already discussed a couple of times that what we can see, for example in the cross section, is a peak which we then call a **resonance**.

The question is: how can we describe this? If we have, for example, two particles where we added the four-momenta and then looked at their mass, and we see a peak-like structure here.

One of the easiest ways to describe this shape is with a **relativistic Breit-Wigner amplitude**:

$$
A(s) = \frac{g^2 \, \rho(s)}{M^2 - s - i M \Gamma(s)}
$$

where:

- $M$ = mass of the resonance
- $\Gamma$ = coupling of the resonance to the initial and final state
- $\rho(s)$ = phase space

We are not just interested in the mass, but also what the width here is. This is, in this case, related to this part. So this is roughly the width divided by two.

This type of concept works well when we have an **isolated resonance**. One really good example for this is the $\Delta(1232)$ resonance, where the mass is at 1232 MeV.

The next $\Delta$ resonance that we have in the spectrum comes at around 1600 MeV. We can safely assume that it is isolated enough so we can use this kind of amplitude to describe it.

We also talked briefly about what kind of width to expect. It's very different, depending on what kind of states you're looking at.

- If you are in the **low-mass quark region**, like we have the $\Delta$ or the nucleon resonances, there we have widths of over 100 MeV.
- If we are in the **heavy quark sector**, then most of them are so narrow that the width is just given by the detector resolution.

Since we have been talking about unitarity, one important thing here is that for a single isolated resonance, the Breit-Wigner description fulfills unitarity.

Unfortunately, in experiments and in reality, we often have the situation where we have **overlapping resonances**, and simply summing up two Breit-Wigners, for example, would not give us unitarity. The unitarity condition would then not be fulfilled.

What we do then instead is to basically start from unitarity and construct a matrix called the **$K$-matrix**, which fulfills unitarity:

$$
T = K (\mathbb{I} - i \rho K)^{-1}
$$

This is what we want to do next.

> [!IMPORTANT]
> **Correction**: The denominator of the amplitude has $g^2$ times $\rho$, which is mass times width, not just $\Gamma$. So it's not $\Gamma$ over two. It's $M \Gamma$.

Let's start with our unitarity condition. We can now bring one of the $T$'s to the other side and also split this up. So we have here $2i$ times the identity matrix.

What we get is we bring this here. This part here is what we call the $K$-matrix $N^{-1}$. Since there's an equal sign between this means that $K$ has to be **Hermitian**.

If we want symmetry between going from an initial state to a final state and the other way around, having the final state as the initial state going to it, then we know that $K$ has real values and is symmetric.

Instead of writing here the transition matrix, we can also write it as the phase space matrix times the invariant matrix and then square root of again phase space matrix.

We can also write $K$ in terms of $T$. In principle, with this kind of definition, either with $T$ or with this invariant matrix $M$, we can expand this into an infinite series with this $K$-matrix.

This $K$-matrix describes here this interaction. Here we have also terms where we have some intermediate state here, or more than one, and so on. This can be expanded into this infinite series.

Now I want to discuss two cases that we have, for example, one single resonance in one channel and how this $K$-matrix can be then modeled.

If you have one resonance and it can only decay into one single channel, this is how we can parameterize it:

$$
K = \frac{g^2}{M^2 - s}
$$

We have again coupling constants, the mass of the resonance, and $s$.

If we now plug this into the invariant matrix, the invariant amplitudes—so what we get out if we do this—is we get again the Breit-Wigner amplitude out.

For the single resonance case, this Breit-Wigner parametrization gives us also unitarity. This is what we also get out using this $K$-matrix approach.

In general, the width can also depend on $s$. So that's not a constant width.

## Two-Resonance Dynamics and Unitary Constraints in Scattering Theory


Now let's think about **single-channel two resonances**. Imagine we have this plot with two peaks. What we can see here is that this does not correspond to the sum of two $\pi$ thresholds. We also don't want this because it doesn't fulfill unitarity.

---

If the masses of the two resonances are far apart, this part would vanish, and we would have just the sum of two Breit-Wigner peaks:

$$
f(E) = \sum_{j=1}^2 \frac{g_j^2}{E - E_j + i\Gamma_j/2}.
$$

In this case, they are so far apart that we can consider them **isolated**. If the masses were the same, we would get just one single peak.

---

> [!IMPORTANT]
> The Breit-Wigner formula describes isolated resonances:
> $$f(E) = \frac{\Gamma/2}{(E - E_0) + i\Gamma/2}$$
> For two resonances, we sum their individual contributions when they're far apart.

---

We have only a couple of minutes left. One important thing to remember is that we are looking at:

* The **imaginary part** of the partial wave
* The **phase shifts**

We expect to see:
- A peak in the imaginary part
- In the real part, we see a phase motion going through zero

---

The best way to intuitively understand this is to think back to mechanics. In a thought experiment with an external frequency scan, you would observe:

1. A resonance at a certain eigenfrequency
2. A phase motion going through 90 degrees

This is similar here: for a resonance state, we also see this phase motion.

---

This ideal behavior only occurs for an **isolated resonance**. With overlapping resonances, it becomes much more complicated to determine:

* How many resonances there are
* How to parameterize them

---

Probably about 5. We already have this from the nuclear top machine. The Argand diagram plots:

- The imaginary part against the real part of $F$
- Forms a circle

We can examine specific values on this circle.

---

For elastic scattering, the energy dependence describes the unitary circle:

$$
(\text{Re}\,f)^2 + \left(\text{Im}\,f - \frac{1}{2}\right)^2 = \left(\frac{1}{2}\right)^2.
$$

Different points on the circle satisfy this equation. For example, at 45 degrees, we would get $1/2 + i/2$.

---

The circle is centered around $(x_0, y_0)$ with radius $R$. For non-elastic scattering:

* There is a deviation from this circle, moving inward
* If unitarity is not fulfilled (as in the case of two-body weakness), the trajectory would go **outside** the unitary circle

## Adjusting Deadlines and Plotting Parameters for Data Analysis


- **Deadline clarification:**
*"So you set the deadline for Sunday, but I do think you have to solve the updated problem. When is the deadline for week seven? For now, I just set it by default."*

- **Moodle update:**
*"They can upload it now on Moodle. I will update the deadline."*

> [!NOTE]
> The speaker acknowledges being over time:
> *"Sorry to be a bit over time again."*

---

For better data visualization:
1. *"make the plotting bigger in a wider range"*
2. *"make the width smaller"*
**Result:** *"Then you really see the structure."*

---

- *"Is there anything important if you begin before? We can start the next step."*
- *"That's a great idea, actually. I was about to suggest exactly that."*
- *"No, it won't. It's not actually. Can you see it there?"*

