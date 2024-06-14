<h1>Natural Log Integration Trivia</h1>
<span></span>

<hr>

**Author:** Ernest VIllacorta
**Date Created:** June 10, 2024
**Last Modified:** June 14, 2024

Hello there, today we will be having a discussion about an integration mathematical trivia. Specifically, we will be discussing about the curve of $y = \ln(x)$.

Let's first graph the curve and see what we are dealing with; It is said that the two areas bounded by the curve $y = \ln(x)$ from $x = 0$ to $x = e$ are equal.

How do we prove that the two bounded areas are equal?

We first need to get the upper and lower limit of each bounded areas.
We know that the lower limit for the first bounded area is at $x = 0$.
We can calculate he upper limit by getting the $x$ at the point of the curve where it intersect with $y = 0$ or the x-axis.

$y = \ln(x)$

Substitute $0$ to $y$

$0 = \ln(x)$

Let's rearrange that

$\ln(x) = 0$

We exponentiate both side

$e^{\ln(x)} = e^{0}$

Logarithm is the inverse of exponentiation thus $e^{\ln(x)}$ can be simplified into $x$ and $e^{0}$ is 1

$x = e^{0}$
$x = 1$

So the limit of our first bounded area is from $x = 0$ to $x = 1$
And the limit of our second bounded area is from $x = 1$ to $x = e$

And in integral form, the first bounded area is: 

$\int_{0}^{1} ln(x) dx$

The second bounded area is:

$\int_{1}^{e} ln(x) dx$

Therefore we could say

$\int_{0}^{1} ln(x) dx = \int_{1}^{e} ln(x) dx$

But this is not right, we have into take into account the signs.
If we take a look into the graph, we notice that the first bounded area is inverted or below the x-axis, thus if we integrate it, we're adding negative areas of the rectangles resultng into a negative area. But we know that the two bounded areas are equal so if we were to integrate from $x = 0$ to $x = e$ then it would be equal to $0$ since that area cancels out.

$\int_{0}^{e} ln(x) dx = 0$

So, we add a negative to one of the area to ensure the equality

$\int_{0}^{1} ln(x) dx = - \int_{1}^{e} ln(x) dx$

Rearranging

$\int_{1}^{e} ln(x) dx = -\int_{0}^{1} ln(x) dx$

To prove this equality or relationship, we can 2 different approach.

We can use our first equation and integrate it, It must result into $0$

Or use the second equation and the 2 bounded areas separetely and check if they are equal.

Let's first do the first approach

We are integrating $\ln(x)$ from $0$ to $1$ with respect to $dx$

$\int_{0}^{1} ln(x) dx = \Big|_{0}^{1} \frac{1}{x}$

We can use the integration by parts to integrate it

$\int u dv = uv - \int v du$

We let:
$u = \ln(x)$
$dv = dx$
Thus,
$du = \frac{d}{dx} \ln(x)$
$du = \frac{1}{x} dx$
$v = \int dx$
$v = x$

We substitute them back to the integration by parts
$\int \ln(x) dx = \ln(x) \cdot x - \int x \frac{1}{x} dx$

$x \frac{1}{x}$ is cancelled out.

$\int \ln(x) dx = \ln(x) \cdot x - \int dx$

$\int dx$ is just $x$

$\int \ln(x) dx = \ln(x) \cdot x - x$

Now that we have the integral of the function, we can evaluate it from $0$ to $1$.

$\int_{0}^{e} ln(x) dx = \Big|_{0}^{e} \ln(x) \cdot x - x$

$\int_{0}^{e} ln(x) dx = [(\ln(e) \cdot e - e) - (\ln(0) \cdot 0 - 0)]$

$\ln(e) = 1$
$1 \cdot 1 = 1$
$1 - 1 = 0$

We can just simplifiy all the terms in the right to $0$

$\int_{0}^{e} ln(x) dx = 0$

Thus this proves that the two bounded areas are equal but opposite in sign which results into $0$ since they cancel out each other.

Let us do the second approach, we already have the integral so we'll just use it and proceed directly to evaluating the integral.

$\int_{0}^{1} ln(x) dx = \Big|_{0}^{1} \ln(x) \cdot x - x$

$\int_{0}^{1} ln(x) dx = [(\ln(1) \cdot 1 - 1) - (\ln(0) \cdot 0 - 0)]$

$\ln(1) = 0$
$0 \cdot 1 = 0$
$0 - 1 = -1$

We can just simplifiy all the terms in the right to $0$

$\int_{0}^{1} ln(x) dx = -1$

For the second bounded area

$\int_{1}^{e} ln(x) dx = \Big|_{1}^{e} \ln(x) \cdot x - x$

$\ln(e) = 1$
$1 \cdot 1 = 1$
$1 - 1 = 0$

We can just simplifiy all the terms in the right to $-1$ since we already solved that from the previous bounded area

$\int_{1}^{e} ln(x) dx = [0 - (-1)]$

$\int_{1}^{e} ln(x) dx = 1$

We can see that the area is 1 sq. units. But the first bounded area is negative. We can substitue back our answer to the equation we wrote to prove the equality.

$\int_{1}^{e} ln(x) dx = -\int_{0}^{1} ln(x) dx$
$1 = -(-1)$
$1 = 1$

In conclusion, we know that the two areas bounded by the curve $y = \ln(x)$ from $x=0$ to $x=e$ are equal.

Thank you for listening.

Credits

Credits to 
**Ernest Villacorta** for the script, animations and editing
**Paolo Mino** for the drafting of the script and researching
**Ralph Joseph Roa** for the voice recording

This video is made possible by the open source framework Manim or (Mathematical Animation) Community forked from 3blue1brown ManimGL.

Video is edited on CapCut.
