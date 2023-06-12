# Ring populations: how to compare cities more agnostically

I love comparing the population of cities. I hate that every city is seemingly measured differently.

How am I supposed to answer my pressing questions like: [is Leeds big enough to deserve a tram][Leeds Supertram]?

[Leeds Supertram]: https://en.wikipedia.org/wiki/Leeds_Supertram

## Internet-Inconsistencies

![Bar chart of population vs source. They vary.](images/bham_pop_comparison_websites.svg)

<figcaption>

"Population of Birmingham" from the first few sources I could find on Google. Presumably the identical ones all use ONS' data, and the others are more 'international' statistics.
[Source](https://github.com/alifeee/blog/blob/main/ring-populations/data/birmingham_pop_from_sources.ipynb).

</figcaption>

![Two graphs. One of total population below vs area. It displays a log-looking plot. The other of population density around an area. It looks like exponential decay.](images/bham-pop-vs-area.svg)

<figcaption>

As you increase the area you're measuring, population increases, and density decreases! Revolutionary!
[Source](https://github.com/alifeee/blog/blob/main/ring-populations/data.birminghampop-vs-km.ipynb).

</figcaption>

![Bar chart of population vs source. This time with ring populations included. They vary. <10 km ring is closest to average.](images/bham_pop_comparison_websites_and_rings.svg)

<figcaption>

The same graph from above!
This time with the population within a 5/10/15/20 km ring around Birmingham.
New insights? Or content padding?
[Source](https://github.com/alifeee/blog/blob/main/ring-populations/data/birmingham_pop_from_sources.ipynb).

</figcaption>

![Maps displaying a 10 km ring around Manchester, Leeds, Birmingham, and Newcastle.](images/ring_comparison.png)

<figcaption>

Here. Find a city you know a bit. Does 10 km seem a good measure? Would your city be improved with a giant, imposing 10 km circle in the sky?
Screenshots from Tom Forth's [Circle Populations] (circle your own city [there!][Circle Populations]).

</figcaption>

![Bar chart showing population of the top 20 UK cities, by population. Shown is the population from "world cities", and then 5/10/20 km rings.](images/ukcities.svg)

Ring populations! Tag yourself.
[Source](https://github.com/alifeee/blog/blob/main/ring-populations/data/ukcities.ipynb).

</figcaption>

[Circle Populations]: https://www.tomforth.co.uk/circlepopulations/
<!-- [Ring Populations]: https://www.tomforth.co.uk/ringpopulations/ -->
