# Coding Projects! #1: Collage generator for Steam games

1. [What tools to use?](#what-tools-to-use)
   1. [How to get Steam library information](#how-to-get-steam-library-information)

Below, you *should* see a lovely image of my four most recently played games on [Steam].

[Steam]: https://steamcommunity.com/id/alifeee/

![Oops. It must have broken. Here *should* be alifeee's 4 most recently played Steam games.](http://45.91.169.110:5000/steamcollage/games?id=alifeee&cols=2&rows=2&sort=recent)

<figcaption>

API status: <img src="http://45.91.169.110:5000/steamcollage/alive_img" onerror="this.src='./didnotload.png'" style="background-color: orange; display: inline-block; height: 1rem; width: 1rem; border-radius: 50%;" />

</figcaption>

This is created fresh every time you reload the page, and comes from [my server].

Is being able to have a live image like that worth the considerable (as you will unearth below) pain?
Maybe. I think it's neat.

I consider myself a fairly visual person, and as such I like to always have an image to use in combination with text (as you see on [*this blog's homepage*] any [lipu tenpo posts][lipu tenpo], and any Notion page I have [unfortunately] made you subscribe to). In the past for these things I have used Python and [Pillow] to make collages, such as this [lipu tenpo] collage:

![Collage of lipu tenpo covers](./images/lipu%20tenpo%20collage.png)

<figcaption>

[lipu tenpo] is a non-profit magazine written entirely in [toki pona]. I originally created this cover image for personal use, but it turned out useful as a banner for the [social media][lipu tenpo].

</figcaption>

I also made a Python script to generate the topic of this blog post: Steam game collages.
This I put this [on GitHub][old steam collage] for anyone to use.

However, as it only worked locally (and my [installation instructions][old steam collage] weren't exactly... *exhaustive*), it couldn't be used very easily.
This meant when people were interested, I ended up just generating an image for them, rather than them being able to act autonomously.
This also meant that any images were fixed in aspect ratio, size, games included, etc.
I did have the ambition to "put it on the web", but knowing little of the web at the time, my thoughts were "surely you can just run a Python file on a website?". After trying, I did not manage this.

But! That's where this blog post comes in! A few years later (and with more knowledge about [websites], [APIs][API], and [servers][server]) I felt I could now come up with a solution for making my collage generator more usable, and less manual.

## What tools to use?

Atomised, the idea of "automatically make collages from Steam game libraries" can be split into:

1. how to get steam library information
1. image manipulation
1. how to host the tool

### How to get Steam library information

In [my first attempt][old steam collage], I used [web scraping] to get a list of all games from a user's [Steam profile page][alifeee's games]. While this worked, it was not robust, and a bit of a hack. By this point, I had more experience using APIs, so I decided to use [Steam's API][steam api].

Annoyingly (and as is often the case with public APIs), it was not easy to read the [documentation][steam api], and Steam has several APIs, with the two biggest helpfully differentiated by one being the ["Steamworks API"][steamworks api], and the other the ["Steamworks Web API"][steamworks web api].

The latter had the two endpoints I needed. [Firstly][api:ResolveVanityUrl], a way to convert [vanity URLs][vanity urls] to [steam IDs][steam ids] (other APIs generally want a steam ID). [Secondly][api:GetOwnedGames], an endpoint which returns the list of games owned by a player.

```bash
GET https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/
```

[*this blog's homepage*]: ..
[my server]: http://server.alifeee.co.uk
[lipu tenpo]: https://linktr.ee/liputenpo
[Pillow]: https://python-pillow.org/
[toki pona]: https://en.wikipedia.org/wiki/Toki_Pona
[old steam collage]: https://github.com/alifeee/steam_collage_api/tree/1483bc0ed5157e9608e7cf31a8a07a50645d1343
[websites]: https://en.wikipedia.org/wiki/Website
[API]: https://en.wikipedia.org/wiki/API
[server]: https://en.wikipedia.org/wiki/Server_(computing)
[web scraping]: https://en.wikipedia.org/wiki/Web_scraping
[alifeee's games]: https://steamcommunity.com/id/alifeee/games/?tab=all
[steam api]: https://steamcommunity.com/dev
[steamworks api]: https://partner.steamgames.com/doc/api
[steamworks web api]: https://partner.steamgames.com/doc/webapi
[api:ResolveVanityUrl]: https://partner.steamgames.com/doc/webapi/ISteamUser
[vanity urls]: https://www.makeuseof.com/how-to-set-up-custom-url-steam-profile/
[steam ids]: https://help.steampowered.com/en/faqs/view/2816-BE67-5B69-0FEC
[api:GetOwnedGames]: https://partner.steamgames.com/doc/webapi/IPlayerService
