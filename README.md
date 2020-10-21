
Датасет содержит:
1. Твиты собственников и топ-менеджеров компаний, государственных деятелей.
2. Котировки акций и курсов валют.
3. Сопоставление твитов и изменений котировок.

Датасет предназначен для исследования влияния словесных интервенций на котировки.3

По котировкам и акциям взяты следующие данные:

1. Курс евро к доллару за 2012 - 2020 годы. Источник: официальные данные ЕЦБ
2. Курс шекеля к евро и доллару за 2008 - 2020 годы. Источник: официальные данные банка Израиля
3. Акции Microsoft за 1986 - 2020 годы. Источник: NASDAQ
4. Акции Тesla за 2010 - 2020 годы. Источник: NASDAQ
5. Акции Virgin America за 2014 - 2016 годы. Источник: NASDAQ
Акции Virgin Australia за 2011 - 2020 годы. Источник: ASX
Акции Virgin Galactic за 2017 - 2020 годы. Источник: NYSE

Твиты собраны по следующим персоналиям:

US Business leaders

Jeff Weiner- LinkedIn @jeffweiner Joined February 2009

Tim Cook- Apple @tim_cook Joined July 2013

Bill Gates- Microsoft @BillGates Joined June 2009

Michael Dell- Dell @MichaelDell Joined July 2009

Mary Barra- GM @mtbarra Joined February 2013

Warren Buffett- Berkshire Hathaway @WarrenBuffett Joined April 2013

Sundar Pichai- Google @sundarpichai CEO, Google and Alphabet Joined March 2008

Asia/ China
Jack Ma Founder of AlibabaGroup @JackMa Joined March 2020

Ma Huateng @ma_tencent CEO of Tencent Holdings Limited Joined September 2017

Russian business leaders

Oleg Tikov @olegtinkov Joined April 2009

European politicians

Emmanuel Macron France @EmmanuelMacron Joined October 2013

Theresa May UK @theresa_may Joined June 2016

Benjamin Netanyahu @netanyahu Prime Minister of Israel Joined October 2008

Reuven Rivlin @PresidentRuvi live updates from the 10th President of the State of Israel - Joined November 2014


Структура датасета:

/

  /People

    /Elon Musk

      elonmusk.json

    /Jeff Bezos

      JeffBezos.json

    ...

  /Assets

    /AMZN

      котрировки компании Amazon

    /TSLA

      котировки компании Tesla

    ...

  /People_vs_Assets

    /Bezos_TSLA

      сопоставление твитов Джеффа Безоса и изменений котировок компании Amazon

    /Musk_TSLA

      сопоставление твитов Илона Маска и изменений котировок компании Tesla

    ...

Структура json-файла твитов:

{'2020-10-19 00:32:08':

  {'contributors': None,

  'coordinates': None,

*(и т. д, разместить структуру твита)*

Структура json-файла котировок:

*(разместить структуру котировок)*

Структура сводной таблицы:

*(разместить структуру сводной таблицы)*
