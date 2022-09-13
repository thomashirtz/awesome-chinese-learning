# chinese-learning
Repository to share resources and tips that can help when learning Chinese.

## Flashcards
### Application
[Anki](https://apps.ankiweb.net/) is the default app for flashcards on android and windows.

### Deck  
The deck that I use extensively is the one I found on Reddit: ["Best Anki Deck for HSK I've come across"](https://www.reddit.com/r/ChineseLanguage/comments/7mjmjc/best_anki_deck_for_hsk_ive_come_across/)

### Settings  
Training vocabulary with flashcards will take quite some time. It is, therefore, _strongly_ recommended to finely tune the settings of the deck before using it extensively. 

<p align="center">
 <a target="_blank" href="https://youtu.be/1XaJjbCSXT0">
  <img src="https://i.ytimg.com/vi/1XaJjbCSXT0/maxresdefault.jpg" width="300"/>
 </a>
</p>


## [Zhongwen](https://github.com/cschiller/zhongwen)(Browser extension)
Zhongwen is a Chinese pop-up dictionary for browsers (Chrome, Firefox, ...). It is useful to get the translation of specific words on a page by hovering over the word with the mouse.

It is also possible to add the hovered vocabulary to a list by pressing "R". The list can be accessed using "Alt + W".

_Extra tip 1:_ The vocabularies can thereafter be downloaded and added to ANKI.

_Extra tip 2:_ If you have some text that you want to analyze using the browser extension zhongwen, you can paste it in [awfice](https://htmlpreview.github.io/?https://github.com/zserge/awfice/blob/main/edit.html) .



## Dictionaries
Two primary chinese-english dictionaries are popular:
1. Pleco
2. Hanping

Both have a free version and a version where you have a one-time purchase to get more vocabulary (definitely worth it). Some comparisons exist on the internet. 

## Translator
1. Google translate: Best translator, not available in China.
2. [Bing translator](https://www.bing.com/translator) : Works in china.
3. [Baidu translator](https://fanyi.baidu.com/#zh/en/)

## Video Resources

### Netflix
Netflix can be used to learn Chinese! It is possible to make the dynamic lookup of subtitles work directly in the browser (at least in Mozilla). Two extensions are needed, as well as a little hack:
1. Install [Zhongwen](https://github.com/cschiller/zhongwen)
2. Install [Subfilter](https://github.com/met/subfilter)
3. Go to the show or movie you want to watch, and change the language from the extension Subfilter to _Simplified Chinese_. (Obviously, the media do need to have Chinese subtitles available.)
4. Press F11 to put it full screen (Zhongwen does not work full screen on Netflix).

### XuetangX
The equivalent of Coursera in Chinese, you can use the Zhongwen + F11 Mode in order to have the possibility of a dictionary pop-up when watching classes.

### Viki
Shows and movies with a built-in lookup of the Chinese subtitles are available. It is extremely well made, however, the selection of shows having the feature was quite poor several years ago.

### Bilibili
The equivalent of youtube in China. However, in contrast to youtube, Netflix, ..., the platform does not have built-in subtitles. It is, therefore, less convenient to learn Chinese with this platform.

### [Chinese Zero To Hero](https://chinesezerotohero.teachable.com/courses) 
The platform contains many Chinese courses. It is not free, however, it works as a one-time purchase. Very clean and exceptionally well made. The classes are based on the books from BLCU.

### Others
1. [Youku (优酷)](https://www.youku.com/)
2. [iQIYI (爱奇艺)](https://www.iqiyi.com/)
3. [MangoTV (芒果TV)](https://w.mgtv.com/) (It has, for example, 爸爸去哪儿)

## Text Ressources

### [Zhihu](https://www.zhihu.com/hot)
Website similar to Quora, where all the new trends are discussed, questions are asked, ...

### [Toutiao](https://www.toutiao.com)
Most popular news aggregator in China.

### [Weibo](https://weibo.com)
The chinese twitter.

## Calligraphy & Writing

### [How to write Chinese character](https://play.google.com/store/apps/details?id=com.ansami.hkchinesechar&hl=en_US&gl=US) (Android application)
It is an excellent android application for learning stroke order as well as to learn how to write characters.

###[书法字典](http://shufazidian.com/)
shufazidian is a website as well as a mini program that display the character selected in different style writing. It is extremely helpful when learning to do some calligraphy.

## Miscellaneous
### Douban
The main website to watch the score of different movies/TV shows. It is the equivalent of IMDB.  
If you want to search for very specific TV shows, you can take a look at the tool I wrote : [douban-crawler](https://github.com/thomashirtz/douban-crawler)
### [chinese-shadowing](https://github.com/thomashirtz/chinese-shadowing)
It is a small tool I wrote in order to do some shadowing using the deck mentioned in the Flashcards section. 


### Pop-up dictionary on documents 
One of the main tricks I used while studying in China. You can convert many different formats into PDFs (by printing them). You can then convert them into HTML and use them in the browser to have a pop-up dictionary with zhongwen.

Note: You might have to give Zhongwen permission to access files on your local file system, at least on Chrome.

### Novels in HTML
Some Chinese novels are available for free online in an HTML format. It is perfect for our new favorite trick, the pop-up dictionary.

Example of a free book : [三体](https://www.shizongzui.cc/santi/),

### Chinese OCR
Here are some Chinese OCRs for converting an image to text using the computer (It can be pretty helpful if you want, for example, put the Chinese textbook's vocabulary list into your Anki deck).
1. [Convertio](https://convertio.co/ocr/chinese/)
2. [Easy ScreenOCR](https://online.easyscreenocr.com/Home/ChineseOCR)

## Pinyin Converter
It is a converter that transforms Chinese characters into pinyin. Such can be very useful, especially when creating Anki cards or else.
1. [Lexilogos](https://www.lexilogos.com/keyboard/pinyin_conversion.htm)
2. [ChineseConverter](https://www.chineseconverter.com/en/convert/chinese-to-pinyin) (Seems to have many different nice tools, including conversion traditional<=>chinese)

### [PotPlayer](https://potplayer.daum.net/)
Potplayer is a really powerful multimedia player. If you own some videos with Chinese subtitles, you can dynamically search online the words that you clicked on.  
This can be set in :
```
Preferences => Subtitles => Research by word 
```
You need to put `%%SS` where the word from the subtitle will be in the URL querry. I generally redirect the query to MDBG:
```
https://www.mdbg.net/chinese/dictionary?page=worddict&wdrst=0&wdqb=%%SS
```
