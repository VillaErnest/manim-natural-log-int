Hello there, today we will be having a discussion about an integration mathematical trivia. Specifically, we will be discussing about the curve of $y = \ln(x)$.

Let's first graph the curve and see what we are dealing with; It is said that the two areas bounded by the curve $y = \ln(x)$ from $x = 0$ to $x = e$ are equal.

How do we prove that the two bounded areas are equal?

We first need to get the upper and lower limit of each bounded areas.
We know that the lower limit for the first bounded area is at $x = 0$.
We can calculate he upper limit by getting the $x$ at the point of the curve where it intersect with $y = 0$ or the x-axis.

Substitute $0$ to $y$

Let's rearrange that

We exponentiate both side

Logarithm is the inverse of exponentiation thus $e^{\ln(x)}$ can be simplified into $x$ and $e^{0}$ is 1

So the limit of our first bounded area is from $x = 0$ to $x = 1$
And the limit of our second bounded area is from $x = 1$ to $x = e$

And in integral form, the first bounded area is: 

The second bounded area is:

Therefore we could say
$\int_{0}^{1} ln(x) dx = \int_{1}^{e} ln(x) dx$

But this is not right, we have into take into account the signs.
If we take a look into the graph, we notice that the first bounded area is inverted or below the x-axis, thus if we integrate it, we're adding negative areas of the rectangles resultng into a negative area. But we know that the two bounded areas are equal so if we were to integrate from $x = 0$ to $x = e$ then it would be equal to $0$ since that area cancels out.

So, we add a negative to one of the area to ensure the equality

Rearranging

To prove this equality or relationship, we can 2 different approach.

We can use our first equation and integrate it, It must result into $0$

Or use the second equation and the 2 bounded areas separetely and check if they are equal.

Let's first do the first approach

We are integrating $\ln(x)$ from $0$ to $1$ with respect to $dx$

We can use the integration by parts to integrate it

$\int u dv = uv - \int v du$

We let:
$u = \ln(x)$
$dv = dx$
Thus,
$du = \frac{1}{x} dx$
$v = x$

We substitute them back to the integration by parts

$x \frac{1}{x}$ is cancelled out.

$\int \ln(x) dx = \ln(x) \cdot x - \int dx$

$\int dx$ is just $x$

$\int \ln(x) dx = \ln(x) \cdot x - x$

Now that we have the integral of the function, we can evaluate it from $0$ to $1$.

$\ln(e) = 1$
$1 \cdot 1 = 1$
$1 - 1 = 0$

We can just simplifiy all the terms in the right to $0$

Thus this proves that the two bounded areas are equal but opposite in sign which results into $0$ since they cancel out each other.

Let us do the second approach, we already have the integral so we'll just use it and proceed directly to evaluating the integral.

$\ln(1) = 0$
$0 \cdot 1 = 0$
$0 - 1 = -1$

We can just simplifiy all the terms in the right to $0$

For the second bounded area

$\ln(e) = 1$
$1 \cdot 1 = 1$
$1 - 1 = 0$

We can just simplifiy all the terms in the right to $-1$ since we already solved that from the previous bounded area

We calculated the area of 1 sq. units and the first bounded area is negative. We can substitue back our answer to the equation we wrote to prove the equality.

In conclusion, we know that the two areas bounded by the curve $y = \ln(x)$ from $x=0$ to $x=e$ are equal.

Thank you for listening.

Credits

Credits to 
**Ernest Villacorta** for the script, animations and editing
**Paolo Mino** for the drafting of the script and researching
**Ralph Joseph Roa** for the voice recording

This video is made possible by the open source framework Manim or (Mathematical Animation) Community forked from 3blue1brown ManimGL.

Video is edited on CapCut.