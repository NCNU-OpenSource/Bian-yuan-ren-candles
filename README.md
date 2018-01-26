# Bian-yuan-ren-candles 🕯️
![pic](http://scontent.cdninstagram.com/t51.2885-15/s480x480/e35/14730745_1013650085427086_9178540712952594432_n.jpg?ig_cache_key=MTM3NTMwMjg4MDU3MTA0NjU1Mg%3D%3D.2)

圖片來源：http://www.imgrum.org/user/long.hair.girl


身為一個專業的邊緣人，自己幫自己過生日應該是基本的吧。

## 簡介

有鑑於現在日漸嚴重的空氣污染問題，身為一個小小的邊緣人，也想為這個世界貢獻一份心力 ~~（雖然沒有人感受的到）~~ 。
為了防止地球被破壞，為了保護世界的和平，大家一起來用邊緣人蠟燭吧！

## 目標
做出就算只有一個人過生日，也可有熱鬧生日派對的fu。
利用 LED 燈呈現蠟燭搖曳的燈光效果，透過麥克風收音的功能，營造出吹蠟燭的效果。
對著麥克風吹蠟燭，LED 上面的蠟燭圖案會隨之改變。

進階功能：  
LED 燈上面除了可以呈現蠟燭圖案之外，還可以透過外部操作的方式，改變想顯示的圖示。比方說：數字、名字。

為了讓生日不要這麼的冷清，此蠟燭還配備了播放生日快樂歌的功能。  
中文版、英文版、日文版、韓文版應有盡有，任君挑選。

當生日快樂歌播完後，是不是還覺得有點不滿足呢？  
此蠟燭在最後還附加了一個貼心的服務 —— 『掌聲響起』。  
伴隨著掌聲，讓你的生日派對不寂寞、不孤單。

在這一年之中最特別的日子裡，就讓邊緣人蠟燭陪你一起度過吧>_____O///。
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/-5ZQxNI0h-0/0.jpg)](https://www.youtube.com/watch?v=-5ZQxNI0h-0)

## 實作所需材料


|   材料名稱      | 數量 | 單價 | 總價 |   來源    |
| -------------- | --- | --- | --- | --------- | 
| 杜邦線（公母）   | 1 (42條)  | 15    | 15   | 課程提供  |
| Raspberry pi   |  2  | 1300   | 2600    | 課程提供  |
| 按鈕            | 3   | 10   | 30    | 課程提供  |
| 8x7 LED矩陣     | 2   | 35   | 70    | 課程提供  |
|麥克風模組        | 1   | 40   | 40    | 課程提供  |
| 外接喇叭         | 1   | 990    | 990   | 漢廷提供  |
| 麵包板           | 1   | 50    | 50   | 課程提供  |

**總價：3795**  假如一根蠟燭十元，你只要使用380次以上就回本囉～～

健康是無價的，讓我們一起使用邊緣人蠟燭守護我們的環境

costdown:使用寄存器可以使用一台pi與價格低廉的喇叭，可以大大降低價格！

## 使用的現有軟體與來源
* Python

* RPI.GPIO 函式庫

## 操作前提

        # 實際操作前，更改/pi1/sshpi.sh的ip位置
          $ ssh pi@{ip} >/dev/null 2>&1 &
          //啟動設備
          $ python start.py


## 實際操作
step 1. 按第一顆控制蠟燭面板按鈕，點燃蠟燭，這邊會連動顯示生日歌曲選擇的面板，面板會顯示中文歌（Ｃ）代號，依序歌曲選擇為Ｃ->Ｅ->Ｊ->Ｋ

step 2. 按第二顆按鈕選想聽的生日歌語言

step 3. 按第三顆按鈕播放生日快樂歌

step 4. 唱完後，對著蠟燭旁的麥克風吹熄蠟燭，音響會播放出鼓掌聲，猶如許多人為你慶生

## 電路圖
![pic](https://github.com/NCNU-OpenSource/Bian-yuan-ren-candles/blob/master/1061LSA%E6%9C%9F%E6%9C%AB_bb.jpg)

## 工作分配
接版版：怡丰，育柔，展瑩，漢廷

coding：怡丰，育柔，展瑩，漢廷

文件、Slide：怡丰，育柔，漢廷

顧問指導團：yy、展瑩、天麟、老大、蛋蛋、班代大大、公主殿下

## 參考資料
LED教學: http://ezzep.blogspot.tw/2012/12/RaspberryPi-5x7LED.html

Sound Senser教學: http://www.instructables.com/id/Sound-Sensor-Raspberry-Pi/ 

Button教學: http://razzpisampler.oreilly.com/ch07.html 

劇本link:https://goo.gl/ZCV4pX

Slide link:https://goo.gl/7w1veC
