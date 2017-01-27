=========
Lino Voga
=========

`Lino Voga <http://voga.lino-framework.org>`_ ist eine Anwendung zum
Verwalten von Kursen oder sonstigen Veranstaltungen, inklusive
Rechnungsausgang an die Teilnehmer und Erfassen der Zahlungen, bei
Bedarf auch Einkaufsrechnungen und sonstige Buchungen bis hin zur
kompletten Buchhaltung.

**Online-Demo**

* http://roger.lino-framework.org/

**Übersicht**

Ein **Kurs** hat eine Liste von *Teilnehmern* (Einschreibungen) und
eine Liste von *Terminen*.

Die **Termine** eines Kurses werden automatisch generiert (z.B. "Jeden
zweiten Montag von 19 bis 21 Uhr"), können dann jedoch manuell
angepasst werden.  Pro Termin kann man die detaillierten
*Anwesenheiten* der Teilnehmer erfassen.

Die **Einschreibungen** zu einem Kurs haben einen *Status* (Angefragt,
Bestätigt). Wenn z.B. ein Kurs überfüllt ist, kann ein Teilnehmer sich
trotzdem in die Warteschlange eintragen.

Bei der Einschreibung wird ein **Tarif** angegeben, aufgrund dessen
Lino einen Fakturierungsvorschlag macht. Es gibt verschiedene
Tarifsysteme: feste Einschreibegebühr, Jahreskarten, Zehnerkarten,
Abonnements pro Termin oder pro Anwesenheit.

Lino verwaltet auch die **Räume**, in denen die Kurse stattfinden, und
passt auf, dass nicht zwei Kurse in den gleichen Raum geplant werden.
Diese Räume kann man auch an externe Veranstalter vermieten, was
ebenfalls automatisch fakturiert werden kann.

Um das Kursangebot übersichtlich zu halten, definiert man Kursreihen,
Themen und Kursarten.

