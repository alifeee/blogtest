# I biked from Birmingham to Cambridge (a tribute to National Cycle Routes)

<div class="toc">

1. [Technicalities - how far *did* I bike?](#technicalities---how-far-did-i-bike)

1. [How to plan a bike route](#how-to-plan-a-bike-route)

    1. [Google Maps hates bikes](#google-maps-hates-bikes)

1. [National Cycle Routes!](#national-cycle-routes)

    1. [Why get lost when you can not get lost](#why-get-lost-when-you-can-not-get-lost)

    1. [Do they go the right way?](#do-they-go-the-right-way)

    1. [Why go the right way when you can go the wrong way](#why-go-the-right-way-when-you-can-go-the-wrong-way)

    1. [How to fix the problem of going the wrong way](#how-to-fix-the-problem-of-going-the-wrong-way)

1. [And what?](#and-what)

1. [Appendix: Tools](#appendix-tools)

</div>

Recently, I biked from Birmingham to Cambridge.

More accurately, I half-biked, half-trained from Birmingham to Cambridge.
If it sounds more impressive, I "biked the distance from Birmingham to Cambridge".

![Sketch of the route that I took from Birmingham to Cambridge. Half of the image is shortcut via train.](./images/route_descriptive.svg)

<figcaption>

Look ma! I did most of it with my own legs!
[Source](https://github.com/alifeee/blog/blob/main/bike-to-cambridge/src/route.ipynb).

</figcaption>

## Technicalities - how far *did* I bike?

![Screenshot from Google Maps showing the crow flies distance from Birmingham to Leamington to Bedford to Cambridge: 148 km](./images/crow_flies_distance_annotated.png)

<figcaption>

If I were a crow, it would be a nice life.
I would also get to Cambridge in 148 km, with stopovers.
From [Google Maps](https://maps.google.com/)

</figcaption>

## How to plan a bike route

### Google Maps hates bikes

![Comparison of the route from Google Maps and cycle.travel. They look broadly similar.](./images/google_vs_cycle.travel_routes_with_legend.png)

<figcaption>

Spot the difference.
From [gpx.studio](https://gpx.studio/).

</figcaption>

![Comparison of road type statistics for the Google Maps route and cycle.travel route. For (Google Maps, cycle.travel): busy roads (46.8 km, 2.4 km), paved roads (90.5 km, 155 km), paved paths (32.6 km, 48.3 km), unpaved paths (21.1 km, 5.3 km), pushing (6.6 km, 0.58 km).](./images/google_vs_cycletravel_stats.svg)

<figcaption>

Which of these would *you* rather bike on?
[Source](https://github.com/alifeee/blog/blob/main/bike-to-cambridge/src/maps_vs_cycleroutes.ipynb).

</figcaption>

## National Cycle Routes!

![Photo of a bike path going down to a canal towpath.](./images/canal-bike-path.jpg)

<figcaption>Ramp down to the Stratford canal, National Cycle Route 5.</figcaption>

### Why get lost when you can not get lost

![Photo of large car half-submerged as it drives through a ford.](./images/ford.jpg)

<figcaption>

Whoosh!
Picture from a bridge next to the ford.
Would've been fun to try and get through on a bike though.

</figcaption>

![Photo of a road in grey weather, with a pothole filled with water.](./images/wet-route.jpg)

<figcaption>

Get to the end of this, but a thousand times, and you might end up in Cambridge.

</figcaption>

### Do they go the right way?

![Screenshot of OS Maps between Birmingham and Cambridge with all national cycle routes shown. There are none that really go in the right direction.](./images/national_cycle_routes_annotated.png)

<figcaption>

Here's a game. Why does everything go the wrong way?
Sorry, that wasn't a game.
From [OS Maps](https://explore.osmaps.com/).

</figcaption>

### Why go the right way when you can go the wrong way

![Polar bar chart, showing the proportion of the route (from cycle.travel) which goes in which direction (North/East/South/etc)](./images/directionality_proposed_route.svg)

<figcaption>

Turns out the fastest way to get somewhere is to go that way.
[Source](https://github.com/alifeee/blog/blob/bike-to-cambridge/bike-to-cambridge/src/directionality.ipynb).

</figcaption>

![Polar bar chart, showing the proportion of each of the three actual bike routes which goes in which direction (North/East/South/etc)](./images/directionality_actual_routes.svg)

<figcaption>

Going the right way is for nerds.
[Source](https://github.com/alifeee/blog/blob/bike-to-cambridge/bike-to-cambridge/src/directionality.ipynb).

</figcaption>

### How to fix the problem of going the wrong way

![Photo of my bike inside a train carriage.](./images/bike-on-train.jpg)

<figcaption>

I'm big. My bike is big.
Sometimes we fit in a train.

</figcaption>

![Screenshot from a PDF showing each of the train lines in the UK](./images/train_routes.png)

<figcaption>

An insight into my definitely organised mind:
what I sketched to see which trains I could use on my journey if I needed to.
Blue is the bike route, with green the trains that could be used as shortcuts.
Background from [National Rail](https://www.nationalrail.co.uk/stations_destinations/rail-maps.aspx) ([PDF](./data/Rail%20map%20v37%20orange%20Dec%2022.pdf)).

</figcaption>

## And what?

![Photo of my bike in front of a millennium milepost.](./images/millenium-milestone.jpg)

<figcaption>

My bike in front of [millennium milepost 897X](https://www.sustrans.org.uk/national-cycle-network/millennium-mileposts).
6 km into day 2, the 80 km day.

</figcaption>

## Appendix: Tools
