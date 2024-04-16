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
   1. [**BLOG POSTS**](#blog-posts)
      1. [how to start blogging](#how-to-start-blogging)
      2. [a hat blog](#a-hat-blog)
   2. [**JUST DATA**](#just-data)
      1. [**DATA I MANUALLY MADE**](#data-i-manually-made)
         1. [my spotify wrapped 2023](#my-spotify-wrapped-2023)
         2. [a toki pona word list](#a-toki-pona-word-list)
         3. [my vscode extension list](#my-vscode-extension-list)
      2. [**DATA THAT'S AUTOMATICALLY UPDATED**](#data-thats-automatically-updated)
         1. [my json resume](#my-json-resume)
         2. [my web bookmarks](#my-web-bookmarks)
   3. [**HOW-TOS**](#how-tos)
      1. [**THINGS I WANTED TO DO MULTIPLE TIMES**](#things-i-wanted-to-do-multiple-times)
         1. [how to generate and host a Factorio map](#how-to-generate-and-host-a-factorio-map)
         2. [how to download data from Toggl's api](#how-to-download-data-from-toggls-api)
         3. [reusable ffmpeg commands](#reusable-ffmpeg-commands)
         4. [how to make bar charts in bash](#how-to-make-bar-charts-in-bash)
         5. [how to make graphs in bash](#how-to-make-graphs-in-bash)
      2. [**THINGS THAT OTHER PEOPLE COULD WANT TO DO**](#things-that-other-people-could-want-to-do)
         1. [a script to remove all styles from an html file](#a-script-to-remove-all-styles-from-an-html-file)
         2. [common RSS extensions](#common-rss-extensions)
         3. [a script to combine Squarespace RSS feeeds](#a-script-to-combine-squarespace-rss-feeeds)
         4. [a script to convert font files to css styles](#a-script-to-convert-font-files-to-css-styles)
         5. [a script to convert gpl files to css styles](#a-script-to-convert-gpl-files-to-css-styles)
      3. [**HOW TO SET UP THINGS ON A LINUX SERVER**](#how-to-set-up-things-on-a-linux-server)
         1. [how to set up rsa encryption keys](#how-to-set-up-rsa-encryption-keys)
         2. [how to set up nginx](#how-to-set-up-nginx)
         3. [how to transfer folders over scp](#how-to-transfer-folders-over-scp)
         4. [how to run a program as a service with systemd](#how-to-run-a-program-as-a-service-with-systemd)
         5. [how to set up a mumble server](#how-to-set-up-a-mumble-server)
         6. [how to install ruby and jekyll on linux](#how-to-install-ruby-and-jekyll-on-linux)
         7. [how to set up ftp on linux](#how-to-set-up-ftp-on-linux)

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

The list is long. I keep comments brief. I have categorised them as to my whims.

### **BLOG POSTS**

#### [how to start blogging]

```md
# How to start blogging

You might not think you should blog. I think you should.

I like your thoughts! I want to be able to read them!

Here are some other reasons: 

- [todepond's thoughts](https://www.todepond.com/wikiblogarden/art/blog/)
- [Max Böck's thoughts](https://mxb.dev/blog/seven-reasons-why-i-dont-write/)

At its simplest, a blog is "text on the Internet". With this in mind, my immediate reccomendation is [bear.blog](#using-bearblog), as it is super simple to set up, and you have text on the Internet, with no ads, and no nonsense.

Otherwise, here are some ways I know to share text on the Internet (listed in vague order of effort involved to set up/technical knowledge required to be learned).

## create text on the internet and link to it from elsewhere

for example on <https://gist.github.com>

...
```

<figcaption>

I created this for one person who asked me "how do I start a blog". Since I made it a gist, I have shared it with many people.

</figcaption>

#### [a hat blog]

```md
I love hats

...
```

<figcaption>

This is a blog about hats.

</figcaption>

### **JUST DATA**

#### **DATA I MANUALLY MADE**

##### [my spotify wrapped 2023]

```toml
# ...
[totals]
minutes = 60_724
songs = 7_309
genres = 151
artists = 4_391
[totals.longest_day]
date = "2023-7-08"
minutes = 861
# ...
```

<figcaption>

I started using [TOML](https://toml.io/en/) for lots of things around the same time Spotify Wrapped came out last year. It was fun to think of a way of putting it into TOML format. TOML is fun.

</figcaption>

##### [a toki pona word list]

```bash
#...
cat words.txt | awk -F'[^a-zA-Z]' 'BEGIN {delete wds} { if (length($0) > 0 && length($0) < 10) { if (!($1 in wds)) {print $1; wds[$1]}  } }' > nimi-ale-pi-toki-pona.txt
#...
```

<figcaption>

I wanted a [toki pona](https://tokipona.org/) word list for something. I can't remember what, but it was probably [lipu tenpo](https://liputenpo.org/) related. I put the command and generated list into a gist because I spent some time tinkering with `awk` to create the command, and I was proud of it. You may spot that theme continuing on.

</figcaption>

##### [my vscode extension list]

```json
{
  "name": "newprofile1",
  "extensions": "[{\"identifier\":{\"id\":\"bbenoist.doxygen\",\"uuid\":\"aab644b7-f446-4774-87fc-2cce8f0d5a4f\"}},{\"identifier\":{\"id\":\"cschlosser.doxdocgen\",\"uuid\":\"da7e26d5-d57c-4742-ab47-d77fb189e195\"},\"displayName\":\"Doxygen Documentation Generator\"},{\"identifier\":{\"id\":\"davidanson.vscode-markdownlint\",\"uuid\":\"daf8b44d-8aae-4da2-80c5-1f770219f643\"},\"displayName\":\"markdownlint\"},{\"identifier\":{\"id\":\"eamodio.gitlens\",\"uuid\":\"4de763bd-505d-4978-9575-2b7696ecf94e\"},\"displayName\":\"GitLens — Git supercharged\"},{\"identifier\":{\"id\":\"esbenp.prettier-vscode\",\"uuid\":\"96fa4707-6983-4489-b7c5-d5ffdfdcce90\"},\"displayName\":\"Prettier - Code formatter\"},{\"identifier\":{\"id\":\"formulahendry.auto-rename-tag\",\"uuid\":\"6e440e71-8ed9-4f25-bb78-4b13096b8a03\"},\"displayName\":\"Auto Rename Tag\"},{\"identifier\":{\"id\":\"github.copilot\",\"uuid\":\"23c4aeee-f844-43cd-b53e-1113e483f1a6\"},\"displayName\":\"GitHub Copilot\"},{\"identifier\":{\"id\":\"github.vscode-github-actions\",\"uuid\":\"04f49bfc-8330-4eee-8237-ea938fb755ef\"},\"displayName\":\"GitHub Actions\"},{\"identifier\":{\"id\":\"github.vscode-pull-request-github\",\"uuid\":\"69ddd764-339a-4ecc-97c1-9c4ece58e36d\"},\"displayName\":\"GitHub Pull Requests and Issues\"},{\"identifier\":{\"id\":\"jock.svg\",\"uuid\":\"4ae6dc82-7981-4f10-bd81-2d72aec37f39\"},\"displayName\":\"SVG\"},{\"identifier\":{\"id\":\"leonhard-s.python-sphinx-highlight\",\"uuid\":\"a0f17d96-c9f3-4ce4-92b7-27b8c936835b\"},\"displayName\":\"Python Sphinx Highlighter\"},{\"identifier\":{\"id\":\"mhutchie.git-graph\",\"uuid\":\"438221f8-1107-4ccd-a6fe-f3b7fe0856b7\"},\"displayName\":\"Git Graph\"},{\"identifier\":{\"id\":\"ms-python.black-formatter\",\"uuid\":\"859e640c-c157-47da-8699-9080b81c8371\"},\"displayName\":\"Black Formatter\"},{\"identifier\":{\"id\":\"ms-python.pylint\",\"uuid\":\"8dc47276-5882-4c5f-903d-7eef7b9d1584\"},\"displayName\":\"Pylint\"},{\"identifier\":{\"id\":\"ms-python.python\",\"uuid\":\"f1f59ae4-9318-4f3c-a9b5-81b2eaa5f8a5\"},\"displayName\":\"Python\"},{\"identifier\":{\"id\":\"ms-python.vscode-pylance\",\"uuid\":\"364d2426-116a-433a-a5d8-a5098dc3afbd\"},\"displayName\":\"Pylance\"},{\"identifier\":{\"id\":\"ms-toolsai.jupyter\",\"uuid\":\"6c2f1801-1e7f-45b2-9b5c-7782f1e076e8\"},\"displayName\":\"Jupyter\"},{\"identifier\":{\"id\":\"ms-toolsai.jupyter-keymap\",\"uuid\":\"9f6dc8db-620c-4844-b8c5-e74914f1be27\"},\"displayName\":\"Jupyter Keymap\"},{\"identifier\":{\"id\":\"ms-toolsai.jupyter-renderers\",\"uuid\":\"b15c72f8-d5fe-421a-a4f7-27ed9f6addbf\"},\"displayName\":\"Jupyter Notebook Renderers\"},{\"identifier\":{\"id\":\"ms-toolsai.vscode-jupyter-cell-tags\",\"uuid\":\"ab4fb32a-befb-4102-adf9-1652d0cd6a5e\"},\"displayName\":\"Jupyter Cell Tags\"},{\"identifier\":{\"id\":\"ms-toolsai.vscode-jupyter-slideshow\",\"uuid\":\"e153ca70-b543-4865-b4c5-b31d34185948\"},\"displayName\":\"Jupyter Slide Show\"},{\"identifier\":{\"id\":\"ms-vscode.cpptools\",\"uuid\":\"690b692e-e8a9-493f-b802-8089d50ac1b2\"},\"displayName\":\"C/C++\"},{\"identifier\":{\"id\":\"ms-vscode.cpptools-extension-pack\",\"uuid\":\"3957b2f6-f086-49b5-a7b4-5da772123130\"},\"displayName\":\"C/C++ Extension Pack\"},{\"identifier\":{\"id\":\"ms-vscode.cpptools-themes\",\"uuid\":\"99b17261-8f6e-45f0-9ad5-a69c6f509a4f\"},\"displayName\":\"C/C++ Themes\"},{\"identifier\":{\"id\":\"ms-vscode.powershell\",\"uuid\":\"40d39ce9-c381-47a0-80c8-a6661f731eab\"},\"displayName\":\"PowerShell\"},{\"identifier\":{\"id\":\"ms-vscode.vscode-typescript-next\",\"uuid\":\"15305aca-2588-4ca0-8147-ab2c64730b82\"},\"displayName\":\"JavaScript and TypeScript Nightly\"},{\"identifier\":{\"id\":\"mushan.vscode-paste-image\",\"uuid\":\"ffaf4ec8-f001-4f02-b671-705ecf079cde\"},\"displayName\":\"Paste Image\"},{\"identifier\":{\"id\":\"naumovs.color-highlight\",\"uuid\":\"121396ad-85a1-45ec-9fd1-d95028a847f5\"},\"displayName\":\"Color Highlight\"},{\"identifier\":{\"id\":\"njpwerner.autodocstring\",\"uuid\":\"2d6fea35-f68e-461d-9b7b-5cd05be99451\"},\"displayName\":\"autoDocstring - Python Docstring Generator\"},{\"identifier\":{\"id\":\"rangav.vscode-thunder-client\",\"uuid\":\"2fd56207-78ef-49d4-95d2-9b801eee4dbf\"},\"displayName\":\"Thunder Client\"},{\"identifier\":{\"id\":\"ritwickdey.liveserver\",\"uuid\":\"b63c44fd-0457-4696-99e9-dbfdf70d77de\"},\"displayName\":\"Live Server\"},{\"identifier\":{\"id\":\"tumido.cron-explained\",\"uuid\":\"6ee451cb-7b81-4520-9eb4-059db43a1431\"},\"displayName\":\"Cron Explained\"},{\"identifier\":{\"id\":\"usernamehw.errorlens\",\"uuid\":\"9d8c32ab-354c-4daf-a9bf-20b633734435\"},\"displayName\":\"Error Lens\"},{\"identifier\":{\"id\":\"valentjn.vscode-ltex\",\"uuid\":\"840e9c85-0e99-42ce-aa62-81088245e699\"},\"displayName\":\"LTeX – LanguageTool grammar/spell checking\"},{\"identifier\":{\"id\":\"yzhang.markdown-all-in-one\",\"uuid\":\"98790d67-10fa-497c-9113-f6c7489207b2\"},\"displayName\":\"Markdown All in One\"}]"
}
```

<figcaption>

When I originally made this, it was human-readable: you could see a nice, multi-line list of my VSCode extensions. They have since changed how the export/import works, so now it looks very ugly. I no longer find this useful.

</figcaption>


#### **DATA THAT'S AUTOMATICALLY UPDATED**

##### [my json resume]

```json
#...
"references": [
  {
    "reference": "\"This is very neat thank you for this contribution.\"",
    "name": " Alexandre Lavigne, open-source pull request.",
    "url": "https://github.com/burnash/gspread/pull/1187#pullrequestreview-1451621771"
  },
  {
    "reference": "\"Thanks @strib and. @alifeee - very good team work!!!!\"",
    "name": "Romano Silva, open-source pull request.",
    "url": "https://github.com/keyteki/keyteki/pull/3222#issuecomment-1589734669"
  },
#...
```

<figcaption>

This is auto-updated by my [CV repository](https://github.com/alifeee/json-resume). I used to use [json-resume](https://jsonresume.org/) a bit more, but I stopped doing the themes how they did it and made it myself. I still use the schema, though, and still update this gist, so I can view my CV in [many](https://registry.jsonresume.org/alifeee?theme=elegant) [different](https://registry.jsonresume.org/alifeee?theme=macchiato) [styles](https://registry.jsonresume.org/alifeee?theme=rickosborne). Neat!

</figcaption>

##### [my web bookmarks]

```json
{
    "last_modified": "2024-03-25T00:44:15.551843Z",
    "bookmarks": {
        "TOP 10 personal websites/blogs": [
            {
                "title": "Tom Forth's Homepage",
                "url": "https://www.tomforth.co.uk/",
                "date_added": "2023-05-29T18:23:46.689000Z",
                "last_modified": "2023-11-12T22:19:05.160000Z"
            },
            {
                "title": "nonnullish",
                "url": "https://nonnullish.pages.dev/",
                "date_added": "2023-09-12T15:53:49.290000Z",
                "last_modified": "2023-11-12T22:19:28.376000Z"
            },
...
```

<figcaption>

After making my CV automatically push to a gist, it was easy to do similar when I was making my [Firefox bookmark exporter](https://github.com/alifeee/firefox-bookmarks). I don't really use this gist, but I guess having the data in machine-readable format is nice. Although [alifeee.co.uk/bookmarks](https://alifeee.co.uk/bookmarks/) probably already fills that role.

</figcaption>

### **HOW-TOS**

#### **THINGS I WANTED TO DO MULTIPLE TIMES**

##### [how to generate and host a Factorio map]

##### [how to download data from Toggl's api]

##### [reusable ffmpeg commands]

##### [how to make bar charts in bash]

##### [how to make graphs in bash]

#### **THINGS THAT OTHER PEOPLE COULD WANT TO DO**

##### [a script to remove all styles from an html file]

##### [common RSS extensions]

##### [a script to combine Squarespace RSS feeeds]

##### [a script to convert font files to css styles]

##### [a script to convert gpl files to css styles]

#### **HOW TO SET UP THINGS ON A LINUX SERVER**

##### [how to set up rsa encryption keys]

##### [how to set up nginx]

##### [how to transfer folders over scp]

##### [how to run a program as a service with systemd]


##### [how to set up a mumble server]

##### [how to install ruby and jekyll on linux]

##### [how to set up ftp on linux]

[how to start blogging]: https://gist.github.com/alifeee/c857bfb45bfd260a9b9dd9c45e4f7478
[a hat blog]: https://gist.github.com/alifeee/48f83a302205772e1a911ac889ae6212

[my spotify wrapped 2023]: https://gist.github.com/alifeee/075086b13fe5cec4c86d0f051973a960
[a toki pona word list]: https://gist.github.com/alifeee/7afeac3587624d66d7b370fe23882252
[my vscode extension list]: https://gist.github.com/alifeee/d46f1f41189b13bb44c2c32f84f69edc

[my web bookmarks]: https://gist.github.com/alifeee/5d84396d0404a879bb41329ec5afa9d3
[my json resume]: https://gist.github.com/alifeee/97f9ac1642b1c46cf66942c3f079a42f

[how to generate and host a Factorio map]: https://gist.github.com/alifeee/fb16acc9b4cc8b6d52e4f3226cc10197
[how to download data from Toggl's api]: https://gist.github.com/alifeee/5ccfdff391f1bfc894f6e21beb78996d
[reusable ffmpeg commands]: https://gist.github.com/alifeee/9e968dbf9f380ab4b15cda8d05d2a89e
[how to make bar charts in bash]: https://gist.github.com/alifeee/a6f14aad9caed6b8a861df0e2850aa10
[how to make graphs in bash]: https://gist.github.com/alifeee/2e1ea8ad5290a553316e715f658f1fd7

[a script to remove all styles from an html file]: https://gist.github.com/alifeee/75df204c2be3815806e1d4be47e54d08
[common RSS extensions]: https://gist.github.com/alifeee/8342d9677c436e2353233f68f34cfe19
[a script to combine Squarespace RSS feeeds]: https://gist.github.com/alifeee/2eb9ac2296a698dc8a05d4ed531d8d36
[a script to convert font files to css styles]: https://gist.github.com/alifeee/8607c787a0c60684827b5f07bbb95a5d
[a script to convert gpl files to css styles]: https://gist.github.com/alifeee/586b92e21f912dde7f74cd498b7cbb56

[how to set up rsa encryption keys]: https://gist.github.com/alifeee/2f4be232f6b9c4b384f4c020a5bc10a1
[how to set up nginx]: https://gist.github.com/alifeee/92defe5a02a2e1dd17cb517135e80ffe
[how to transfer folders over scp]: https://gist.github.com/alifeee/4a6cead6cd3e79a6620100ea00de5e42
[how to run a program as a service with systemd]: https://gist.github.com/alifeee/606ffd2cefaceeeff92a037e797e5458
[how to set up a mumble server]: https://gist.github.com/alifeee/2b8831d503438ff147fb8df6c01858c4
[how to install ruby and jekyll on linux]: https://gist.github.com/alifeee/829344ed02efb0952e81fc35c445df18
[how to set up ftp on linux]: https://gist.github.com/alifeee/f11e7295659576c236869079a3105025
