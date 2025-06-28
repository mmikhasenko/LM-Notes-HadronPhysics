<!--
Cosine simularity: 0.9477788073897907
-->
## Introduction to Analytic and Holomorphic Functions

Today's lecture will discuss unitarity and complex functions, building on what was briefly mentioned in the previous lecture. This topic is important and connects to concepts you already know from mathematics.  

I will introduce two mathematical definitions: **analytic functions** and **holomorphic functions**, which are often used interchangeably.  

A function is called **analytic** at a point $x_0$ if it can be represented by a Taylor series that converges to the function in a neighborhood of $x_0$. Mathematically, this means:  

$$
f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(x_0)}{n!} (x - x_0)^n
$$

Here, $f^{(n)}(x_0)$ are the coefficients (derivatives of $f$ evaluated at $x_0$). If such a series exists, the function is analytic at $x_0$.  

Similarly, a function is called **holomorphic** if its complex derivative exists at every point in its domain, meaning the derivative is well-defined regardless of the direction of approach in the complex plane.  

::: callout-note
The terms *analytic* and *holomorphic* are equivalent for complex functions. Don't be intimidated by the word "holomorphic"—it simply means the function is analytic.
:::
<!--
Cosine simularity: 0.945084418823526
-->
## Properties and Examples of Analytic Functions

Don't be afraid of the word holomorphic—this is just mathematicians inventing cool words. As an example, let me give you functions that are fully analytic. All polynomials are analytic. A rational function (polynomial divided by polynomial) is analytic except at a finite number of points, which are the zeros of the denominator.  

When we define a function as analytic at a point, and when we talk about a domain, it means every point in this domain is a point of analyticity. For example, $\sqrt{x}$ is analytic everywhere except at zero. Zero is called a **branch point**, where the derivative does not exist and no Taylor series converges to the function. Both conditions fail, making it non-analytic at that point.  

Real analytic functions are another interesting class—they are real-valued and analytic, with certain scalability properties. For example, $\sqrt{x}$ is real analytic. There is a key property called the **Schwarz reflection principle**: if you evaluate the function in the complex plane, it satisfies  

$$
f(\overline{z}) = \overline{f(z)}
$$  

where $\overline{z}$ is the complex conjugate. Using our example, we can test this at $1 + i$.

<!--
Cosine simularity: 0.9155999997945228
-->
## Introduction to Analytic Functions and Complex Plane Visualization

For analytic functions of a single argument, it is convenient to visualize the domain as a complex plane, where the x-axis represents the real part of the argument and the y-axis represents the imaginary part. At every point in this plane, we can compute the function. While this diagram does not fully describe the function, it helps illustrate its behavior.  

The **stress deflection principle** suggests a relationship between the upper and lower half-planes: values in the lower plane can be computed using values from the upper plane. For example, consider the function evaluated at $1 + i$.  

$$
1 + i = \sqrt{2} \cdot e^{i \pi/4}
$$

Here, $\sqrt{2}$ is the magnitude (length) and $\pi/4$ (45 degrees) is the angle. Evaluating the function further, we obtain:  

$$
\sqrt{1 + i} = \sqrt[4]{2} \cdot e^{i \pi/8}
$$

This demonstrates how analytic functions can be decomposed into their magnitude and phase components in the complex plane.

<!--
Cosine simularity: 0.9124673701607288
-->
## Integration of Discontinuous Functions in Complex Analysis

We can evaluate $4 \sqrt{2} e^{i \pi/8}$ and $1 - i = \sqrt{2} e^{-i \pi/4}$ by considering their arguments. The function can be evaluated either directly or by using the conjugated argument to obtain the conjugated images.  

In the context of contour integration, if we integrate a function over a closed contour in the complex plane, the value of the integral is determined by all non-analytic features inside the contour. For poles, this is given by residues; for branch points, it involves the behavior around the discontinuity.  

::: callout-important
Even for discontinuous functions, the integral can be numerically well-defined. For example, integrating $\sqrt{x}$ over a circle of radius 1 converges despite the discontinuity at $x = 0$.
:::
Consider the function defined on the unit circle:  

-Above $\phi = 0$, the function is $+i$.  
- Below $\phi = 0$, it is $-i$.  
This creates a jump discontinuity at $\phi = 0$ (or $2\pi$).  

To compute the integral, we parameterize $x = e^{i \phi}$:  

$$
\int_{0}^{2\pi} e^{i \phi} \cdot i \, d\phi \cdot \sqrt{e^{i \phi}}
$$

Simplifying, this becomes:  

$$
\int_{0}^{2\pi} e^{i \phi (1 + \frac{1}{2})} \cdot i \, d\phi = \int_{0}^{2\pi} e^{i \frac{3}{2} \phi} \cdot i \, d\phi
$$

However, because the function is discontinuous, we cannot naively evaluate it at the endpoints. Instead, we shift the integration range to avoid the discontinuity:  

$$
\int_{-\pi}^{\pi} e^{i \frac{3}{2} \phi} \cdot i \, d\phi
$$

This ensures the function is continuous within the new range, making the integral well-defined. The key takeaway is that even with discontinuities, careful treatment of the integration domain allows for convergent results.  

The example illustrates how branch points and discontinuities can be handled in complex integration, similar to integrating around branch cuts.

<!--
Cosine simularity: 0.9449375259218931
-->
## Analyticity and Unitarity in Scattering Amplitudes

The integration direction is equivalent to integrating the function in this direction. If we shrink the contour, it becomes an integral from zero to minus one of the function evaluated above. One probably finds the same answer, which in this case will be five.  

This is a nice property of analytic functions, where Cauchy's theorem plays a crucial role. It states that you can deform your contour of integration freely as long as you avoid non-analytic regions. You can compute the integral along a circular contour or shrink it into a different path. For this example, I encourage you to verify that these methods yield the same result. If they don’t, we can discuss it further—I believe it’s a straightforward calculation, but we’ll proceed for now.  

What remains is to evaluate the imaginary part of the expression, which is simply $\sqrt{x} \cdot i$ (or without the $i$), leading to a simple integration on the real axis.  

The scattering amplitude is a remarkable function. Returning to our earlier discussion, we derived the optical theorem and examined the analytic structure of this function. The claim is that the amplitude is a "real magic" function—or at least part of it.  

Let’s clarify the assumptions and physical principles here. The amplitude itself is not directly measurable in experiments; we only observe its square. Access to the amplitude is indirect, mediated by observables. However, scattering theory and probability conservation impose constraints on the amplitude, particularly on its imaginary part, and dictate where this imaginary part exists.  

The analyticity of the amplitude is a postulate—a foundational principle of our framework. It’s stronger than an assumption; it’s the building block of our series. All theories we’ve discussed so far incorporate unitarity, which is tied to causality—a property linked to analyticity.  

The amplitude being analytic is postulated in our theory, but it’s connected to causality: events outside each other’s light cones cannot influence one another. This relationship between causality and analyticity is discussed in various textbooks, but we take it as a given here.  

Unitarity further refines this picture. The amplitude is real analytic below the threshold, meaning it has no imaginary part in this regime. The imaginary part arises only above the threshold, as it’s associated with particle production in intermediate states. Below threshold, the amplitude is purely real.  

::: callout-important
The optical theorem connects the imaginary part of the amplitude to the total cross-section, reinforcing the relationship between analyticity and unitarity.
:::
This structure—analyticity, unitarity, and causality—forms the backbone of scattering theory, ensuring consistency with physical principles while enabling predictive power.  

<!--
Cosine simularity: 0.9521017548198791
-->
## Threshold Singularities and Branch Points in Scattering Amplitudes

Below the threshold, the amplitude has no imaginary part—it is purely real. Consider a diagram on the x-axis representing the complex plane of energy, where $S = E^2$ and $E$ is the center-of-mass energy. The amplitude $A(S)$ is an analytic function, but we typically deal with its values only above the threshold. However, the principles of our theory allow us to extend the domain of definition into the full complex plane using analyticity.  

This means we can treat the amplitude as a complex function, probing it not just for real interaction energies (e.g., 5 GeV) but also for complex values. This extended function exhibits singularities, particularly branch points. The absence of an imaginary part below threshold and its sudden appearance above threshold indicates the emergence of these singularities.  

For example, the two-particle threshold introduces a square-root singularity, as seen in the prefactor of the imaginary part of the amplitude:  

$$
\text{Im} \, A(s) = \frac{1}{2} \cdot \frac{1}{8\pi} \cdot \frac{2p}{\sqrt{s}} |a(s)|^2
$$

Here, $p$ is the breakup momentum, given by:  

$$
p = \frac{\lambda^{1/2}}{2\sqrt{s}}, \quad \lambda^{1/2}(s, m_1^2, m_2^2) = \sqrt{[s - (m_1 + m_2)^2][s - (m_1 - m_2)^2]}
$$

The breakup momentum $p$ vanishes at the threshold, where the system has minimal energy—just the sum of the particle masses. At this point, the particles have no residual momentum, and the singularity arises from the vanishing of $p$.  

::: callout-note
The phase space factor $\frac{2p}{\sqrt{s}}$ in the imaginary part of the amplitude is directly tied to the two-body phase space and vanishes at threshold, reflecting the kinematic constraints of particle production.
:::
This structure is generic: every threshold introduces singularities, and their form depends on the number of particles involved. For a detailed derivation, refer to Gribov's book, but the square-root singularity for the two-particle case is straightforward to derive from the properties of the imaginary part and phase space.  

<!--
Cosine simularity: 0.9657801956878016
-->
## Threshold Singularities and the Schwarz Reflection Principle  

For mathematically, you see that if you compute the two-body breakup momentum, you find that it is equal to the Cullen function:  

$$
x^2 + y^2 + z^2 - 2xy - 2yz - 2zx
$$  

This can be arranged as the product of two terms:  

$$
(x - y + z) \cdot (x - y - z)
$$  

Here, $x, y, z$ represent the masses of the two particles and their differences. The first term gives a singularity at the threshold, while the second gives a singularity at the pseudothreshold.  

The relation we wrote is valid only above the threshold, where the imaginary part is non-zero and appears only once you cross the threshold. This imaginary part exhibits a square-root behavior, indicating that the function itself has a square-root singularity.  

::: callout-note
The square-root singularity above the threshold suggests a branch point in the amplitude, connecting the function's behavior in the upper and lower half-planes.
:::
This connects to the Schwarz reflection principle. Since our function was real and analytic on a segment of the real axis, the Schwarz reflection principle applies. It relates the amplitude in the upper half-plane to the amplitude in the lower half-plane. If the function $F(z)$ is analytic in the upper half-plane and real on the real axis, then:  

$$
F(z^*) = F^*(z)
$$  

This allows us to analytically continue the amplitude into the full complex plane, revealing the structure of singularities and their implications for scattering amplitudes.

<!--
Cosine simularity: 0.8956985218406526
-->
## Analytic Structure and Branch Points in Complex Functions

The function $F(x + i\epsilon)$ tells us that the imaginary part flips when crossing the real axis from above to below. This is a relation where $\epsilon$ is infinitesimal.  

The term "infinitesimal" means very, very small. In this context, $i\epsilon$ is a small imaginary displacement indicating whether you are evaluating the function just above or just below the real axis.  

This behavior arises due to phase space considerations. If there were no phase space configuration summations, the imaginary part could be directly related to the amplitude itself, and there might not even be branch points. However, summing over phase space configurations introduces a square-root branch point.  

This branch point indicates that the amplitude has a singularity starting at the threshold and extending in the positive direction.  

::: callout-note
The amplitude's branch point structure is tied to the analytic continuation of the function across the real axis, where the function's value changes depending on the direction of approach.
:::
To illustrate this, consider a simple real analytic function with a branch cut, such as the square root function. The square root of $x$ has a branch cut on the left side of the complex plane.  

To determine where the branch cut lies, evaluate the function just above and below the real axis:  

- For $x = -1 + i\epsilon$, $\sqrt{-1 + i\epsilon} = i$  

-For $x = -1 - i\epsilon$, $\sqrt{-1 - i\epsilon} = -i$  

This shows that the function changes sign when crossing the branch cut, confirming its non-analytic nature.  

A branch point splits the complex plane into distinct Riemann sheets, where the function takes different values on each sheet. The branch cut is the curve connecting the branch point to infinity, separating these sheets.  

The square-root singularity is a common feature in scattering amplitudes, particularly near kinematic thresholds. This structure is mathematically unavoidable due to the phase space constraints and leads to the analytic properties observed in physical amplitudes.  

The Schwarz reflection principle further connects the behavior of the amplitude in the upper and lower half-planes. If $F(z)$ is analytic in the upper half-plane and real on the real axis, then:  

$$
F(z^*) = F^*(z)
$$  

This allows for the analytic continuation of the amplitude into the full complex plane, revealing the underlying singularity structure.

<!--
Cosine simularity: 0.9321677706056716
-->
## Analytic Continuation and Branch Cuts in Complex Functions

The functions in question exhibit analyticity everywhere except at certain points, and you must work to verify this analyticity. Essentially, you need to analytically continue these functions. If you observe the pattern, you can always make the function analytic, but it requires extending the domain of analyticity.  

Returning to the example, consider the function $-X$. Its analytic structure can be evaluated in the complex plane, revealing full analyticity except for a branch cut extending to the right. Evaluating this function at $-1$ gives:  

$$
F(-1) = 1 - (-1) = 2
$$  

This is an example of a real analytic function. Another example is the amplitude:  

$$
A(s) = \sqrt{-s + m_1 m_2}
$$  

This function has similar properties.  

In the $x$-plane, the first function has a branch cut on the right, while the second function has a shifted cut. When these cuts overlap, there is no discontinuity, and the function remains analytic in that region. The correct structure consists of cuts connecting two points, which can be subtle to identify at first glance.  

::: callout-note
The absence of a jump in the function where cuts overlap indicates analyticity in that region, despite the presence of branch cuts elsewhere.
:::
The square-root function serves as a simple illustration of branch cuts. For example:  

- $\sqrt{-1 + i\epsilon} = i$  

-$\sqrt{-1 - i\epsilon} = -i$  

This sign change across the branch cut confirms the non-analytic behavior.  

The Schwarz reflection principle connects the function's behavior in the upper and lower half-planes:  

$$
F(z^*) = F^*(z)
$$  

This allows for analytic continuation and reveals the underlying singularity structure. The branch points and cuts are intrinsic to the function's behavior in the complex plane.

<!--
Cosine simularity: 0.9784571421257063
-->
## Branch Points and Cuts in Complex Square Roots  

The cuts connect two points, which is a tricky concept. The first time I saw this in a mathematical context, I was shocked because the branch points are the same — there are two points $X$ and $X$ where the function is non-analytic.  

The location of the cut is determined by where the imaginary part of the expression under the square root has an argument of $\pi$ or $-\pi$. For the regular square root function, the cut appears where the argument is either $1$ or $-1$.  

To understand where Mathematica, C, or Python libraries would draw a cut, you need to analyze where the expression under the square root has an argument touching $\pi$ or $-\pi$. The cut lies between the points and also extends along a line to infinity.  

::: callout-note
The first cut goes to infinity, and the second cut also goes to infinity, but this behavior differs from other cases.
:::
If you split the product into two square roots, the argument changes, and you remove these two cuts. This is not meant to confuse but to warn that one must be careful with how expressions are written. The exact way you split the square root affects the function’s behavior — they may appear the same on the real axis but differ in the complex plane.

<!--
Cosine simularity: 0.9669317522559626
-->
## Resonances and Internet Router Analogy in Complex Plane

The amplitude $A$ is given by:

$$
A = \frac{g^2}{m_R^2 - s}, \quad m_R^2 = \left( m_R - i \frac{\Gamma}{2} \right)^2, \quad g^2 = -\text{Res}_{m_R^2}A
$$

On the complex plane, the functions are different. To prove they are not equal, we can evaluate the function here minus one. The analytic structure of this function consists of one cut and then a second cut, with two branch points connected by the cut. To transform from this configuration to another, we can take this cut, rotate it over here, take the other cut, rotate it over there, and cancel the two cuts. This shows that the function in the original configuration has a different value minus one.  

Evaluating the top expression gives:

$$
\sqrt{-2 + 2 - 1 - 2 + 2}
$$

while evaluating the second expression gives:

$$
\sqrt{2i}
$$

The product of these results is $-\sqrt{2}$. Resonances are poles of the scattering amplitude. When you hear about resonances, think of the intensity flow. The function in the complex plane is like the structure of a house, and the routers in the house are the resonances. The farther you are from the router, the weaker the signal you receive. If you sit at a point with good Internet, you are likely close to a router.  

This is analogous to our position in the house where people experience different Internet strengths. The routers represent the resonances. Here, the Y-axis represents the complex $S$ plane, with real $S$ on the axis and minus imaginary $S$ indicated here. This is the same as the complex frame. A square represents the strength of your Internet when you sit on the couch. The middle of the square is the closest distance to the router (resonance), so the signal strength is highest. As you move away, the Internet weakens.  

Now, let's make the house more complex by adding several floors. The cuts represent the map of the room. The couch where people sit is on the real axis, but the house has multiple floors with different electronics. If there is a router in another room, you can still experience its influence from your position.  

Sheet one represents floor one, and sheet two represents floor two. The gate is like stairs connecting the floors. If a router is placed here, the signal strength is strong here and here, but weakens around the corner. The distance increases, and the signal must travel around the wall. The gate to the other floor allows access only from one side.  

The picture of floors and routers is helpful but can be overwhelming. The routers are the resonances, and you can see them on each floor if they are above the threshold. When you hear about the complex plane and poles, think of the intensity flow in the house.  

<!--
Cosine simularity: 0.9379185276533604
-->
## Complex Plane and Branch Cuts in Router Analogy  

The pulse can be visualized as the intensity floor in the complex domain. There are gates connecting different floors, but these do not change the level—they simply link one floor to another. On this multi-level surface, routers are placed, influencing the intensity observed on the relaxers.  

::: callout-note
The difference between a larger room and multiple floors is negligible. Both are infinitely large, but the floors are smoothly connected, requiring multiple maps or sheets for representation—similar to shopping mall floor plans.
:::
For the square root function $\sqrt{x}$, the branch cut is conventionally placed to the right, but practically, nothing prevents placing it to the left. Consider evaluating the function at $-1$:  

$$
\sqrt{-1} = i
$$  

For $-1 + \epsilon$ (where $\epsilon$ is infinitesimal), the result remains $i$. Rotating the branch cut simply reconfigures the "rooms" (sheets) without altering the function's behavior. The cut is merely a way to separate floors, not a physical barrier—there are no walls blocking signal strength.  

::: callout-tip
For practical convenience, it is natural to place the branch cut in the most accessible location, such as the negative real axis.
:::
The analytic structure of the function involves branch points connected by cuts. Transforming between configurations involves rotating cuts and canceling overlapping segments. For example, evaluating:  

$$
\sqrt{-2 + 2 - 1 - 2 + 2}
$$  

yields a different result than:  

$$
\sqrt{2i}
$$  

The product of these results is $-\sqrt{2}$.  

In the router analogy, resonances are like routers in a house. The signal strength (intensity) diminishes with distance from the router. Sitting close to a router (resonance) ensures strong Internet (amplitude), while moving away weakens it. The complex plane is structured like a multi-floor house, with cuts representing the map of connected rooms.  

::: callout-important
The real axis is where observers (people on the couch) reside, but routers on other floors (sheets) still influence the signal. Gates (branch cuts) act as staircases connecting floors, allowing access from specific directions.
:::
The routers (resonances) are visible on each floor if they lie above the threshold. The farther the router, the weaker its influence, analogous to poles in the complex plane. The picture of floors and routers helps visualize the analytic structure, though it can become overwhelming.

<!--
Cosine simularity: 0.9136396991673359
-->
## Poles and Resonances in the Complex Plane

The branch cut can be placed in a convenient location, such as to the right, but it can also be rotated to the left. This exposes a larger range of the complex plane for analysis, even though the function may no longer be real.  

When measuring an amplitude above threshold (at $(M_1 + M_2)^2$), the observed value is influenced by nearby structures in the complex plane. If a resonance appears in the data, it corresponds to a pole beneath it in the complex plane.  

::: callout-note
Resonances are always associated with poles, and this is how we define particles — as poles in the amplitude.
:::
A single-pole amplitude has the form:  

$$
A(s) = \frac{1}{s - s_0}
$$  

where $s_0$ (or $\bar{m}^2$) is the pole location where the denominator vanishes. This is a complex number, with its real and imaginary parts defining the mass and width of the resonance:  

- **Mass of the pole**: Real part of $\sqrt{s_0}$  

-**Width of the pole**: Twice the imaginary part of $\sqrt{s_0}$ (i.e., $\Gamma = -2 \ \text{Im}(\sqrt{s_0})$)  

These quantities relate to the experimentally observed mass and width of the resonance.  

::: callout-important
The pole is literally a zero of the denominator in the amplitude, and its position in the complex plane determines the physical properties of the resonance.
:::
The influence of a pole diminishes with distance, analogous to signal strength weakening as you move away from a router. The complex plane acts like a multi-level structure, where resonances (poles) on different "floors" (sheets) still affect observations made on the real axis.  

::: callout-tip
For practical analysis, it is often most convenient to place branch cuts where they provide the clearest access to the poles of interest.
:::
The observed amplitude at a given point on the real axis is shaped by nearby poles, and their effects are directly visible in the data. This framework connects the mathematical structure of the amplitude to measurable physical quantities.

<!--
Cosine simularity: 0.940092977628945
-->
## Analytic Structure and Pole Characterization in Resonances

Pole locations are related to the observed mass and width, which are experimentally measurable. When observing a signal, it has a peak location and a full width at half maximum (FWHM). For narrow resonances, the width $\Gamma$ is approximately equal to the FWHM, and the mass $M$ is approximately equal to the peak location. However, this is not the case for broad resonances.  

The analytic structure of this function is simply a pole — there are no branch points or other complexities. A slightly more complex example involves the relativistic Wigner case, which includes a pole in the $K$-matrix and a square root branch point from phase space. The $K$-matrix is a method to incorporate poles while maintaining the correct analytic structure, and it works for multiple loops.  

The ultimate goal in data analysis is to characterize resonances by their pole mass and width. This is achieved using parameterizations like the $K$-matrix or other frameworks.  

::: callout-note
For narrow resonances, the pole mass and width directly correspond to the observed peak and FWHM, but this approximation breaks down for broader resonances.
:::
The $K$-matrix ensures the proper analytic structure, including poles and branch cuts, while remaining applicable to multi-loop processes.  

<!--
Cosine simularity: 0.9481211051651367
-->
## Branch Points and Threshold Singularities in Amplitude Analysis

We parameterize the amplitude using the $K$-matrix or, in simpler cases, the Breit-Wigner formula, which is a limiting case of the $K$-matrix unless constraints are applied. The amplitude's expression can be complex, with many terms, but it remains an analytic function. By fitting data, we determine the parameters and then explore the analytic structure.  

For branch points, you must decide their placement (e.g., to the left or right in the complex plane). Importantly, all features in the amplitude—peaks, spikes, or cusps—originate from singularities in the complex plane. A peak typically indicates a pole, while a cusp (seen in $|A|^2$ vs. $S$ plots) corresponds to another type of branch point.  

Every threshold introduces a singularity. For two-particle systems, this is a branch point. For example, $\pi\pi$ or $KK$ thresholds introduce branch points at specific energies (e.g., $KK$ at 1 GeV). These manifest as spikes in the amplitude, signaling the presence of a branch point in the complex plane.  

::: callout-note
Each branch point requires attaching a "tail" (branch cut) in the complex plane, which influences the amplitude's behavior.
:::
The $K$-matrix method ensures the correct analytic structure, incorporating both poles and branch points while remaining applicable to multi-loop processes.  

<!--
Cosine simularity: 0.9598991744416047
-->
## Threshold Enhancements and Pole Structures in Amplitude Analysis

Every branch point requires attaching a "tail" (branch cut) in the complex plane, and the placement of the cut is arbitrary — it's up to you how to draw it. However, this introduces additional Riemann surfaces.  

For a triangle diagram, if the amplitude has square root singularities at threshold, these thresholds only open new surfaces in the complex plane. The real singularities — or the strong features that produce intensity peaks — are poles.  

When the amplitude squared exhibits threshold behavior but rises sharply and then falls, this suggests the presence of nearby poles. If the poles lie below threshold, the amplitude peaks at that location. In such cases, this typically indicates a bound state — a pole on the real axis. However, a pole on the real axis does not produce a resonance-like peak.  

::: callout-note
Threshold enhancements are often signs of poles below threshold, which correspond to bound states.
:::
An analogous example is the signal strength from a router: the intensity is strongest near the router and diminishes with distance. This is how threshold enhancements can be understood. There is also the phenomenon of poles at the same locations but beneath the threshold.

<!--
Cosine simularity: 0.9755648752216739
-->
## Virtual States and Molecular Nature in Particle Physics

There is another phenomenon of the poles at the same locations, but underneath another sheet which is called a virtual state. Both of them are not that different from each other. This state can live forever — it is a real state that can travel, a particle that does not decay. Another case is the one that does not travel and does not decay. This distinction is one of the objectives and discussion points in the field.  

When you observe a new structure, the key questions are:  

-What kind of structure is it?  
- Is it related to a threshold?  
- Is it a pole sitting below a certain threshold?  
- Or is it a resonance in the complex plane unrelated to a threshold?  

Relation to a threshold indicates molecular nature. Every threshold involves two masses summed together, implying a continuum — one particle interacting with another. If a pole is related to a threshold, part of the wave function for this state is likely of molecular type.  

::: callout-note
Identifying thresholds and the complex structure of resonance poles is crucial for determining whether a state has molecular characteristics.
:::
<!--
Cosine simularity: 0.924689262282351
-->
## False Thresholds and Imaginary Parts in Amplitude Analysis

The expression $(S - M_1 + M_2)^2$ corresponds to the "soil threshold," but it is actually a **false threshold**. It appears artificially in our calculations due to the breakup momentum. However, the amplitude itself is not supposed to have a singularity at this point.  

This indicates that you should not take this expression literally and continue it beyond the threshold. Instead, the correct approach involves using the phase space factor $\frac{2p}{\sqrt{S}}$, which is the **imaginary part** of the amplitude.  

::: callout-note
The false threshold arises when only the imaginary part of the amplitude is considered. If you take the full bubble diagram, the false threshold disappears.
:::
The imaginary part can be derived from unitarity: when you cut the diagram, it corresponds to the product of matrix elements (both equal to 1) and the two-body phase space. This is why the false threshold appears — it is an artifact of isolating the imaginary part.  

Originally, we planned to compute the bubble diagram explicitly in this lecture, as it is closely related to unitarity. However, the discussion on false thresholds and their origin provides key insights into why such singularities are not physical.  

<!--
Cosine simularity: 0.8862112540954399
-->
## Climbing Kilimanjaro and Pumping Techniques

The period is when you take the imaginary part. The full amplitude does not have it.  

The easiest level for climbing Kilimanjaro is level one. We start with the green and orange, then proceed to gray, yellow, white, brown, and blue.  

For pumping, use three fingers at once without hardware. Start with the spot and orange, then release and hang on these two.  

The green and the last one is orange chicken.  

<!--
Cosine simularity: 0.9758889978114851
-->
## Market Writing and Infinite Concepts

All right. Now green and the last one is orange chicken.  
That's a large step. It's a matter of writing market here.  
Did you find infinite? But not the mother. Say the M1 and M2.  
But it's still well done.  

<!--
Cosine simularity: 0.9960124838713215
-->
## Pinchus Demonstration and Clarification

M1 and M2. Right. Okay. But it's still well done. Thanks a lot. You're about less. Nice. I'm not yet at pinches. Pinchus is like this. This is something different.
