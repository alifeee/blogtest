# Coding Projects! #2: Proximity-based voice chat for Factorio

Earlier this year, I played [Barotrauma] weekly for 21 weeks with friends. Barotrauma is "2D co-op submarine simulator – in space, with survival horror and RPG elements", and most importantly for me: it has a proximity voice-chat system. This means that if you are crafting some nuclear fuel rods at the rear of the ship, you will not hear your crewmates being torn apart by eldritch beings that found their way into the front of the ship. You will - on your way past the medbay to fix a leak in the crew quarters - hear the medical doctors through the door discussing which of the crewmembers to use for their next *'experiment'*. You will be picked as the next dead-man-walking to leave the submarine to mine precious metals, and will make your way across the ship to get orders in-person from the captain.

As you can tell, I had a lot of fun playing Barotrauma; it probably deserves a blog post of its own. When we played, we were usually around 8 players, which, had we used Discord for voice chat, would have been chaos trying to hear what everyone was saying. Proximity chat added greatly to our enjoyment of the game, and planted the question in my mind of which other games which could be as fun. As far as I think of it, there are a few criteria which make Factorio great and that I would like in another game that could be as fun. They are:

- Proximity chat. Games which come to mind immediately which have this are Among Us and Minecraft. There are [lists online][proxchat games].
- Campaign-based. By this, I mean games where you play the same save, and wouldn't start fresh every week. Among Us is out.
- Players are... in proximity to each other. In Barotrauma, you can always hear mutterings and ramblings of other people as you are all trapped inside a submarine. In Minecraft, you travel massive distances and make bases separate from each other.

The games on the [above list][proxchat games] that are probably most like what I'm after are Sea of Thieves and Ark/Rust. However, the secret fourth category is: people I know must own the game. So, after all that, I was suggested [Factorio], which I thought would be a bunch of fun to play with a bunch of people. Factorio doesn't pass the third criterion of "players are always vaguely close to each other", but it's a great game, so I'm sure I can allow it on fail on the list. Since I've not started the collective game, it remains to be seen how close people remain to each other when playing: maybe people stick together more if they have proximity chat!

There is only one problem with Factorio: it didn't have proximity chat. That, my dear friend, is why we're here. I wanted to play Factorio with proximity chat so much that I made it myself. Within these words lies the tales, struggle, and strife of that process.

1. [Research](#research)
   1. [How do other games do it?](#how-do-other-games-do-it)
   2. [How can I do it for Factorio?](#how-can-i-do-it-for-factorio)
   3. [Using Mumble](#using-mumble)
2. [Making the Factorio Mod](#making-the-factorio-mod)
3. [Making the Mumble Plugin](#making-the-mumble-plugin)
   1. [Initial attempt (outdated documentation)](#initial-attempt-outdated-documentation)
   2. [For real this time](#for-real-this-time)
      1. [Simple steps](#simple-steps)
      2. [Integrate with the Factorio mod](#integrate-with-the-factorio-mod)
      3. [Build it on Windows](#build-it-on-windows)
   3. [It works! (for a bit)](#it-works-for-a-bit)
   4. [It works! (weirdly)](#it-works-weirdly)
   5. [It works! (actually)](#it-works-actually)
4. [Conclusion](#conclusion)

## Research

### How do other games do it?

The only game I had played with user-created proximity chat before was [Among Us]. I had remembered that we had all downloaded ["BetterCrewLink"](https://github.com/OhMyGuus/BetterCrewLink), which was a desktop app, which connected to a voice server, connected to the game running on your machine, and somehow did proximity chat from that. Looking at the code on GitHub, the program read the memory addresses of things like player position, and also looked like it implemented its own entire [VoIP] system (Voice over IP).

This seemed a lot of work. I didn't fancy creating (or even trying to clone) what is basically Discord or TeamSpeak, so I did some more Googling.

### How can I do it for Factorio?

Googling around, the only mention I could find of Factorio and proximity voice chat was a single [Reddit thread].

![Screenshot of Reddit thread. Title: "Positional VoIP audio?". Content: "Has anyone considered implementing positional audio for Factorio?"](images/reddit_thread_title.png)

Without this thread, I don't think I would have started trying to make a Factorio proximity chat mod. But, with the thread, I had some leads. [Faxxobeat] made me aware that [Mumble] - an open source voice chat client (like Discord or TeamSpeak) - had support for "positional audio" via "plugins". There were already [plugins for many games][Mumble repo#plugins] and lots of documentation on PA (Positional Audio). This sounded like an approachable plan, since this way all I had to do to implement proximity chat in Factorio was make a plugin for Mumble, which would handle the rest of the voice chat. And, reading the [requirements for a Mumble plugin][Mumble PA#data], I just had to write a plugin which gave Mumble the player position, player name and the current game server. It seemed "easy enough".

### Using Mumble

I found a *lot* of different documentation for Mumble and Mumble's PA. There was a...

## Making the Factorio Mod

## Making the Mumble Plugin

### Initial attempt (outdated documentation)

### For real this time

#### Simple steps

#### Integrate with the Factorio mod

#### Build it on Windows

### It works! (for a bit)

### It works! (weirdly)

### It works! (actually)

## Conclusion

![Screenshot of Factorio players, speaking. They say "Proximity Voice Chat!"; "Pardon?"](./og-image.png)

[Barotrauma]: https://store.steampowered.com/app/602960/Barotrauma/
[proxchat games]: https://www.familygamingdatabase.com/en-gb/search/list/Proximity+Chat
[Factorio]: https://factorio.com/
[Among Us]: https://www.innersloth.com/games/among-us/
[VoIP]: https://en.wikipedia.org/wiki/Voice_over_IP
[Reddit thread]: https://www.reddit.com/r/factorio/comments/ixtqgs/positional_voip_audio/
[Faxxobeat]: https://www.reddit.com/user/Faxxobeat/
[Mumble]: https://www.mumble.info/
[Mumble repo#plugins]: https://github.com/mumble-voip/mumble/tree/master/plugins
[Mumble PA#data]: https://www.mumble.info/documentation/user/positional-audio/#pa-data
