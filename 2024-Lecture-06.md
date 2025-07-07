## Lambda Baryon Decay: Weak Interaction, Matrix Elements, and Helicity States


Let's start with the recap.
The physics reaction to consider is the lambda baryon decay into a proton and pion:
$$
\Lambda \to p + \pi^-
$$

We go through our **standard checklist** to understand this reaction:

1. What type of interaction is responsible?
2. What variables describe the process?
3. Write the matrix element for the process.
4. Calculate the polarized decay width.

Take two minutes to think about these items, and then we'll discuss.

---

What interaction is responsible? I like drawing cartoon diagrams (not Feynman diagrams) to visualize this. Here’s the lambda decaying into a proton and pion, with a block representing the interaction.

Is this a **strong interaction**? No, it’s **weak** because flavor is changing:
$$
u, d, s \to u, d, \bar{u}d
$$
The strangeness changes, and strangeness transitions can only occur via weak interactions. Strong interactions preserve flavor.

Since this is a weak interaction, **parity is not conserved**. This decay violates parity.

---

Now, the first item is to check the particles. The second is: what variables describe the process, and how many are there?

This is a **one-to-two transition**, and we work in the **center-of-mass frame**. The lambda is at rest initially, and the proton and pion are the decay products. The momentum magnitude is fixed by the particle masses. There is no orientation in space, so no angular variables. The only direction is given by the momentum, and we can align the $z$-axis with it.

---

Next, the matrix element. The amplitude for this process is denoted $H$. What does $H$ depend on? No variables, because the kinematics are fixed. The only dependencies are the discrete spin projection indices.

The particles involved have spins:

- **Lambda**: $J^P = \frac{1}{2}^+$
- **Proton**: $J^P = \frac{1}{2}^+$
- **Pion**: $J^P = 0^-$

Since parity is not conserved, the **spin structure matters**. By angular momentum conservation, the proton’s spin projection must match the lambda’s.

The matrix element is written as:
$$
H_\lambda = \langle p(\vec{p}, \lambda_p), \pi^-(-\vec{p}) | T | \Lambda(0, \lambda_\Lambda) \rangle
$$
Here, $\lambda_\Lambda = \lambda_p$ due to spin conservation. The initial state is on the left, and the final state on the right.

The pion is spinless, so its state is $|0, 0\rangle$. The proton has helicity $\lambda_p$, and the lambda has spin projection $\lambda_\Lambda$.

The amplitude $H_\lambda$ has two values: $\lambda = \pm \frac{1}{2}$.

---

Next, the unpolarized decay width:
$$
\Gamma = \frac{1}{2m_\Lambda} \frac{1}{2} \sum_\lambda |H_\lambda|^2 \frac{|\vec{p}|}{8\pi^2 m_\Lambda}
$$
The phase space integral simplifies to 1 because the kinematics are aligned.

This decay is the **main channel** for lambda decay, determining its lifetime of about $10^{-9}$ seconds. In experiments, the lambda is identified by its decay to a proton and pion, with charged tracks pointing to a secondary vertex.

::: callout-note
Did I forget the $\frac{1}{2}$ from $\frac{1}{2J+1}$? No, it’s absorbed correctly because only two terms survive in the sum.
:::
This becomes more interesting when there’s a **preferred direction** in space, such as when the lambda is moving. The direction of motion provides a reference axis, and we can study the decay in the helicity frame.

---

Now, let’s discuss helicity states in more detail.

The $|JM\rangle$ states are basis states for a particle with spin $J$, quantized along the $z$-axis with projection $M$. Acting with $J_z$ gives:
$$
J_z |JM\rangle = M |JM\rangle
$$

We use **active transformations**: rotating or boosting the particle, not the coordinate system. For example, boosting a particle along the $z$-axis increases its momentum without changing its spin projection.

Rotating a state about the $y$-axis mixes the spin projections. The coefficients are given by **Wigner D-functions**:
$$
D^J_{m'm}(\theta) = \langle Jm' | e^{-i\theta J_y} | Jm \rangle
$$

For **spin-$\frac{1}{2}$**, the rotation matrix is:
$$
R_{1/2}(\theta) = e^{-i\theta \sigma_y / 2} = \cos\left(\frac{\theta}{2}\right) - i\sigma_y \sin\left(\frac{\theta}{2}\right)
$$

---

For a moving particle, there are two ways to define spin states:

1. **Helicity states**: Spin quantized along the direction of motion.
2. **Canonical states**: Spin quantized along the $z$-axis.

These are related. A helicity state is constructed by boosting and rotating a canonical state:
$$
|p, \lambda\rangle = R(\hat{p}) B_z(p) |0, \lambda\rangle
$$

When you rotate a helicity state, the momentum rotates but the helicity remains the same. Boosting is trickier because it changes the momentum direction relative to the spin.

The **Lorentz boost matrix** for a 4-vector is:
$$
B_z(\beta) = \begin{pmatrix}
\gamma & 0 & 0 & \gamma\beta \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
\gamma\beta & 0 & 0 & \gamma
\end{pmatrix}, \quad \gamma = \frac{1}{\sqrt{1-\beta^2}}
$$

For canonical states, you first rotate the particle, then boost it. This ensures the spin projection is along the $z$-axis in the lab frame.

## Distinguishing Canonical and Helicity States in Particle Decays and Rotations


Note on the notation: I have to distinguish.
When I just tell you $P, M$, you need to ask, is it canonical? Strictly speaking, when you see $P, J$, and then another number, there is no way to figure out whether I'm talking about a canonical state or a helicity state.

However, for the general notation, before I put the numbers here instead of $M$ and $\lambda$, $M$ usually refers to the z-axis projection, and $\lambda$ refers to the helicity.
It's way better if you indicate that explicitly.
So if I talk about helicity, I might say "helicity" here, or I can say "canonical" here.
Adding these indices to the state to indicate what I'm talking about would be better.
If I just say $J, P$, it might be confusing.
Still, I will be doing this sometimes because of rushing.

---

Now it's also clear how to relate the two.
But before we start talking about canonical, let me just show you the transformation of canonical states.
I want to rotate, and then I immediately rotate.
Put a definition of the state: it's a rotation and then acting on the state $B^{-1}(P) \ket{0, J, M}$.
And then I only have to deal with matrices before it becomes something I can apply.
So this is equal to...
I will try to make on this side the same as I have on the right side to replace these two canonical $R$.

What I have done: I inserted right here $R'^{-1} R'$.
Then I put these matrices together, and now this—what is this?—is something that gives me a canonical state if applied to this state at rest.
The only thing that remains is I have to apply the rotation operator to the state at rest.
And this, you know, is the Wigner D-matrix acting on this state.
Therefore, what I'm going to get is the sum of Clebsch-Gordan coefficients.

::: callout-note
**Key Transformation**:
The canonical state $\ket{P, J, M}_{\text{can}}$ is defined as:
$$\ket{P, J, M}_{\text{can}} = R B_z^{-1}(P) \ket{0, J, M}$$
where $R$ is the rotation operator and $B_z^{-1}(P)$ is the inverse boost along the $z$-axis.
:::
---

**Question:** Doesn't the momentum $P$ also change because we change the angle?
**Response:** Very good, thanks.
So, it gets rotated.
But you're not sure if it's just $R P$? It should include $R'$.
$R'$ is the second one—$R' P$.
Maybe I would just call it $P'$ instead.
Somebody else can do the computation.
Let me just say $P'$ and then explain what $P'$ is.

So, $P'$ is $R' P$.
Or it is also equal to $R' R$ acting on $P_z$.
Here I boosted, so the momentum became non-zero.
Once I boosted after the boost along the z-axis, my momentum is just $P_z$, and then in the following operation, I apply the rotation.
So here I apply the rotation, and now $R' P_z$, and that way I get $P'$.

---

I learned how to boost yourself in the exercises, and now let's discuss their relation to bosons.
If you need to relate one to another, this is a gluon state.
This is a canonical state.
Here we have $\ket{P, J, M}_{\text{can}}$.
What I want—I want to write so clearly—they are not equal to each other, but one can express $\ket{P, J, \lambda}_{\text{hel}}$ as the linear combination of canonical states.
And these coefficients are then...
I would like you to have a clear understanding of how we find these coefficients.

::: callout-note
**Helicity State Relation**:
The helicity state $\ket{P, J, \lambda}_{\text{hel}}$ can be expressed as:
$$\ket{P, J, \lambda}_{\text{hel}} = \sum_{M} C_{M \lambda} \ket{P, J, M}_{\text{can}}$$
where $C_{M \lambda}$ are Clebsch-Gordan coefficients.
:::
---

I wanted to quickly come back to the lambda decay and tell a little bit more about how we derived the formula.
The large peak formula is the many D functions and $H$'s from the last lecture.
I'm going to consider now a lambda that moves in the wave frame.
It is a helicity state, and then it decays.

In order to get a z-axis, we need the direction of motion of lambda in the lab frame, and that gives us after the boost the z-axis.
The way to define the z-axis in this manner is called the helicity frame for lambda.
This is when we say "lab frame." You always have to describe from which frame you are boosting, because it depends.
In different frames, the direction of lambda will be different, and there will be differences when you arrive at the rest frame of lambda depending on from which frame you boost it.

The helicity frame is defined as the rest frame of the particle obtained by boosting from the frame where it was moving.
The angle of the decay of the particle—when you take one of the particles, particle number one, and use this to define the angle—is called the helicity angle.
That's common jargon in hadron physics.
When we talk about the helicity angle, it implies that we boosted to the rest frame and then took one of the particles as the reference and measured the angle from there.
But all of the motion is still in the same plane as before.
The boost and the two-particle system are now exactly opposite.

---

We start with a lambda flying in the z-direction with a certain velocity.
Then it decays.
It has a proton and a pion in some plane.
And then we invert the boost, and we still have the proton and pion in the same plane.
If I took this picture out, you would not have the plane any longer.
The plane is formed by three vectors.
So I need the original direction of motion of lambda to define the axis with respect to which I can measure the angle, and then I have a plane.
This is our recap exercise.
We started without knowing that, so we only had one axis.
But now we have a plane.
Now I have one more variable on which the amplitude depends, in addition to these two discrete variables.
This is the scattering angle or the helicity angle.

I have to compute now a final state here going to be frozen binary.
Here, on the right side, we have configurations of lambda sitting in its rest state with the proton in lambda.
And on the left side, we have this configuration.
The way to proceed is to apply rotation to this configuration and arrive at the back.
So the answer for this is $H_{\lambda_p \lambda_\pi} T_{\lambda \lambda}$.
And the problem of $T_{\lambda}$.
That's the equation we had last time, where I was describing the matrix element for the sequence of the decays.

Let me apply $T$ on the final state.
I want to simplify this.
This is $T$ acting on the proton.
We want to evaluate the application of the transition operator that takes pion-proton and then transforms this to lambda.
This is the meaning of our operator.
This operator acting now on the pion-proton state that has the $P$ vector $(0,0)$.
We notice that this is rotated about the y-axis by the angle $\theta$.
We want to align this because, on the left state, we have aligned combinations.
So we have a rotation.
Now we pull out the rotation, and then we have the same combination now along the z-axis.
Proton goes forward, time goes backward, and rotation is explicit.

Since these operators commute—strong interactions conserve spin—therefore, one can compute the transition operator and rotation and then act first with the transition and then by rotation.
Essentially, this transition operator transforms pion-proton to lambda.
We explicitly do this by inserting the identity state here.
Here I have a $\ket{\lambda}_{\text{hel}}$ for the left state.
This part is a path $\lambda_p$.
It's going to give me just the state of the lambda with the same spin.
This matrix element we just evaluated—this is just a Clebsch-Gordan coupling.
The identity that we inserted here should have some overall possible combinations.
Therefore, that would be a sum over $\lambda$.
This will give me delta functions for the $\lambda_p \lambda_\pi$.
And that's why I want only one state—I can do this.
Now the last step to do is to apply rotation to it.

It's good to see it once.
But once you get the idea, it's easy to believe that in the same case of the cascade reaction, what you have for every bit of the transition is the product of this block helicity that is the transition matrix element for the aligned transition.
And then the rotation I want to evaluate as well.
Now, the differential cross section exists as a function of the angle.
This is my equation.
We know that these are—so these are our $\cos \theta, -\sin \theta, \sin \theta, \cos \theta$ matrices.
For the spin-half, we just had an explicit matrix, and we have two coupling constants that are measured in experiment.
You can take them to compute the angular distribution.

It's a little bit disappointing right now if I just tell you the answer.
The answer is the same as you had before, because you have a $\sin^2 \theta + \cos^2 \theta$, which is one.
And this is in front of the first one.
In front of the second one, you have a $-\sin^2 \theta + \cos^2 \theta$.

All right, so what we learned now in this example is that once you have an unpolarized particle, you're not going to observe any interesting angular distribution.
We actually summed over the final state, we summed over the initial state.
There is no non-trivial angle distribution that remains for the $2\pi$ before we integrate the whole $\cos \theta$.
Now we have a differential $\cos \theta$—right before, we just wrote the gamma is equal to...
and then the phase space has...
it has a $d\Omega / 4\pi$, an integral $d(\cos \theta) / 2$, $d\phi / 2\pi$.
This is one decision.
And now I just move this $\cos \theta$ to the other side.

---

Polarized decay.
Now finally, polarized decay.
When I get non-trivial distributions if I polarize my particle.
So let me say when lambda was flying, it had only spin, only $\lambda$.
And now finally we have something.
I have a formula.
But now let's try to see what I'm going to see in the experiment.

Lambda travels with a certain momentum, and the projection of the spin to the direction of motion is equal to $1/2$.
And then it decays.
In the decay of this state, we are going to find that it's more likely for the proton to travel forward than backward.
But this is the angle of the proton.
Interestingly, this violates parity.
Because you can apply parity to the initial state and final state and find out that by applying parity you flip the momentum, you don't flip the spin.
And then in the final configuration you flip momentum, you don't flip the spin.
So parity implies that there cannot be a symmetry.
Parity is violated here.
This is also consistent with the fact that we consider inside of the blob here...
big decay amplitudes.
Parity...
we likely put the weak decay in.

::: callout-important
**Parity Violation in Decay**:
The differential decay rate for polarized particles (e.g., $\Lambda$) shows parity violation:
$$\frac{d\Gamma}{d\cos\theta} \propto 1 + \alpha P \cos\theta$$
where $\alpha$ is the asymmetry parameter and $P$ is the polarization. This asymmetry arises from weak interactions.
:::
## Parity Violation in Asymmetric Angular Distribution


No, it's not.
Well, it is.

You told me that it's a **linear function**.
No, I don't.

The point is in the **general**.
It's a great question.

::: callout-important
Where this parity violation appears is when the two terms are not equal to each other. If they were equal, $\sin^2\theta + \cos^2\theta$ would give 1 with no angle dependence.
:::
The parity violation is in the fact that these terms are not equal. This introduces an **asymmetry**, making the distribution angle-dependent, as seen in the formula:

$$
\frac{d\sigma}{d\Omega} \propto 1 + \alpha \cos\theta
$$

Here, $\alpha 
eq 0$ signals **parity violation**, breaking the isotropy of $\sin^2\theta + \cos^2\theta = 1$.

## Polarization and Angular Distribution in Λ Decay


Thanks for the question. That's **really important** to know, and in fact, they are not.

Moreover, we consider the **polarized decay**: the 100% polarization $\lambda = \frac{1}{2}$ is a pure state, a spin projection $\frac{1}{2}$, and it's fully polarized. One can also consider a **mixed state** where it's not fully polarized.

Most realistically, the degree of polarization for the $\Lambda$ is not 100% but around **60%**. That's what we have. In the $B$ decay case, the $\Lambda$ is produced with a polarization of 60%, and in that case, the asymmetry is smaller.

---

The **angular distribution of the decay** is given by:

$$
\frac{d\Gamma}{d\cos\theta} = \Gamma_0 (1 + \alpha \lambda \cos\theta),
$$

where:

- $\Gamma_0$ is the **total decay rate**,
- $\alpha$ is the **analyzing power** (polarizing power),
- $\lambda$ is the **degree of polarization** ($0 \leq \lambda \leq 1$),
- $\theta$ is the **decay angle**.

---

We can rewrite these equations by contracting the matrix element with the polarization matrix and find that the **difference between two edges** defines how well this particular decay reflects polarization. The quantity $\alpha$ is often called the **polarizing power**. It tells you how well this decay is suited to measure the initial polarization.

::: callout-important
If the couplings are equal to each other, you don't have sensitivity to the initial polarization. It can also happen even for big decays that the couplings are equal. Parity can be violated, but for most cases, there is a non-zero analyzing power.
:::
This $\alpha$ is **non-zero**, and that's why by looking at the angular distribution, you see **parity violation**. But you can also measure the initial polarization. That's called the **polarimetry technique**, and it's actively used.

---

Look at the angular distributions. All particles have **known spin**, and the couplings are known. But these values have to be measured in advance, and in that case, you can measure polarization.

This **initial polarization** is a **super powerful observable**. Particles like $\Lambda$ with spin carry polarization out of the interaction point, which is part of the information. How $\Lambda$ is produced—with what momentum and with what polarization—tells us about the **internals of the interaction**.

Imagine $\Lambda$ is produced in the **quark-gluon plasma**. Its polarization can now be related to the properties of the plasma. This is a kind of **free carrier of information** out of the mess of the quark-gluon interaction.

Polarization plays an **important role**, if not more than other observables. This particle not only carries polarization but also, by decaying, gives us a way to measure it.

---

## Engaging with Questions Before the Lecture


**Questions, questions, questions.**
We have time, but it is up.

Instead of starting a new lecture, I would like to give you *a question I have in mind* for the lecture.
For example:

* If I were to explain the material to you, you would already know it
* But I haven't

::: callout-note
The speaker is using a Socratic approach - testing understanding before delivering content. Common in physics lectures to gauge baseline knowledge.
:::
So I'll just give you the question and see if you know it *without my lecture*.
Meanwhile, tell me if you have questions.

## Analytic Functions, Contour Integrals, and Dispersion Relations


Can you find half or maybe a quarter page? Maybe we can take Ilya—can you help obtain quarter-page pieces of paper?

---

**Next lecture**, we will move on to discussing **analytic functions** and properties of amplitudes in the complex plane. This requires you to have a little bit of **complex analysis**. We’ll discuss this further—the next sheet also has a bit of discussion on the complex plane.

So, we need a little bit of **complex algebra**, from 1 to 7. From 1 to 7. Let me just say where this comes from.

---

::: callout-important
**Key Theorem**:
The **Cauchy Integral Theorem** states that for any analytic function $F(z)$ inside and on a closed contour $C$:
$$
\oint_C F(z) \, dz = 0.
$$
:::
What is written here is obtained by doing the **contour integral**. I started with a small circle—my function is analytic—and I’m going to stretch the circle in all directions. This is my complex plane ($x$-plane).

The **Cauchy integral** of $F(x)$, if no singularities occur inside my integration contour, is zero for any analytic function:
$$
\oint_C F(z) \, dz = 0.
$$

---

Then, there is a theorem that tells me I can insert a **singularity** explicitly inside the circle. If I integrate $\frac{F(x')}{x' - x} \, dx'$ and integrate this around—the integral was zero, but now let me put a pole explicitly inside like this.

When I integrate, my integral is no longer zero—it’s equal to the function evaluated at the pole, and that’s my $F$. This is given by **Cauchy's Integral Formula**:
$$
F(a) = \frac{1}{2\pi i} \oint_C \frac{F(z)}{z - a} \, dz.
$$

---

Now, I have this beast here. It’s something similar, but I started from a small contour and stretched it to infinity. Here is infinity—this part of the contour drops out, and the only thing that remains is the integral from 1 to 7.

I’m integrating the **imaginary part** of $F(x)$ from 1 to 7 and asking: Can this equation be satisfied? This relates to the **dispersion relation**:
$$
\text{Re}\, F(x) = \frac{1}{\pi} \mathcal{P} \int_{1}^{7} \frac{\text{Im}\, F(x')}{x' - x} \, dx'.
$$

---

**Second question**: What is the **analytic structure**? What do you mean by "analytic"?

::: callout-note
**Analytic Functions**: A function is **analytic** in a region if it is **complex differentiable** at every point in that region. This implies the function is infinitely differentiable and can be represented by a **power series** locally.
:::
## Branch Points, Cuts, and Analytic Structure in Complex Integration


Cut both branch points.
This is **super unusual** for math courses, but that's what we use all the time in physics—this type of integral where the leftover of the contour is from $1$ to $7$, and what you integrate is your function $F$.

Since it comes from both sides, from this side and that side, and they have opposite signs, what remains is the **imaginary part**. The real part is the same. It cancels out when you calculate. So the thing that remains is the integral from the same.

If you have anything to say about that, write it down. Maybe it's too complicated.

---

Let’s make a round. Say a few words about this. Start with:

- Can you be satisfied?
- Can we be satisfied?

Three is a solution. You can just take the constant $3$ because it has no imaginary part. The real question is, if you remove the three, at least there are **non-trivial solutions**. Sometimes non-constant words like *non-vanishing*.

If you say $F(X) = 3$, it has no imaginary part. Then the imaginary part is not present anywhere. The question is, if you remove the three—well, that's the question.

If you just ask this, I think you're completely right. But I was actually thinking of **non-trivial solutions**. Do we say it exists or not?

---

You can probably put power series in. It might work—**totally could work**.

It can be satisfied. The answer is: Give me any function, whatever you want. I put it here. Any function $X$—that integral actually converges for any value.

Take $\sqrt{X}$. Put it here, and it's satisfied. Just anything put inside the imaginary part, it's satisfied. The reason we're satisfied is this: it's a way to construct the function.

::: callout-important
The function $F(X)$ can be constructed using the integral representation:
$$
F(x) = \frac{1}{\pi} \int_1^7 \frac{\sqrt{t}}{t - x} dt
$$
where the integral is taken along the real axis, avoiding the branch cut.
:::
---

Let me show you: this $\sqrt{X}$, I put it here instead of this expression, $\sqrt{X}$. Then this way I compute my function $F(X)$. This is a **super special function**. Its imaginary part is equal to $\sqrt{X}$ in the region from $-1$ to $7$.

In $-1$ to $7$, if I evaluate, the imaginary part is equal to that. In the rest of the complex plane, the function is non-zero. But there are no singularities.

This insertion that I made is actually done by introducing some **non-trivial analytic structures**. Now we have three candidates. Let's give them votes.

---

What kind of non-analytic structures have I introduced? It's like a continuous stretch of poles—a stretch of poles. What is meant by a cut? They just end somewhere.

The cut is the non-analytic structure where the function on one side is different from the function on the other side. It's like $\sqrt{-1 + i}$ and $\sqrt{-1 - i}$.

We see that this one is equal to $+i$ and this one is equal to $-i$. On different sides, I have different values. This is a cut. It's not really anything else than a spectrum of poles.

Poles have divergence, and this thing does not have divergence. So what will you say? You go for poles.

---

Are you attracted by the concept of **branch points** or **cuts**? I was thinking about cuts, but now I'm convinced both solutions are not poles.

In the integral, there are no poles. The integrand has poles, but they are at zero.

You have to analytically continue something. It's like you probably have to take it above the complex line or the real line, and below, probably differently.

The branch point is where it starts and where it ends. You forget about the branch work for the elements.

---

The analytic structure of my function in the $X$ plane has:

- A branch point at $1$,
- A branch point at $7$,
- And they're connected by a cut.

There are no poles. The function doesn't have any poles.

The way we construct the function here—in this way, you introduce on the cut, you don't do your space.

---

It's really funny to think where this guy didn't come from, go where. You can look at this plane and take a walk here. You don't experience any poles, any singularities.

We can dive under. You end up in a different world that has a gate. Through the gate, you go to the other world. There you find poles—this is zero, it has poles. And it has $\sqrt{X}$, so it has another cut.

The function has an **interesting and complicated structure** in the complex plane. On the regular complex plane where we call the function, it doesn't have any singularities except one gate.

Through the gate, you can go to the other so-called sheet, and there you have a lot of stuff going on.

---

You just get used to it. It's really fun to think of this. We will discuss a little bit more of the complex chart structure and how scattering—what is actually the complex structure of the scattering amplitudes.

## Branch Points, Poles, and Multivalued Functions in Complex Analysis


**Opening Remarks:**
*Sorry for being late, and thanks for coming.*
*We have a two-week break next week.*
*We don’t have class, so have a nice holiday.*

---

**Simplifying the Problem:**
*Let’s make it simpler because it can be.*
*Let’s make a constant in order to simplify—oh, I don’t even need this.*

---

**Integration and Logarithmic Behavior:**
The integral will always converge from 1 to 7.
This is what we have.
This is a logarithm.
The logarithm itself can have a pole.

Let’s evaluate the function at 8:
$$
\log(1 - 8) - \log(17 - 8).
$$
I’m going to say $8 \pm \epsilon$, and then:
$$
\log(1) = 0, \quad \log(-1) = i\pi.
$$
$$
\log(-x) = \log(x) + i\pi.
$$

---

**Results and Continuity:**
We arrive at the result that may equal each other.
The difference here is $-i\pi$ and $+i\pi$.
In the equation, this is continuous, and here is the jump.
The real part of $x$ cannot be between 1 and 7 because we want to have a structure around it.

We cannot have $x$ from 1 to 7 because we have the structures looping around it.
The structure is looking around.
You introduced the branch points at the edges and then a cut connecting these points.

---

**Singularities and Branch Points:**
It’s explicitly clear on the determinant itself by doing a simple integral.
This expression has an $n$-structure: a cut, branch point at 1, branch point at 7, and then a cut.
Is it anything else but a pole? No.

A branch point can have a divergence—like the function could be infinity there—but it doesn’t have to.
This function’s branch point is zero.
The function is zero here; the function is infinity here.

The pole is this:
$$
\frac{1}{x^3} \text{ is a pole of third order.}
$$
$$
\frac{1}{(x - c)\log(x - c)} \text{ is not a pole.}
$$

::: callout-note
**Key distinction:**

- A **pole** is an isolated singularity that can be resolved by an infinitesimal shift in the complex plane.
- A **branch point** (e.g., for $\sqrt{x}$ or $\log(x)$) is non-isolated and requires branch cuts to define the function uniquely.
:::
---

**Teaching Style and Context:**
*For us, your lectures are a bit unstructured, and you’re a bit all over the place.*
*But it also makes it more fun because of your sketches of boosts, beasts, and rotations—just sketches.*
*You don’t really prove anything like in other courses.*
*It’s not a strict or rigorous proof of everything—it’s just not fun for a while.*

*I’m fine teaching advanced people, but you have to be more structured for younger students.*

---

**Metaphor of "Gates" and Multivalued Functions:**
We go through the gate, but outside the gate, you said the function is fine, it’s continuous.
Here you said it’s another gate.
This is the first world, second world enter.
Here we can walk around the gate; it’s fine.
But then it goes through the gate and ends up in another world.

You can go through the gate and appear in that world.
It has many more gates.
You can go around this and enter on the other side—that’s where you come out here.
If you do this, you are not at the end.

It’s a third world.
Then it’s an infinite number of worlds because it’s a loop at infinity.
This gives an infinite number of worlds, but this one is simpler.

---

**Practical Application and Fun Idea:**
Imagine taking VR glasses and walking through this.
That would be quite fun.
You can suggest this to Matrix Netflix.
Make it an escape room—you only get out if you find the first gate.

---

**Connection to Physics:**
Where does this function appear?
All scattering amplitudes as functions of **Mandelstam variables** ($s, t, u$) have energies—the area state.

