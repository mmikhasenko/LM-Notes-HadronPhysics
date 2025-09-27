### Recording and Transcribing Lectures with Whisper


My experiment with recording lectures has been **relatively successful**, so I could recover what I was speaking.

::: callout-note
**Speech-to-Text Technology:**
There is an open large language model from OpenAI called **Whisper** that can translate audio to text. Since the architecture is known, it runs even on CPUs in parallel, such as on a Mac. You just:

1. Download it
2. Execute it
And then you have a transcript of your speech.
:::
---

*Important notes about recording:*

- The lecture is recorded
- I do it for myself
- It might be converted to a document

::: callout-tip
**Collaboration Opportunity:**
If someone would volunteer to:

* Type the questions
* Add the equations
* Check them
That would be helpful.
:::
---

I don't know what to do with that yet, but just *for fun* and for exploring the technologies, I will keep the recordings.

**Important limitation:**
It records only me in the sense that it mostly captures my voice. Don't hesitate to talk back, as this will not appear in the recordings anyway.

### Isospin Assignments and Matrix Representations for Hadrons


Today we will discuss **structure functions**, the structure of hadrons, their internal composition, and how we study them.
Before diving deeper, let’s start with a recap and address a few questions. These questions will remain on the board for later discussion.

---

**Question 1**: Without consulting the PDG, determine the isospin of these particles based on their quark content:

- $c \bar{s}$
- $b q$
- $b s$
- $q \bar{q}$

**Question 2**: What is the dimensionality of the isospin matrix acting on a system of three quarks with two possible charges?
If we treat the quarks as a wave function in two dimensions—where spin-up corresponds to the $u$-quark and spin-down to the $d$-quark—what is the size of this matrix?

**Question 3**: What are the irreducible representations of this matrix’s action on the quarks? In other words, how does it decompose into independent blocks that do not interact?

---

When discussing isospin, we focus on **light quarks**. The first meson, $c \bar{s}$, contains no light quarks, so its isospin is $0$.

For the $B$-mesons:

- If the quark $q$ is light (e.g., $u$ or $d$), the isospin is $\frac{1}{2}$.
- If $q$ is heavy (e.g., $c$ or $b$), the isospin is $0$.

The $s$-quark belongs to the light quarks in $SU(3)$ but is excluded in isospin discussions. For the $b s$ state, if $s$ is the only light quark, the isospin is $\frac{1}{2}$.

For a pentaquark with three light quarks, the isospin matches that of the $\Delta$-baryons. The $\Delta$ states ($\Delta^{++}$, $\Delta^+$, $\Delta^0$, $\Delta^-$) have isospin $\frac{3}{2}$.

---

::: callout-important
**Clarification**: When assigning isospin to a particle, we refer to the **length of the isospin vector**, not its projection. For example, the $B$-meson’s isospin $\frac{1}{2}$ implies two charge states:

- $B^+ = b \bar{u}$
- $B^0 = b \bar{d}$

The antiparticles are fully conjugated:

- $B^- = \bar{b} u$
- $\bar{B}^0 = \bar{b} d$

These form a separate triplet in the antiparticle space.
:::
---

1. **Isospin assignments for mesons**:
$$
I = \begin{cases}
0 & \text{(no light quarks)} \\
\frac{1}{2} & \text{(one light quark)} \\
1 & \text{(two light quarks)}
\end{cases}
$$

2. **Isospin of the $\Delta$-baryon**:
$$
I_\Delta = \frac{3}{2}
$$

3. **Dimensionality of the isospin matrix for three quarks**:
$$
\text{dim}(\mathbf{I}) = 8 \times 8
$$

4. **Irreducible representations for three quarks in $SU(2)$**:
$$
\mathbf{2} \otimes \mathbf{2} \otimes \mathbf{2} = \mathbf{4} \oplus \mathbf{2} \oplus \mathbf{2}
$$

- $\mathbf{4}$: Symmetric (spin-$\frac{3}{2}$, like $\Delta$).
- $\mathbf{2}$: Mixed-symmetry (spin-$\frac{1}{2}$).

5. **Charge states of $B$-mesons**:
$$
B^+ = b \bar{u}, \quad B^0 = b \bar{d}, \quad B^- = \bar{b} u, \quad \bar{B}^0 = \bar{b} d
$$

### Spin and Charge Combinations in Quark Systems


Now, **Cascade B** has spin **1/2**.

- **1/2** means that the dimensionality is $2J + 1 = 2$.
- There are two particles of this type: **Cascade B** and **Cascade B**.

---

Now, the **charges**.
The quark charges are:

- **Lower row (D, S, B)**: $Q = -\frac{1}{3}$
- **Upper row (U, C, T)**: $Q = +\frac{2}{3}$

When I combine three lower-row quarks like **DDD**, the total charge is $-1$.
If I combine three upper-row quarks like **UUU**, the total charge is $+2$.
*Intermediate combinations give other values.*

---

Here, I combined **B** and **S**.

- I almost have the full bottom row: **B** and **S**.
- If I had another lower-row quark, the total charge would be $-1$, but instead, I have an upper-row quark, so the total charge is **zero**.
- That's why it's zero here.
- If you replace it with a lower-row quark, you get $-1$.

---

Now we come to the last case, which has **three quarks** and several possible combinations.

- What is the spin of this state?
- What are the possible combinations for spin **1/2** (P-C plus and P-C zero)?
- For spin **3/2**, I will have P-C.
- The **1/3** means four particles in the multiplet, like **Delta plus-plus**.

::: callout-note
The dimensionality of the isospin matrix acting on three quarks is $2^3 = 8$.
We have an $8 \times 8$ matrix, but we can split it into irreducible representations.
:::
---

An interesting question: What is the antiparticle for **P-C plus**?

- For **P-C plus**, the antiparticle is not **P-C minus**—it's **P-C plus bar**.
- For baryons, it's important to distinguish baryons from antibaryons because they have different quark components.

---

Now, let's discuss the **irreducible representation** of the three quarks.
Combining three spin-**1/2** particles:

1. First, combine two spin-**1/2** particles to get spin-0 or spin-1.
2. Then, combine the result with the third spin-**1/2** particle.
3. The dimensionality check: $2 \times 2 \times 2 = 8$ matches $2 + 2 + 4$.

---

To construct the basis for the highest isospin state, start with $|uuu\rangle$ and apply the lowering operator:
$$
J_- |J, J\rangle = \sqrt{2J} \, |J, J-1\rangle
$$
For $J = 3/2$, this gives:
$$
J_- |3/2, 3/2\rangle = \sqrt{3} \, |3/2, 1/2\rangle
$$
The normalized state is:
$$
|3/2, 1/2\rangle = \frac{1}{\sqrt{3}}(|uud\rangle + |udu\rangle + |duu\rangle)
$$

---

For the spin-**1/2** states, we construct orthogonal combinations:
$$
|1/2, 1/2\rangle = \frac{1}{\sqrt{6}}(2|uud\rangle - |udu\rangle - |duu\rangle)
$$
Applying the lowering operator gives:
$$
|1/2, -1/2\rangle = \frac{1}{\sqrt{6}}(2|ddu\rangle - |dud\rangle - |udd\rangle)
$$

---

The same logic applies to higher spins.

- For example, combining two spin-1 particles gives spin-0, spin-1, or spin-2.
- The dimensionality check: $3 \times 3 = 1 + 3 + 5$.

This is **standard spin algebra**, applicable to both integer and half-integer spins.
The key is to start with the highest state and use lowering operators to construct the rest.
**Normalization and orthogonality** are ensured by Clebsch-Gordan coefficients.

---

For practical calculations, you can derive these coefficients using ladder operators.
For example, the spin-1 triplet states are:
$$
|1, 1\rangle = |\uparrow \uparrow\rangle, \quad |1, 0\rangle = \frac{1}{\sqrt{2}}(|\uparrow \downarrow\rangle + |\downarrow \uparrow\rangle), \quad |1, -1\rangle = |\downarrow \downarrow\rangle
$$
The singlet state is:
$$
|0, 0\rangle = \frac{1}{\sqrt{2}}(|\uparrow \downarrow\rangle - |\downarrow \uparrow\rangle)
$$

---

This method works for **any spin combination**.
For three quarks, the irreducible representations are:

- A **quartet** (spin-**3/2**)
- Two **doublets** (spin-**1/2**)

The same principles apply to **isospin** and **flavor SU(3)**, though SU(3) is more complex.
For **SU(2)**, it’s straightforward spin addition.
You need to be comfortable with:

- Dimensionalities
- Lowering operators
- Orthogonal combinations

---

This is **foundational** for:

- Quantum mechanics
- Particle physics
- Group theory

**Practice is essential**—start with simple cases and build up.

### Symmetries and Construction of the Proton Wave Function in SU(4) Space



In order to proceed and talk about structure functions, today in the lecture we need to get the proton wave function, because that's something from which the understanding of the internal structure of the hadrons comes.
In the homework, you will have other questions related to the delta's internal structure.

---


I would like to start with the symmetries of the baryon wave function.
We have to operate in the $SU(4)$ space.
One of them is **color**, which we've already discussed.
The baryon wave function would have color indices and must be color-neutral, as all hadrons are.

We have to work with:

1. A **space wave function** that essentially describes how the wave function is distributed in space—its dependence on $x$ and time $t$.
2. **Isospin**
3. **Spin**

::: callout-important
It's important to realize that, in the general case, they are **not factorizable**.
You cannot say you have to deal with the product of the functions.
The wave function lives in this product of the four spaces and can mix the spaces.
You need to have a sum of the components in these spaces.
It would be unfair to write, in the general case, isospin times the rest—not true in general.
:::
---


The color wave function is a **singlet**, meaning it's a number, a scalar; it doesn't have dimensionality in components.
Therefore, the color wave function can be factored out.

There is a good argument why the space wave function is a scalar and can be factored out as well.
I haven't convinced myself of that, but one should find the argument for it in the literature.
That's something I ask you to take as given—I don't have a good justification.

So the wave function for coordinate dependence will also factorize.
What remains is **spin and isospin**, and these two do not factorize.
That's a large-dimensional representation.

---


We are going to deal with baryons made of three quarks, and every quark has a spin.
So we are still working with the same group, but now we have many dimensions.
Every quark is the product of two: **flavor** and **spin**.
And since it's a product of three quarks, we are going to deal with a basis in six dimensions.
It's the same thing as before.

To build the representation of particles in these six dimensions, we are going to act with the lowering operator, starting with something we know—one we know with no ambiguities: the delta, which has spin $\frac{3}{2}$.

When the delta has spin $\frac{3}{2}$, the only combination we can come up with is $|\!u\!\!\uparrow u\!\!\uparrow u\!\!\uparrow \rangle$.
The $\Delta^{++}$ with $J_z = \frac{3}{2}$ is obtained by acting with the lowering operator.

---


What happens if we act with the lowering operator in the isospin space? $G_-$ acting on $|\!u\!\!\uparrow u\!\!\uparrow u\!\!\uparrow \rangle$.

- If we act with the lowering operator in the **spin space**, we reduce the projection.
- If we act with the lowering operator in the **flavor space**, we reduce the charge and obtain a different particle: the $\Delta^+$.

Then you can think about how to construct $\Delta^-$, $\Delta^0$ with $J_z = \frac{1}{2}$.
We need to act twice with the lowering operator in the flavor space and once with the lowering operator in the spin space.

---


Now, the proton appears as a wave function that is orthogonal.
So,
$$
\frac{1}{2} \otimes \frac{1}{2} \otimes \frac{1}{2} = \left( \frac{3}{2} \right) \oplus \left( \frac{1}{2} \right) \oplus \left( \frac{1}{2} \right)
$$

This is $4 + 2 + 2$ dimensions.
The proton is the particle made of the same quarks as the delta but has isospin $\frac{1}{2}$ and spin $\frac{1}{2}$.
Therefore, we have to construct a wave function that is orthogonal in both spin and isospin spaces.

That's one way—we're not going to do that because it's not super clear to you yet.
I think it's just technically complicated, but you would be able to do it if you sit and work on it for a few hours.

---


What we are going to do is explore the symmetry.
The baryon wave function in the symmetric configuration is symmetric.
This is a new symmetry—we haven't discussed this yet.
It's not related to $SU(2)$ directly; it's something new we’ve introduced.

We are now going to swap dimensions—just take one particle with its spin and isospin and swap it with another.
This is sort of an external look at those symmetries.
We have a basis function that we construct, and now we can examine whether they have certain permutation symmetry.
We didn't intend to construct them with built-in symmetry, and we will see that most of them have no symmetry—they are not eigenstates of permutation.

---


But before doing that, let's see what we actually demand from the function.
The total $\psi$ must be symmetric under permutation.
So, $\psi_{\text{antisymmetric}}(1,2,3) = -\psi(2,1,3)$.
Here, we essentially swap the dimensions of particle 1 and particle 2.

The color wave function is antisymmetric.
To see this, you need to examine its form because this is a different group—color transforms under $SU(3)$.

In three dimensions, there are three colors, and in that case, it's not as simple as spin algebra.
The representations of $SU(3)$ are more complicated: there are decuplets, octets, and that comes from combining three quarks.

$$
\mathbf{3} \otimes \mathbf{3} \otimes \mathbf{3} = \mathbf{1} \oplus \mathbf{8} \oplus \mathbf{8} \oplus \mathbf{10}
$$

These are dimensions—not spins.
Three times three times three equals $1 + 8 + 8 + 10$ (27 total).

The singlet is 1, and the wave function for the singlet can be constructed similarly to what we discussed.
But you see that it's easiest to start with the highest-dimensional representation (the 10) because for them, you would know.

For the 10, you would start with $|RRR \rangle$ and act with the lowering operator to get the full multiplet.
Then you construct the octets—there are two of them—and for components like $|RGB \rangle$, $|RBG \rangle$, etc., you need to find combinations that match.

But the answer is essentially that the totally antisymmetric combination is:
$$
\psi_{\text{color}} = |RGB\rangle - |RBG\rangle + |GRB\rangle - |GBR\rangle + |BRG\rangle - |BGR\rangle
$$

It's easy to write down if you start with one term and add all permutations, where the sign depends on whether the permutation is odd or even.
All even permutations have a plus sign, odd permutations have a minus sign.
From this, you find that the color wave function is antisymmetric under permutation—if you swap two, you get a minus sign.

The space wave function is symmetric—we are talking about ground-state baryons, which are in the simplest symmetric configuration.
Now, the spin + isospin wave function must be symmetric.

---


Let's do an example of the combinations we are allowed to work with.
In order to construct a wave function for a proton, we have to combine it in the representation that has isospin one-half and spin one-half.

Let's examine some of these basis functions.
Is this symmetric or antisymmetric under permutation? Well, it depends on which particles I pick.
If I pick particle one and two and swap them, this doesn't change.
This one becomes $D U U$, and that one becomes $U D D$.
The plus sign remains, and there is a plus $D U D$, $D U U$, and minus.
So essentially, the function is different—it doesn't have a definite symmetry under permutation; it just goes to different wave functions.

However, it's symmetric under permutations of quarks 2 and 3.
If I take these two and permute them, these terms stay the same, and this series remains unchanged.
So we construct a spin wave function that is symmetric only under the permutation of 2 and 3.
And that's what one observes.

The proton wave function can be essentially guessed by combining spin: combining $\frac{1}{2}$, $\frac{1}{2}$ spin, $\frac{1}{2}$ in flavor—symmetric flavor and symmetric spin.
Here we have symmetric, and that was antisymmetric.
You see, under the permutation of the screen, if I swap 2 and 3, the wave function becomes that but with a minus sign.
Therefore, it's antisymmetric.
Symmetric under 2-3, antisymmetric under 1-2.

In order to build the proton wave function, I take the flavor representation from here and combine it with the spin wave function.
The spin wave function is from here again, but instead of $U$ and $D$, I'm going to write up and down.

What does this tell us? That it is not symmetric in the first two particles?
It tells us that it's illegal to use that.
We cannot use it.
It does not represent a valid baryon wave function.
If we use just this term without that, it would be illegal.
The point is that the wave function transforms into another wave function.

When we combine three quarks, we get the spin-$\frac{3}{2}$ representation and two spin-$\frac{1}{2}$ representations.
If I apply the permutation operator to this, it leaves the representation.
So the matrix that permutes is no longer decomposable in this representation.
Since this permutation operator is external to the group (it doesn't belong to the rotation group), it's not the same as rotating.
Therefore, we effectively see that this multiplet mixes with this one.
To construct the proton, we need both of these spin-$\frac{1}{2}$ dimensions, and that's essentially what we do.

One more comment on the same line: The delta lives here.
The delta is a valid baryon.
If I apply the permutation to this multiplet, I stay within the same multiplet.
But for the proton, it lives in the mixture of these two.

Now, one has to do the algebra to find the answer, and then it's going to be...
So the proton wave function is going to be—I'll write these components—the proton is spin-up, where one diagonal is going to be $U U D$, $U D U$, $D U U$, and off-diagonally done.
If you guys are satisfied with that, you should recover it.

The other combination is up-up-down, up-down-up, down-up-up.
The way I—this is what I just worked out, and that's the answer for the matrix.
I show the coefficients in the basis of $U$ and $D$, in the basis of three quarks of different flavors with different spin orientations.
Along the rows, I put the same quark content; among the columns, I have the same spin orientation.
So here it's going to be $U D$—same spin up-up-down, but then particle number is going to be $U D U$.

And now, the normalization part quickly: all of them are orthogonal to each other, so the normalization just comes by summing these numbers straight: 4, 4, 4, 12 plus 6, 18.
We have it—we have the wave function of the proton.
Now we can evaluate the cool properties of the proton.
That came as a surprise.

---

::: callout-note
The proton wave function construction involves combining symmetric and antisymmetric components in spin and flavor spaces to satisfy the overall antisymmetry requirement due to the color wave function. This ensures the Pauli exclusion principle is obeyed for the quarks inside the baryon.
:::
### Probing Proton Structure: Elastic Scattering, Form Factors, and the Three-Quark Model


Now, let's discuss **three studies of structure**.
One of the ways we study and examine the structure is to use something we know very well.
We take actually one of the simplest and first questions we can answer: *What is the charge distribution inside the hadron?* That's done with the electron probing the charge.

When we scatter an electron off a hadron in this reaction, almost all variables are fixed.
Essentially, the **center-of-mass energy** is fixed, and then there is just one variable remaining that describes the entire kinematics: the **angle**.
When I scatter two particles and the energy is fixed, there is just one angle.

---

Therefore, the experiment on the **structure functions**—the experiment that helps us understand the proton structure—is **electron-proton scattering**, observing the probability of the electron going in different directions.
With the scattering experiment, we measure the **angular distribution**.
From this, we gain insights into the proton's **charge distribution** and **magnetic moment**.
That's called a **scattering experiment**.

It's important to realize we will write many variables, like the $Q^2$ momentum transfer, but it's all encoded in one.
Essentially, you need to know the probability for the electron to go forward slightly.
The kinematics in the lab frame look like this: the proton collides with the electron, and then the electron goes in a certain direction.

---

This is a simple **two-body scattering matrix**, and the only variable that determines everything is the angle.
So, what's the probability for the electron to scatter? Will it have almost no change in direction, or will it go perpendicular? That determines the proton's internal structure.
It's amazing to think this way.

Those who took nuclear physics before can easily tell me: *what is the most probable outcome?* Where will the electron go—perpendicular, 30 degrees, 20 degrees? Do you have a feeling?

::: callout-note
The **Rutherford scattering formula** for point-like particles is:
$$\frac{d\sigma}{d\Omega} \propto \frac{1}{\sin^4(\theta/2)}$$
This explains the huge peak at small angles in the scattering probability.
:::
Something you might remember is the $\frac{1}{Q^4}$ Rutherford scattering term, $\frac{1}{\sin^4(\theta/2)}$.
There's a huge peak at around zero angle in the probability.
Most of the time, the electron prefers to go straight with zero scattering angle.
The deviation from that behavior tells us about the proton's structure.

---

That process is called **elastic scattering**—where initial particles are the same as the final state particles.
In contrast, **inelastic scattering** is another important process where we probe the proton's structure, and the proton dissociates.
Here, the proton stays intact in elastic scattering, but in inelastic scattering, the electron and proton produce many different particles.

The result for the **differential cross-section** is derived from non-relativistic scattering, and you get the same even for point-like particles.
An example of a point-like particle is the electron—it has no internal structure.
If you scatter electrons or muons, you get an ideal cross-section of $\frac{1}{\sin^4(\theta/2)}$.

---

Elastic scattering has this huge peak at zero angle in the probability.
If you calculate the diagrams for QED, you write the matrix element as $\bar{u}\gamma^\mu u$, with propagators and spinors.
For this course, we analyze it generally, so we won't go into details, but it's important to understand dimensionalities and the objects themselves.
The matrix element is a **scalar**—it has no dimensionality, just a number obtained by contracting structures like spinors and gamma matrices.

When dealing with the proton, we extend the vertex function with **form factors**.
What's the dimensionality of this object? It's a simple function of $Q^2$.
It's convenient to introduce combinations of these form factors: the **electric and magnetic form factors**, $G_E$ and $G_M$.

---

In non-relativistic theory, they have a straightforward interpretation—they show the **charge and magnetic distributions in momentum space**.
We can transform these to coordinate space via **Fourier transform**.
The normalization of these form factors is fixed:

- $G_E(0)$ gives the total charge (**1 for the proton**),
- $G_M(0)$ gives the magnetic moment.

The **magnetic moment** is a quantity that reacts to a magnetic field.
For an electron, it's $\frac{e}{2m_e}$ (spin 1/2).
For the proton, it's different due to its structure.
Experimentally, the proton's magnetic moment is about **2.79**, not 1 as naively expected.

---

This discrepancy arises because the proton is made of **quarks**.
In the quark model, we account for quark charges ($\frac{2}{3}$, $-\frac{1}{3}$) and masses.
The proton's magnetic moment comes from the **wave function structure**, and the result matches experiment surprisingly well.
For the neutron, it's **-1.91**, again showing internal structure.

In summary, just knowing **SU(2) and spin algebra**, we can build the proton wave function and understand its magnetic moment—a clear sign the proton isn't point-like.
In the homework, you'll work with the **Δ baryon's wave function** and magnetic moment operator.

Apologies for running late, but thank you for your attention.
We spent a lot of time on these **foundational concepts**, but they're crucial.
I hope to discuss more in future lectures.

---

Another interesting thing here was the way to understand that there are **three parts inside a proton**.
I remember from color? No, from scattering.
From scattering, yeah.
So how do you address three colors? Not three colors, but three quarks.
But not three colors.
Exactly.
Three quarks.

Because—let's think of the foil.
So if protons they—correct.
I think it's also coming from various form factors.
Form factors? From experiment.
And you see the distribution of these form factors.

Nice.
I don't think the mission is the magnetic moment.
I think because it really comes from some experimental distribution.
But I'm not sure which exactly observable it was.

I remember three generations of particles comes from the widths of the W boson.
But this is—it's completely different.
Three colors? It's the spectroscopy of the mesons.
So that's the Eightfold Way.
Because at this time, I think it was only part red.
But now three quarks in the problem.

Why does it—I think it's related to colors because only with three you can get an octet and decuplet.
Yeah, but I'm talking about experiments.
Yeah, at the time they were not great.
Good point.
Good question.

---

::: callout-note
Key experimental values for magnetic moments:

- Proton: $\mu_p \approx 2.79 \frac{e}{2m_p}$
- Neutron: $\mu_n \approx -1.91 \frac{e}{2m_p}$
These values arise from the proton's quark structure and wave function.
:::