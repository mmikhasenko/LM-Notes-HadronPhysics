## Kinematics of Decay and Scattering: The Källén Function and Dalitz Plot


**Lecture number 9.**
We start with a recap.
Let's discuss the problems:
- Who is finished with the first?
- Who is finished with the second?
Good.

---

What's the name of the area of the decay that we have here? The usual representation of the decay in the coordinates of the invariants is called the **Dalitz plot**. But you can use the same type of coordinates for the **crossed process**, for the **scattering process**.

> [!IMPORTANT]
> The **Källén function** (or triangle function) defines the kinematic boundary for both decay and scattering processes:
> \[
> \lambda(S, T, U) = S^2 + T^2 + U^2 - 2ST - 2SU - 2TU = 0
> \]

I don't want you to know the equation by heart, but rather I want to stress that the same equation would be relevant not just for the Dalitz plot and the decay region, but exactly the same equation would determine the border of the scattering process.

---

Can anyone tell me what equation that is? It's the **Källén function**.
The Källén function of \( S, T, U \) is equal to zero:
\[
\lambda(S, T, U) = 0
\]

The Källén function is the determinant of the **Chew-Low functions**. The Chew-Low function has the mass of the decaying particle, the pair mass of the two particles, and then the other one.

---

If you want to plot the area, you just look for the solutions in the plane.
Is this just common knowledge? It's easy to derive—either for scattering or for the decay.

The fact that it describes both appears once you look at the equations. Essentially, changing one particle to the other side does not change the kinematics. This comes from considering the scattering angle and requiring that the scattering angle is either \( +1 \) or \( -1 \), which determines the border:
\[
\cos \theta = \pm 1
\]

---

The meaning of this scattering angle changes slightly when you go from the scattering domain to the decay domain. But it's always seen in the **rest frame of two particles**.

For the **S channel**:
- Here's particle 1,
- Here's particle 2,
- 1, 2, 3.

This is the cosine theta. The condition for the border is determined by the equations where \( \cos \theta = \pm 1 \). It's the same for the decay and for the scattering.

---

The only difference is the **direction of the arrow**.
- For the **decay**, two particles collide, and the system you consider is the center of mass for the whole system—that's for the scattering.
- For the **decay**, it's just a subsystem of the final state.

The way you derive it: you write the cosine in terms of the invariants, set \( \cos \theta = 1 \), and arrive at the same equation.

---

> [!NOTE]
> The **scattering angle** \(\theta\) in the center-of-mass frame relates to invariants via:
> \[
> \cos \theta = \frac{t - u}{\sqrt{\lambda(s, m_1^2, m_2^2)}}
> \]
> where \(s, t, u\) are Mandelstam variables and \(\lambda\) is the Källén function.

## Scattering Kinematics, Unitarity, and the Optical Theorem



> [!NOTE]
> Key formulas discussed in this section:
> - Breakup momentum (phase space factor):
>   $$
>   \rho = \frac{1}{16\pi^2} \cdot \frac{2p}{\sqrt{s}}
>   $$
> - Unitarity condition for partial wave amplitude:
>   $$
>   \text{Im}\, A_l(s) = \rho(s) |A_l(s)|^2
>   $$
> - Optical theorem:
>   $$
>   \text{Im}\, A(s, t=0) = 2\sqrt{s}\, p\, \sigma_{\text{tot}}(s)
>   $$

I'm surprised you need scattering.
Most of the variables are defined for momentum, and then you use energy conservation.
You can introduce Källén functions there—or tuning functions.
The channel function is just a breakup momentum.
I would consider this once you derive it, once you can consider this as common knowledge.
It's easy to remember, is it not? You have derived this one or you can look it up in the Bjorken and Drell book.
I just don't really see how to derive it.

The recipe is you start with the scattering kinematics, and that's unique because you know that the ranges of the physical region correspond to the cosine going to plus one or minus one.
But let's not get distracted because there's a lot of material here.

---


One thing to realize is that once you input this into Mathematica and ask what are the regions in the complex two-dimensional plane where this equation is satisfied, you don't get only this—you also get the other regions that correspond to the crossed process.
Here, I'm asking what other physical processes are connected by crossing and to draw the regions.

The answer here is that the regions will lie somewhere here, and these lines where the Kibble function is zero are the borders of the other process.
The process asked to indicate here can be understood by looking at your original kinematics.
If this is zero going to 1, 2, 3, that process.
Here we define $S$ so that process would correspond to—the variable $S$ that you have here for any place inside the Dalitz plot is a positive quantity, and you want to keep it positive.
For this area, it's bigger but still positive, while the other one becomes negative.

For this area, these two particles are still in the physical space, so they are in either the initial state or final state, while the other one gets crossed to the other side.
It's a $0, \bar{3}$ scattering into $1, 2$.
The process we talk about when we discuss this domain is $\pi^+ \pi^- \rightarrow \pi^0 \omega$.
Then we put it there by $\pi^+ \omega \rightarrow \pi^0 \pi^0$, and we talk about this domain, but in terms of $\pi^- \pi^0 \rightarrow \omega$, what is $1, 2,$ and $3$? One has to be always consistent—this is zero, depending on the axis, right?

The $\omega \pi^0$—I call this one, this is two, this is three.
So the process here would be zero.
But why? For the first process, we moved $\pi^-$ to the other side, not $\pi^0$.
Because one axis is $\omega \pi^0$ and another is $\pi^- \pi^0$, right? $\pi^-$.
No, it's diagonal.
No, it's $\pi^- \pi^0$.
So that one.
If there are two $\pi^0$s, shouldn't we move $\pi^0$ to the other side?

---


I argue that way.
I have here $\omega$ and here $\pi^0$, and that's what my channel represents.
That's the threshold for their channel.
That's the threshold for that channel, and that will be the production threshold for the initial state.
I always have this $S$ increasing along this axis.

Are these asymptotes of the hyperbola?
Well, yes.
I'm asking because in the original Mandelstam paper, they're not.
They try to go over it—I never understood.
No, going over is fine, but the question is, do they approach them in the infinite energy region, and that's where you can neglect the masses?
I think so.
Asymptotes means not here, and they can cross.
But when the energy gets high, do you approach this line?
I think so.

Is it that line or is it slightly offset by the threshold?
Let me draw it here—what scattering process we are dealing with.
The zero scatters with the particle: $1, 2$; $1, 3$; $2, 3$.
The energy is positive.
Here is the zero with one bar.
The process here is $\pi^+ \omega \rightarrow \pi^- \pi^0$.
You see that for the particle you cross to the other side, it becomes an antiparticle.
But for $\omega$ and $\pi^0$, particle and antiparticle are the same.

---


Things get a bit trickier once you take into account that particles have spin.
I should have written here $\lambda$ because $\omega$ has spin, and then helicities also have peculiar relations with respect to crossing.
We don't talk about that—for kinematic considerations, it's enough.
You can think of particles as scalars.
To really relate the amplitudes with helicity indices requires more work.

Draw regions, indicate process.
I think we did draw roughly the regions together.
More accurately, you have to open a computational notebook—otherwise, it's intuitive.

---


> [!IMPORTANT]
> The optical theorem relates the forward scattering amplitude to the total cross-section:
> $$
> \text{Im}\, A(s, t=0) = 2\sqrt{s}\, p\, \sigma_{\text{tot}}(s)
> $$
> This is derived from unitarity and is valid in the elastic region.

Questions here quickly: the second unitarity equations.
We consider the elastic scattering process.
Shall we break this down?
What does it mean?
What are $S$ and $T$?
Maybe you guys follow—what is $A$?
What is $S$ for the scheme?
$A$ is the scattering amplitude, $S$ is Mandelstam $S$.
How do you compute this variable?
It's like $P_0, P_1$.
And $T$ is not a Mandelstam variable related to the—it's computed by the difference of these two momenta, and then the scattering amplitude.

I'm saying "process," but in fact, it's the scattering amplitude.
What does elastic mean here?
I don't think we discussed elastic, but maybe you've heard of this.
Energy is conserved—energy is always conserved.
That we're doing the same check?
Exactly.
The initial state and the final state are the same.
That's what I mean.
Actually, here it's somewhat slang—"elastic" is used in different contexts.
But when we talk about an elastic process, we usually say the initial state is the same as the final state.
Elastic scattering.

Formulate $A$ using explicit dependence.
Formulate partial wave unitarity and the optical theorem.
Alex, can you tell me the unitarity equation for $A$?
Can you help me?
Like, what should I relate?
I don't know how you've introduced amplitudes so far, but I always see that this—you know, normalized with regards to energy, which introduces a phase space factor.
So I would say it's like $1/(1 + i\rho A)$.

Sorry, $A$ times—phase space factor times $A$.
Equals 1?
Absolutely equals 1.
So my first guess would be $1/(1 \pm i\rho A)$.
I want to write the unitarity equation for $A$.
How unitarity constrains my $A$?
When you do this consideration, you get constraints on the imaginary part of $A$, and then the imaginary part of $A$ is related to other amplitudes.

Maybe I draw it diagrammatically first, and then you help me get the equations.
But this is the optical theorem, right?
No, that's the unitarity equation for $A$.

What is the difference between $T, T',$ and $T''$?
Very good.
We are discussing the elastic process, and so $S$ and $T$ are defined.
The imaginary part of the amplitude is related to the amplitude squared in the elastic region.
This is the unitarity equation—one has to integrate over all intermediate states when you contract one amplitude to another.
But since it's elastic, it's the same state that's present here.

The same particles—the only difference is that the integration takes into account that the configuration of the particles in the intermediate states could be different.
If I consider this process of the initial state scattering to the final state, the intermediate state that appears in unitarity equations—well, essentially what the unitarity equation says is that you have to sum over all intermediate states that appear for the elastic region.

It's just different configurations—there is only one type of particle state present, and therefore the integration or phase space includes only different orientations of the particles.
They are the same particles.
Once you go to high energy, there will be many more intermediate states that come into the unitarity equations.

To clarify—maybe this drawing can clarify the configuration we have to integrate over.
We fix the initial state, we fix the final state, and then $T$ is the scattering angle between the initial and final state.
We say they form a plane—this sits in the $xz$-plane.
Here is the $x$-axis, here is the $z$-axis in the plane.
The only variable we have, $T$, is connected to the scattering angle between the initial and final state.

This angle $\theta$ is connected to $T$.
What appears in the intermediate state is the arbitrary configuration in the space of the vector of the intermediate state here.
I call here $P_1, P_2$; here is $Q_3, Q_4$; and here is $P_3, P_4$.
There are two scattering processes: first from $P$ to $Q$, and then from $Q$ to $P$ again.
We have to integrate—the plane is fixed, $Q$ points somewhere in space, and we have to integrate over all possible configurations.
That's why $T', T''$ come in.

This is the unitarity equation for the full amplitude.
Great simplification.
Can you write phase space explicitly?
Because $T'$ and $T''$ are what they should be in the phase space.
It's a regular two-body phase space, and we have to integrate over all possible configurations of one vector and a second vector, but there is a constraint making them back-to-back.

Writing this in terms of $T'$ and $T''$ is a highly nontrivial task.
The way to proceed—to get our regular unitarity that we know, where the amplitude is related to itself—requires partial wave expansion.
The next step would be to do what we discussed last lecture: take each amplitude $A$ here, $A$ here, and $A$ there, and expand them into partial waves.

The partial waves would involve the connection between the scattering angle in $T$ or $T''$, and then we use properties of angular momentum and the angular functions to get rid of this integral essentially.
Once we do, this equation becomes very simple.
Instead of the integral over phase space, we simply have a phase space factor—it's not an integral, it's just an energy-dependent factor.

So this $\rho$ is:
$$
\rho = \frac{1}{16\pi^2} \cdot \frac{2p}{\sqrt{s}},
$$
where $p$ is the breakup momentum in the system.
It's a function of energy.
And then here $A$ appears—that's the unitarity equation for the partial wave.
The partial wave amplitude has only one dependence, on $S$, and things drastically simplify.
There is no $T$ any longer.

Another thing I wanted to point out—coming back here—you see that there is $T'$ and $T''$.
The reason they are different is that $T'$ is measured for the vector $Q$ with respect to $P_1$.
So it's the amplitude computed between $Q_3$ and $P_1$—this vector and that vector.
Then $T''$ is computed between $Q_3$ and $P_3$—the intermediate and final state.
Either take these vectors or these vectors, and that's what makes the variables different.

There is one limit where these variables become the same: when you have not just elastic scattering but forward scattering.
When you have kinematics where you collide the particles and they just pass through—it's forward scattering.
In that case, $A$ is equal to—sorry, $T$ is equal to zero.
And in that case, if $P_1 = P_4$, $T'$ and $T''$ become the same.

Forget—there are two values for $T$: $T = 0$ and $T =$ (some negative value).
For this type of scattering, forward and backward—no, for backward, $T$ equals its maximum value, it's negative.
But for forward scattering—you're right, but it's a different limit.

Now I want to discuss the forward limit.
In the forward limit, the point is that this amplitude becomes the same as this amplitude, and we can write the squared amplitude already right here.

My question was, isn't it the same for backward as well?
No, I don't think so.
The reason is—for forward, we have to consider this is $P_1$, and this is $Q$, and this is $P_3$, and this is $Q$, right?
That's forward scattering.
And that's why what makes this angle the same as this angle.
If you consider backward scattering, $P_3$ will be in that direction, $Q_3$ will be this, and the angle is different.

You can identify $T'$ and $T''$ to be the same in backward scattering, but—

Finishing this, I wanted to give the final expression for the optical theorem that comes from this.
It's nothing else but the full cross-section.
Here you have the optical theorem: the amplitude for forward scattering is equal to the flux times the full cross-section.

It's important to acknowledge the fact here that this is valid in the elastic region.
Forward scattering is really important because that's when you identify—that's how you get rid of one of the variables.
The cross-section is a function of $S$ only—the total cross-section doesn't know anything about angular dependence.
So you integrate this, and this happens once you identify two amplitudes to be the same and take into account the phase space.

This is from unitarity.
This is the first condition written down, and what comes down—the dependence on the cross-section and the flux is the optical theorem for you.

So what is what here?
The first is unitarity.
The second is the optical theorem.
I'm not sure we discussed this last time, but the optical theorem comes in quantum mechanics.
Here is the analog of this, related to the transition matrix element amplitude we have in the scattering process.

---


- **Unitarity for $A$**:
The imaginary part of the amplitude is related to the amplitude squared in the elastic region.
- **Partial wave unitarity**:
$$
\text{Im}\, A_l(s) = \rho(s) |A_l(s)|^2
$$
Here, $A_l(s)$ depends only on $S$, and partial waves don't mix—only the same $L$ appears on both sides.
- **Optical theorem**:
Relates the forward scattering amplitude to the total cross-section:
$$
\text{Im}\, A(s, t=0) = 2\sqrt{s}\, p\, \sigma_{\text{tot}}(s)
$$

Good.
When we discussed the optical theorem last time—so that's good that we discussed today.
It's important to relate the concepts to each other.

Today in the lecture, we will go through analytic functions and see how scattering matrix principles are constrained by their properties.
How scattering amplitudes are constrained by the properties of the scattering matrix, such as Dyson analyticity and partial analyticity.
To consider this first part, I want to make the first part a little more mathematical by discussing analytic functions and real functions.
I will say a few words about analytic continuation at the end.

## Analyticity and Singularities in Hadron Scattering Amplitudes


In hadron physics, we deal with interactions that are not driven by simple Lagrangian or Hamiltonian dynamics.
We cannot proceed unless we restrict ourselves to specific **near-threshold interactions**.
We cannot derive the scattering amplitudes from first principles.
Instead, a different approach is used.

We study general principles of scattering theory, and it appears to be constraining enough to derive the general form of the amplitude, with parametric freedom around branches that could be fixed from the data.
Therefore, the approach utilized in hadron physics to describe the scattering of hadrons, especially in experimental data, is to use **general parameterizations of the amplitudes** that satisfy unitarity and elasticity.
Rarely, crossing symmetry can be satisfied—very rarely.
Then, we fix the parametric freedom and obtain the scattering amplitude as a mathematical expression to study its properties.

While studying the properties of the scattering amplitude, we obtain properties of the objects we describe—the **resonances**.
So that's the program of hadron spectroscopy: amplitude building and scattering theory tools to access the properties of the objects.
We study resonances, and one of the constraints is **analyticity**—another one, especially, telling that the function constrains different regions in the variables.
If a function depends on $s$ and $t$, this function must extend in validity beyond the physical region, and extra constraints arise.

---

> [!IMPORTANT]
> **Key Insight**: The scattering amplitude $\mathcal{A}(s,t)$ is a complex function of Mandelstam variables $s$ and $t$, which can be analytically continued into the complex plane. This allows us to study singularities (poles, branch cuts) that reveal physical properties like resonances.

---

Then, we consider the amplitude as a complex function of its variables—the scattering amplitude.
While observables are all real values (the cross-section is a real number), the amplitude itself is a complex number: it has an **absolute value** and a **phase**.
This, in turn, gives important information about the scattering process.

As we saw in the problem we discussed earlier, the amplitude was a function of two variables, $s$ and $t$.
So it's a **multivariable function**—a complex multivariable function.
And it appears that we will gain some benefits and new insights into the amplitude if we consider it not just as a complex function, but also as a function of **complex variables**.

What we are going to do, as part of the theoretical exploration, is take our $s$ variable—something that used to be physical—and make it complex.
We'll see what the properties of the amplitude are when we make the energy of the scattering complex, or when we make the angle of the scattering a complex number—not 30 degrees, but $30^\circ + i$.
And we'll see that this gives us new insight.

What's important for us is not just that the amplitude is a complex function, but also that it's an **analytic function** of its arguments everywhere in the complex plane, except for a few minor segments.

---

Before going into the details, I would like to discuss analytic functions.
So here is the mathematical part of the lecture.
I would like to remind you what analytic functions are, or as we also call them, **holomorphic functions**.
Don't be scared by this word—"holomorphic" simply means analytic.

A holomorphic or analytic function is one that matches its Taylor series in the vicinity of every point of the complex plane or its domain.
If you look in mathematics books, it says an analytic function is one that is **complex differentiable** everywhere in the complex plane.
But we will consider domains of analyticity—the function doesn't have to be analytic everywhere in the complex plane, just in certain domains.
And in that domain, complex differentiability simply means it's equal to its Taylor series.
So there is a polynomial series that approximates the function exactly at every point in the plane or in the vicinity of every point.

I could remind you what the Taylor series means, but you probably remember that expression with the derivatives—essentially a polynomial.
That's the point.
The series can go to infinity, but the function must match it.

Now let's discuss examples.
Clearly, if required, the function matches the polynomial series.
Any polynomial function is analytic in $\mathbb{C}$.
Polynomials are excellent functions—analytic everywhere—but also simpler functions like $\sqrt{z}$ or $\log z$ are analytic everywhere except on a line segment.
And this line segment is the **branch cut**.
For every branch cut, we have two **branch points**.
Sometimes one of the branch points is at infinity, and the other is in the finite range.
And then the line that connects the branch points is called the branch cut.

---

> [!NOTE]
> **Branch Cut Examples**:
> - $\sqrt{z}$: Branch cut along $(-\infty, 0]$
> - $\log z$: Branch cut along $(-\infty, 0]$
> - $\sqrt{z - a}$: Branch cut from $a$ to $-\infty$
> - $\sqrt{(z - a)(z - b)}$: Branch cut connecting $a$ and $b$

---

Let me draw a few examples convenient to discuss.
The $z$-plane, where along the $x$-axis we have the real part of $z$ and the $y$-axis is the imaginary part of $z$.
And then for every point I can plot, it is the real part of $z$ plus $i$ times the imaginary part of $z$.
So what I can do using this plot is to indicate where the function is analytic and where it is not.
There are regions of analyticity.

For example, for a function like $\sqrt{z}$, there is this branch point at zero and the branch cut going to the left, indicating that if I compute the function on one side and on the other side, I get different values.
I think it's pretty clear: if I compute $\sqrt{z}$ at $-1 + i\epsilon$, I get $+i$.
And if I compute this from that side, I get $-i$.
It doesn't happen on that side.
If I compute the function at $1 + i\epsilon$, I get $1$.
And if I compute it from that direction, like $1 - i\epsilon$, I also get $1$.
But on that side, there is a discontinuity of the function.

Just to demonstrate that the branch cut doesn't have to be at 0.
For the function $\sqrt{z - 1}$, the branch cut starts at 1.
We go backwards.
For the function $\sqrt{-z}$, the branch cut starts at 0 and goes upwards.
For the function $\sqrt{(z - 1)z}$, the branch cut starts at zero and goes to 1.
For the function $\sqrt{z^2 - 1}$, the branch cut is more complicated.
It starts at 1, goes to 0, then to $+\infty$, comes back from $-\infty$ again to $-1$.
The last example is $\log z$.
In that case, the branch cut starts at zero and goes backwards.

Another class of functions and another type of singularity that is present is the **poles**.
Poles are functions that have poles.
They are isolated singularities where a function approaches infinity, complex infinity.
For example, $\frac{1}{z - (1 - i)}$.
When $z$ is equal to $1 - i$, we approach the pole of the function; the function is undefined, it's complex infinity.
And then once we go away from this point, the amplitude value $R$ is really high.

What I want to say is that the pole value would be felt even away from it.
We will see that all of the features that we see in the scattering, like bumps or cusps, are related to the singularities in the complex plane.
The branch points are just doors to other domains of analyticity.
The poles are something that makes the strength of the amplitude.

I was thinking of this nice example of the complex multi-floor house that has many internet routers, and the poles are your routers.
If you want to have strong internet, you better sit next to the router, and that provides you a signal.
The closer you are to this internet router, the better internet you have—it's a higher value of the absolute value of the amplitude.
If you measure the process and you see that the cross section is large, something must be driving this large cross section.
And it's probably a pole somewhere in the complex plane.

Interesting things about the cuts—those cuts.
One thing to consider is that the cuts are the doors to other domains, every cut.
You probably have heard it said that branch points are fixed, but the way you draw the cuts is arbitrary—up to you.
I don't like this way of putting it.
But this is another way of saying that the way we draw the cut, you can draw the cut differently by extending the domain.

The way I'd like to think of this is that for every cut value, you can come up with different functions.
You deal with a function that has a branch point at zero and the cuts towards the left.
And the claim is you can come up with a different function, call it $f_2$, that's defined in the complex plane such that it's analytically continuous.
The function above the cut analytically continues the domain of analyticity.
So I can come up with a different function.
In that case, it's $-\sqrt{z}$.
But I can tell you the recipe to come up with this $f_2$ such that if you join the function—you take this domain and that domain—so there are no cuts any longer.
The branch point is still there, but the function is analytic in this domain.
If I take this and that, one can see this as the way to go beneath the cut.
So you can analytically continue the function down.
And that's the perspective that I offer.

There is the function defined everywhere in $\mathbb{C}$ except a finite number of points, except a finite number of segments.
And you can compute.
If I ask you to compute a value, you can compute the value everywhere.
The cut locations are fixed; we don't touch them.
We just come up with a different function $f_2$ that's—for a start—it has nothing to do with $f$.
It's again another function that I define everywhere except a finite number of segments.
But what makes us consider them together? The one analytically continues the other.

If you come back to this function, $\sqrt{z - 1} - \sqrt{z}$, shouldn't there be two branches? Two branch cuts.
One from 1 to $-\infty$, from 0 to $-\infty$.
Yes, so what is this? This is minus.
If it's a minus, you're right.
But if it's multiplied, then that's different.

For all of the functions with the cuts, we can discuss what is $f_2$, what function makes analytic continuation.
For any of them, you can ask me a question: What happens? What function would analytically continue the domain of analysis in that direction?
And I know the answer.
Just minus sign here or here or there.
For any way you approach the cut, there should be analytic continuation.

## Riemann Sheets, Analytic Continuation, and Real Analyticity in Scattering Amplitudes


The other notion, the other way people talk about this, is **Riemann sheets**.
Instead of saying there is one function, a second function, a third function, people say there is just one **multivalued function** with values on different Riemann sheets.
But this is the same as saying there are $F_1, F_2, F_3$.
So $F_1$ is the value of the function on the first Riemann sheet, $F_2$ on the second, and so on.

**Questions?**
Now, while I’m cleaning this up, can you come up with the **analytic continuation**?
What would $F_2$ look like here if I want to analytically continue?
And here—quickly, what is $F_2$? What is $F_3$?

For the **square root**, the other sheet or branch is simply the negative value.
You can convince yourself by computing $\sqrt{I + \epsilon}$ and $\sqrt{I - \epsilon}$ for $F_3$.
They should match if the continuation is correct.

Now, what is $F_2$ here?
It can’t be the same, because I can demonstrate it with the **logarithm**.
Here, $F_1$ is $\log(-1 + i\epsilon)$, which equals $i\pi$.
On the other side, $\log(-1 - i\epsilon)$ equals $-i\pi$.
No, it’s actually $+i\pi$.
We computed this already—it’s $-i\pi$.
If we add $i\pi$, we get the value on that side: $F_2 = +i\pi$, ensuring analytic continuation.

> [!NOTE]
> The logarithm function on different sheets:
> \[
> F_1(-1 + i\epsilon) = \log(-1 + i\epsilon) = i\pi
> \]
> \[
> F_2(-1 - i\epsilon) = \log(-1 - i\epsilon) = -i\pi
> \]

Why is it Sheet 3 right away?
It’s not Sheet 3—it’s just labeling.
You can call it 2 or whatever.
The function going in that direction is $F_3$, which analytically continues from below, while $F_2$ continues from above.
This is just my notation.

---

An interesting aspect closely related to the **scattering amplitude** is **real analyticity**.
You can take "real analytic" literally—a function that is analytic and real.
But I’d like to extend this definition: a function is **real analytic** if it has a segment along the real axis where it is real.

Imagine the $z$-plane with the real $x$-axis.
If $F$ is real for real $z$, it has peculiar properties.
It satisfies the **reflection principle**.
Analyticity is a special type of continuity—once you move away from the real axis, the imaginary part must appear.
If the imaginary part grows in the positive direction above the axis, it must grow in the negative direction below.
This is the **Schwarz reflection principle**:

\[
f(z^*) = f(z)^*
\]

The star denotes **complex conjugation**—flipping the imaginary part.

We started with a function real on a segment.
Analytic continuation shows the only way it stops being real is by developing a **branch point**.
The function becomes non-real only when a branch point and cut appear.
The imaginary part develops oppositely on either side of the cut: positive on one side, negative on the other.
The **discontinuity** across the cut is twice the imaginary part because they grow in opposite directions.

\[
\text{Disc}\, f(z) = 2i\,\text{Im}\, f(z)
\]

Now, the second branch cut opens.
For analytic functions, the domain must be open.
You can always extend a closed segment to an open one.
But once you include an edge, you can’t guarantee smoothness in a small circle around it.

**Scattering amplitudes** are real analytic functions.
For a 2-to-2 scattering amplitude $A$, we consider it on the **Mandelstam plane** with $S$ and $T$.
If we fix $T$ (e.g., for 30-degree scattering), $A$ becomes a function of $S$ alone.
In the complex $S$-plane, $A$ has thresholds for the $S$- and $U$-channels and a real segment.
The Schwarz reflection principle applies, linking the discontinuity to the imaginary part:

\[
\text{Disc}\, A(s) = 2i\,\text{Im}\, A(s)
\]

This connects to **unitarity**, as the imaginary part relates to the discontinuity.

Analyticity helps explain peaks in the amplitude.
Branch points on the real axis cause **kinks**—derivatives don’t exist there.
If the function spikes, there might be a **pole** beneath the cut.
By examining $F_2$, you can trace the origin of such features.

---

In **multichannel scattering**, the amplitude has branch points for all coupled channels.
A **scattering channel** is a subsystem of particles that can participate in initial or final states.
Examples include:

- $\pi\pi$
- $KK$
- $\eta\eta$
- $\eta'\psi$
- $\pi\Lambda$
- $KN$

These channels scatter into each other and are labeled by indices $a, b, c$.

Another example is **baryon scattering**: $\Lambda K$ and $\Xi\pi$.
These are **coupled channels**—their scattering problems are interconnected.
The amplitude $A_{ab}(s)$ describes scattering from channel $a$ to $b$.
For example:

\[
A_{\Xi\pi \to \Xi\pi}(s), \quad A_{\Lambda K \to \Lambda K}(s), \quad A_{\Xi\pi \to \Lambda K}(s)
\]

All these amplitudes share the same complex plane with branch points for each channel.

Away from the **elastic region**, more scattering possibilities arise.
In unitary equations, you don’t just have $a \to a$ but also **cross-channel terms**.
This reflects the coupled nature of the problem.

## Causality, Analyticity, and the Optical Theorem in Scattering Amplitudes


That brings me to the end questions. Having dared to use the word **causality**, I always assume that the answer for causality is connected to **analyticity**. That forces the amplitude to be real analytic.

I didn’t prove it—I said it's given that the amplitude has this form. But that actually originates from the **causality principle**: you must have only singularities along the real axis and only of the type of cuts and poles. There are no singularities in the complex plane allowed—cuts are not allowed to go upwards. This is the only configuration that's allowed.

It’s because I had to demarcate the location of the poles or just the fact that the function is analytic. The function must be analytic everywhere in the complex plane away from the real axis. That's what causality tells us.

But that seems more like a tool. In the end, you're just trying to describe physics effects. You get the answer, but you don’t care where it comes from—it comes from **probability considerations**.

This causality seems like a decent thing to say: actions come afterwards. Causes come after actions. But this is always the case. You use **microcausality**.

With this hypothesis, you get disconnected regions, but then you can elevate it to complexify them. That's what you're doing here. At some stage, you also mentioned **complex scattering**. That would mean you make $T$ complex as well. You can relate all these regions, and that’s the **monodromy processes** which transfer things more than just...

The introduction in the Martin experiment suggests that these are all interrelated objects—different amplitudes that look different but are connected.

> [!NOTE]
> **Why complex angles?** The function $S$ is a complex function of two variables. It’s complicated to treat them simultaneously. $T$ is almost an angle—it depends on the angle. It’s a function of two variables, and both could be complex.

We haven’t discussed this, but causality seems to relate all these different regions. Are you asking how causality acts in the multivariable case? How does it lead to analyticity?

In two dimensions, you go to four dimensions because $s$ and $t$ will be complex. Instead of talking about the domain of real analyticity where you have a segment of real values, you need a domain where the function is real and exists.

We demonstrated it here: for fixed $t$ (negative, in a scattering region), the distance between branch points is controlled by $t$. Change $t$, and they get closer. If you look at a slice, there’s a region where they overlap and no longer have a segment of real analyticity. But since for different $t$ there is a segment, we can discuss real analytic properties and analytically continue to the overlapping region.

Why do the branch points move when you change $t$? The threshold $(m_1 + m_2)^2$ is fixed, but the other point moves.

---

Now, the **optical theorem**. It comes from unitarity. You have a transition matrix element $\langle B | T | A \rangle$, which equals the matrix element because these states don’t know about each other.

This is like squeezing in an intermediate state. The identity is the integral over the product of states. In continuous form, this is shorthand for summing over intermediate states $C$.

The optical theorem appears in this form:

$$
\text{Im}\, \mathcal{M}(A \to A) = \sum_C \int d\Pi_C |\mathcal{M}(A \to C)|^2
$$

This comes from unitarity $S^\dagger S = \mathbb{1}$, or equivalently $i(T - T^\dagger) = T^\dagger T$.

The left-hand side has a delta function, and the right-hand side has the phase space factor. The delta function cancels, leaving the basis.

You can wrap this into a **partial wave expansion**:

$$
\mathcal{M}(s, t) = 16\pi \sum_\ell (2\ell + 1) a_\ell(s) P_\ell(\cos\theta)
$$

The generalized optical theorem comes from Heisenberg and is derived from unitarity.

The amplitude $\mathcal{M}$ is written as $\tilde{\mathcal{M}}$ times a kinematic factor. The singularity-free argument suppresses the volume divergence.

For less competitive momenta, the imaginary part of the amplitude is proportional to the matrix element squared.

---

Key points:
- **Causality** restricts singularities to the real axis.
- **Analyticity** is enforced by causality.
- The **optical theorem** links unitarity and scattering amplitudes.
- **Partial wave expansions** decompose amplitudes into angular momentum components.

