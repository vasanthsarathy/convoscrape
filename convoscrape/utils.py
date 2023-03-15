search_help = """
# Advanced Search Help

Directly Adapted from (igorbrigadir's github repo)[https://github.com/igorbrigadir/twitter-advanced-search]

Class | Operator | Finds Tweets… | Eg:
-- | -- | -- | --
Tweet content | `nasa esa` <br> `(nasa esa)` | Containing both "`nasa`" and "`esa`". Spaces are implicit AND. Brackets can be used to group individual words if using other operators. | [🔗](https://twitter.com/search?q=esa%20nasa&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `nasa OR esa` | Either "`nasa`" or "`esa`". OR must be in uppercase. | [🔗](https://twitter.com/search?q=nasa%20OR%20esa&src=typed_query&f=live  "Last Checked: 2022-11-01")
&nbsp; | `"state of the art"` | The complete phrase "`state of the art`". Will also match "`state-of-the-art`". Also use quotes to prevent spelling correction. | [🔗](https://twitter.com/search?q=%22state%20of%20the%20art%22&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `"this is the * time this week"` | A complete phrase with a wildcard. ` * ` does not work outside of a quoted phrase or without spaces. | [🔗](https://twitter.com/search?q=%22this%20is%20the%20*%20time%20this%20week%22&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `+radiooooo` | Force a term to be included as-is. Useful to prevent spelling correction. | [🔗](https://twitter.com/search?q=%2Bradiooooo&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `-love` <br> `-"live laugh love"` | `-` is used for excluding "`love`". Also applies to quoted phrases and other operators. | [🔗](https://twitter.com/search?q=bears%20-chicagobears&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `#tgif` | A hashtag | [🔗](https://twitter.com/search?q=%23tgif&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `$TWTR` | A cashtag, like hashtags but for stock symbols | [🔗](https://twitter.com/search?q=%24TWTR%20OR%20%24FB%20OR%20%24AMZN%20OR%20%24AAPL%20OR%20%24NFLX%20OR%20%24GOOG&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `What ?` | Question marks are matched | [🔗](https://twitter.com/search?q=(Who%20OR%20What%20OR%20When%20OR%20Where%20OR%20Why%20OR%20How)%20%3F&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `:) OR :(` | Some emoticons are matched, positive `:) :-) :P :D` or negative `:-( :(` | [🔗](https://twitter.com/search?q=%3A%29%20OR%20%3A-%29%20OR%20%3AP%20OR%20%3AD%20OR%20%3A%28%20OR%20%3A-%28&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | 👀 | Emoji searches are also matched. Usually needs another operator to work. | [🔗](https://twitter.com/search?q=%F0%9F%91%80%20lang%3Aen&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `url:google.com` | urls are tokenized and matched, works very well for subdomains and domains, not so well for long urls, depends on url. Youtube ids work well. Works for both shortened and canonical urls, eg: `gu.com` shortener for `theguardian.com`. When searching for Domains with hyphens in it, you have to replace the hyphen by an underscore (like `url:t_mobile.com`) but underscores `_` are also tokenized out, and may not match | [🔗](https://twitter.com/search?q=url%3Agu.com&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `lang:en` | Search for tweets in specified language, not always accurate, see the full [list](#supported-languages) and special `lang` codes below. | [🔗](https://twitter.com/search?q=lang%3Aen&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | | |
Users | `from:user` | Sent by a particular `@username` e.g. `"dogs from:NASA"` | [🔗](https://twitter.com/search?q=dogs%20from%3Anasa&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `to:user` | Replying to a particular `@username` | [🔗](https://twitter.com/search?q=%23MoonTunes%20to%3Anasa&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `@user` | Mentioning a particular `@username`. Combine with `-from:username` to get only mentions | [🔗](https://twitter.com/search?q=%40cern%20-from%3Acern&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `list:715919216927322112` <br> `list:esa/astronauts` | Tweets from members of this public list. Use the list ID from the API or with urls like `twitter.com/i/lists/715919216927322112`. List slug is for old list urls like `twitter.com/esa/lists/astronauts`. Cannot be negated, so you can't search for "not on list". | [🔗](https://twitter.com/search?q=list%3A715919216927322112%20OR%20list%3Aesa%2Fastronauts&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `filter:verified` | From verified users | [🔗](https://twitter.com/search?q=filter%3Averified&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `filter:blue_verified` | From "verified" users that paid $8 for Twitter Blue | [🔗](https://twitter.com/search?q=filter%3Ablue_verified%20-filter%3Averified&src=typed_query&f=live "Last Checked: 2022-11-10")
&nbsp; | `filter:follows` | Only from accounts you follow. Cannot be negated. | [🔗](https://twitter.com/search?q=filter%3Afollows%20lang%3Aen&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `filter:social` <br> `filter:trusted` | Only from algorithmically expanded network of accounts based your own follows and activities. Works on "`Top`" results not "`Latest`" | [🔗](https://twitter.com/search?q=kitten%20filter%3Asocial&src=typed_query "Last Checked: 2022-11-01")
&nbsp; | | |
Geo | `near:city` | Geotagged in this place. Also supports Phrases, eg: `near:"The Hague"` | [🔗](https://twitter.com/search?q=near%3A%22The%20Hague%22&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `near:me` | Near where twitter thinks you are | [🔗](https://twitter.com/search?q=near%3Ame&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `within:radius` | Within specific radius of the "near" operator, to apply a limit. Can use km or mi. e.g. `fire near:san-francisco within:10km` | [🔗](https://twitter.com/search?q=fire%20near%3Asan-francisco%20within%3A10km&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `geocode:lat,long,radius` | E.g., to get tweets 10km around twitters hq, use `geocode:37.7764685,-122.4172004,10km` | [🔗](https://twitter.com/search?q=geocode%3A37.7764685%2C-122.4172004%2C10km&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `place:96683cc9126741d1` | Search tweets by [Place Object](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/geo-objects.html#place) ID eg: USA Place ID is `96683cc9126741d1` | [🔗](https://twitter.com/search?q=place%3A96683cc9126741d1&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | | |
Time | `since:2021-12-31` | On or after (inclusive) a specified date. 4 digit year, 2 digit month, 2 digit day separated by `-` a dash. | [🔗](https://twitter.com/search?q=since%3A2019-06-12%20until%3A2019-06-28%20%23nasamoontunes&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `until:2021-12-31` | Before (NOT inclusive) a specified date. Combine with a "since" operator for dates between. | [🔗](https://twitter.com/search?q=since%3A2019-06-12%20until%3A2019-06-28%20%23nasamoontunes&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `since:2021-12-31_23:59:59_UTC` | On or after (inclusive) a specified date and time in the specified timezone. 4 digit year, 2 digit month, 2 digit day separated by `-` dashes, an `_` underscore separating the 24 hour clock format hours:minutes:seconds and timezone abbreviation. | [🔗](https://twitter.com/search?q=%22%23NASA%22%20since%3A2022-10-13_00%3A00%3A00_UTC%20until%3A2022-10-14_00%3A02%3A00_UTC&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `until:2021-12-31_23:59:59_UTC` | Before (NOT inclusive) a specified date and time in the specified timezone. Combine with a "since" operator for dates between. | [🔗](https://twitter.com/search?q=%22%23NASA%22%20since%3A2022-10-13_00%3A00%3A00_UTC%20until%3A2022-10-14_00%3A02%3A00_UTC&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `since_time:1142974200` | On or after a specified unix timestamp in seconds. Combine with the "until" operator for dates between. Maybe easier to use than `since_id` below. | [🔗](https://twitter.com/search?q=since_time%3A1561720321%20until_time%3A1562198400%20%23nasamoontunes&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `until_time:1142974215` | Before a specified unix timestamp in seconds. Combine with a "since" operator for dates between. Maybe easier to use than `max_id` below. | [🔗](https://twitter.com/search?q=since_time%3A1561720321%20until_time%3A1562198400%20%23nasamoontunes&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `since_id:tweet_id` | After (NOT inclusive) a specified Snowflake ID | [🔗](https://twitter.com/search?q=since_id%3A1138872932887924737%20max_id%3A1144730280353247233%20%23nasamoontunes&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `max_id:tweet_id` | At or before (inclusive) a specified Snowflake ID (see [Note](#snowflake-ids) below) | [🔗](https://twitter.com/search?q=since_id%3A1138872932887924737%20max_id%3A1144730280353247233%20%23nasamoontunes&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `within_time:2d` <br> `within_time:3h` <br> `within_time:5m` <br> `within_time:30s` | Search within the last number of days, hours, minutes, or seconds | [🔗](https://twitter.com/search?q=nasa%20within_time%3A30s&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | | |
Tweet Type | `filter:nativeretweets` | Only retweets created using the retweet button. Works well combined with `from:` to show only retweets. Only works within the last 7-10 days or so. | [🔗](https://twitter.com/search?q=from%3Anasa%20filter%3Anativeretweets&src=typed_query&f=live "Last Checked: 2022-11-10")
&nbsp; | `include:nativeretweets` | Native retweets are excluded by default. This shows them. In contrast to `filter:`, which shows only retweets, this includes retweets in addition to other tweets. Only works within the last 7-10 days or so. | [🔗](https://twitter.com/search?q=from%3Anasa%20include%3Anativeretweets%20&src=typed_query&f=live "Last Checked: 2022-11-10")
&nbsp; | `filter:retweets` | Old style retweets ("RT") + quoted tweets. | [🔗](https://twitter.com/search?q=filter%3Aretweets%20from%3Atwitter%20until%3A2009-11-06%09&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `filter:replies` | Tweet is a reply to another Tweet. good for finding conversations, or threads if you add or remove `to:user` | [🔗](https://twitter.com/search?q=from%3Anasa%20filter%3Areplies%20-to%3Anasa&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `conversation_id:tweet_id` | Tweets that are part of a thread (direct replies and other replies) | [🔗](https://twitter.com/search?q=conversation_id%3A1140437409710116865%20lang%3Aen&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `filter:quote` | Contain Quote Tweets | [🔗](https://twitter.com/search?q=from%3Anasa%20filter%3Aquote&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `quoted_tweet_id:tweet_id` | Search for quotes of a specific tweet | [🔗](https://twitter.com/search?q=quoted_tweet_id%3A1138631847783608321&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `quoted_user_id:user_id` | Search for all quotes of a specific user | [🔗](https://twitter.com/search?q=quoted_user_id%3A11348282&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `card_name:poll2choice_text_only` <br> `card_name:poll3choice_text_only` <br> `card_name:poll4choice_text_only` <br> `card_name:poll2choice_image` <br> `card_name:poll3choice_image` <br> `card_name:poll4choice_image`| Tweets containing polls. For polls containing 2, 3, 4 choices, or image Polls. | [🔗](https://twitter.com/search?q=lang%3Aen%20card_name%3Apoll4choice_text_only%20OR%20card_name%3Apoll3choice_text_only%20OR%20card_name%3Apoll2choice_text_only&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | | |
Engagement | `filter:has_engagement` | Has some engagement (replies, likes, retweets). Can be negated to find tweets with no engagement. Note all of these are mutually exclusive with `filter:nativeretweets` or `include:nativeretweets`, as they apply to the retweet, not the original tweet, so they won't work as expected. | [🔗](https://twitter.com/search?q=breaking%20filter%3Anews%20-filter%3Ahas_engagement&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `min_retweets:5` | A minimum number of Retweets. Counts seem to be approximate for larger (1000+) values. | [🔗](https://twitter.com/search?q=min_retweets%3A5000%20nasa&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `min_faves:10` | A minimum number of Likes | [🔗](https://twitter.com/search?q=min_faves%3A10000%20nasa&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `min_replies:100` | A minimum number of replies | [🔗](https://twitter.com/search?q=min_replies%3A1000%20nasa&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `-min_retweets:500` | A maximum number of Retweets | [🔗](https://twitter.com/search?q=-min_retweets%3A500%20nasa&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `-min_faves:500` | A maximum number of Likes | [🔗](https://twitter.com/search?q=-min_faves%3A500%20nasa&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `-min_replies:100` | A maximum number of replies | [🔗](https://twitter.com/search?q=-min_replies%3A100%20nasa&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | | |
Media | `filter:media` | All media types. | [🔗](https://twitter.com/search?q=filter%3Amedia%20cat&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `filter:twimg` | Native Twitter images (`pic.twitter.com` links) | [🔗](https://twitter.com/search?q=filter%3Atwimg%20cat&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `filter:images` | All images. | [🔗](https://twitter.com/search?q=filter%3Aimages%20cat&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `filter:videos` | All video types, including native Twitter video and external sources such as Youtube. | [🔗](https://twitter.com/search?q=filter%3Avideos%20cat&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `filter:periscope` | Periscopes | [🔗](https://twitter.com/search?q=filter%3Aperiscope%20cat&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `filter:native_video` | All Twitter-owned video types (native video, vine, periscope) | [🔗](https://twitter.com/search?q=filter%3Anative_video%20cat&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `filter:vine` | Vines (RIP) | [🔗](https://twitter.com/search?q=filter%3Avine%20cat&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `filter:consumer_video` | Twitter native video only | [🔗](https://twitter.com/search?q=filter%3Aconsumer_video%20cat&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `filter:pro_video` | Twitter pro video (Amplify) only | [🔗](https://twitter.com/search?q=filter%3Apro_video%20cat&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `filter:spaces` | Twitter Spaces only | [🔗](https://twitter.com/search?q=filter%3Aspaces&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | | |
More Filters | `filter:links` | Only containing some URL, includes media. use `-filter:media` for urls that aren't media | [🔗](https://twitter.com/search?q=filter%3Afollows%20filter%3Alinks%20-filter%3Amedia&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `filter:mentions` | Containing any sort of `@mentions` | [🔗](https://twitter.com/search?q=filter%3Amentions%20from%3Atwitter%20-filter%3Areplies&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `filter:news` | Containing link to a news story. Combine with a list operator to narrow the user set down further. | [🔗](https://twitter.com/search?q=filter%3Anews%20lang%3Aen&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `filter:safe` | Excluding NSFW content. Excludes content that users have marked as "Potentially Sensitive". Doesn't always guarantee SFW results. | [🔗](https://twitter.com/search?q=filter%3Asafe%20%23followfriday&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `filter:hashtags` | Only Tweets with Hashtags. | [🔗](https://twitter.com/search?q=from%3Anasa%20filter%3Ahashtags&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | | |
App specific | `source:client_name` | Sent from a specified client e.g. source:tweetdeck (See [Note](#common-clients) for common ones) eg: `twitter_ads` doesn't work on it's own, but does with another operator. | [🔗](https://twitter.com/search?q=source%3A%22GUCCI%20SmartToilet%E2%84%A2%22%20lang%3Aen&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `card_domain:pscp.tv` | Matches domain name in a Twitter Card. Mostly equivalent to `url:` operator. | [🔗](https://twitter.com/search?q=card_domain%3Apscp.tv&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `card_url:pscp.tv` | Matches domain name in a Card, but with different results to `card_domain`. | [🔗](https://twitter.com/search?q=card_url%3Apscp.tv&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `card_name:audio` | Tweets with a Player Card (Links to Audio sources, Spotify, Soundcloud etc.) | [🔗](https://twitter.com/search?q=card_name%3Aaudio&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `card_name:animated_gif` | Tweets With GIFs | [🔗](https://twitter.com/search?q=card_name%3Aanimated_gif&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `card_name:player` | Tweets with a Player Card | [🔗](https://twitter.com/search?q=card_name%3Aplayer&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `card_name:app` <br> `card_name:promo_image_app` | Tweets with links to an App Card. `promo_app` does not work, `promo_image_app` is for an app link with a large image, usually posted in Ads. | [🔗](https://twitter.com/search?q=card_name%3Aapp%20OR%20card_name%3Apromo_image_app&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `card_name:summary` | Only Small image summary cards | [🔗](https://twitter.com/search?q=card_name%3Asummary&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `card_name:summary_large_image` | Only large image Cards | [🔗](https://twitter.com/search?q=card_name%3Asummary_large_image&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `card_name:promo_website` | Larger than `summary_large_image`, usually posted via Ads | [🔗](https://twitter.com/search?q=card_name%3Apromo_website%20lang%3Aen&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `card_name:promo_image_convo` <br> `card_name:promo_video_convo` | Finds [Conversational Ads](https://business.twitter.com/en/help/campaign-setup/conversational-ad-formats.html) cards. | [🔗](https://twitter.com/search?q=carp%20card_name%3Apromo_image_convo&src=typed_query&f=live "Last Checked: 2022-11-01")
&nbsp; | `card_name:3260518932:moment` | Finds Moments cards. `3260518932` is the user ID of `@TwitterMoments`, but the search finds moments for everyone, not that specific user. | [🔗](https://twitter.com/search?q=card_name%3A3260518932%3Amoment&src=typed_query&f=live "Last Checked: 2022-11-01")


## Matching:

On web and mobile, keyword operators can match on: The user's name, the @ screen name, tweet text, and shortened, as well as expanded url text (eg, `url:trib.al` finds accounts that use that shortener, even though the full url is displayed).

By default "Top" results are shown, where "Top" means tweets with some engagements (replies, RTs, likes). "Latest" has most recent tweets. People search will match on descriptions, but not all operators work. "Photos" and "Videos" are presumably equivalent to `filter:images` and `filter:videos`.

Exact Tokenization is not known, but it's most likely a custom one to preserve entities. URLs are also tokenized. Spelling correction appears sometimes, and also plurals are also matched, eg: `bears` will also match tweets with `bear`. `-` not preceeding an operator are removed, so "state-of-the-art" is the same as "state of the art".

Private accounts are not included in the search index, and their tweets do no appear in results. Locked and suspended accounts are also hidden from results. There are other situations where tweets may not appear: [anti-spam measures](https://help.twitter.com/en/rules-and-policies/enforcement-options), or tweets simply have not been indexed due to server issues.

Twitter is using some words as signal words. E.g. when you search for “photo”, Twitter assumes you’re looking for Tweets with attached photos. If you want to search for Tweets which literally contain the word “photo”, you have to wrap it in double quotes `"photo"`.


## Building Queries:

Most "`filter:type`" can also be negated using the "`-`" symbol, with exceptions like `filter:follows` which can't be negated. `exclude:links` is the same as `-filter:links`. It's sometimes worth trying an alias like that in case the search doesn't work first time.

Example: I want Tweets from @Nasa with all types of media except images

`from:NASA filter:media -filter:images`

Combine complex queries together with booleans and parentheses to refine your results.

Example 1: I want mentions of either "puppy" or "kitten", with mentions of either "sweet" or "cute", excluding Retweets, with at least 10 likes.

`(puppy OR kitten) AND (sweet OR cute) -filter:nativeretweets min_faves:10`

Example 2: I want mentions of "space" and either "big" or "large" by members of the NASA astronauts List, sent from an iPhone or twitter.com, with images, excluding mentions of #asteroid, since 2011.

`space (big OR large) list:nasa/astronauts (source:twitter_for_iphone OR source:twitter_web_client) filter:images since:2011-01-01 -#asteroid`

To find any quote tweets, search for the tweet permalink, or the tweet ID with `url` eg: `https://twitter.com/NASA/status/1138631847783608321` or `url:1138631847783608321`, see [note](#quote-tweets) for more.

For some queries you may want to use parameters with hyphens or spaces in it, e.g. `site:t-mobile.com` or `app:Twitter for iOS`. Twitter doesn’t accept hyphens or spaces in parameters and won’t display any tweets for this query. You can still search for those parameters by replacing all hyphens and spaces with underscores, e.g. `site:t_mobile.com` or `app:Twitter_for_iOS`.
"""
