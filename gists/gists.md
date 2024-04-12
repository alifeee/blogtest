# Why I like (GitHub) gists and a short tour through ones I have created

1. [What are gists?](#what-are-gists)
2. [Why I like creating gists](#why-i-like-creating-gists)
   1. [I can share them with people](#i-can-share-them-with-people)
   2. [I can share them with myself in the future](#i-can-share-them-with-myself-in-the-future)
   3. [The ramblings of my existence can end up in the same place](#the-ramblings-of-my-existence-can-end-up-in-the-same-place)
3. [Why I like finding other people's gists](#why-i-like-finding-other-peoples-gists)
   1. [Someone else has probably done what I want to do before](#someone-else-has-probably-done-what-i-want-to-do-before)
4. [I could or should put things elsewhere (not on GitHub)](#i-could-or-should-put-things-elsewhere-not-on-github)
5. [My gists, or "the gist-list"](#my-gists-or-the-gist-list)

## What are gists?

[GitHub Gists] are "some text on the Internet". Usually, people put code snippets or Markdown in them, and then can share a link to anyone. It's like [Pastebin] but without (explicit) ads. Here's [an example gist] and here's [the same on Pastebin].

Gists can be used for blog posts, or just to share copied text, or to host a single-branch version controlled script or code snippet. They are also often used to host data which is automatically updated from elsewhere, and can be referenced as the most up-to-date version of that data, for example by ideas like <https://jsonresume.org/>.

Anyone with a GitHub account can make a gist. It's a very easy way to share nicely formatted text (for example in Markdown), which is why it's the first - and most simple - thing I suggest in my ["how to blog" guide].

There are [good reasons][o kepeken ala GitHub] you may not want to support GitHub. There are other ways to share snippets, with [other gist tools], [Pastebin], and other options. However, a lot of other code- or text-sharing websites seem fleeting, have ads, and do not look as nice (honourable mention here to <https://wormhole.app/>, a website for sharing *files* that looks incredible.)

[GitHub Gists]: https://gist.github.com/
[Pastebin]: https://pastebin.com/
[an example gist]: https://gist.github.com/alifeee/586b92e21f912dde7f74cd498b7cbb56
[the same on Pastebin]: https://pastebin.com/i7U9KSEu
["how to blog" guide]: https://gist.github.com/alifeee/c857bfb45bfd260a9b9dd9c45e4f7478
[o kepeken ala GitHub]: https://liputenpo.org/toki/nanpa-tenpo/o-kepeken-ala-ilo-ike-ni/
[other gist tools]: https://github.com/thomiceli/opengist

## Why I like creating gists

I like creating gists because they make text easy to share with two groups of people.

### I can share them with people

The first group of people is "other people", either specifically for someone, or just information or code I share a lot, so I like having a quick link to it. Gists I've made in this category include:

- [how to create a blog?](https://gist.github.com/alifeee/c857bfb45bfd260a9b9dd9c45e4f7478) - I share this one with people whenever they muse about blogging and talk about using some complicated- or expensive-sounding tool, to try and convince them that they need not take on such an undertaking, and can just "put text on the Internet".
- [Remove all CSS styles from HTML files with bash](https://gist.github.com/alifeee/75df204c2be3815806e1d4be47e54d08) - this is a bash script I wrote and shared for [CSS Naked Day 2024](https://css-naked-day.github.io/). There were lots of ways of removing styles for site-builders and site-backends, but none for pure HTML.
- [How to use Ruby and Jekyll on Linux](https://gist.github.com/alifeee/829344ed02efb0952e81fc35c445df18) - when I set up Jekyll to edit a website for the first time, it was really confusing, partly because I'd never used Ruby before.

### I can share them with myself in the future

The second group of people is really just one person, and they are "me in the future". Most of my usage of gists has been to remember how I did some specific thing with code or how I installed something. Writing it down in the first place help future me *a lot* to remember, because all I have to remember is in what context I did the thing, and then I can find out exactly how by reading the gist. Some examples of gists that have been very helpful to future- (well, now past-) me are:

- [How to setup RSA keys for automatic SSH login](https://gist.github.com/alifeee/2f4be232f6b9c4b384f4c020a5bc10a1) - I found cryptography and keys confusing for a long time. Writing down what I did helped me set it up and get more confident doing so in future.
- [Plot graphs using the terminal (bash)](https://gist.github.com/alifeee/2e1ea8ad5290a553316e715f658f1fd7) - I often `cat` data out to the terminal. It's nice to graph it. This is a way of doing so *in* the terminal, so doesn't require a UI library.
- [Common RSS URL extensions](https://gist.github.com/alifeee/8342d9677c436e2353233f68f34cfe19) - is what it says on the tin

### The ramblings of my existence can end up in the same place

I make a lot of random scripts. In another world, they would end up either buried in random repositories on GitHub, or buried in random folders on my computer or laptop. They would get lost.

Gists make it easy to paste a script somewhere, and then find it later, as they are all (I'm sure much to GitHub's enjoyment) in the same place.

## Why I like finding other people's gists

More than just being able to share my own code, I like gists because other people have the same ideas as me!

### Someone else has probably done what I want to do before

If I'd like to accomplish a small scripting task, understand something self-contained, or find a code snippet for a specific task, I often search for it on the web. Unfortunately, in our Lord's year 2024, pages and pages of whatever search I make are mostly AI garbage ([here][verge-ai] is an article I have not read to pretend to verify my point). One help here is independent search engines like [Marginalia Search] or [Wiby]. While they are fun for exploring a more indie version of the web, I also find adding `"site:gist.github.com"` to my web search often results in finding exactly what I want to do.

[verge-ai]: https://www.theverge.com/2023/6/26/23773914/ai-large-language-models-data-scraping-generation-remaking-web
[Marginalia Search]: https://search.marginalia.nu/
[Wiby]: https://wiby.me/about/

For example, here is a small list of gists from my Internet history that I've found to be useful recently (and as a by-product, an eye into my life and desires for the past several months).

- [Simple XSL boilerplate for styling Atom feeds](https://gist.github.com/andrewstiefel/57a0a400aa2deb6c9fe18c6da4e16e0f)
- [Git's Merge vs. Rebase vs. Squash](https://gist.github.com/mitchellh/319019b1b8aac9110fcfb1862e0c97fb)
- [CSS Train Departure board](https://gist.github.com/veltman/f2b2a06d4ffa62f4d39d5ebac5ceeef0)
- [Change End of Line Sequence from CRLF to LF to all files in a project](https://gist.github.com/tjsudarsan/f2bfe4c4d567243e302cf8ba40e1c7e5)
- [How to copy, read and write Paxton fobs and cards with an RFIDler](https://gist.github.com/natmchugh/18e82761dbce52fa284c87c190dc926f)
- [Simple Morse en- & decoding for Arduino](https://gist.github.com/madc/4474559)
- [Getting started with the D1 mini (ESP8266)](https://gist.github.com/carljdp/e6a3f5a11edea63c2c14312b534f4e53)
- [Globally install FFmpeg and convert video to GIF](https://gist.github.com/JaimeStill/8adb695ee46425f1ee9830357cd9c6bb)
- [RevealJS cheat sheet](https://gist.github.com/peeweek/55d6c2eb006d11c7da01fde974325f33)
- [Decoding Morse Code With JavaScript](https://gist.github.com/bennadel/9760604)
- [Make an issue on GitHub using API V3 and Python](https://gist.github.com/JeffPaine/3145490)
- [how to print Avery labels with only a .csv and a web browser](https://gist.github.com/kgodard/5072573)
- [how to make a Google Form → GitHub issue Google Apps Script](https://gist.github.com/bmcbride/62600e48274961819084)

## I could or should put things elsewhere (not on GitHub)

The existence of GitHub in the above has mainly been a sidenote. The main thing that excites me about gists is the collaborative nature of them. This is not something that GitHub must have control over, and indeed something that they probably *shouldn't* have control over.

I've been reading recently a lot about self- or community-hosted alternatives to different things like Git servers (like [sourcehut](https://sourcehut.org/)) and, I use [Mastodon](https://joinmastodon.org/) (talking of self-hosting, I'd like to find an instance that's not [mastodon.social](https://mastodon.social/)) a lot.

I could put my snippets on my website, or something more free. But, I haven't.

## My gists, or "the gist-list"
