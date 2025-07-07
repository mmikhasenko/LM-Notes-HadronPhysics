## Unitarity, Analyticity, and the Schwarz Reflection Principle


In today's lecture, I would like to discuss **unitarity** and **complex numbers**, and move towards discussing **complex functions**.
We had too little time in the previous lecture to cover these aspects, but they are **important to understand** and connect to what you already know from mathematics.

---

I will introduce two mathematical concepts:

- **Analytic functions**
- **Holomorphic functions** (which are interchangeable terms)

A function is called **analytic** if there is a Taylor series equal to the function in the vicinity of each point.
If there are coefficients such that the series gives exact values of the function, then the function is analytic at the point $X$.

::: callout-note
The Taylor series expansion for an analytic function at point $x_0$ is:
$$
f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(x_0)}{n!} (x - x_0)^n
$$
:::
A function is analytic at $X_0$ if the series exists for $(X - X_0)^N$, with coefficients depending on $X_0$:
$$
f(X) = \sum_{n=0}^{\infty} \frac{f^{(n)}(X_0)}{n!} (X - X_0)^n.
$$
If the **complex derivatives** exist—meaning the limit exists when approaching the point from any direction—the function is called **holomorphic**, which is the same as analytic.
*Holomorphic is just a fancy word for analytic—mathematicians like cool terms.*

---

- **All polynomials** are fully analytic.
- **Rational functions** (polynomials divided by polynomials) are analytic except at the zeros of the denominator.
- A function is analytic in a **domain** if every point in that domain is a point of analyticity.
- The **square root function** $\sqrt{X}$ is analytic everywhere except at zero, where it has no derivative or valid Taylor series—this is called a **branch point**.

---

**Real analytic functions** are another interesting class.
For example, $\sqrt{X}$ is real analytic.
They satisfy the **Schwarz reflection principle**: when extended to the complex plane, the function evaluated at the conjugate point equals the conjugate of the function:
$$
f(\overline{z}) = \overline{f(z)}.
$$

::: callout-note
Demonstration using $1 + i = \sqrt{2} e^{i\pi/4}$:

- $\sqrt{1 + i} = 2^{1/4} e^{i\pi/8}$
- $\sqrt{1 - i} = 2^{1/4} e^{-i\pi/8}$
This confirms the reflection principle since $\sqrt{\overline{z}} = \overline{\sqrt{z}}$.
:::
---

For **analytic functions** of a single argument, it's useful to visualize the domain as the complex plane:

- **Real part** on the x-axis
- **Imaginary part** on the y-axis

The Schwarz reflection principle implies **symmetry** between the upper and lower planes—values in the lower plane can be derived from the upper plane via conjugation.

For instance:

- $1 + i$ has magnitude $\sqrt{2}$ and angle $\pi/4$
- Its square root is $2^{1/4} e^{i\pi/8}$
- Similarly, $1 - i$ gives the conjugate result, illustrating the reflection principle.

## Cauchy's Theorem and Numerical Integration of Discontinuous Functions



I would like to cover **Cauchy's theorem**.
It states that the integral over a closed contour in the complex plane of a function is equal to all **non-analytic contributions** inside this contour.
If it's a pole, it's given by residues. If it's a branch point, the correct way is to contour around it, and so on—the left side captures all non-analytic behavior.

::: callout-important
**Cauchy's Integral Theorem (general form)**:
$$
\oint_\gamma f(z) \, dz = 2\pi i \sum \text{Res}(f, a_k)
$$
where $\gamma$ is a closed contour and $a_k$ are the poles (or other singularities) inside $\gamma$.
:::
What I realized recently is that this is actually a **numerically well-defined procedure** to integrate a discontinuous function.
For example, we can compute the integral of $\sqrt{z}$ over a circle of radius 1, and the integral converges despite the function being discontinuous at the branch point.

On the circle, the function is parameterized as $z = e^{i\phi}$.
Above the branch cut, it's $+i$, and below, it's $-i$.
If I plot the function in the integration domain, the integral becomes:
$$
\int_0^{2\pi} i e^{i\phi} \sqrt{e^{i\phi}} \, d\phi.
$$
The key point is that within the integration domain $0$ to $2\pi$, the function jumps at $\phi = 0$ due to the branch cut.
Yet, the integral remains well-defined because it’s equivalent to integrating around the branch point.

Let me emphasize this more clearly. The integral is:
$$
\int_0^{2\pi} e^{i\phi} \cdot i \cdot \sqrt{e^{i\phi}} \, d\phi.
$$
This simplifies to:
$$
\int_0^{2\pi} e^{3i\phi/2} \, d\phi.
$$
However, since the function is discontinuous, I cannot naively evaluate it at the endpoints.

---


A better approach is to shift the integration range to $-\pi$ to $\pi$, where the function is continuous.
Mathematically, this becomes:
$$
\int_{-\pi}^{\pi} e^{3i\phi/2} \, d\phi.
$$
Evaluating this properly accounts for the branch cut.

The deeper insight here is that this integral equals the integral of the **discontinuity across the branch cut**.
If I shrink the contour, it’s equivalent to integrating $\sqrt{z}$ along the real axis from $0$ to $-1$.
You’ll find the same result—this is the power of **Cauchy's theorem**.

It tells you that you can deform the contour freely, as long as you avoid **non-analytic regions**.
You can compute the integral along the circle or shrink it to a real-axis integration.
For this example, I encourage you to verify that both methods give the same answer.

---


The final step is to evaluate the real-axis integral:
$$
\int_{-1}^0 \sqrt{x} \, dx.
$$
This is straightforward, and the result aligns with the contour integration.
The key takeaway is that even with discontinuities, **Cauchy's theorem** provides a rigorous way to compute such integrals.

::: callout-note
**Equivalence of Methods**:
The integral along the branch cut ($\int_{-1}^0 \sqrt{x} \, dx$) matches the contour integral result, demonstrating the flexibility of contour deformation in complex analysis.
:::
## The Scattering Amplitude: Analyticity, Unitarity, and Threshold Behavior


The **scattering amplitude** is the *real magic function*.
Let's come back to our two sketches in the amplitude, for which we derived the **optical theorem** and discussed the **analytic structure** of this function.
The claim is that the amplitude is a *real magic function*, or part of it.

---

1. **Assumptions**:
The amplitude is not accessed directly in the experiment, so we cannot validate its properties exactly.
What we measure is the amplitude squared.
Access to the amplitude itself is only available through our observables.

2. **Constraints from Scattering Theory**:
However, scattering theory and probability conservation imply that certain properties of the amplitude constrain the imaginary part and tell us where the imaginary part is present.

---

::: callout-important
**Analyticity as a Postulate**:
The fact that it's analytic is a postulate.
This is something we have to assume—though it's stronger than an assumption.
We don't assume its analytic properties; this is the building principle of our series.
:::
---

- **Unitarity**:
All series we have seen so far have unitarity built in.
Therefore, not only unitarity but also **causality**, which is related to analyticity.

- **Causality and Analyticity**:
The amplitude being an analytic function is a principle postulated in our theory.
It is related to the **causality** of the theory—that the past does not influence events outside the causality cone.

This connection is not derived here, but you can find it in several books linking causality to analyticity.
We take it as a postulate.

---

- **Analyticity**:
The amplitude is analytic, and unitarity further tells us that it is **real analytic below the threshold**.

- **Imaginary Part and Thresholds**:
The imaginary part is connected to the appearance of particles in intermediate states.
This only occurs **above threshold**, because the interaction introduces an imaginary part there.
Below threshold, the amplitude has no imaginary part; it is purely real.

---

1. **Optical Theorem**:
$$
\text{Im}\, f(0) = \frac{k}{4\pi} \sigma_{\text{tot}}
$$

2. **Unitarity Condition**:
$$
\text{Im}\, f(\theta) = \frac{k}{4\pi} \int f^*(\theta') f(\theta) \, d\Omega'
$$

3. **Threshold Behavior**:
$$
f(E) = \begin{cases}
\text{real} & \text{if } E < E_{\text{threshold}} \\
\text{complex} & \text{if } E \geq E_{\text{threshold}}
\end{cases}
$$

## Analyticity, Threshold Singularities, and Unitarity in Scattering Amplitudes



So here I have a diagram on the $x$-axis. Again, it's a complex plane of the energy. The variable $S$ is $E^2$, where $E$ is the center-of-mass energy, and the amplitude as a function of $S$ is an analytic function.

What we get to deal with is only the values of this amplitude above the threshold. However, the past tenets of our theory tell you that using analyticity, we can extend the domain of the definition into the full complex plane.

::: callout-important
**Key Idea**: The amplitude $A(s)$ can be analytically continued into the complex plane, allowing us to evaluate it at complex energies, not just real ones above threshold.
:::
I hope you wrap your mind around the idea that now we can extend this analytic domain and think of our amplitude as a complex function. So instead of energy of the interactions of, say, 5 GeV, you can put a complex number there and then probe the function away from the real axis.

Now, this function has a certain range of singularities. From the fact that the imaginary part is not present below threshold and then suddenly appears above threshold tells you that a certain singular disk pops up. And these singularities are the branch points.

At every threshold, there are nice derivations of the threshold singularities for different numbers of particles. In Gribov's book, I leave it out. However, something easy to see is the two-body threshold. And I want to show you that it introduces square root singularities. It simply follows from the fact that the imaginary part has a square root.

---


So let me show you that the imaginary part of the amplitude from unitarity that we derived last time is related to the amplitude squared itself. The unitarity condition is:

$$
\text{Im}\, A(s) = \frac{1}{2} |A(s)|^2 \cdot \Phi_2(s)
$$

where $\Phi_2(s)$ is the two-body phase space factor.

The prefactor here is the phase space—simply two-body phase space. The one-half comes from $(A - A^*)$. So, the imaginary part here—I replace it—and $\frac{1}{2}$ over here.

The two-body phase space has the form:

$$
\Phi_2(s) = \frac{2p}{\sqrt{s}}
$$

where $p$ is the breakup momentum. This is something that actually makes a singularity, something that vanishes at the threshold.

---


The breakup momentum is the momentum particles have. Clearly, if you are at the threshold, you have a minimal energy of the system. It's simply two masses of the particles. They don't have free energy; they don't have momentum. And that's something that vanishes, and it vanishes.

Mathematically, you see that if you compute this two-body breakup momentum—I think you've done it in earlier exercises—you find that it's equal to the Källén function:

$$
p = \frac{\sqrt{\lambda(s, m_1^2, m_2^2)}}{2\sqrt{s}}
$$

where $\lambda$ is the Källén function:

$$
\lambda(x, y, z) = x^2 + y^2 + z^2 - 2xy - 2yz - 2zx
$$

or equivalently:

$$
\lambda(x, y, z) = (x - (y + z)^2)(x - (y - z)^2)
$$

Remember this: the first term gives you a singularity at the threshold, and the second one gives you a singularity at the pseudo-threshold.

## Square Root Behavior and Schwarz Reflection Principle in Threshold Energy Analysis


Interior relations, as we wrote it, as we derived, are valid **only above the threshold**. The imaginary part is non-zero and present only once you go above the threshold.

This imaginary part behaves like a **square root function**:

$$
\text{Im}\, f(E) \propto \sqrt{E - E_{\text{th}}},
$$

where $E$ is the energy and $E_{\text{th}}$ is the threshold energy. This indicates that the function itself has a **square root branch point**.

---

Above the threshold, the function exhibits this square root behavior. It would be useful to connect this to the **Schwarz reflection principle**.

::: callout-important
Since our function was real and analytic on a segment of the real axis, the Schwarz reflection principle applies. It relates the amplitude in the upper half-plane to the amplitude in the lower half-plane:

$$
f(E + i\epsilon) = \overline{f(E - i\epsilon)},
$$

for real $E$ and small $\epsilon > 0$, where $\overline{f}$ denotes the complex conjugate.
:::
---

This means the imaginary part flips sign when you cross the real axis:

$$
\text{Im}\, f(E + i\epsilon) = -\text{Im}\, f(E - i\epsilon).
$$

The relation holds for $\epsilon$ small enough.

---

- The **square root behavior** of $\text{Im}\, f(E)$ is tied to the threshold energy $E_{\text{th}}$.
- The **Schwarz reflection principle** ensures symmetry between the upper and lower half-planes.
- The sign flip in the imaginary part reflects the **discontinuity** across the real axis.

## Analytic Structure and Branch Cuts in Square Root Functions


Have you heard a song with the word **"infinitesimal"**? I think it's by one of the rock bands. I was really impressed. This is now in pop, in rock. People like the word. Maybe next time I'll bring you something. I was impressed recently. Who is singing **"Infinite"**? You know, *Mother Mother*. That's about *Mother Mother*. So listen to the song **"Infinitesimal."** I like the song actually, but it just means very, very small—**infinitesimal**.

---

I'm going to use this $i\varepsilon$, and you've seen it before. This is just the little number that indicates you are like a very, very small amount above the real axis or below the real axis. It happens due to the **phase space**. We realized that if the function had no phase space configuration summations on the right, you could relate the imaginary part to the real part itself, and there would not be branch points. But it's unavoidable. You have to sum over phase configurations, and that gives you the **square root branch point**. It also tells you that the amplitude has a branch point starting at the threshold and going in the positive direction.

---

::: callout-note
The $i\varepsilon$ prescription is a common technique in complex analysis and quantum field theory to handle poles and branch cuts by shifting the contour infinitesimally away from the real axis.
:::
---

I wanted to quickly give an example of such a function—an example of a **real analytic function**, discarding this cut to the right. An example of a real analytic function like our scattering amplitude, but something very simple with a square root function that has a cut to the right. So $\sqrt{x}$ doesn’t work—its cut is on the left. Let’s cut to the left. How do I see where it has the cut? Simply because $\text{Amplitude}(1 + \varepsilon) = \text{Amplitude}(1 - \varepsilon)$, there is no cut. Then, $\sqrt{-1 - \varepsilon} = -i$, and $\sqrt{-1 + \varepsilon} = i$. On this side, the function evaluated from above and below have different values. That tells me in which direction I put my cut.

---

This is a **branch point**, and this is a **non-analytic point**. But for every branch point, there is a cut attached, and it splits my manifold. Analyticity into the functions—into the surfaces—differentiates. Everywhere else except this point, the functions are analytic. But you have to work to see this analyticity. Essentially, you have to **analytically continue** functions. If you see the pattern, you want to make this function analytic. It's always possible, but you have to work a little by extending the domain of analyticity.

---

Coming back to the example, you'll understand it better once I finish this. If I take $-\sqrt{x}$, what was the analytic structure of $-\sqrt{x}$? According to the same logic, I can evaluate the function somewhere in the complex plane and find that it's now analytic here, fully analytic, and it has a cut to the right. Now, let's evaluate this function at $-1$. What does it equal? So I evaluate my function here, and it gives me $\sqrt{1}$. This is an example of a **real analytic function**. Or let's take the simplest amplitude: the amplitude $\mathcal{A}(s) = \sqrt{-(s - m_1^2 - m_2^2)}$, which has similar properties. It has similar properties.

---

Quickly, while I'm cleaning the board—what is the analytic structure of this? This is in the $x$-plane. The first one I put as $-9$ to make it more interesting. This first one has the cut on the right, and the second one has a cut—it's very similar but shifted by one. Essentially, it has this structure: one cut, then a second cut. When you have this situation, there is no jump here. You can jump twice, and the cuts overlap, so there's no jump in the function. It's analytic right here. The correct answer is just the cuts connecting two points.

---

This one is tricky. The first time I saw it in a mathematical context, I was really shocked because the branch points are the same. There are two points, $x$ and $x$, where the function is non-analytic. But the locations of the cuts are determined by where the expression under the square root has an argument of $\pi$ or $-\pi$. For a regular square root function, the cut appears where the argument is either $\pi$ or $-\pi$. To understand where your Mathematica, C, or Python library would draw a cut, you need to know where the expression under the square root has an argument touching $\pi$ or $-\pi$.

---

And then, apparently, this is indeed between the points but also along this line. This is the first cut going to infinity, and this is the second cut going to infinity. It's crazy. And this is actually different from this. If you just split the product into two square roots, then the argument—then you remove these two. It's not to confuse you, but to warn you that you must be careful how you write the expression, exactly how you split the square root, because that makes the function different. On the real axis, I think they will be the same, but on the complex plane, the functions are different.

---

To prove to you that this is not equal to that, we can simply evaluate the function at $-1$. I think that's an easy exercise. The way I see that they are different is because I know the analytic structure of this: one cut and then a second cut. There are just two branch points connected by the cut. To go from this to that, I can take this cut, rotate it over here, take this one, rotate it over there, and cancel the two cuts—make them cancel each other. That tells me the function in the original configuration has a different value at $-1$. If I evaluate it, I should see this immediately.

---

If I evaluate the top one, I get $\sqrt{(-2)(-1)}$. If I evaluate the second one, I get $\sqrt{2} \cdot i$. Then the product of them gives me $-\sqrt{2}$.

---

::: callout-warning
Be cautious when splitting square roots in complex analysis: $\sqrt{ab}
:::eq \sqrt{a} \cdot \sqrt{b}$ in general due to branch cut ambiguities. The example shows $\sqrt{(-2)(-1)} 
eq \sqrt{-2} \cdot \sqrt{-1}$ because of differing branch cut configurations.

## Resonances as Poles in the Scattering Amplitude: A House Analogy for Complex Plane Dynamics


Its resonances are **poles of the scattering amplitude**. When you hear that, you're probably going to hear this many times in the future.

I would like you to think of the **intensity flow**. The function in the complex plane is the complex structure of a house. In this house, there are just a few routers. You desperately want your Internet—the farther you are from the router, the weaker the signal you get. If you sit at a point and have really good Internet, you're probably sitting near the router.

Similarly, this is our couch in the house where people usually sit and experience different strengths of the Internet. The routers are the **resonances**. Here I have combined two modes on the Y-axis. On the complex S-plane, the real $s$ is on the axis, and this indicates minus imaginary $s$. This is the same as I would have for the complex frame.

I draw a square representing the strength of your Internet when you sit on this couch. In the middle, you have the closest distance to the router, the **resonance pole**, and therefore your strength is the highest. If you sit far away, your Internet weakens.

---

Now let's make the model more complicated. We have several layers, and this is given by the **cuts**. Here is my map of the room. As usual, I am the source where people sit on the real axis. But in this case, the model is more complex. There is a room with different electronics, different floors, so I can go to another room.

I experience all the routers in another room. If there is a router sitting here in another room, I want to see its influence from my car. This is floor one, and the next is floor two. Sheet one is floor one, and sheet two is floor two. Here's the gate—think of it as stairs from one floor to another.

If I have my router here, I have really good strength here and here as well. But if I go around the corner, I start losing the signal. The distance becomes large, and the way to get Internet is around the wall. This is the gate to another floor, and I can only enter on that side.

---

::: callout-important
**Key Insight**: The resonances are the resonances. I see them on each floor. If they are above the threshold, it's too complicated.
:::
When you hear about the complex plane and the poles, think of the **intensity floor** somewhere in the complex domain. This is all complex domain. There are gates to other floors—don't think of them as changing the level, but as connecting one to another. On this surface with different levels, you place the resonances. These resonances influence your intensity, which you see on the detectors.

---

What is the difference between a bigger room and multiple floors? No difference. The rooms are infinitely big. But since at every point I can be on different floors connected smoothly, I have to draw several maps, several sheets. In shopping malls, you also have multiple floors with shops indicated because it's hard to show everything on a single one.

For simplicity, I would use the term **"branch cut,"** which tells us the cut should be to the right. But I would never do it practically like that. The branch cut tells me that, but nothing happens if I place the cut to the left.

---

I will demonstrate with the **square root function**. It has a branch cut, and I'm carrying my function value here. There is nothing happening if I draw the cut in different directions. This function is the same function as before.

At $s = -1$, you have $i$. At $s = -1 + \epsilon$, you have $i$. This function and that function are exactly the same in this dimension. The difference is that I took my branch cut and rotated it to the right, opening the space underneath.

---

I just made a renovation and changed how the rooms are located in the house. But it changes nothing in the strength of the interaction because there are no walls. Everything is continuous. The cut is just a way to separate different floors. There is no wall preventing the signal strength.

For practical reasons, it's convenient to open up the closest room to us. Therefore, it's more natural to place the cut in a convenient location. The cut goes to the right, but I turn it to the left. Now my function is not real, but I expose a bigger range of the complex plane to analyze.

---

If I sit here on the real axis, this point is influenced by all singularities in the complex plane that are nearby. If I have a pole here, I don't have to care about the rooms anymore. I immediately see the effect in the strength of my interaction if my router is nearby. This is the most convenient way to think of the complex plane and the scattering amplitude.

---

I measure my amplitude above threshold at $s = (M_1 + M_2)^2$. What I measure is influenced by structures near threshold. If there is a resonance in the data, it means there is a pole below that makes this resonance. A resonance is always a pole—this is how we define particles.

Particles are always poles in the amplitude. We have conventions for defining the width and mass of the resonance, and they come from the pole location. A single-pole amplitude has the form:

$$
A(s) \sim \frac{1}{s - s_{\text{pole}}}
$$

where $s_{\text{pole}}$ is the complex pole location. The denominator vanishes at $s = s_{\text{pole}}$, which is a complex number. The real and imaginary parts are called the mass and width of the pole.

We define the mass as $\Re\sqrt{s_{\text{pole}}}$ and the width as $-2\Im\sqrt{s_{\text{pole}}}$. These are related to the observed mass and width. If you see a signal, it has a peak location and a full width at half maximum. For narrow resonances, $\Gamma \approx \text{FWHM}$ and $m \approx \text{peak location}$. For broad resonances, this is not the case.

---

What is the analytic structure of this function? It is simply a pole. There are no branch points, nothing else. A slightly more complex example is the **K-matrix**, which incorporates poles and correct analytic structure, including square-root branch points from phase space:

$$
A(s) = \frac{K(s)}{1 - i\rho(s)K(s)}
$$

It works for multiple loops.

---

The last comment is on data analysis. The goal is to characterize resonances by their pole location. We use parameterizations like the K-matrix or P-vector. A simple Breit-Wigner is a limit case of the K-matrix. The amplitude has a complicated expression but is analytic.

You fit parameters to the data, then explore the analytic expression. You know it has a branch point, but the direction of the cut is your choice. What's important is that everything you see—peaks, spikes—has an origin in the complex plane. If there's a peak, there's likely a pole there.

## Thresholds, Branch Points, and Poles in Amplitude Analysis


Another important phenomenon you see sometimes in the data is the **cusp**.
This is amplitude squared, this is $S$.
And then you see a cusp.
That type of singularity is also known as a **branch point**.

---

The first threshold introduces a branch point—every threshold introduces a singularity.
For two particles, it's a branch point.
We already discussed this branch point.
But if there are more than two particles, combinations like $\pi\pi$, $KK$, or $K\bar{K}$ would give a branch point at **1 GeV**.

---

Then my amplitude might have a spike like this.
It's an indication that in the complex plane all is fine, but there is a branch point.
For every branch point, I have to attach a tail.
This is the location of my cut—it's up to me how to draw it—but it introduces more surfaces.
This is a direction.

---

The last thing to realize is that this is a triangle.
We know that at threshold the function has **square root singularities**.
But thresholds are only opening new surfaces for you.
Thresholds are only determining the map of your complex plane.

---

The real singularities, or the **strong singularities** that make intensity peak, are **poles**.
So this situation, where your amplitude squared has this threshold behavior but then rises very quickly and falls, indicates that there are some poles nearby.
If the poles were underneath—if the poles were like that—that kind of function would peak at the place.

---

But in that case, what likely happens is that there is a **bound state**, a pole here.
If there is a pole on the real axis, it would not show up as a nice resonance-like peaking structure.

---

::: callout-note
**Threshold condition for two-particle production**:
$$
S = (M_1 + M_2)^2
$$
where $S$ is the Mandelstam variable (center-of-mass energy squared), and $M_1, M_2$ are the masses of the two particles.
:::
---

Think again about the map of routers and the internet.
If you have a router here and you sit on the couch, the signal strength will be highest here and then lower, lower, lower there.
That's simply how to understand **threshold enhancements**.

Threshold enhancements are often indications of poles below threshold—these are bound states.
There is another phenomenon: poles at the same locations but underneath another sheet, called a **virtual state**.
These are not that different from each other.

---

The bound state can live forever—it's a real state that can travel, a particle that does not decay.
The virtual state does not travel and does not decay.
This is simply an enhancement.

This is a distinction—one of the objectives and discussion points in the field.
When you observe a new structure, what kind is it?

- Is it related to a threshold?
- Is it a pole sitting below a certain threshold?
- Or is it a resonance in the complex plane unrelated to a threshold?

---

Relation to a threshold indicates a **molecular nature**.
Remember, every threshold has two masses summed—it implies a continuum.
There is one particle and a second particle interacting.
This is our threshold.

If there is a pole related to a threshold, likely part of the wave function for this state is of this type—a **molecular type**.
That's why identifying all thresholds and the complex structure, and where the resonance pole sits, is so important.

---

Finishing the lecture—quick questions:

- "$S - (M_1 + M_2)^2$."
- "The other so-called threshold—what is what?"
- "With the so-called threshold $S - (M_1 - M_2)^2$?"
- "Yes. What's with this one?"
- "It's a 'zeta threshold.' It appears artificially in our expressions because of the breakup momentum.
But if you look at the amplitude, it's not supposed to have a singularity there.

---

You cannot literally take this expression and continue at the threshold.
This is a sort of **false threshold**.
We don't see this.
It tells you this is an indication that you should not take this expression literally and build it into your model.

Instead of using phase space—$\frac{1}{8\pi} \frac{2p}{\sqrt{S}}$—it's actually the imaginary part of this bubble.
The imaginary part.

---

You see this simply from unitarity: once you cut this diagram, the imaginary part would be equal to the matrix element here and there, which are both 1, and the two-body phase space because you cut two lines.
Here is the two-body phase space.

The 'surface threshold' here is present because you use only the imaginary part in your amplitude.
If you were to take the full bubble diagram, you don't have a surface threshold there."

